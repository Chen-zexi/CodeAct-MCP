#!/usr/bin/env python3
"""
Test script for measuring agent search effectiveness.

This script establishes a baseline for how effectively agents can use
Glob, Grep, and Bash tools to find documentation and resources in the sandbox.

Results are stored in test_output/ for comparison.
"""

import asyncio
import json
import os
import sys
import time
import traceback
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional
import importlib.util

# Add project to path
sys.path.insert(0, "/Users/chen/projects/codeact-mcp")

from src.codeact_mcp.session import SessionManager
from src.codeact_mcp.config import CoreConfig

# Import search tools directly to avoid Tavily initialization issue
def load_module_from_path(module_name, file_path):
    """Load a module directly from file path."""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

glob_module = load_module_from_path(
    "glob_tool",
    "/Users/chen/projects/codeact-mcp/src/agent/langchain_tools/search/glob.py"
)
grep_module = load_module_from_path(
    "grep_tool",
    "/Users/chen/projects/codeact-mcp/src/agent/langchain_tools/search/grep.py"
)
bash_module = load_module_from_path(
    "bash_tool",
    "/Users/chen/projects/codeact-mcp/src/agent/langchain_tools/bash/execute.py"
)

create_glob_tool = glob_module.create_glob_tool
create_grep_tool = grep_module.create_grep_tool
create_execute_bash_tool = bash_module.create_execute_bash_tool


class TestResult:
    """Capture results for a single tool test."""
    def __init__(self):
        self.success = False
        self.result_count = 0
        self.duration_ms = 0
        self.raw_result = ""
        self.error = None
        self.params = {}

    def to_dict(self) -> Dict:
        return {
            "success": self.success,
            "result_count": self.result_count,
            "duration_ms": self.duration_ms,
            "raw_result": self.raw_result[:2000] if len(self.raw_result) > 2000 else self.raw_result,
            "error": str(self.error) if self.error else None,
            "params": self.params
        }


class ScenarioResult:
    """Capture results for a search scenario across all tools."""
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.tools_tested: Dict[str, TestResult] = {}

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "description": self.description,
            "tools_tested": {
                tool: result.to_dict()
                for tool, result in self.tools_tested.items()
            }
        }


class BaselineResults:
    """Capture all baseline results."""
    def __init__(self):
        self.timestamp = datetime.utcnow().isoformat() + "Z"
        self.sandbox_id = ""
        self.scenarios: List[ScenarioResult] = []
        self.errors: List[str] = []

    def add_scenario(self, scenario: ScenarioResult):
        self.scenarios.append(scenario)

    def to_dict(self) -> Dict:
        # Calculate summary
        total_tests = 0
        passed = 0
        tool_stats: Dict[str, Dict] = {}

        for scenario in self.scenarios:
            for tool_name, result in scenario.tools_tested.items():
                total_tests += 1
                if result.success:
                    passed += 1

                if tool_name not in tool_stats:
                    tool_stats[tool_name] = {
                        "total": 0,
                        "success": 0,
                        "total_duration_ms": 0
                    }

                tool_stats[tool_name]["total"] += 1
                if result.success:
                    tool_stats[tool_name]["success"] += 1
                tool_stats[tool_name]["total_duration_ms"] += result.duration_ms

        tool_comparison = {}
        for tool_name, stats in tool_stats.items():
            tool_comparison[tool_name] = {
                "avg_duration_ms": round(stats["total_duration_ms"] / stats["total"], 2) if stats["total"] > 0 else 0,
                "success_rate": round(stats["success"] / stats["total"], 2) if stats["total"] > 0 else 0
            }

        return {
            "timestamp": self.timestamp,
            "sandbox_id": self.sandbox_id,
            "scenarios": [s.to_dict() for s in self.scenarios],
            "errors": self.errors,
            "summary": {
                "total_tests": total_tests,
                "passed": passed,
                "tool_comparison": tool_comparison
            }
        }


async def run_tool_test(tool, params: Dict, validator_func) -> TestResult:
    """Run a single tool test and capture results."""
    result = TestResult()
    result.params = params

    start_time = time.time()
    try:
        raw_result = await tool.ainvoke(params)
        result.raw_result = raw_result
        result.duration_ms = int((time.time() - start_time) * 1000)

        # Validate result
        result.success, result.result_count = validator_func(raw_result)
    except Exception as e:
        result.duration_ms = int((time.time() - start_time) * 1000)
        result.error = str(e)
        result.success = False

    return result


async def scenario_tool_discovery(glob_tool, grep_tool, bash_tool) -> ScenarioResult:
    """Scenario A: Find all available tools in the alphavantage module."""
    scenario = ScenarioResult(
        "tool_discovery",
        "Find all Python files in the tools directory"
    )

    # Test Glob
    def validate_glob(result):
        files_found = result.count(".py")
        # Should find at least mcp_client.py, tavily.py, alphavantage.py, __init__.py
        return files_found >= 3, files_found

    result = await run_tool_test(
        glob_tool,
        {"pattern": "*.py", "path": "tools"},
        validate_glob
    )
    scenario.tools_tested["Glob"] = result
    print(f"  Glob: {'PASS' if result.success else 'FAIL'} ({result.result_count} files, {result.duration_ms}ms)")

    # Test Grep
    def validate_grep(result):
        # Search for "def " to find function definitions
        matches = result.count(":")
        return matches > 0, matches

    result = await run_tool_test(
        grep_tool,
        {"pattern": "^def ", "path": "tools", "glob": "*.py", "output_mode": "files_with_matches"},
        validate_grep
    )
    scenario.tools_tested["Grep"] = result
    print(f"  Grep: {'PASS' if result.success else 'FAIL'} ({result.result_count} matches, {result.duration_ms}ms)")

    # Test Bash
    def validate_bash(result):
        files_found = result.count(".py")
        return files_found >= 3, files_found

    result = await run_tool_test(
        bash_tool,
        {"command": "ls -la tools/*.py", "description": "List Python files in tools"},
        validate_bash
    )
    scenario.tools_tested["Bash"] = result
    print(f"  Bash: {'PASS' if result.success else 'FAIL'} ({result.result_count} files, {result.duration_ms}ms)")

    return scenario


async def scenario_docs_lookup(glob_tool, grep_tool, bash_tool) -> ScenarioResult:
    """Scenario B: Find documentation for a specific tool (GLOBAL_QUOTE or similar)."""
    scenario = ScenarioResult(
        "documentation_lookup",
        "Find documentation for a specific tool"
    )

    # Test Glob - find all doc files
    def validate_glob(result):
        files_found = result.count(".md")
        return files_found > 0, files_found

    result = await run_tool_test(
        glob_tool,
        {"pattern": "*.md", "path": "tools/docs"},
        validate_glob
    )
    scenario.tools_tested["Glob"] = result
    print(f"  Glob: {'PASS' if result.success else 'FAIL'} ({result.result_count} docs, {result.duration_ms}ms)")

    # Test Grep - search for specific content in docs
    def validate_grep(result):
        matches = result.count(":")
        return matches > 0, matches

    result = await run_tool_test(
        grep_tool,
        {"pattern": "symbol", "path": "tools/docs", "output_mode": "files_with_matches"},
        validate_grep
    )
    scenario.tools_tested["Grep"] = result
    print(f"  Grep: {'PASS' if result.success else 'FAIL'} ({result.result_count} matches, {result.duration_ms}ms)")

    # Test Bash
    def validate_bash(result):
        files_found = result.count(".md")
        return files_found > 0, files_found

    result = await run_tool_test(
        bash_tool,
        {"command": "ls tools/docs/*.md | head -20", "description": "List documentation files"},
        validate_bash
    )
    scenario.tools_tested["Bash"] = result
    print(f"  Bash: {'PASS' if result.success else 'FAIL'} ({result.result_count} files, {result.duration_ms}ms)")

    return scenario


async def scenario_parameter_search(glob_tool, grep_tool, bash_tool) -> ScenarioResult:
    """Scenario C: Find all tools that accept a 'symbol' parameter."""
    scenario = ScenarioResult(
        "parameter_search",
        "Find all tools that accept a 'symbol' parameter"
    )

    # Glob can't search content, so skip or use as file finder
    def validate_glob(result):
        # Just find Python files - not ideal for this task
        files_found = result.count(".py")
        return files_found >= 1, files_found

    result = await run_tool_test(
        glob_tool,
        {"pattern": "*.py", "path": "tools"},
        validate_glob
    )
    scenario.tools_tested["Glob"] = result
    print(f"  Glob: {'PASS' if result.success else 'FAIL'} ({result.result_count} files, {result.duration_ms}ms)")

    # Test Grep - search for symbol parameter
    def validate_grep(result):
        matches = result.count("symbol")
        return matches > 0, matches

    result = await run_tool_test(
        grep_tool,
        {"pattern": "symbol", "path": "tools", "glob": "*.py", "output_mode": "content"},
        validate_grep
    )
    scenario.tools_tested["Grep"] = result
    print(f"  Grep: {'PASS' if result.success else 'FAIL'} ({result.result_count} occurrences, {result.duration_ms}ms)")

    # Test Bash with grep
    def validate_bash(result):
        matches = result.count("symbol")
        return matches > 0, matches

    result = await run_tool_test(
        bash_tool,
        {"command": "grep -r 'symbol' tools/*.py | head -30", "description": "Search for symbol parameter"},
        validate_bash
    )
    scenario.tools_tested["Bash"] = result
    print(f"  Bash: {'PASS' if result.success else 'FAIL'} ({result.result_count} matches, {result.duration_ms}ms)")

    return scenario


async def scenario_content_search(glob_tool, grep_tool, bash_tool) -> ScenarioResult:
    """Scenario D: Find usage examples or specific content in documentation."""
    scenario = ScenarioResult(
        "content_search",
        "Find documentation containing specific terms"
    )

    # Glob - find all markdown files
    def validate_glob(result):
        files_found = result.count(".md")
        return files_found > 0, files_found

    result = await run_tool_test(
        glob_tool,
        {"pattern": "*.md", "path": "tools/docs"},
        validate_glob
    )
    scenario.tools_tested["Glob"] = result
    print(f"  Glob: {'PASS' if result.success else 'FAIL'} ({result.result_count} files, {result.duration_ms}ms)")

    # Grep - search for Returns section in docs
    def validate_grep(result):
        matches = result.count("Returns")
        return matches > 0, matches

    result = await run_tool_test(
        grep_tool,
        {"pattern": "Returns", "path": "tools/docs", "output_mode": "content", "A": 2},
        validate_grep
    )
    scenario.tools_tested["Grep"] = result
    print(f"  Grep: {'PASS' if result.success else 'FAIL'} ({result.result_count} matches, {result.duration_ms}ms)")

    # Bash - use grep
    def validate_bash(result):
        matches = result.count("Returns")
        return matches > 0, matches

    result = await run_tool_test(
        bash_tool,
        {"command": "grep -r 'Returns' tools/docs/ | head -20", "description": "Search for Returns in docs"},
        validate_bash
    )
    scenario.tools_tested["Bash"] = result
    print(f"  Bash: {'PASS' if result.success else 'FAIL'} ({result.result_count} matches, {result.duration_ms}ms)")

    return scenario


async def scenario_pattern_matching(glob_tool, grep_tool, bash_tool) -> ScenarioResult:
    """Scenario E: Complex pattern matching to find specific file types."""
    scenario = ScenarioResult(
        "pattern_matching",
        "Find files using complex patterns"
    )

    # Glob - find all files recursively (test ** pattern)
    def validate_glob(result):
        # Check if any files found
        if "No files" in result or "0 file" in result:
            return False, 0
        files_found = result.count("\n")
        return files_found > 0, files_found

    result = await run_tool_test(
        glob_tool,
        {"pattern": "**/*.md", "path": "tools"},
        validate_glob
    )
    scenario.tools_tested["Glob_recursive"] = result
    print(f"  Glob **: {'PASS' if result.success else 'FAIL'} ({result.result_count} files, {result.duration_ms}ms)")

    # Glob - simple pattern
    def validate_glob_simple(result):
        files_found = result.count(".md")
        return files_found > 0, files_found

    result = await run_tool_test(
        glob_tool,
        {"pattern": "*.md", "path": "tools/docs"},
        validate_glob_simple
    )
    scenario.tools_tested["Glob_simple"] = result
    print(f"  Glob *: {'PASS' if result.success else 'FAIL'} ({result.result_count} files, {result.duration_ms}ms)")

    # Grep - find files with specific extension content
    def validate_grep(result):
        matches = result.count(":")
        return matches > 0, matches

    result = await run_tool_test(
        grep_tool,
        {"pattern": "def.*\\(", "path": "tools", "glob": "*.py", "output_mode": "count"},
        validate_grep
    )
    scenario.tools_tested["Grep"] = result
    print(f"  Grep: {'PASS' if result.success else 'FAIL'} ({result.result_count} matches, {result.duration_ms}ms)")

    # Bash - find command
    def validate_bash(result):
        files_found = result.count(".md")
        return files_found > 0, files_found

    result = await run_tool_test(
        bash_tool,
        {"command": "find tools -name '*.md' | head -20", "description": "Find markdown files"},
        validate_bash
    )
    scenario.tools_tested["Bash"] = result
    print(f"  Bash: {'PASS' if result.success else 'FAIL'} ({result.result_count} files, {result.duration_ms}ms)")

    return scenario


def generate_summary(results: BaselineResults, output_dir: Path) -> str:
    """Generate a human-readable summary."""
    data = results.to_dict()
    summary = data["summary"]

    lines = [
        "# Search Effectiveness Baseline Report",
        f"\n**Generated**: {results.timestamp}",
        f"**Sandbox ID**: {results.sandbox_id}",
        "",
        "## Summary",
        f"- **Total Tests**: {summary['total_tests']}",
        f"- **Passed**: {summary['passed']} ({round(summary['passed']/summary['total_tests']*100, 1)}%)",
        "",
        "## Tool Comparison",
        "",
        "| Tool | Success Rate | Avg Duration (ms) |",
        "|------|-------------|-------------------|",
    ]

    for tool, stats in summary["tool_comparison"].items():
        lines.append(f"| {tool} | {stats['success_rate']*100:.0f}% | {stats['avg_duration_ms']:.0f} |")

    lines.extend([
        "",
        "## Scenario Results",
        ""
    ])

    for scenario in results.scenarios:
        lines.append(f"### {scenario.name}")
        lines.append(f"*{scenario.description}*")
        lines.append("")

        for tool, result in scenario.tools_tested.items():
            status = "PASS" if result.success else "FAIL"
            lines.append(f"- **{tool}**: {status} ({result.result_count} results, {result.duration_ms}ms)")
            if result.error:
                lines.append(f"  - Error: {result.error}")
        lines.append("")

    if results.errors:
        lines.extend([
            "## Errors",
            ""
        ])
        for error in results.errors:
            lines.append(f"- {error}")

    return "\n".join(lines)


async def main():
    """Main test function."""
    print("\n" + "=" * 60)
    print("AGENT SEARCH EFFECTIVENESS BASELINE TEST")
    print("=" * 60)

    results = BaselineResults()
    session = None

    # Create output directory
    output_dir = Path("/Users/chen/projects/codeact-mcp/test_output")
    output_dir.mkdir(exist_ok=True)

    try:
        # Setup
        print("\n[SETUP] Initializing sandbox environment...")
        config = CoreConfig.load()
        session = SessionManager.get_session("search-effectiveness-test", config)
        await session.initialize()

        sandbox = session.sandbox
        results.sandbox_id = sandbox.sandbox_id
        print(f"  Sandbox ID: {sandbox.sandbox_id}")

        # Create tools
        print("\n[SETUP] Creating tools...")
        glob_tool = create_glob_tool(sandbox)
        grep_tool = create_grep_tool(sandbox)
        bash_tool = create_execute_bash_tool(sandbox)
        print("  Created: Glob, Grep, Bash")

        # Run scenarios
        print("\n[TEST] Running search scenarios...\n")

        print("Scenario A: Tool Discovery")
        results.add_scenario(await scenario_tool_discovery(glob_tool, grep_tool, bash_tool))

        print("\nScenario B: Documentation Lookup")
        results.add_scenario(await scenario_docs_lookup(glob_tool, grep_tool, bash_tool))

        print("\nScenario C: Parameter Search")
        results.add_scenario(await scenario_parameter_search(glob_tool, grep_tool, bash_tool))

        print("\nScenario D: Content Search")
        results.add_scenario(await scenario_content_search(glob_tool, grep_tool, bash_tool))

        print("\nScenario E: Pattern Matching")
        results.add_scenario(await scenario_pattern_matching(glob_tool, grep_tool, bash_tool))

    except Exception as e:
        print(f"\n[ERROR] {e}")
        traceback.print_exc()
        results.errors.append(str(e))

    finally:
        # Cleanup
        if session:
            print("\n[CLEANUP] Cleaning up session...")
            await SessionManager.cleanup_session("search-effectiveness-test")

        # Save results
        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")

        # Save JSON
        json_path = output_dir / f"baseline_{timestamp}.json"
        with open(json_path, "w") as f:
            json.dump(results.to_dict(), f, indent=2)
        print(f"\n[OUTPUT] Saved baseline to: {json_path}")

        # Save summary
        summary_path = output_dir / f"summary_{timestamp}.md"
        summary = generate_summary(results, output_dir)
        with open(summary_path, "w") as f:
            f.write(summary)
        print(f"[OUTPUT] Saved summary to: {summary_path}")

        # Print summary
        data = results.to_dict()
        total = data["summary"]["total_tests"]
        passed = data["summary"]["passed"]
        print(f"\n{'=' * 60}")
        print(f"TEST SUMMARY: {passed}/{total} passed ({round(passed/total*100, 1)}%)")
        print("=" * 60)

        print("\nTool Comparison:")
        for tool, stats in data["summary"]["tool_comparison"].items():
            print(f"  {tool}: {stats['success_rate']*100:.0f}% success, {stats['avg_duration_ms']:.0f}ms avg")

        return 0 if passed == total else 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
