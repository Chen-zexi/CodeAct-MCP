"""Research sub-agent definition for deepagent.

This sub-agent specializes in web research using Tavily search
and strategic thinking for comprehensive information gathering.
"""

from datetime import datetime
from typing import Any, Dict, List

from ..prompts.task_workflow import RESEARCHER_INSTRUCTIONS
from ..tools.research import tavily_search, think_tool


def get_research_subagent_config(
    max_researcher_iterations: int = 3,
    mcp_tools: List[Any] = None,
) -> Dict[str, Any]:
    """Get configuration for the research sub-agent.

    Args:
        max_researcher_iterations: Maximum search iterations
        mcp_tools: Additional MCP tools to include (per-subagent config)

    Returns:
        Sub-agent configuration dictionary for deepagent
    """
    # Format researcher instructions with current date
    instructions = RESEARCHER_INSTRUCTIONS.format(
        date=datetime.now().strftime("%Y-%m-%d")
    )

    # Base tools for research
    tools = [tavily_search, think_tool]

    # Add any MCP tools configured for this sub-agent
    if mcp_tools:
        tools.extend(mcp_tools)

    return {
        "name": "research-agent",
        "description": (
            "Delegate research to the sub-agent researcher. "
            "Give this researcher one specific topic or question at a time. "
            "The researcher will search the web and provide findings with citations."
        ),
        "system_prompt": instructions,
        "tools": tools,
    }


def create_research_subagent(
    max_researcher_iterations: int = 3,
    mcp_tools: List[Any] = None,
) -> Dict[str, Any]:
    """Create a research sub-agent for deepagent.

    This is a convenience wrapper around get_research_subagent_config.

    Args:
        max_researcher_iterations: Maximum search iterations
        mcp_tools: Additional MCP tools for this sub-agent

    Returns:
        Sub-agent configuration dictionary
    """
    return get_research_subagent_config(
        max_researcher_iterations=max_researcher_iterations,
        mcp_tools=mcp_tools,
    )
