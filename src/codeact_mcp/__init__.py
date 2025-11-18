"""
CodeAct MCP - Code Execution with Model Context Protocol

A system implementing the CodeAct pattern where agents generate executable Python code
to interact with MCP servers, reducing token consumption by up to 98.7%.

This package provides the core infrastructure:
- CodeActSandbox: Daytona sandbox management
- MCPRegistry: MCP server connections and tool discovery
- ToolFunctionGenerator: Convert MCP schemas to Python functions
- Session/SessionManager: Session lifecycle management
- Config: Configuration loading

For agent implementations, see the agent package.
"""

__version__ = "0.2.0"

from .sandbox import CodeActSandbox, ExecutionResult, ChartData
from .session import Session, SessionManager
from .config import CoreConfig
from .mcp_registry import MCPRegistry, MCPToolInfo
from .tool_generator import ToolFunctionGenerator

# Backward compatibility alias
Config = CoreConfig

__all__ = [
    "CodeActSandbox",
    "ExecutionResult",
    "ChartData",
    "Session",
    "SessionManager",
    "CoreConfig",
    "Config",  # Backward compatibility
    "MCPRegistry",
    "MCPToolInfo",
    "ToolFunctionGenerator",
]
