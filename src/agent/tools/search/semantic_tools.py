"""Semantic search tools for MCP tool discovery."""

import json
from typing import Any, List, Optional

import structlog
from langchain_core.tools import tool

logger = structlog.get_logger(__name__)


def create_search_tools_tool(sandbox: Any):
    """Factory function to create semantic tool search.

    Args:
        sandbox: CodeActSandbox instance

    Returns:
        Configured search_tools function
    """

    @tool
    async def search_tools(query: str, top_k: int = 5) -> str:
        """Search for MCP tools using semantic similarity.

        This tool finds the most relevant tools based on meaning, not just keywords.
        Use it when you need to find tools for a specific task or concept.

        Args:
            query: Natural language description of what you're looking for
                   Examples: "get stock price history", "inflation data", "calculate volatility"
            top_k: Number of results to return (default: 5)

        Returns:
            List of matching tools with descriptions and usage info

        Examples:
            Find tools for price data:
            query = "historical stock prices"

            Find economic indicators:
            query = "inflation rate data CPI"

            Find technical analysis tools:
            query = "calculate moving average trend"

            Find options data:
            query = "option chain call put strike"
        """
        try:
            logger.info("Searching tools semantically", query=query, top_k=top_k)

            # Load tool index
            index_path = "/home/daytona/tools/tool_index.json"
            content = sandbox.read_file(index_path)
            if not content:
                return "ERROR: Tool index not found. Run sandbox setup first."

            index = json.loads(content)
            tools = index.get("tools", [])

            if not tools:
                return "No tools found in index."

            # Simple semantic search using keyword matching and synonyms
            # For production, use sentence-transformers + FAISS
            query_lower = query.lower()
            query_terms = query_lower.split()

            scored_tools = []
            for tool_entry in tools:
                searchable = tool_entry.get("searchable_text", "").lower()
                name = tool_entry.get("name", "").lower()
                description = tool_entry.get("description", "").lower()

                # Score based on term matches
                score = 0

                # Exact name match gets highest score
                if query_lower in name:
                    score += 100

                # Full query in searchable text
                if query_lower in searchable:
                    score += 50

                # Individual term matches
                for term in query_terms:
                    if term in name:
                        score += 20
                    if term in description:
                        score += 10
                    if term in searchable:
                        score += 5

                if score > 0:
                    scored_tools.append((score, tool_entry))

            # Sort by score
            scored_tools.sort(key=lambda x: x[0], reverse=True)
            top_results = scored_tools[:top_k]

            if not top_results:
                return f"No tools found matching '{query}'. Try different keywords or check available categories with list_tool_categories."

            # Format results
            result = f"Found {len(top_results)} relevant tool(s) for '{query}':\n\n"
            for i, (score, tool_entry) in enumerate(top_results, 1):
                name = tool_entry["name"]
                desc = tool_entry.get("description", "No description")
                server = tool_entry.get("server", "unknown")
                category = tool_entry.get("category", "other")
                required = tool_entry.get("required_params", [])

                result += f"{i}. **{name}** (server: {server}, category: {category})\n"
                result += f"   {desc[:200]}{'...' if len(desc) > 200 else ''}\n"
                if required:
                    result += f"   Required params: {', '.join(required)}\n"
                result += f"   Import: from tools.{server} import {name}\n\n"

            logger.info(
                "Semantic search completed",
                query=query,
                results=len(top_results)
            )

            return result.rstrip()

        except Exception as e:
            error_msg = f"Failed to search tools: {str(e)}"
            logger.error(error_msg, query=query, error=str(e), exc_info=True)
            return f"ERROR: {error_msg}"

    return search_tools


def create_list_categories_tool(sandbox: Any):
    """Factory function to create category listing tool.

    Args:
        sandbox: CodeActSandbox instance

    Returns:
        Configured list_tool_categories function
    """

    @tool
    async def list_tool_categories() -> str:
        """List all available tool categories.

        Returns a list of categories that can be used with list_tools_by_category
        to explore available tools by domain.

        Returns:
            List of category names with tool counts
        """
        try:
            logger.info("Listing tool categories")

            # Load tool index
            index_path = "/home/daytona/tools/tool_index.json"
            content = sandbox.read_file(index_path)
            if not content:
                return "ERROR: Tool index not found. Run sandbox setup first."

            index = json.loads(content)
            categories = index.get("categories", {})

            if not categories:
                return "No categories found."

            # Format results
            result = "Available tool categories:\n\n"
            for category, tools in sorted(categories.items()):
                result += f"- **{category}**: {len(tools)} tools\n"

            result += "\nUse list_tools_by_category(category) to see tools in a specific category."

            logger.info("Listed categories", count=len(categories))

            return result

        except Exception as e:
            error_msg = f"Failed to list categories: {str(e)}"
            logger.error(error_msg, error=str(e), exc_info=True)
            return f"ERROR: {error_msg}"

    return list_tool_categories


def create_list_by_category_tool(sandbox: Any):
    """Factory function to create category browser tool.

    Args:
        sandbox: CodeActSandbox instance

    Returns:
        Configured list_tools_by_category function
    """

    @tool
    async def list_tools_by_category(category: str) -> str:
        """List all tools in a specific category.

        Args:
            category: Category name (use list_tool_categories to see available categories)
                      Examples: "technical_indicators", "economic_indicators", "price_data"

        Returns:
            List of tool names and brief descriptions in the category
        """
        try:
            logger.info("Listing tools by category", category=category)

            # Load tool index
            index_path = "/home/daytona/tools/tool_index.json"
            content = sandbox.read_file(index_path)
            if not content:
                return "ERROR: Tool index not found. Run sandbox setup first."

            index = json.loads(content)
            categories = index.get("categories", {})
            all_tools = {t["name"]: t for t in index.get("tools", [])}

            if category not in categories:
                available = ", ".join(sorted(categories.keys()))
                return f"Category '{category}' not found. Available categories: {available}"

            tool_names = categories[category]

            if not tool_names:
                return f"No tools in category '{category}'."

            # Format results
            result = f"Tools in category '{category}' ({len(tool_names)} total):\n\n"
            for name in sorted(tool_names):
                tool_info = all_tools.get(name, {})
                desc = tool_info.get("description", "")
                # Truncate description
                short_desc = desc[:100] + "..." if len(desc) > 100 else desc
                server = tool_info.get("server", "unknown")
                result += f"- **{name}**: {short_desc}\n"
                result += f"  Import: from tools.{server} import {name}\n"

            logger.info(
                "Listed tools by category",
                category=category,
                count=len(tool_names)
            )

            return result.rstrip()

        except Exception as e:
            error_msg = f"Failed to list tools: {str(e)}"
            logger.error(error_msg, category=category, error=str(e), exc_info=True)
            return f"ERROR: {error_msg}"

    return list_tools_by_category


def create_get_tool_info_tool(sandbox: Any):
    """Factory function to create tool info lookup.

    Args:
        sandbox: CodeActSandbox instance

    Returns:
        Configured get_tool_info function
    """

    @tool
    async def get_tool_info(tool_name: str) -> str:
        """Get detailed information about a specific tool.

        Args:
            tool_name: Name of the tool to look up
                       Example: "TIME_SERIES_DAILY", "CPI", "BETA"

        Returns:
            Full tool information including description, parameters, and usage example
        """
        try:
            logger.info("Getting tool info", tool_name=tool_name)

            # Load tool index
            index_path = "/home/daytona/tools/tool_index.json"
            content = sandbox.read_file(index_path)
            if not content:
                return "ERROR: Tool index not found. Run sandbox setup first."

            index = json.loads(content)
            tools = index.get("tools", [])

            # Find tool
            tool_info = None
            for t in tools:
                if t["name"].upper() == tool_name.upper():
                    tool_info = t
                    break

            if not tool_info:
                # Suggest similar tools
                similar = [t["name"] for t in tools if tool_name.upper() in t["name"].upper()][:5]
                if similar:
                    return f"Tool '{tool_name}' not found. Similar tools: {', '.join(similar)}"
                return f"Tool '{tool_name}' not found. Use search_tools to find available tools."

            # Format results
            name = tool_info["name"]
            desc = tool_info.get("description", "No description")
            server = tool_info.get("server", "unknown")
            category = tool_info.get("category", "other")
            params = tool_info.get("parameters", [])

            result = f"# {name}\n\n"
            result += f"**Server**: {server}\n"
            result += f"**Category**: {category}\n\n"
            result += f"## Description\n{desc}\n\n"

            if params:
                result += "## Parameters\n\n"
                for param in params:
                    pname = param["name"]
                    ptype = param.get("type", "any")
                    pdesc = param.get("description", "")
                    required = "required" if param.get("required") else "optional"
                    result += f"- **{pname}** ({ptype}, {required}): {pdesc}\n"
                    if "enum" in param:
                        result += f"  Values: {', '.join(param['enum'])}\n"
                    if "default" in param:
                        result += f"  Default: {param['default']}\n"

            result += f"\n## Usage\n\n```python\nfrom tools.{server} import {name}\n\n"

            # Generate example call
            required_params = [p for p in params if p.get("required")]
            if required_params:
                param_strs = [f'{p["name"]}="example"' for p in required_params]
                result += f"result = {name}({', '.join(param_strs)})\n"
            else:
                result += f"result = {name}()\n"

            result += "print(result)\n```"

            logger.info("Got tool info", tool_name=name)

            return result

        except Exception as e:
            error_msg = f"Failed to get tool info: {str(e)}"
            logger.error(error_msg, tool_name=tool_name, error=str(e), exc_info=True)
            return f"ERROR: {error_msg}"

    return get_tool_info
