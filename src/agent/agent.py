"""CodeAct Agent - Main agent using deepagent with CodeAct pattern.

This module creates a CodeAct agent that:
- Uses deepagent's create_deep_agent for orchestration
- Integrates Daytona sandbox via DaytonaBackend
- Provides MCP tools through execute_code
- Supports sub-agent delegation for specialized tasks
"""

from typing import Any, Dict, List, Optional

import structlog
from deepagents import create_deep_agent

from src.codeact_mcp.mcp_registry import MCPRegistry
from src.codeact_mcp.sandbox import CodeActSandbox, ExecutionResult

from src.agent.backends import DaytonaBackend
from src.agent.config import AgentConfig
from src.agent.tools import create_execute_bash_tool
from src.agent.prompts.base import build_mcp_section, format_tool_summary
from src.agent.prompts.task_workflow import (
    TASK_WORKFLOW_INSTRUCTIONS,
    SUBAGENT_DELEGATION_INSTRUCTIONS,
)
from src.agent.subagents import create_subagents_from_names
from src.agent.tools import create_execute_code_tool

logger = structlog.get_logger(__name__)


# Default limits for sub-agent coordination
DEFAULT_MAX_CONCURRENT_TASK_UNITS = 3
DEFAULT_MAX_TASK_ITERATIONS = 3
DEFAULT_MAX_GENERAL_ITERATIONS = 10


class CodeActAgent:
    """Agent that uses deepagent with CodeAct pattern for MCP tool execution.

    This agent:
    - Uses deepagent's built-in filesystem tools via DaytonaBackend
    - Provides execute_code tool for MCP tool invocation
    - Supports sub-agent delegation for specialized tasks
    """

    def __init__(self, config: AgentConfig):
        """Initialize CodeAct agent.

        Args:
            config: Agent configuration
        """
        self.config = config
        self.llm = config.get_llm_client()

        logger.info(
            "Initialized CodeActAgent with deepagent",
            provider=config.llm_definition.provider,
            model=config.llm_definition.model_id,
        )

    def _build_system_prompt(self, tool_summary: str) -> str:
        """Build the system prompt for the agent.

        Args:
            tool_summary: Formatted MCP tool summary

        Returns:
            Complete system prompt
        """
        # Combine workflow and delegation instructions
        max_concurrent = DEFAULT_MAX_CONCURRENT_TASK_UNITS
        max_iterations = DEFAULT_MAX_TASK_ITERATIONS

        instructions = (
            TASK_WORKFLOW_INSTRUCTIONS
            + "\n\n"
            + "=" * 80
            + "\n\n"
            + SUBAGENT_DELEGATION_INSTRUCTIONS.format(
                max_concurrent_task_units=max_concurrent,
                max_task_iterations=max_iterations,
            )
        )

        # Add MCP tool information
        mcp_section = build_mcp_section(tool_summary)

        return instructions + mcp_section

    def _get_tool_summary(self, mcp_registry: MCPRegistry) -> str:
        """Get formatted tool summary for prompts.

        Args:
            mcp_registry: MCP registry

        Returns:
            Formatted tool summary string
        """
        tools_by_server = mcp_registry.get_all_tools()

        # Convert to format expected by formatter
        tools_dict = {}
        for server_name, tools in tools_by_server.items():
            tools_dict[server_name] = [tool.to_dict() for tool in tools]

        # Build server configs dict for formatter
        server_configs = {s.name: s for s in self.config.mcp.servers}

        # Get tool exposure mode from config
        mode = self.config.mcp.tool_exposure_mode

        return format_tool_summary(tools_dict, mode=mode, server_configs=server_configs)

    def create_agent(
        self,
        sandbox: CodeActSandbox,
        mcp_registry: MCPRegistry,
        subagent_names: List[str] = None,
        additional_subagents: List[Dict[str, Any]] = None,
    ) -> Any:
        """Create a deepagent with CodeAct pattern capabilities.

        Args:
            sandbox: CodeActSandbox instance for code execution
            mcp_registry: MCPRegistry with available MCP tools
            subagent_names: List of subagent names to include (default: ["research"])
            additional_subagents: Additional sub-agent configurations

        Returns:
            Configured deepagent that can execute tasks
        """
        # Create the execute_code tool for MCP invocation
        execute_code_tool = create_execute_code_tool(sandbox, mcp_registry)

        # Create the Bash tool for shell command execution
        bash_tool = create_execute_bash_tool(sandbox)

        # Get tool summary for system prompt
        tool_summary = self._get_tool_summary(mcp_registry)

        # Build system prompt
        system_prompt = self._build_system_prompt(tool_summary)

        # Default to research subagent if none specified
        if subagent_names is None:
            subagent_names = ["research"]

        # Create subagents from names using the registry
        subagents = create_subagents_from_names(
            names=subagent_names,
            sandbox=sandbox,
            mcp_registry=mcp_registry,
            max_researcher_iterations=DEFAULT_MAX_TASK_ITERATIONS,
            max_iterations=DEFAULT_MAX_GENERAL_ITERATIONS,
        )

        if additional_subagents:
            subagents.extend(additional_subagents)

        # Create the Daytona backend for filesystem operations
        backend = DaytonaBackend(sandbox)

        logger.info(
            "Creating deepagent",
            tool_count=2,  # execute_code, Bash
            subagent_count=len(subagents),
        )

        # Create deepagent with filesystem middleware using Daytona backend
        # Note: deepagent's FilesystemMiddleware will use our DaytonaBackend
        # for all filesystem operations (ls, read, write, edit, glob, grep)
        agent = create_deep_agent(
            model=self.llm,
            tools=[execute_code_tool, bash_tool],  # MCP tools via execute_code, shell via Bash
            system_prompt=system_prompt,
            subagents=subagents if subagents else None,
            # The backend will be used by deepagent's FilesystemMiddleware
            backend=backend,
        )

        return agent


class CodeExecutor:
    """Executor that combines agent and sandbox for complete task execution."""

    def __init__(self, agent: CodeActAgent, mcp_registry: MCPRegistry):
        """Initialize executor.

        Args:
            agent: CodeAct agent for task execution
            mcp_registry: MCP registry with available tools
        """
        self.agent = agent
        self.mcp_registry = mcp_registry

        logger.info("Initialized CodeExecutor")

    async def execute_task(
        self,
        task: str,
        sandbox: CodeActSandbox,
        max_retries: int = 3,
    ) -> ExecutionResult:
        """Execute a task using deepagent with automatic error recovery.

        Args:
            task: User's task description
            sandbox: CodeActSandbox instance
            max_retries: Maximum retry attempts

        Returns:
            Final execution result
        """
        logger.info("Executing task with deepagent", task=task[:100])

        # Create the agent with injected dependencies
        agent = self.agent.create_agent(sandbox, self.mcp_registry)

        try:
            # Configure recursion limit
            recursion_limit = max(max_retries * 5, 15)

            # Execute task via deepagent
            agent_result = await agent.ainvoke(
                {"messages": [("user", task)]},
                config={"recursion_limit": recursion_limit},
            )

            # Parse result into ExecutionResult
            return self._parse_agent_result(agent_result, sandbox)

        except Exception as e:
            logger.error("Agent execution failed", error=str(e))

            return ExecutionResult(
                success=False,
                stdout="",
                stderr=f"Agent execution error: {str(e)}",
                duration=0,
                files_created=[],
                files_modified=[],
                execution_id="agent_error",
                code_hash="",
            )

    def _parse_agent_result(
        self, agent_result: dict, sandbox: CodeActSandbox
    ) -> ExecutionResult:
        """Parse deepagent result into ExecutionResult.

        Args:
            agent_result: Result from agent.ainvoke()
            sandbox: Sandbox instance to query for files

        Returns:
            ExecutionResult with execution details
        """
        messages = agent_result.get("messages", [])

        if not messages:
            return ExecutionResult(
                success=False,
                stdout="",
                stderr="Agent returned no messages",
                duration=0,
                files_created=[],
                files_modified=[],
                execution_id="no_messages",
                code_hash="",
            )

        # Find tool messages
        tool_messages = [
            msg for msg in messages if hasattr(msg, "type") and msg.type == "tool"
        ]

        if not tool_messages:
            # Extract final AI message
            ai_messages = [
                msg for msg in messages if hasattr(msg, "type") and msg.type == "ai"
            ]
            final_message = ai_messages[-1].content if ai_messages else "No execution"

            return ExecutionResult(
                success=True,  # Agent completed without code execution
                stdout=final_message,
                stderr="",
                duration=0,
                files_created=[],
                files_modified=[],
                execution_id="no_tool_calls",
                code_hash="",
            )

        # Get last tool message
        last_tool_msg = tool_messages[-1]
        observation = (
            last_tool_msg.content
            if hasattr(last_tool_msg, "content")
            else str(last_tool_msg)
        )

        # Check success
        success = "SUCCESS" in observation or "ERROR" not in observation

        # Extract stdout/stderr
        if success:
            stdout = observation.replace("SUCCESS", "").strip()
            stderr = ""
        else:
            stdout = ""
            stderr = observation.replace("ERROR", "").strip()

        # Get files from sandbox
        files_created = []
        try:
            if hasattr(sandbox, "_list_result_files"):
                result_files = sandbox._list_result_files()
                files_created = [f for f in result_files if f]
        except Exception:
            pass

        return ExecutionResult(
            success=success,
            stdout=stdout,
            stderr=stderr,
            duration=0.0,
            files_created=files_created,
            files_modified=[],
            execution_id=f"agent_step_{len(tool_messages)}",
            code_hash="",
        )


# For LangGraph deployment compatibility
def create_codeact_agent(config: Optional[AgentConfig] = None) -> CodeActAgent:
    """Create a CodeActAgent instance.

    Factory function for LangGraph deployment.

    Args:
        config: Optional agent configuration. If None, loads from default.

    Returns:
        Configured CodeActAgent
    """
    if config is None:
        config = AgentConfig.load()
        config.validate_api_keys()

    return CodeActAgent(config)


# =============================================================================
# LangGraph Deployment - Module-level agent
# =============================================================================

import asyncio
from langgraph.graph import StateGraph, MessagesState, START, END

from src.codeact_mcp.session import SessionManager

# Global session state for sandbox persistence (lazy initialization)
_session = None
_codeact_agent = None
_config = None


async def _ensure_initialized():
    """Ensure CodeAct session is initialized with sandbox and MCP registry."""
    global _session, _codeact_agent, _config

    if _session is None:
        # Use async config loading to avoid blocking I/O
        _config = await AgentConfig.load_async()
        _config.validate_api_keys()

        core_config = _config.to_core_config()
        _session = SessionManager.get_session("langgraph-deployment", core_config)
        await _session.initialize()

        # CodeActAgent.__init__ calls get_llm_client() which has blocking I/O
        # (dynamic imports) - wrap in thread to be safe
        _codeact_agent = await asyncio.to_thread(CodeActAgent, _config)

    return _session, _codeact_agent


async def codeact_node(state: MessagesState):
    """Main CodeAct agent node - initializes sandbox on first call and runs agent."""
    session, codeact_agent = await _ensure_initialized()

    # Create the deepagent with full CodeAct capabilities
    inner_agent = codeact_agent.create_agent(
        sandbox=session.sandbox,
        mcp_registry=session.mcp_registry,
        subagent_names=["research"],
    )

    # Run the full agent (deepagent handles its own tool loop)
    result = await inner_agent.ainvoke(state)
    return result


# Build a simple wrapper graph for LangGraph deployment
# The actual agent logic is in the deepagent created by CodeActAgent
workflow = StateGraph(MessagesState)
workflow.add_node("codeact", codeact_node)
workflow.add_edge(START, "codeact")
workflow.add_edge("codeact", END)

# Compile the graph for LangGraph deployment
agent = workflow.compile()
