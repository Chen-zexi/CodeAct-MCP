"""Utility functions for displaying messages and prompts in Jupyter notebooks."""

import json
from pathlib import Path

from IPython.display import Image, Markdown, display
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


def format_message_content(message):
    """Convert message content to displayable string."""
    parts = []
    tool_calls_processed = False

    # Handle main content
    if isinstance(message.content, str):
        parts.append(message.content)
    elif isinstance(message.content, list):
        # Handle complex content like tool calls (Anthropic format)
        for item in message.content:
            if item.get("type") == "text":
                parts.append(item["text"])
            elif item.get("type") == "tool_use":
                parts.append(f"\n🔧 Tool Call: {item['name']}")
                parts.append(f"   Args: {json.dumps(item['input'], indent=2)}")
                parts.append(f"   ID: {item.get('id', 'N/A')}")
                tool_calls_processed = True
    else:
        parts.append(str(message.content))

    # Handle tool calls attached to the message (OpenAI format) - only if not already processed
    if (
        not tool_calls_processed
        and hasattr(message, "tool_calls")
        and message.tool_calls
    ):
        for tool_call in message.tool_calls:
            parts.append(f"\n🔧 Tool Call: {tool_call['name']}")
            parts.append(f"   Args: {json.dumps(tool_call['args'], indent=2)}")
            parts.append(f"   ID: {tool_call['id']}")

    return "\n".join(parts)


def format_messages(messages):
    """Format and display a list of messages with Rich formatting."""
    for m in messages:
        msg_type = m.__class__.__name__.replace("Message", "")
        content = format_message_content(m)

        if msg_type == "Human":
            console.print(Panel(content, title="🧑 Human", border_style="blue"))
        elif msg_type == "Ai":
            console.print(Panel(content, title="🤖 Assistant", border_style="green"))
        elif msg_type == "Tool":
            console.print(Panel(content, title="🔧 Tool Output", border_style="yellow"))
        else:
            console.print(Panel(content, title=f"📝 {msg_type}", border_style="white"))


def format_message(messages):
    """Alias for format_messages for backward compatibility."""
    return format_messages(messages)


def show_prompt(prompt_text: str, title: str = "Prompt", border_style: str = "blue"):
    """Display a prompt with rich formatting and XML tag highlighting.

    Args:
        prompt_text: The prompt string to display
        title: Title for the panel (default: "Prompt")
        border_style: Border color style (default: "blue")
    """
    # Create a formatted display of the prompt
    formatted_text = Text(prompt_text)
    formatted_text.highlight_regex(r"<[^>]+>", style="bold blue")  # Highlight XML tags
    formatted_text.highlight_regex(
        r"##[^#\n]+", style="bold magenta"
    )  # Highlight headers
    formatted_text.highlight_regex(
        r"###[^#\n]+", style="bold cyan"
    )  # Highlight sub-headers

    # Display in a panel for better presentation
    console.print(
        Panel(
            formatted_text,
            title=f"[bold green]{title}[/bold green]",
            border_style=border_style,
            padding=(1, 2),
        )
    )


def print_agent_config(config, session):
    """Display agent configuration summary.

    Args:
        config: AgentConfig instance
        session: Session instance with mcp_registry
    """
    print("=" * 70)
    print("AGENT CONFIGURATION SUMMARY")
    print("=" * 70)

    # 1. LLM Configuration
    print("\n📦 LLM CONFIGURATION")
    print("-" * 40)
    print(f"  Name:      {config.llm.name}")
    print(f"  Model ID:  {config.llm_definition.model_id}")
    print(f"  Provider:  {config.llm_definition.provider}")
    if config.llm_definition.parameters:
        print(f"  Parameters: {config.llm_definition.parameters}")

    # 2. MCP Servers and Tools
    print("\n🔌 MCP SERVERS")
    print("-" * 40)
    tools_by_server = session.mcp_registry.get_all_tools()
    total_tools = 0
    for server_name, tools in tools_by_server.items():
        tool_names = [t.name for t in tools]
        total_tools += len(tools)
        print(f"  {server_name}: {len(tools)} tools")
        print(f"    {tool_names}")
    print(f"\n  Total: {len(tools_by_server)} servers, {total_tools} tools")

    # 3. Native Tools
    print("\n🛠️ NATIVE TOOLS")
    print("-" * 40)
    print("  Glob, Grep, Read, Write, Edit, Bash, execute_code")

    # 4. Subagents
    print("\n🤖 SUBAGENTS")
    print("-" * 40)
    print("  research-agent: tavily_search, think_tool (web research)")

    print("\n" + "=" * 70)


def print_sandbox_tree(sandbox, path=".", indent=""):
    """Print directory tree of sandbox.

    Args:
        sandbox: CodeActSandbox instance
        path: Starting path in sandbox (default: ".")
        indent: Current indentation string (used recursively)
    """
    entries = sandbox.list_directory(path)
    dirs = [e for e in entries if e["type"] == "directory"]
    files = [e for e in entries if e["type"] == "file"]

    for i, entry in enumerate(dirs + files):
        is_last = i == len(dirs) + len(files) - 1
        connector = "└── " if is_last else "├── "
        suffix = "/" if entry["type"] == "directory" else ""
        print(f"{indent}{connector}{entry['name']}{suffix}")

        if entry["type"] == "directory":
            new_indent = indent + ("    " if is_last else "│   ")
            print_sandbox_tree(sandbox, entry["path"], new_indent)


def display_sandbox_image(sandbox, filepath):
    """Display a single image from the sandbox.

    Args:
        sandbox: CodeActSandbox instance
        filepath: Path to image file in sandbox (e.g., "results/chart.png")
    """
    image_bytes = sandbox.download_file_bytes(filepath)
    if image_bytes:
        print(f"📊 {filepath}")
        display(Image(data=image_bytes))
    else:
        print(f"❌ Could not load image: {filepath}")


def display_sandbox_images(sandbox, directory="results"):
    """Display all images from a sandbox directory.

    Args:
        sandbox: CodeActSandbox instance
        directory: Directory path in sandbox (default: "results")
    """
    image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg'}

    try:
        entries = sandbox.list_directory(directory)
    except Exception as e:
        print(f"❌ Could not list directory {directory}: {e}")
        return

    image_count = 0
    for entry in entries:
        if entry["type"] == "file":
            ext = Path(entry["name"]).suffix.lower()
            if ext in image_extensions:
                filepath = entry["path"]
                image_bytes = sandbox.download_file_bytes(filepath)
                if image_bytes:
                    print(f"📊 {filepath}")
                    display(Image(data=image_bytes))
                    image_count += 1

    if image_count == 0:
        print(f"No images found in {directory}/")
    else:
        print(f"\n✅ Displayed {image_count} image(s)")


def display_result(sandbox, filepath: str = "results/result.md"):
    """Display a markdown file from sandbox, rendered in notebook.

    Args:
        sandbox: CodeActSandbox instance
        filepath: Path to markdown file in sandbox (default: results/result.md)
    """
    content = sandbox.read_file(filepath)
    if content:
        display(Markdown(content))
    else:
        print(f"Could not load markdown file: {filepath}")
