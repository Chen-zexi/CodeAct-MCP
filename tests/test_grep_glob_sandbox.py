#!/usr/bin/env python3
"""
Test script for Grep and Glob tools in a real sandbox environment.

This script:
1. Sets up a Daytona sandbox with MCP tools
2. Creates test files in the sandbox
3. Tests Glob and Grep tool functionality
4. Provides detailed diagnostics if anything fails
"""

import asyncio
import sys
import traceback
import importlib.util
from typing import Any

# Add project to path
sys.path.insert(0, "/Users/chen/projects/codeact-mcp")

from src.codeact_mcp.session import SessionManager
from src.codeact_mcp.config import CoreConfig

# Import search tools directly to avoid Tavily initialization issue
def load_module_from_path(module_name, file_path):
    """Load a module directly from file path to bypass package import chain."""
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
create_glob_tool = glob_module.create_glob_tool
create_grep_tool = grep_module.create_grep_tool


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


async def setup_environment():
    """Set up the sandbox environment."""
    print("\n" + "=" * 60)
    print("SETUP: Initializing sandbox environment")
    print("=" * 60)

    # Load configuration
    print("\n1. Loading CoreConfig from config.yaml...")
    config = CoreConfig.load()
    print(f"   Daytona base URL: {config.daytona.base_url}")
    print(f"   Filesystem allowed dirs: {config.filesystem.allowed_directories}")
    print(f"   Path validation enabled: {config.filesystem.enable_path_validation}")

    # Create and initialize session
    print("\n2. Creating session...")
    session = SessionManager.get_session("test-grep-glob", config)

    print("\n3. Initializing session (this may take a moment)...")
    await session.initialize()
    print("   Session initialized successfully!")

    # Get sandbox info
    sandbox = session.sandbox
    print(f"\n4. Sandbox info:")
    print(f"   Sandbox ID: {sandbox.sandbox_id}")
    print(f"   Working directory: {getattr(sandbox, 'working_directory', 'unknown')}")

    # Get tools - create directly to avoid other import issues
    print("\n5. Creating Glob and Grep tools...")
    glob_tool = create_glob_tool(sandbox)
    grep_tool = create_grep_tool(sandbox)
    print(f"   Created tools: [{glob_tool.name}, {grep_tool.name}]")

    return session, sandbox, glob_tool, grep_tool


async def create_test_files(sandbox):
    """Create test files in the sandbox for testing."""
    print("\n" + "=" * 60)
    print("SETUP: Creating test files in sandbox")
    print("=" * 60)

    test_files = {
        "test_file1.py": """# Test Python file 1
def hello():
    print("Hello World")

def goodbye():
    print("Goodbye World")
""",
        "test_file2.py": """# Test Python file 2
import os

def search_pattern():
    return "SEARCH_TARGET_ALPHA"

class MyClass:
    pass
""",
        "test_file3.txt": """This is a text file.
It contains some SEARCH_TARGET_ALPHA text.
And also SEARCH_TARGET_BETA here.
Multiple lines for testing.
""",
        "subdir/nested_file.py": """# Nested Python file
def nested_function():
    return "SEARCH_TARGET_ALPHA"
""",
    }

    for filepath, content in test_files.items():
        try:
            # Create directory if needed
            if "/" in filepath:
                dir_path = "/".join(filepath.split("/")[:-1])
                try:
                    await sandbox.execute_command(f"mkdir -p {dir_path}")
                except Exception as e:
                    print(f"   Warning creating dir {dir_path}: {e}")

            # Write file
            await sandbox.write_file(filepath, content)
            print(f"   Created: {filepath}")
        except Exception as e:
            print(f"   Error creating {filepath}: {e}")
            traceback.print_exc()

    # List created files
    print("\n   Listing files in sandbox:")
    try:
        files = sandbox.glob_files("*", ".")
        for f in files[:20]:  # Limit output
            print(f"   - {f}")
        if len(files) > 20:
            print(f"   ... and {len(files) - 20} more")
    except Exception as e:
        print(f"   Error listing files: {e}")


async def test_glob_tool(glob_tool, sandbox, results: TestResult):
    """Test the Glob tool."""
    print("\n" + "=" * 60)
    print("TESTING: Glob Tool")
    print("=" * 60)

    # Test 1: Basic pattern
    print("\n--- Test 1: Basic *.py pattern ---")
    try:
        result = await glob_tool.ainvoke({"pattern": "*.py"})
        print(f"Result:\n{result}")

        if "test_file1.py" in result and "test_file2.py" in result:
            results.success("Glob *.py pattern", "Found expected Python files")
        else:
            results.failure("Glob *.py pattern", f"Expected files not found in result")
    except Exception as e:
        results.failure("Glob *.py pattern", str(e))
        traceback.print_exc()

    # Test 2: Nested pattern
    print("\n--- Test 2: Nested **/*.py pattern ---")
    try:
        result = await glob_tool.ainvoke({"pattern": "**/*.py"})
        print(f"Result:\n{result}")

        if "nested_file.py" in result or "subdir" in result:
            results.success("Glob **/*.py pattern", "Found nested files")
        else:
            results.failure("Glob **/*.py pattern", "Nested files not found")
    except Exception as e:
        results.failure("Glob **/*.py pattern", str(e))
        traceback.print_exc()

    # Test 3: Specific directory
    print("\n--- Test 3: Pattern in specific directory ---")
    try:
        result = await glob_tool.ainvoke({"pattern": "*.py", "path": "subdir"})
        print(f"Result:\n{result}")

        if "nested_file.py" in result:
            results.success("Glob in subdir", "Found file in subdirectory")
        elif "No files found" in result or "0 file" in result:
            results.failure("Glob in subdir", "No files found in subdir")
        else:
            results.success("Glob in subdir", "Query executed")
    except Exception as e:
        results.failure("Glob in subdir", str(e))
        traceback.print_exc()

    # Test 4: Text files
    print("\n--- Test 4: *.txt pattern ---")
    try:
        result = await glob_tool.ainvoke({"pattern": "*.txt"})
        print(f"Result:\n{result}")

        if "test_file3.txt" in result:
            results.success("Glob *.txt pattern", "Found text file")
        else:
            results.failure("Glob *.txt pattern", "Text file not found")
    except Exception as e:
        results.failure("Glob *.txt pattern", str(e))
        traceback.print_exc()

    # Diagnostic: Direct sandbox.glob_files() call
    print("\n--- Diagnostic: Direct sandbox.glob_files() ---")
    try:
        direct_result = sandbox.glob_files("*.py", ".")
        print(f"Direct glob_files result: {direct_result}")
        if direct_result:
            results.success("Direct glob_files", f"Found {len(direct_result)} files")
        else:
            results.failure("Direct glob_files", "No files returned")
    except Exception as e:
        results.failure("Direct glob_files", str(e))
        traceback.print_exc()


async def test_grep_tool(grep_tool, sandbox, results: TestResult):
    """Test the Grep tool."""
    print("\n" + "=" * 60)
    print("TESTING: Grep Tool")
    print("=" * 60)

    # Test 1: Basic search
    print("\n--- Test 1: Search for SEARCH_TARGET_ALPHA ---")
    try:
        result = await grep_tool.ainvoke({
            "pattern": "SEARCH_TARGET_ALPHA",
            "output_mode": "files_with_matches"
        })
        print(f"Result:\n{result}")

        if "test_file2.py" in result or "test_file3.txt" in result:
            results.success("Grep basic search", "Found files with target string")
        else:
            results.failure("Grep basic search", "Expected files not found")
    except Exception as e:
        results.failure("Grep basic search", str(e))
        traceback.print_exc()

    # Test 2: Content output mode
    print("\n--- Test 2: Content output mode ---")
    try:
        result = await grep_tool.ainvoke({
            "pattern": "SEARCH_TARGET_ALPHA",
            "output_mode": "content"
        })
        print(f"Result:\n{result}")

        if "SEARCH_TARGET_ALPHA" in result:
            results.success("Grep content mode", "Found content with matches")
        else:
            results.failure("Grep content mode", "Target string not in content output")
    except Exception as e:
        results.failure("Grep content mode", str(e))
        traceback.print_exc()

    # Test 3: Count mode
    print("\n--- Test 3: Count output mode ---")
    try:
        result = await grep_tool.ainvoke({
            "pattern": "SEARCH_TARGET_ALPHA",
            "output_mode": "count"
        })
        print(f"Result:\n{result}")
        results.success("Grep count mode", "Count query executed")
    except Exception as e:
        results.failure("Grep count mode", str(e))
        traceback.print_exc()

    # Test 4: Filter with glob
    print("\n--- Test 4: Filter with glob *.py ---")
    try:
        result = await grep_tool.ainvoke({
            "pattern": "SEARCH_TARGET_ALPHA",
            "glob": "*.py",
            "output_mode": "files_with_matches"
        })
        print(f"Result:\n{result}")

        # Should find .py files but not .txt
        if "test_file3.txt" not in result:
            results.success("Grep with glob filter", "Correctly filtered to .py files")
        else:
            results.failure("Grep with glob filter", ".txt file should be filtered out")
    except Exception as e:
        results.failure("Grep with glob filter", str(e))
        traceback.print_exc()

    # Test 5: Case insensitive
    print("\n--- Test 5: Case insensitive search ---")
    try:
        result = await grep_tool.ainvoke({
            "pattern": "search_target_alpha",  # lowercase
            "i": True,
            "output_mode": "files_with_matches"
        })
        print(f"Result:\n{result}")

        if "test_file2.py" in result or "test_file3.txt" in result:
            results.success("Grep case insensitive", "Found with case-insensitive search")
        else:
            results.failure("Grep case insensitive", "Case-insensitive search failed")
    except Exception as e:
        results.failure("Grep case insensitive", str(e))
        traceback.print_exc()

    # Test 6: Context lines
    print("\n--- Test 6: Context lines (-A 1 -B 1) ---")
    try:
        result = await grep_tool.ainvoke({
            "pattern": "SEARCH_TARGET_BETA",
            "output_mode": "content",
            "A": 1,
            "B": 1
        })
        print(f"Result:\n{result}")
        results.success("Grep with context", "Context query executed")
    except Exception as e:
        results.failure("Grep with context", str(e))
        traceback.print_exc()

    # Diagnostic: Direct sandbox.grep_content() call
    print("\n--- Diagnostic: Direct sandbox.grep_content() ---")
    try:
        direct_result = sandbox.grep_content(
            pattern="SEARCH_TARGET_ALPHA",
            path=".",
            output_mode="files_with_matches"
        )
        print(f"Direct grep_content result: {direct_result}")
        if direct_result:
            results.success("Direct grep_content", f"Found {len(direct_result)} matches")
        else:
            results.failure("Direct grep_content", "No matches returned")
    except Exception as e:
        results.failure("Direct grep_content", str(e))
        traceback.print_exc()


async def investigate_diagnostics(sandbox, results: TestResult):
    """Deep diagnostic investigation if tools are failing."""
    print("\n" + "=" * 60)
    print("DIAGNOSTICS: Deep investigation")
    print("=" * 60)

    # Check sandbox internals
    print("\n--- Checking sandbox internals ---")

    # 1. Test list_directory
    print("\n1. Testing list_directory():")
    try:
        contents = sandbox.list_directory(".")
        print(f"   Root directory contents: {contents[:10]}...")
        if contents:
            results.success("list_directory", f"Found {len(contents)} items")
        else:
            results.failure("list_directory", "Empty directory listing")
    except Exception as e:
        results.failure("list_directory", str(e))
        traceback.print_exc()

    # 2. Test search_files
    print("\n2. Testing search_files():")
    try:
        files = sandbox.search_files("*.py", ".")
        print(f"   search_files result: {files}")
        if files:
            results.success("search_files", f"Found {len(files)} files")
        else:
            results.failure("search_files", "No files found")
    except Exception as e:
        results.failure("search_files", str(e))
        traceback.print_exc()

    # 3. Test read_file
    print("\n3. Testing read_file():")
    try:
        content = sandbox.read_file("test_file1.py")
        print(f"   read_file result (first 100 chars): {content[:100]}...")
        if content and "hello" in content.lower():
            results.success("read_file", "Successfully read file content")
        else:
            results.failure("read_file", "Unexpected content or empty")
    except Exception as e:
        results.failure("read_file", str(e))
        traceback.print_exc()

    # 4. Check config
    print("\n4. Checking configuration:")
    print(f"   enable_path_validation: {sandbox.config.filesystem.enable_path_validation}")
    print(f"   allowed_directories: {sandbox.config.filesystem.allowed_directories}")

    # 5. Test path validation
    print("\n5. Testing validate_path():")
    try:
        valid_paths = [".", "test_file1.py", "/home/daytona"]
        for p in valid_paths:
            is_valid = sandbox.validate_path(p)
            print(f"   validate_path('{p}'): {is_valid}")
    except Exception as e:
        print(f"   Error in validate_path: {e}")
        traceback.print_exc()


async def cleanup(session_id: str):
    """Clean up the session."""
    print("\n" + "=" * 60)
    print("CLEANUP: Cleaning up session")
    print("=" * 60)

    try:
        await SessionManager.cleanup_session(session_id)
        print("   Session cleaned up successfully")
    except Exception as e:
        print(f"   Error during cleanup: {e}")


async def main():
    """Main test function."""
    print("\n" + "=" * 60)
    print("GREP/GLOB SANDBOX TEST")
    print("=" * 60)

    results = TestResult()
    session = None

    try:
        # Setup
        session, sandbox, glob_tool, grep_tool = await setup_environment()

        # Create test files
        await create_test_files(sandbox)

        # Run tests
        await test_glob_tool(glob_tool, sandbox, results)
        await test_grep_tool(grep_tool, sandbox, results)

        # Run diagnostics
        await investigate_diagnostics(sandbox, results)

    except Exception as e:
        print(f"\n❌ FATAL ERROR: {e}")
        traceback.print_exc()
        results.failure("Setup/Execution", str(e))

    finally:
        # Cleanup
        if session:
            await cleanup("test-grep-glob")

        # Summary
        results.summary()

        # Return exit code
        return 0 if results.failed == 0 else 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
