"""Test script to demonstrate the difference between summary and detailed tool exposure modes."""

from src.agent.prompts import format_tool_summary
from codeact_mcp.mcp_registry import MCPToolInfo


def create_sample_tools():
    """Create sample tools for testing."""
    tavily_tools = [
        MCPToolInfo(
            name="tavily_search",
            description="Search the web using Tavily search engine",
            input_schema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search query"},
                    "max_results": {"type": "integer", "description": "Maximum results", "default": 10}
                },
                "required": ["query"]
            },
            server_name="tavily"
        )
    ]

    filesystem_tools = [
        MCPToolInfo(
            name="read_file",
            description="Read contents of a file",
            input_schema={
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "File path to read"}
                },
                "required": ["path"]
            },
            server_name="filesystem"
        ),
        MCPToolInfo(
            name="write_file",
            description="Write content to a file",
            input_schema={
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "File path to write"},
                    "content": {"type": "string", "description": "Content to write"}
                },
                "required": ["path", "content"]
            },
            server_name="filesystem"
        ),
        MCPToolInfo(
            name="list_directory",
            description="List contents of a directory",
            input_schema={
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "Directory path to list"}
                },
                "required": ["path"]
            },
            server_name="filesystem"
        )
    ]

    github_tools = [
        MCPToolInfo(
            name="create_issue",
            description="Create a new GitHub issue",
            input_schema={
                "type": "object",
                "properties": {
                    "repo": {"type": "string", "description": "Repository name (owner/repo)"},
                    "title": {"type": "string", "description": "Issue title"},
                    "body": {"type": "string", "description": "Issue body"}
                },
                "required": ["repo", "title"]
            },
            server_name="github"
        ),
        MCPToolInfo(
            name="list_issues",
            description="List issues in a GitHub repository",
            input_schema={
                "type": "object",
                "properties": {
                    "repo": {"type": "string", "description": "Repository name (owner/repo)"},
                    "state": {"type": "string", "description": "Issue state (open, closed, all)", "default": "open"}
                },
                "required": ["repo"]
            },
            server_name="github"
        )
    ]

    return {
        "tavily": [tool.to_dict() for tool in tavily_tools],
        "filesystem": [tool.to_dict() for tool in filesystem_tools],
        "github": [tool.to_dict() for tool in github_tools]
    }


def print_section(title: str, content: str):
    """Pretty print a section."""
    print("\n" + "="*80)
    print(f"  {title}")
    print("="*80)
    print(content)
    print("="*80 + "\n")


def count_tokens_estimate(text: str) -> int:
    """Rough estimate of token count (1 token ≈ 4 characters)."""
    return len(text) // 4


def main():
    """Demonstrate the difference between summary and detailed modes."""

    print("\n" + "🔧 TOOL EXPOSURE MODE COMPARISON".center(80))
    print("="*80)
    print("This demonstrates the configurable tool_exposure_mode setting.\n")

    tools_by_server = create_sample_tools()

    # Generate summary mode output
    summary_output = format_tool_summary(tools_by_server, mode="summary")
    summary_tokens = count_tokens_estimate(summary_output)

    # Generate detailed mode output
    detailed_output = format_tool_summary(tools_by_server, mode="detailed")
    detailed_tokens = count_tokens_estimate(detailed_output)

    # Display results
    print_section(
        '📋 SUMMARY MODE (tool_exposure_mode: "summary")',
        summary_output
    )

    print(f"Token estimate: ~{summary_tokens} tokens")
    print("\nCharacteristics:")
    print("  ✓ Minimal token usage")
    print("  ✓ Shows MCP server names and tool counts")
    print("  ✓ Provides import paths and module locations")
    print("  ✓ Encourages progressive tool discovery via filesystem")
    print("  ✓ Recommended for most use cases (follows the article pattern)")

    print_section(
        '📋 DETAILED MODE (tool_exposure_mode: "detailed")',
        detailed_output
    )

    print(f"Token estimate: ~{detailed_tokens} tokens")
    print("\nCharacteristics:")
    print("  ✓ Complete tool signatures in prompt")
    print("  ✓ All parameters and descriptions visible upfront")
    print("  ✓ No need to read docs for basic usage")
    print("  ✓ Higher token usage")
    print("  ✓ Useful when you want all tool info immediately available")

    # Token savings
    token_savings = ((detailed_tokens - summary_tokens) / detailed_tokens) * 100

    print("\n" + "="*80)
    print("  📊 TOKEN EFFICIENCY COMPARISON")
    print("="*80)
    print(f"Summary mode:  ~{summary_tokens} tokens")
    print(f"Detailed mode: ~{detailed_tokens} tokens")
    print(f"Savings:       ~{token_savings:.1f}% reduction with summary mode")
    print("="*80)

    print("\n" + "💡 CONFIGURATION".center(80))
    print("="*80)
    print("""
To configure the mode, edit config.yaml:

mcp:
  tool_exposure_mode: "summary"  # or "detailed"

Summary mode (recommended):
  - Minimal prompt tokens (~500 tokens for typical setups)
  - Agents discover tools progressively via filesystem
  - Follows the pattern from the Anthropic article
  - Best for token efficiency and scalability

Detailed mode:
  - Full tool information in prompt (~2000 tokens)
  - All tool signatures visible upfront
  - No need to read documentation files
  - Best when you want immediate tool visibility
    """)
    print("="*80)
    print("\n✨ Test complete!\n")


if __name__ == "__main__":
    main()
