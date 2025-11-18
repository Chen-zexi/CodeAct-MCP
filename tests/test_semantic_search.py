#!/usr/bin/env python3
"""
Test script for semantic search tool discovery.

This script tests the new tool discovery tools:
1. Tool indexer generates correct metadata
2. search_tools finds relevant tools by meaning
3. list_tool_categories returns all categories
4. list_tools_by_category returns tools in category
5. get_tool_info returns detailed tool information
"""

import asyncio
import sys
import traceback
import importlib.util

# Add project to path
sys.path.insert(0, "/Users/chen/projects/codeact-mcp")

from src.codeact_mcp.session import SessionManager
from src.codeact_mcp.config import CoreConfig


# Import search tools directly to avoid initialization issues
def load_module_from_path(module_name, file_path):
    """Load a module directly from file path."""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


semantic_module = load_module_from_path(
    "semantic_tools",
    "/Users/chen/projects/codeact-mcp/src/agent/tools/search/semantic_tools.py"
)

create_search_tools_tool = semantic_module.create_search_tools_tool
create_list_categories_tool = semantic_module.create_list_categories_tool
create_list_by_category_tool = semantic_module.create_list_by_category_tool
create_get_tool_info_tool = semantic_module.create_get_tool_info_tool


class TestResult:
    """Track test results."""
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.errors = []

    def success(self, name: str, details: str = ""):
        self.passed += 1
        print(f"✅ PASS: {name}")
        if details:
            print(f"   {details}")

    def failure(self, name: str, reason: str):
        self.failed += 1
        self.errors.append((name, reason))
        print(f"❌ FAIL: {name}")
        print(f"   Reason: {reason}")

    def summary(self):
        total = self.passed + self.failed
        print("\n" + "=" * 60)
        print(f"TEST SUMMARY: {self.passed}/{total} passed")
        if self.errors:
            print("\nFailed tests:")
            for name, reason in self.errors:
                print(f"  - {name}: {reason}")
        print("=" * 60)


async def test_tool_index_generation(sandbox, results: TestResult):
    """Test that tool index is generated correctly."""
    print("\n" + "=" * 60)
    print("TEST: Tool Index Generation")
    print("=" * 60)

    try:
        # Check that tool_index.json exists
        content = sandbox.read_file("/home/daytona/tools/tool_index.json")
        if not content:
            results.failure("Tool index exists", "tool_index.json not found")
            return

        import json
        index = json.loads(content)

        # Check structure
        if "tools" not in index:
            results.failure("Tool index structure", "Missing 'tools' key")
            return

        if "categories" not in index:
            results.failure("Tool index structure", "Missing 'categories' key")
            return

        tool_count = len(index["tools"])
        category_count = len(index["categories"])

        print(f"   Tools indexed: {tool_count}")
        print(f"   Categories: {list(index['categories'].keys())}")

        if tool_count > 100:
            results.success("Tool index generation", f"Indexed {tool_count} tools in {category_count} categories")
        else:
            results.failure("Tool index generation", f"Expected 100+ tools, got {tool_count}")

        # Check tool entry structure
        if index["tools"]:
            sample_tool = index["tools"][0]
            required_fields = ["name", "description", "category", "parameters", "searchable_text"]
            missing = [f for f in required_fields if f not in sample_tool]
            if missing:
                results.failure("Tool entry structure", f"Missing fields: {missing}")
            else:
                results.success("Tool entry structure", f"All required fields present")

    except Exception as e:
        results.failure("Tool index generation", str(e))
        traceback.print_exc()


async def test_search_tools(search_tool, results: TestResult):
    """Test semantic search functionality."""
    print("\n" + "=" * 60)
    print("TEST: search_tools")
    print("=" * 60)

    test_cases = [
        ("inflation rate", ["CPI", "INFLATION"], "Economic indicators"),
        ("stock price history", ["TIME_SERIES"], "Price data"),
        ("calculate beta market", ["BETA"], "Technical indicator"),
        ("moving average", ["SMA", "EMA", "WMA"], "Moving averages"),
        ("earnings report", ["EARNINGS"], "Fundamentals"),
    ]

    for query, expected_tools, description in test_cases:
        try:
            result = await search_tool.ainvoke({"query": query, "top_k": 5})
            print(f"\n--- Query: '{query}' ({description}) ---")
            print(f"Result preview: {result[:300]}...")

            # Check if any expected tool is in the results
            found = any(tool in result.upper() for tool in expected_tools)
            if found:
                results.success(f"search_tools: {query}", f"Found expected tools")
            else:
                results.failure(f"search_tools: {query}", f"Expected one of {expected_tools}")

        except Exception as e:
            results.failure(f"search_tools: {query}", str(e))
            traceback.print_exc()


async def test_list_categories(list_categories_tool, results: TestResult):
    """Test category listing."""
    print("\n" + "=" * 60)
    print("TEST: list_tool_categories")
    print("=" * 60)

    try:
        result = await list_categories_tool.ainvoke({})
        print(f"Result:\n{result}")

        # Check for expected categories
        expected_categories = ["technical_indicators", "economic_indicators", "price_data"]
        found = all(cat in result.lower() for cat in expected_categories)

        if found:
            results.success("list_tool_categories", "Found expected categories")
        else:
            results.failure("list_tool_categories", f"Missing some expected categories: {expected_categories}")

    except Exception as e:
        results.failure("list_tool_categories", str(e))
        traceback.print_exc()


async def test_list_by_category(list_by_category_tool, results: TestResult):
    """Test listing tools by category."""
    print("\n" + "=" * 60)
    print("TEST: list_tools_by_category")
    print("=" * 60)

    test_cases = [
        ("technical_indicators", ["SMA", "RSI", "MACD", "BETA"]),
        ("economic_indicators", ["CPI", "GDP"]),
        ("price_data", ["TIME_SERIES"]),
    ]

    for category, expected_tools in test_cases:
        try:
            result = await list_by_category_tool.ainvoke({"category": category})
            print(f"\n--- Category: {category} ---")
            print(f"Result preview: {result[:400]}...")

            # Check if expected tools are in results
            found = any(tool in result.upper() for tool in expected_tools)
            if found:
                results.success(f"list_tools_by_category: {category}", f"Found expected tools")
            else:
                results.failure(f"list_tools_by_category: {category}", f"Expected some of {expected_tools}")

        except Exception as e:
            results.failure(f"list_tools_by_category: {category}", str(e))
            traceback.print_exc()

    # Test invalid category
    try:
        result = await list_by_category_tool.ainvoke({"category": "nonexistent"})
        if "not found" in result.lower():
            results.success("list_tools_by_category: invalid", "Correctly handles invalid category")
        else:
            results.failure("list_tools_by_category: invalid", "Should report category not found")
    except Exception as e:
        results.failure("list_tools_by_category: invalid", str(e))


async def test_get_tool_info(get_tool_info_tool, results: TestResult):
    """Test getting detailed tool information."""
    print("\n" + "=" * 60)
    print("TEST: get_tool_info")
    print("=" * 60)

    test_tools = ["CPI", "BETA", "TIME_SERIES_DAILY"]

    for tool_name in test_tools:
        try:
            result = await get_tool_info_tool.ainvoke({"tool_name": tool_name})
            print(f"\n--- Tool: {tool_name} ---")
            print(f"Result preview: {result[:500]}...")

            # Check for expected sections
            has_description = "description" in result.lower() or tool_name in result
            has_parameters = "parameter" in result.lower()
            has_usage = "import" in result.lower() or "usage" in result.lower()

            if has_description and has_parameters:
                results.success(f"get_tool_info: {tool_name}", "Found description and parameters")
            else:
                results.failure(f"get_tool_info: {tool_name}", f"Missing sections (desc={has_description}, params={has_parameters})")

        except Exception as e:
            results.failure(f"get_tool_info: {tool_name}", str(e))
            traceback.print_exc()

    # Test invalid tool
    try:
        result = await get_tool_info_tool.ainvoke({"tool_name": "NONEXISTENT_TOOL"})
        if "not found" in result.lower():
            results.success("get_tool_info: invalid", "Correctly handles invalid tool")
        else:
            results.failure("get_tool_info: invalid", "Should report tool not found")
    except Exception as e:
        results.failure("get_tool_info: invalid", str(e))


async def main():
    """Main test function."""
    print("\n" + "=" * 60)
    print("SEMANTIC SEARCH TOOL DISCOVERY TEST")
    print("=" * 60)

    results = TestResult()
    session = None

    try:
        # Setup
        print("\n[SETUP] Initializing sandbox environment...")
        config = CoreConfig.load()
        session = SessionManager.get_session("semantic-search-test", config)
        await session.initialize()

        sandbox = session.sandbox
        print(f"  Sandbox ID: {sandbox.sandbox_id}")

        # Create tools
        print("\n[SETUP] Creating semantic search tools...")
        search_tool = create_search_tools_tool(sandbox)
        list_categories_tool = create_list_categories_tool(sandbox)
        list_by_category_tool = create_list_by_category_tool(sandbox)
        get_tool_info_tool = create_get_tool_info_tool(sandbox)
        print("  Created: search_tools, list_tool_categories, list_tools_by_category, get_tool_info")

        # Run tests
        print("\n[TEST] Running semantic search tests...")
        await test_tool_index_generation(sandbox, results)
        await test_search_tools(search_tool, results)
        await test_list_categories(list_categories_tool, results)
        await test_list_by_category(list_by_category_tool, results)
        await test_get_tool_info(get_tool_info_tool, results)

    except Exception as e:
        print(f"\n❌ FATAL ERROR: {e}")
        traceback.print_exc()
        results.failure("Setup/Execution", str(e))

    finally:
        # Cleanup
        if session:
            print("\n[CLEANUP] Cleaning up session...")
            await SessionManager.cleanup_session("semantic-search-test")

        # Summary
        results.summary()

        return 0 if results.failed == 0 else 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
