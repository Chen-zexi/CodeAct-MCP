"""
Tool Indexer - Generate searchable metadata for MCP tools.

This module creates a structured index of all MCP tools with:
- Name, description, parameters
- Automatic categorization
- Searchable text for semantic matching
"""

import json
import re
from typing import Any, Dict, List, Optional
import structlog

from .mcp_registry import MCPToolInfo

logger = structlog.get_logger()

# Category definitions with keyword patterns
CATEGORY_PATTERNS = {
    "price_data": [
        r"TIME_SERIES",
        r"GLOBAL_QUOTE",
        r"price",
        r"quote",
        r"intraday",
        r"daily",
        r"weekly",
        r"monthly",
    ],
    "technical_indicators": [
        r"SMA",
        r"EMA",
        r"WMA",
        r"DEMA",
        r"TEMA",
        r"TRIMA",
        r"KAMA",
        r"MAMA",
        r"T3",
        r"MACD",
        r"RSI",
        r"STOCH",
        r"ADX",
        r"CCI",
        r"AROON",
        r"BBANDS",
        r"ATR",
        r"OBV",
        r"AD\b",
        r"TRIX",
        r"ULTOSC",
        r"MFI",
        r"WILLR",
        r"ROC",
        r"MOM",
        r"BOP",
        r"CMO",
        r"PPO",
        r"APO",
        r"MIDPOINT",
        r"MIDPRICE",
        r"SAR",
        r"TRANGE",
        r"NATR",
        r"HT_",
        r"BETA",
        r"VWAP",
    ],
    "economic_indicators": [
        r"CPI",
        r"INFLATION",
        r"GDP",
        r"UNEMPLOYMENT",
        r"TREASURY",
        r"FEDERAL_FUNDS",
        r"RETAIL_SALES",
        r"NONFARM",
        r"DURABLES",
        r"economic",
    ],
    "fundamentals": [
        r"BALANCE_SHEET",
        r"INCOME_STATEMENT",
        r"CASH_FLOW",
        r"EARNINGS",
        r"OVERVIEW",
        r"LISTING",
        r"ETF",
        r"IPO",
        r"INSIDER",
        r"fundamental",
        r"financial statement",
    ],
    "forex": [
        r"FX_",
        r"CURRENCY_EXCHANGE",
        r"forex",
        r"exchange rate",
    ],
    "crypto": [
        r"DIGITAL_CURRENCY",
        r"CRYPTO",
        r"crypto",
        r"bitcoin",
        r"ethereum",
    ],
    "commodities": [
        r"COMMODITY",
        r"WTI",
        r"BRENT",
        r"NATURAL_GAS",
        r"COPPER",
        r"ALUMINUM",
        r"WHEAT",
        r"CORN",
        r"COTTON",
        r"SUGAR",
        r"COFFEE",
        r"ALL_COMMODITIES",
    ],
    "options": [
        r"OPTION",
        r"option",
        r"call",
        r"put",
        r"strike",
    ],
    "analytics": [
        r"ANALYTICS",
        r"analytics",
        r"window",
    ],
    "search": [
        r"SEARCH",
        r"search",
        r"SYMBOL_SEARCH",
    ],
}


class ToolIndexer:
    """Generate and manage tool metadata index."""

    def __init__(self):
        self.tools: List[Dict[str, Any]] = []
        self.categories: Dict[str, List[str]] = {}

    def add_tools(self, tools: List[MCPToolInfo]) -> None:
        """Add tools to the index.

        Args:
            tools: List of MCPToolInfo objects
        """
        for tool in tools:
            tool_entry = self._create_tool_entry(tool)
            self.tools.append(tool_entry)

            # Add to category index
            category = tool_entry["category"]
            if category not in self.categories:
                self.categories[category] = []
            self.categories[category].append(tool_entry["name"])

        logger.info(
            "Added tools to index",
            tool_count=len(tools),
            categories=list(self.categories.keys()),
        )

    def _create_tool_entry(self, tool: MCPToolInfo) -> Dict[str, Any]:
        """Create a structured entry for a tool.

        Args:
            tool: MCPToolInfo object

        Returns:
            Dictionary with tool metadata
        """
        # Extract parameters from input_schema
        parameters = self._extract_parameters(tool.input_schema)

        # Determine category
        category = self._categorize_tool(tool.name, tool.description)

        # Create searchable text combining all relevant info
        searchable_text = self._create_searchable_text(
            tool.name, tool.description, parameters
        )

        return {
            "name": tool.name,
            "description": tool.description,
            "server": tool.server_name,
            "category": category,
            "parameters": parameters,
            "required_params": self._get_required_params(tool.input_schema),
            "searchable_text": searchable_text,
        }

    def _extract_parameters(self, input_schema: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Extract parameter information from JSON schema.

        Args:
            input_schema: JSON schema for tool input

        Returns:
            List of parameter dictionaries
        """
        parameters = []
        properties = input_schema.get("properties", {})
        required = input_schema.get("required", [])

        for name, schema in properties.items():
            param = {
                "name": name,
                "type": schema.get("type", "any"),
                "description": schema.get("description", ""),
                "required": name in required,
            }
            if "enum" in schema:
                param["enum"] = schema["enum"]
            if "default" in schema:
                param["default"] = schema["default"]
            parameters.append(param)

        return parameters

    def _get_required_params(self, input_schema: Dict[str, Any]) -> List[str]:
        """Get list of required parameter names.

        Args:
            input_schema: JSON schema for tool input

        Returns:
            List of required parameter names
        """
        return input_schema.get("required", [])

    def _categorize_tool(self, name: str, description: str) -> str:
        """Determine the category for a tool.

        Args:
            name: Tool name
            description: Tool description

        Returns:
            Category name
        """
        combined = f"{name} {description}"

        for category, patterns in CATEGORY_PATTERNS.items():
            for pattern in patterns:
                if re.search(pattern, combined, re.IGNORECASE):
                    return category

        return "other"

    def _create_searchable_text(
        self, name: str, description: str, parameters: List[Dict[str, Any]]
    ) -> str:
        """Create combined searchable text for semantic matching.

        Args:
            name: Tool name
            description: Tool description
            parameters: List of parameter info

        Returns:
            Combined searchable text
        """
        parts = [name, description]

        # Add parameter names and descriptions
        for param in parameters:
            parts.append(param["name"])
            if param.get("description"):
                parts.append(param["description"])

        # Add synonyms/related terms based on name
        synonyms = self._get_synonyms(name, description)
        parts.extend(synonyms)

        return " ".join(parts)

    def _get_synonyms(self, name: str, description: str) -> List[str]:
        """Get synonyms and related terms for better semantic matching.

        Args:
            name: Tool name
            description: Tool description

        Returns:
            List of synonym terms
        """
        synonyms = []

        # Add common synonyms
        synonym_map = {
            "CPI": ["consumer price index", "inflation", "cost of living"],
            "GDP": ["gross domestic product", "economic output", "economy size"],
            "SMA": ["simple moving average", "moving average", "trend"],
            "EMA": ["exponential moving average", "weighted average", "trend"],
            "RSI": ["relative strength index", "overbought", "oversold", "momentum"],
            "MACD": ["moving average convergence divergence", "momentum", "trend"],
            "BETA": ["market risk", "volatility", "systematic risk", "correlation"],
            "ATR": ["average true range", "volatility", "range"],
            "BBANDS": ["bollinger bands", "volatility", "standard deviation"],
            "STOCH": ["stochastic", "oscillator", "momentum"],
            "TIME_SERIES": ["historical prices", "price history", "stock data"],
            "GLOBAL_QUOTE": ["current price", "latest quote", "real-time price"],
            "BALANCE_SHEET": ["assets", "liabilities", "equity", "financial position"],
            "INCOME_STATEMENT": ["revenue", "profit", "earnings", "P&L"],
            "CASH_FLOW": ["cash flow statement", "operating cash", "free cash flow"],
            "EARNINGS": ["EPS", "earnings per share", "quarterly results"],
            "OPTION": ["options", "derivatives", "call", "put", "strike price"],
            "UNEMPLOYMENT": ["jobs", "labor market", "employment rate"],
            "TREASURY": ["bonds", "yield", "interest rate", "government debt"],
        }

        for key, terms in synonym_map.items():
            if key in name.upper():
                synonyms.extend(terms)

        return synonyms

    def generate_index(self) -> Dict[str, Any]:
        """Generate the complete tool index.

        Returns:
            Dictionary with tools and category index
        """
        return {
            "version": "1.0",
            "tool_count": len(self.tools),
            "categories": self.categories,
            "tools": self.tools,
        }

    def save_index(self, filepath: str) -> None:
        """Save the index to a JSON file.

        Args:
            filepath: Path to save the index
        """
        index = self.generate_index()
        with open(filepath, "w") as f:
            json.dump(index, f, indent=2)
        logger.info("Saved tool index", filepath=filepath, tool_count=len(self.tools))

    def get_tools_by_category(self, category: str) -> List[str]:
        """Get tool names in a category.

        Args:
            category: Category name

        Returns:
            List of tool names
        """
        return self.categories.get(category, [])

    def get_all_categories(self) -> List[str]:
        """Get all category names.

        Returns:
            List of category names
        """
        return list(self.categories.keys())

    def search_tools(self, query: str) -> List[Dict[str, Any]]:
        """Simple keyword search across tools.

        Args:
            query: Search query

        Returns:
            List of matching tool entries
        """
        query_lower = query.lower()
        matches = []

        for tool in self.tools:
            if query_lower in tool["searchable_text"].lower():
                matches.append(tool)

        return matches


def create_tool_index(tools: List[MCPToolInfo]) -> ToolIndexer:
    """Create a tool index from MCP tools.

    Args:
        tools: List of MCPToolInfo objects

    Returns:
        ToolIndexer with tools added
    """
    indexer = ToolIndexer()
    indexer.add_tools(tools)
    return indexer
