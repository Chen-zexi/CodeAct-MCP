"""Integration test for MCP tool transformation.

This test verifies that MCP tools are correctly transformed to Python modules
in the Daytona sandbox.

Run with:
    uv run python tests/test_mcp_tool_transformation.py

Options:
    --no-cleanup    Keep sandbox running after test (for manual inspection)

Example:
    uv run python tests/test_mcp_tool_transformation.py --no-cleanup
"""

import argparse
import asyncio
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.codeact_mcp.session import SessionManager
from src.codeact_mcp.config import CoreConfig


def parse_args():
    parser = argparse.ArgumentParser(description="Test MCP tool transformation")
    parser.add_argument(
        "--no-cleanup",
        action="store_true",
        help="Keep sandbox running after test for manual inspection"
    )
    return parser.parse_args()


async def test_mcp_tool_transformation(no_cleanup: bool = False):
    """Test that MCP tools are correctly transformed to Python modules.

    Args:
        no_cleanup: If True, keep sandbox running after test for manual inspection
    """

    print("=" * 60)
    print("MCP Tool Transformation Integration Test")
    print("=" * 60)

    # Load config
    print("\n[1] Loading configuration...")
    config = CoreConfig.load()
    print(f"    Daytona API URL: {config.daytona.base_url}")
    print(f"    MCP servers configured: {len(config.mcp.servers)}")
    for server in config.mcp.servers:
        print(f"      - {server.name}")

    # Create session
    print("\n[2] Creating session and initializing sandbox...")
    session = SessionManager.get_session("test-mcp-transformation", config)

    try:
        await session.initialize()
        print("    Session initialized successfully!")

        # Check MCP registry
        print("\n[3] Checking MCP Registry...")
        tools_by_server = session.mcp_registry.get_all_tools()

        total_tools = 0
        for server_name, tools in tools_by_server.items():
            print(f"\n    Server: {server_name}")
            print(f"    Tools discovered: {len(tools)}")
            for tool in tools:
                print(f"      - {tool.name}: {tool.description[:50]}...")
                total_tools += 1

        print(f"\n    Total tools discovered: {total_tools}")

        # Check sandbox directory structure
        print("\n[4] Checking sandbox directory structure...")
        sandbox = session.sandbox

        # Get the actual work directory
        work_dir = getattr(sandbox, '_work_dir', '/workspace')
        print(f"\n    Sandbox work directory: {work_dir}")

        # List work directory
        try:
            workspace_contents = sandbox.list_directory(work_dir)
            print(f"\n    {work_dir} contents:")
            for item in workspace_contents:
                name = item.get("name") or item.get("path", "unknown")
                item_type = "dir" if item.get("is_dir") or item.get("type") == "directory" else "file"
                print(f"      [{item_type}] {name}")
        except Exception as e:
            print(f"    Error listing {work_dir}: {e}")

        # List tools directory
        tools_dir = f"{work_dir}/tools"
        try:
            tools_contents = sandbox.list_directory(tools_dir)
            print(f"\n    {tools_dir} contents:")
            for item in tools_contents:
                name = item.get("name") or item.get("path", "unknown")
                item_type = "dir" if item.get("is_dir") or item.get("type") == "directory" else "file"
                print(f"      [{item_type}] {name}")
        except Exception as e:
            print(f"    Error listing {tools_dir}: {e}")

        # Read generated tool modules
        print("\n[5] Reading generated tool modules...")

        # Read mcp_client.py
        try:
            mcp_client_path = f"{work_dir}/tools/mcp_client.py"
            mcp_client_content = sandbox.read_file(mcp_client_path)
            if mcp_client_content:
                lines = mcp_client_content.split('\n')
                print(f"\n    tools/mcp_client.py ({len(lines)} lines)")
                print("    First 20 lines:")
                for i, line in enumerate(lines[:20], 1):
                    print(f"      {i:3}: {line[:70]}")
            else:
                print("    tools/mcp_client.py: NOT FOUND or empty")
        except Exception as e:
            print(f"    Error reading mcp_client.py: {e}")

        # Read each server's tool module
        for server_name in tools_by_server.keys():
            try:
                module_path = f"{work_dir}/tools/{server_name}.py"
                module_content = sandbox.read_file(module_path)
                if module_content:
                    lines = module_content.split('\n')
                    print(f"\n    tools/{server_name}.py ({len(lines)} lines)")
                    print("    First 50 lines (showing function signatures):")
                    for i, line in enumerate(lines[:50], 1):
                        print(f"      {i:3}: {line[:80]}")
                else:
                    print(f"\n    tools/{server_name}.py: NOT FOUND or empty")
            except Exception as e:
                print(f"    Error reading {server_name}.py: {e}")

        # List documentation files
        docs_dir = f"{work_dir}/tools/docs"
        try:
            docs_contents = sandbox.list_directory(docs_dir)
            print(f"\n    {docs_dir} contents:")
            for item in docs_contents:
                name = item.get("name") or item.get("path", "unknown")
                print(f"      - {name}")
        except Exception as e:
            print(f"    Error listing {docs_dir}: {e}")

        # Test execute_code with a simple import
        print("\n[6] Testing tool import in sandbox...")

        # Get the first available server/tool for testing
        if tools_by_server:
            first_server = list(tools_by_server.keys())[0]
            first_tool = tools_by_server[first_server][0]
            # Convert tool name to valid Python identifier
            func_name = first_tool.name.replace("-", "_").replace(".", "_")

            test_code = f'''
import sys
sys.path.insert(0, '{work_dir}')

try:
    from tools.{first_server} import {func_name}
    print(f"Successfully imported {func_name} from tools.{first_server}")
    print(f"Function: {{{func_name}}}")
    doc = {func_name}.__doc__
    if doc:
        print(f"Docstring: {{doc[:200]}}...")
    else:
        print("Docstring: None")
except Exception as e:
    print(f"Import failed: {{e}}")
'''

            try:
                result = await sandbox.execute(test_code)
                print(f"\n    Execution result:")
                print(f"    Success: {result.success}")
                print(f"    Stdout:\n{result.stdout}")
                if result.stderr:
                    print(f"    Stderr:\n{result.stderr}")
            except Exception as e:
                print(f"    Execution error: {e}")

        print("\n" + "=" * 60)
        print("Test completed!")
        print("=" * 60)

    except Exception as e:
        print(f"\nError during test: {e}")
        import traceback
        traceback.print_exc()

    finally:
        # Cleanup
        if no_cleanup:
            print("\n[7] Skipping cleanup (--no-cleanup flag set)")
            print(f"    Sandbox ID: {sandbox.sandbox_id if sandbox else 'N/A'}")
            print(f"    Session: test-mcp-transformation")
            print("\n    To manually cleanup later:")
            print("    >>> from src.codeact_mcp.session import SessionManager")
            print("    >>> import asyncio")
            print("    >>> asyncio.run(SessionManager.cleanup_session('test-mcp-transformation'))")
            print("\n    Press Ctrl+C to exit (sandbox will remain running)")
            try:
                # Keep script running so user can inspect
                while True:
                    await asyncio.sleep(60)
            except KeyboardInterrupt:
                print("\n    Exiting (sandbox still running)")
        else:
            print("\n[7] Cleaning up session...")
            await SessionManager.cleanup_session("test-mcp-transformation")
            print("    Session cleaned up.")


if __name__ == "__main__":
    args = parse_args()
    asyncio.run(test_mcp_tool_transformation(no_cleanup=args.no_cleanup))
