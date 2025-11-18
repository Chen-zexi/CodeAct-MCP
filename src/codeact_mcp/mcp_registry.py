"""MCP Server Registry - Connect to and manage external MCP servers."""

import asyncio
import os
from typing import Any, Dict, List, Optional

import structlog
import httpx
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.client.sse import sse_client

from .config import CoreConfig, MCPServerConfig

logger = structlog.get_logger(__name__)


class MCPToolInfo:
    """Information about an MCP tool."""

    def __init__(
        self,
        name: str,
        description: str,
        input_schema: Dict[str, Any],
        server_name: str,
    ):
        """Initialize tool info.

        Args:
            name: Tool name
            description: Tool description
            input_schema: JSON schema for tool input
            server_name: Name of the MCP server providing this tool
        """
        self.name = name
        self.description = description
        self.input_schema = input_schema
        self.server_name = server_name

    def get_parameters(self) -> Dict[str, Any]:
        """Extract parameter information from input schema.

        Returns:
            Dictionary mapping parameter names to their info
        """
        params = {}

        if "properties" in self.input_schema:
            required_params = self.input_schema.get("required", [])

            for param_name, param_info in self.input_schema["properties"].items():
                params[param_name] = {
                    "type": param_info.get("type", "any"),
                    "description": param_info.get("description", ""),
                    "required": param_name in required_params,
                    "default": param_info.get("default"),
                }

        return params

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary.

        Returns:
            Dictionary representation
        """
        return {
            "name": self.name,
            "description": self.description,
            "parameters": self.get_parameters(),
            "server_name": self.server_name,
            "return_type": "Any",  # MCP doesn't specify return types
        }


class MCPServerConnector:
    """Connector for an individual MCP server.

    Uses nested async with pattern following MCP SDK best practices.
    The connector acts as an async context manager that keeps the
    stdio_client and ClientSession contexts alive.
    """

    def __init__(self, config: MCPServerConfig):
        """Initialize server connector.

        Args:
            config: Server configuration
        """
        self.config = config
        self.session: Optional[ClientSession] = None
        self.tools: List[MCPToolInfo] = []

        # Background task management
        self._connection_task: Optional[asyncio.Task] = None
        self._ready: asyncio.Event = asyncio.Event()
        self._disconnect_event: asyncio.Event = asyncio.Event()
        self._connection_error: Optional[Exception] = None

        logger.info("Initialized MCPServerConnector", server=config.name)

    def _prepare_env(self) -> Dict[str, str]:
        """Prepare environment variables by expanding placeholders.

        Expands environment variable placeholders like ${VAR} in the server
        config's env dict before passing to the MCP server process.

        Returns:
            Dictionary with expanded environment variables
        """
        if not self.config.env:
            return dict(os.environ)

        # Start with current environment
        expanded_env = dict(os.environ)

        # Expand each configured env var and merge
        for key, value in self.config.env.items():
            if isinstance(value, str):
                # Expand environment variable placeholders like ${VAR}
                expanded_value = os.path.expandvars(value)
                expanded_env[key] = expanded_value

                # Log if we expanded a placeholder
                if "${" in value and expanded_value != value:
                    logger.debug(
                        "Expanded environment variable",
                        server=self.config.name,
                        var=key,
                        from_placeholder=value,
                    )
            else:
                # Non-string values pass through as-is
                expanded_env[key] = value

        return expanded_env

    def _expand_url(self) -> Optional[str]:
        """Expand environment variable placeholders in URL.

        Returns:
            Expanded URL or None if no URL configured
        """
        if not self.config.url:
            return None

        # Expand environment variable placeholders like ${VAR}
        expanded_url = os.path.expandvars(self.config.url)

        if "${" in self.config.url and expanded_url != self.config.url:
            logger.debug(
                "Expanded URL environment variables",
                server=self.config.name,
            )

        # Warn if expansion failed (env var not set)
        if "${" in expanded_url:
            logger.warning(
                "URL contains unexpanded environment variables - check if env var is set",
                server=self.config.name,
                url=self.config.url,
            )

        return expanded_url

    async def __aenter__(self):
        """Enter async context manager - start connection task.

        Returns:
            Self for use in async with statement
        """
        logger.info("Connecting to MCP server", server=self.config.name)

        # Start background task that keeps nested contexts alive
        self._connection_task = asyncio.create_task(
            self._run_connection(), name=f"mcp-{self.config.name}"
        )

        # Wait for connection to be ready or fail
        await self._ready.wait()

        if self._connection_error:
            # Connection failed, raise the error
            raise self._connection_error

        logger.info(
            "Connected to MCP server",
            server=self.config.name,
            tool_count=len(self.tools),
        )

        return self

    async def _run_connection(self) -> None:
        """Background task that maintains the nested async with contexts.

        This follows MCP SDK best practices by using proper nested async with
        statements within a single task, ensuring contexts are entered and
        exited in LIFO order within the same task.
        """
        try:
            if self.config.transport == "http":
                # HTTP transport - use direct JSON-RPC over HTTP POST
                url = self._expand_url()
                if not url:
                    raise ValueError(f"URL required for HTTP transport: {self.config.name}")

                # HTTP transport doesn't use ClientSession - we make direct requests
                self._http_url = url
                self._http_client = httpx.AsyncClient(timeout=60.0)
                self._message_id = 0

                # Discover tools via HTTP
                await self._discover_tools_http()

                logger.debug(
                    "MCP HTTP connection established",
                    server=self.config.name,
                )

                # Signal that connection is ready
                self._ready.set()

                # Keep alive until disconnect
                await self._disconnect_event.wait()

                # Cleanup
                await self._http_client.aclose()

                logger.debug(
                    "MCP HTTP connection disconnect signaled",
                    server=self.config.name,
                )

            elif self.config.transport == "sse":
                # SSE transport - use URL-based connection
                url = self._expand_url()
                if not url:
                    raise ValueError(f"URL required for SSE transport: {self.config.name}")

                async with sse_client(url) as (read_stream, write_stream):
                    async with ClientSession(read_stream, write_stream) as session:
                        self.session = session

                        # Initialize and discover tools
                        # SSE connections need retry due to endpoint event timing
                        await self.session.initialize()
                        await self._discover_tools_with_retry()

                        logger.debug(
                            "MCP SSE connection established",
                            server=self.config.name,
                        )

                        # Signal that connection is ready
                        self._ready.set()

                        # Keep contexts alive until disconnect is signaled
                        await self._disconnect_event.wait()

                        logger.debug(
                            "MCP SSE connection disconnect signaled",
                            server=self.config.name,
                        )
            else:
                # Stdio transport (default) - use command-based connection
                server_params = StdioServerParameters(
                    command=self.config.command,
                    args=self.config.args,
                    env=self._prepare_env(),
                )

                # Proper nested async with pattern (MCP SDK best practice)
                async with stdio_client(server_params) as (read_stream, write_stream):
                    async with ClientSession(read_stream, write_stream) as session:
                        self.session = session

                        # Initialize and discover tools
                        await self.session.initialize()
                        await self._discover_tools()

                        logger.debug(
                            "MCP connection contexts established",
                            server=self.config.name,
                        )

                        # Signal that connection is ready
                        self._ready.set()

                        # Keep contexts alive until disconnect is signaled
                        await self._disconnect_event.wait()

                        logger.debug(
                            "MCP connection disconnect signaled",
                            server=self.config.name,
                        )

        except Exception as e:
            # Store error and signal ready so __aenter__ can raise it
            self._connection_error = e
            self._ready.set()

            # Log with full exception details
            import traceback
            error_details = traceback.format_exc()

            logger.error(
                "Failed to connect to MCP server",
                server=self.config.name,
                error=str(e),
                error_type=type(e).__name__,
                traceback=error_details,
            )

    async def _discover_tools(self) -> None:
        """Discover available tools from the server."""
        if not self.session:
            raise RuntimeError("Not connected to server")

        try:
            # List tools
            tools_response = await self.session.list_tools()

            self.tools = []
            for tool in tools_response.tools:
                tool_info = MCPToolInfo(
                    name=tool.name,
                    description=tool.description or "",
                    input_schema=tool.inputSchema or {},
                    server_name=self.config.name,
                )
                self.tools.append(tool_info)

            logger.info(
                "Discovered tools",
                server=self.config.name,
                tools=[t.name for t in self.tools],
            )

        except Exception as e:
            logger.error(
                "Failed to discover tools",
                server=self.config.name,
                error=str(e),
            )
            raise

    async def _discover_tools_http(self) -> None:
        """Discover available tools via HTTP transport."""
        try:
            # Send tools/list request
            self._message_id += 1
            request = {
                "jsonrpc": "2.0",
                "id": self._message_id,
                "method": "tools/list",
                "params": {}
            }

            response = await self._http_client.post(
                self._http_url,
                json=request,
                headers={"Content-Type": "application/json"}
            )
            response.raise_for_status()
            result = response.json()

            if "error" in result:
                raise RuntimeError(f"MCP error: {result['error']}")

            # Parse tools from response
            tools_data = result.get("result", {}).get("tools", [])
            self.tools = []

            for tool in tools_data:
                tool_info = MCPToolInfo(
                    name=tool.get("name", ""),
                    description=tool.get("description", ""),
                    input_schema=tool.get("inputSchema", {}),
                    server_name=self.config.name,
                )
                self.tools.append(tool_info)

            logger.info(
                "Discovered tools via HTTP",
                server=self.config.name,
                tool_count=len(self.tools),
            )

        except Exception as e:
            logger.error(
                "Failed to discover tools via HTTP",
                server=self.config.name,
                error=str(e),
            )
            raise

    async def _call_tool_http(self, tool_name: str, arguments: Dict[str, Any]) -> Any:
        """Call a tool via HTTP transport.

        Args:
            tool_name: Name of the tool
            arguments: Tool arguments

        Returns:
            Tool result
        """
        self._message_id += 1
        request = {
            "jsonrpc": "2.0",
            "id": self._message_id,
            "method": "tools/call",
            "params": {
                "name": tool_name,
                "arguments": arguments
            }
        }

        response = await self._http_client.post(
            self._http_url,
            json=request,
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()
        result = response.json()

        if "error" in result:
            raise RuntimeError(f"MCP tool call failed: {result['error']}")

        return result.get("result", {})

    async def _discover_tools_with_retry(self, max_retries: int = 3) -> None:
        """Discover tools with retry logic for SSE connections.

        SSE connections may have timing issues where the endpoint event
        hasn't been received yet. This method retries tool discovery
        with exponential backoff.

        Args:
            max_retries: Maximum number of retry attempts
        """
        for attempt in range(max_retries):
            try:
                await self._discover_tools()
                if self.tools:  # Success if we got tools
                    return

                # Got empty tools list - might be timing issue
                if attempt < max_retries - 1:
                    wait_time = 0.5 * (2 ** attempt)
                    logger.warning(
                        "Tool discovery returned 0 tools, retrying",
                        server=self.config.name,
                        attempt=attempt + 1,
                        wait_time=wait_time,
                    )
                    await asyncio.sleep(wait_time)

            except Exception as e:
                if attempt == max_retries - 1:
                    raise

                wait_time = 0.5 * (2 ** attempt)
                logger.warning(
                    "Tool discovery failed, retrying",
                    server=self.config.name,
                    attempt=attempt + 1,
                    wait_time=wait_time,
                    error=str(e),
                )
                await asyncio.sleep(wait_time)

    async def call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Any:
        """Call a tool on this server.

        Args:
            tool_name: Name of the tool
            arguments: Tool arguments

        Returns:
            Tool result
        """
        logger.debug(
            "Calling MCP tool",
            server=self.config.name,
            tool=tool_name,
            arguments=arguments,
        )

        try:
            # Route to appropriate transport
            if self.config.transport == "http":
                result = await self._call_tool_http(tool_name, arguments)
                logger.debug("MCP tool call completed", server=self.config.name, tool=tool_name)

                # HTTP returns dict directly
                if isinstance(result, dict) and "content" in result:
                    content = result["content"]
                    if isinstance(content, list) and len(content) > 0:
                        first = content[0]
                        if isinstance(first, dict) and "text" in first:
                            return first["text"]
                return result

            else:
                # SSE/stdio transport uses session
                if not self.session:
                    raise RuntimeError("Not connected to server")

                result = await self.session.call_tool(tool_name, arguments)

                logger.debug("MCP tool call completed", server=self.config.name, tool=tool_name)

                # Extract content from result
                if hasattr(result, "content") and result.content:
                    # Return first content item's text
                    if len(result.content) > 0:
                        content_item = result.content[0]
                        if hasattr(content_item, "text"):
                            return content_item.text
                        return str(content_item)

                return str(result)

        except Exception as e:
            logger.error(
                "MCP tool call failed",
                server=self.config.name,
                tool=tool_name,
                error=str(e),
            )
            raise

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Exit async context manager - signal disconnect and wait for task.

        Args:
            exc_type: Exception type if an exception occurred
            exc_val: Exception value if an exception occurred
            exc_tb: Exception traceback if an exception occurred
        """
        logger.info("Disconnecting from MCP server", server=self.config.name)

        # Signal the background task to disconnect
        self._disconnect_event.set()

        # Wait for the background task to complete
        if self._connection_task:
            try:
                await self._connection_task
            except Exception as e:
                logger.warning(
                    "Error during disconnect task completion",
                    server=self.config.name,
                    error=str(e),
                )

        # Clean up
        self.session = None
        self._connection_task = None

        logger.debug(
            "Disconnected from MCP server",
            server=self.config.name,
        )


class MCPRegistry:
    """Registry of all configured MCP servers."""

    def __init__(self, config: CoreConfig):
        """Initialize MCP registry.

        Args:
            config: Application configuration
        """
        self.config = config
        self.connectors: Dict[str, MCPServerConnector] = {}

        logger.info("Initialized MCPRegistry")

    async def connect_all(self) -> None:
        """Connect to all configured MCP servers.

        This method enters the async context for each connector,
        following the proper async with pattern.
        """
        logger.info(
            "Connecting to MCP servers",
            server_count=len(self.config.mcp.servers),
        )

        # Create connectors
        for server_config in self.config.mcp.servers:
            connector = MCPServerConnector(server_config)
            self.connectors[server_config.name] = connector

        # Enter all connector contexts in parallel using proper async with pattern
        # We collect the futures to handle errors properly
        results = await asyncio.gather(
            *[connector.__aenter__() for connector in self.connectors.values()],
            return_exceptions=True,
        )

        # Check for connection errors
        errors = [r for r in results if isinstance(r, Exception)]
        if errors:
            logger.warning(
                "Some MCP servers failed to connect",
                error_count=len(errors),
                errors=[str(e) for e in errors],
            )

        logger.info("MCP servers connected", servers=list(self.connectors.keys()))

    async def disconnect_all(self) -> None:
        """Disconnect from all MCP servers.

        This method exits the async context for each connector,
        ensuring proper cleanup in reverse order.
        """
        logger.info("Disconnecting from all MCP servers")

        # Exit all connector contexts in parallel
        await asyncio.gather(
            *[
                connector.__aexit__(None, None, None)
                for connector in self.connectors.values()
            ],
            return_exceptions=True,
        )

        self.connectors.clear()

    def get_all_tools(self) -> Dict[str, List[MCPToolInfo]]:
        """Get all tools organized by server.

        Returns:
            Dictionary mapping server names to lists of tools
        """
        tools_by_server = {}

        for server_name, connector in self.connectors.items():
            tools_by_server[server_name] = connector.tools

        return tools_by_server

    def get_tool_info(self, server_name: str, tool_name: str) -> Optional[MCPToolInfo]:
        """Get information about a specific tool.

        Args:
            server_name: Name of the server
            tool_name: Name of the tool

        Returns:
            Tool info or None if not found
        """
        connector = self.connectors.get(server_name)
        if not connector:
            return None

        for tool in connector.tools:
            if tool.name == tool_name:
                return tool

        return None

    async def call_tool(
        self,
        server_name: str,
        tool_name: str,
        arguments: Dict[str, Any],
    ) -> Any:
        """Call a tool on a specific server.

        Args:
            server_name: Name of the server
            tool_name: Name of the tool
            arguments: Tool arguments

        Returns:
            Tool result
        """
        connector = self.connectors.get(server_name)
        if not connector:
            raise ValueError(f"Server not found: {server_name}")

        return await connector.call_tool(tool_name, arguments)

    async def __aenter__(self):
        """Async context manager entry."""
        await self.connect_all()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.disconnect_all()
