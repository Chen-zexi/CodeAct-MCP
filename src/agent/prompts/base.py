"""Base prompt templates for CodeAct agent code generation."""

CODE_GENERATION_PROMPT = """You are a helpful AI assistant with access to code execution. Your task is to accomplish the given task by calling the execute_code tool with Python code.

AVAILABLE MCP SERVERS AND TOOLS:
{tool_summary}

WORKSPACE STRUCTURE:
- tools/: Contains Python modules for each MCP server
  - Each MCP server has a module: tools/{{server_name}}.py
  - Import tools like: from tools.{{server_name}} import {{tool_name}}
- tools/docs/: Detailed documentation for each tool in Markdown format
  - Read tools/docs/{{tool_name}}.md for full parameter details when needed
- results/: Save your output files here
- data/: Input data files (if any)

HOW TO USE MCP TOOLS:
1. Tools are exposed as Python APIs in the sandbox environment
2. Import tools from the tools module: from tools.{{server_name}} import {{tool_name}}
3. BEFORE using any tool, check its exact signature:
   - Read the module file: tools/{{server_name}}.py
   - Check documentation: tools/docs/{{server_name}}/*.md
   - Verify required vs optional parameters
4. To discover available tools:
   - Check the AVAILABLE MCP SERVERS AND TOOLS section above
   - List files in tools/ directory to see available modules
   - Read tools/docs/*.md files for detailed documentation

CRITICAL: Always verify tool signatures before calling! Different servers have different APIs.
Example workflow:
```python
# First, check what tools are available
import os
print(os.listdir('tools/'))

# Read the module to see exact function signatures
with open('tools/{{server_name}}.py') as f:
    print(f.read()[:2000])  # See function definitions

# Then use the tool with correct parameters
from tools.{{server_name}} import {{tool_name}}
result = {{tool_name}}(param="value")
```

PRE-CONFIGURED DEPENDENCIES:
The sandbox has these libraries pre-installed:
- Data: pandas, numpy, json, csv
- Visualization: matplotlib, seaborn
- HTTP: requests, httpx
- Utilities: datetime, re, collections, statistics

OUTPUT HANDLING GUIDELINES:

Working with tabular data - always use pandas:
```python
import pandas as pd
data = some_tool(param="value")
df = pd.DataFrame(data)
df['change'] = df['value'].pct_change()
print(df.describe().to_string())
```

Handling large results - save to files, return summaries:
```python
import pandas as pd
data = get_data(limit=1000)
df = pd.DataFrame(data)

# Save full data to file
df.to_csv('results/output.csv', index=False)

# Return only summary
print(f"Saved {{len(df)}} rows to results/output.csv")
print(f"Value range: {{df['value'].min():.2f}} - {{df['value'].max():.2f}}")
```

Numerical formatting:
```python
print(f"Currency: ${{value:.2f}}")
print(f"Percentage: {{pct:.2%}}")
print(f"Large number: {{num:,.0f}}")
```

OUTPUT FORMAT REQUIREMENTS:

ALWAYS save tool/API results to files in results/ directory. Choose format based on data type:
- **JSON**: API responses, nested data, complex objects (most versatile)
- **CSV**: Tabular data, time series, lists with consistent fields
- **Markdown**: Reports, summaries, documentation

Example patterns:
```python
import json

# API response → JSON (preserves structure for reprocessing)
result = some_tool(param="value")
with open('results/api_response.json', 'w') as f:
    json.dump(result, f, indent=2)
print("Saved API response to results/api_response.json")

# Tabular data → CSV (easy to load with pandas later)
df.to_csv('results/data_output.csv', index=False)
print(f"Saved {{len(df)}} rows to results/data_output.csv")

# Report/summary → Markdown
report = f\"\"\"# Analysis Report
## Summary
{{summary_text}}
## Data
{{formatted_data}}
\"\"\"
with open('results/analysis_report.md', 'w') as f:
    f.write(report)
print("Saved report to results/analysis_report.md")
```

IMPORTANT: All files intended for user consumption MUST go in results/ directory.
Always print the output path so the user knows where to find results.

EFFICIENT INFORMATION GATHERING:

Before reading files, use targeted approaches:
1. Understand structure first - use ls or glob
2. Search before reading - use grep to find specific content
3. Read in chunks - use offset/limit for large files

Examples:
```python
# DON'T: Read entire 1000-line module
content = read_file("tools/{{server_name}}.py")

# DO: Search for the specific function
grep("def {{tool_name}}", path="tools/{{server_name}}.py")

# DO: Read just what you need
read_file("results/large_data.csv", limit=10)  # Just header
```

RESULTS MANAGEMENT:
- results/ - Analysis output, reports, processed data
- data/ - Input data files
- tools/ - Generated MCP tool modules (read-only)

Write to file when: >50 rows, will be referenced later, specific format needed
Print when: summaries, small tables (<20 rows), confirming operations

TASK:
{task}

EXAMPLE CODE STRUCTURE:
```python
# Import the tool you need
from tools.{{server_name}} import {{tool_name}}
import json

# Use the tool
results = {{tool_name}}(param="value")

# Process data in sandbox (don't pass large data through context!)
filtered = [item for item in results if meets_criteria(item)]

# Save results
with open('results/output.json', 'w') as f:
    json.dump(filtered, f, indent=2)

print(f"Saved {{len(filtered)}} results to output.json")
```

GUIDELINES FOR YOUR CODE:
1. Import tools from the 'tools' module (e.g., from tools.{server_name} import {tool_name})
2. Process and transform data locally in your code - DO NOT return large datasets
3. Save results to files in results/ directory using relative paths
4. Use proper error handling (try/except blocks)
5. Add comments explaining your approach
6. Print a summary of what was accomplished (e.g., "Saved 15 results to output.csv")
7. For large data operations, process in chunks or use streaming
8. Prefer pandas for data manipulation when appropriate

INSTRUCTIONS:
Use the execute_code tool to run Python code that accomplishes the task. You can optionally provide an explanation of your approach.

Now use the execute_code tool to accomplish the task:
"""

MULTI_TURN_PROMPT = """You are a helpful AI assistant with access to code execution. You previously generated code that encountered an error.

PREVIOUS CODE:
```python
{previous_code}
```

ERROR:
{error_message}

STDOUT:
{stdout}

AVAILABLE TOOLS:
{tool_summary}

ORIGINAL TASK:
{task}

Analyze the error and fix the code. Consider:
1. What caused the error?
2. How can you fix it?
3. Do you need to check file existence, handle None values, validate inputs?
4. Should you add more error handling?

Use the execute_code tool with the corrected Python code that resolves the error:
"""

TOOL_DISCOVERY_PROMPT = """You need to discover available tools before accomplishing a task.

TASK:
{task}

Generate Python code that:
1. Reads available tool documentation from tools/docs/
2. Lists all available tools and their descriptions
3. Identifies which tools are needed for the task
4. Prints the relevant tools

Example:
```python
import os

docs_dir = "tools/docs"
tool_docs = {}

for filename in os.listdir(docs_dir):
    if filename.endswith(".md"):
        tool_name = filename[:-3]
        with open(os.path.join(docs_dir, filename)) as f:
            tool_docs[tool_name] = f.read()

print("Available tools:")
for tool_name in tool_docs:
    print(f"  - {tool_name}")

# Identify relevant tools for: {task}
```

Generate the tool discovery code:
"""

TOOL_SUMMARY_TEMPLATE = """
{server_name}:
{tools}
"""

TOOL_ITEM_TEMPLATE = "  - {tool_name}({parameters}) -> {return_type}: {description}"

# MCP section template for system prompts
MCP_SECTION_TEMPLATE = """
================================================================================

# MCP Tools (via execute_code)

You have access to MCP servers with specialized tools. Use the execute_code tool
to run Python code that invokes these tools.

{tool_summary}

## Using MCP Tools

Import and use MCP tools in your execute_code calls:

```python
from tools.{{server_name}} import {{tool_name}}

result = tool_name(param="value")
print(result)
```

Workspace directories:
- tools/ - MCP tool modules
- results/ - Save output files here
- data/ - Input data files
"""


def build_mcp_section(tool_summary: str) -> str:
    """Build the MCP section for the system prompt.

    Args:
        tool_summary: Formatted tool summary from format_tool_summary()

    Returns:
        Complete MCP section string
    """
    return MCP_SECTION_TEMPLATE.format(tool_summary=tool_summary)


def format_tool_summary(tools_by_server: dict, mode: str = "summary", server_configs: dict = None) -> str:
    """Format tool information for prompt.

    Args:
        tools_by_server: Dictionary mapping server names to lists of tool info dicts
        mode: "summary" for brief server overview, "detailed" for full tool listings (global default)
        server_configs: Optional dict mapping server names to MCPServerConfig objects

    Returns:
        Formatted string for prompt
    """
    # If we have server configs, use per-server mode logic
    if server_configs:
        return _format_tool_summary_per_server(tools_by_server, server_configs, mode)

    # Fallback to global mode when no server configs
    if mode == "summary":
        return _format_tool_summary_brief(tools_by_server, server_configs)
    elif mode == "detailed":
        return _format_tool_summary_detailed(tools_by_server, server_configs)
    else:
        # Default to summary for unknown modes
        return _format_tool_summary_brief(tools_by_server, server_configs)


def _format_tool_summary_per_server(tools_by_server: dict, server_configs: dict, default_mode: str = "summary") -> str:
    """Format tool summary with per-server exposure modes.

    Each server can have its own tool_exposure_mode, falling back to the global default.

    Args:
        tools_by_server: Dictionary mapping server names to lists of tool info dicts
        server_configs: Dict mapping server names to MCPServerConfig objects
        default_mode: Global default mode to use if server doesn't specify one

    Returns:
        Formatted string for prompt
    """
    lines = []

    for server_name, tools in tools_by_server.items():
        config = server_configs.get(server_name)

        # Determine mode for this server (per-server override or global default)
        server_mode = default_mode
        if config and config.tool_exposure_mode:
            server_mode = config.tool_exposure_mode

        if server_mode == "detailed":
            # Format this server in detailed mode
            lines.extend(_format_server_detailed(server_name, tools, config))
        else:
            # Format this server in brief mode
            lines.extend(_format_server_brief(server_name, tools, config))

    if not lines:
        return "\nNo MCP servers configured."

    summary = "\n".join(lines)

    # Add important guidance about checking tool signatures
    guidance = """

IMPORTANT: Before using any MCP tool, you MUST check the exact function signature:
1. Read the tool module: Read tools/{server_name}.py to see function signatures
2. Check tool documentation: Read tools/docs/{server_name}/*.md for details
3. Verify parameters: Ensure you pass correct types and required arguments"""

    return f"{summary}{guidance}"


def _format_server_brief(server_name: str, tools: list, config) -> list:
    """Format a single server in brief/summary mode.

    Args:
        server_name: Name of the server
        tools: List of tool info dicts
        config: MCPServerConfig for this server (or None)

    Returns:
        List of formatted lines
    """
    tool_count = len(tools)
    tools_word = "tool" if tool_count == 1 else "tools"
    lines = []

    # Server header with description
    if config and config.description:
        lines.append(f"\n{server_name}: {config.description}")
    else:
        lines.append(f"\n{server_name}:")

    # Add instruction if available
    if config and config.instruction:
        lines.append(f"  Instructions: {config.instruction}")

    lines.append(f"  - Module: tools/{server_name}.py")
    lines.append(f"  - Tools: {tool_count} {tools_word} available")
    lines.append(f"  - Import: from tools.{server_name} import <tool_name>")
    lines.append(f"  - Documentation: tools/docs/{server_name}/*.md")

    return lines


def _format_server_detailed(server_name: str, tools: list, config) -> list:
    """Format a single server in detailed mode with full tool signatures.

    Args:
        server_name: Name of the server
        tools: List of tool info dicts
        config: MCPServerConfig for this server (or None)

    Returns:
        List of formatted lines
    """
    lines = []

    # Server header with description
    if config and config.description:
        lines.append(f"\n{server_name}: {config.description}")
    else:
        lines.append(f"\n{server_name}:")

    # Add instruction if available
    if config and config.instruction:
        lines.append(f"  Instructions: {config.instruction}")

    lines.append(f"  Module: tools/{server_name}.py")
    lines.append(f"  Available tools:")

    for tool in tools:
        tool_line = f"    - {tool['name']}("

        # Add parameters
        if tool.get("parameters"):
            params = tool["parameters"]
            if isinstance(params, list):
                tool_line += ", ".join(params)
            elif isinstance(params, dict):
                param_strs = []
                for pname, pinfo in params.items():
                    ptype = pinfo.get("type", "any")
                    required = pinfo.get("required", False)
                    if required:
                        param_strs.append(f"{pname}: {ptype}")
                    else:
                        default = pinfo.get("default", "None")
                        param_strs.append(f"{pname}: {ptype} = {default}")
                tool_line += ", ".join(param_strs)

        tool_line += ")"

        # Add return type
        if tool.get("return_type"):
            tool_line += f" -> {tool['return_type']}"

        # Add description
        if tool.get("description"):
            tool_line += f": {tool['description']}"

        lines.append(tool_line)

    return lines


def _format_tool_summary_brief(tools_by_server: dict, server_configs: dict = None) -> str:
    """Format brief tool summary (server names, descriptions, and module locations).

    This is the recommended mode for token efficiency, providing agents with:
    - MCP server names and descriptions
    - Usage instructions per server
    - Tool count per server
    - Module import path
    - Guidance to read docs for details

    Args:
        tools_by_server: Dictionary mapping server names to lists of tool info dicts
        server_configs: Optional dict mapping server names to MCPServerConfig objects

    Returns:
        Formatted string for prompt
    """
    lines = []

    for server_name, tools in tools_by_server.items():
        tool_count = len(tools)
        tools_word = "tool" if tool_count == 1 else "tools"

        # Get server config for description/instruction
        config = server_configs.get(server_name) if server_configs else None

        # Server header with description
        if config and config.description:
            lines.append(f"\n{server_name}: {config.description}")
        else:
            lines.append(f"\n{server_name}:")

        # Add instruction if available
        if config and config.instruction:
            lines.append(f"  Instructions: {config.instruction}")

        lines.append(f"  - Module: tools/{server_name}.py")
        lines.append(f"  - Tools: {tool_count} {tools_word} available")
        lines.append(f"  - Import: from tools.{server_name} import <tool_name>")
        lines.append(f"  - Documentation: tools/docs/{server_name}/*.md")

    if not lines:
        return "\nNo MCP servers configured."

    summary = "\n".join(lines)

    # Add important guidance about checking tool signatures
    guidance = """

IMPORTANT: Before using any MCP tool, you MUST check the exact function signature:
1. Read the tool module: Read tools/{server_name}.py to see function signatures
2. Check tool documentation: Read tools/docs/{server_name}/*.md for details
3. Verify parameters: Ensure you pass correct types and required arguments"""

    return f"{summary}{guidance}"


def _format_tool_summary_detailed(tools_by_server: dict, server_configs: dict = None) -> str:
    """Format detailed tool summary (full tool signatures and descriptions).

    This mode includes all tool names, parameters, and descriptions in the prompt.
    Uses more tokens but provides complete tool information upfront.

    Args:
        tools_by_server: Dictionary mapping server names to lists of tool info dicts
        server_configs: Optional dict mapping server names to MCPServerConfig objects

    Returns:
        Formatted string for prompt
    """
    lines = []

    for server_name, tools in tools_by_server.items():
        # Get server config for description/instruction
        config = server_configs.get(server_name) if server_configs else None

        # Server header with description
        if config and config.description:
            lines.append(f"\n{server_name}: {config.description}")
        else:
            lines.append(f"\n{server_name}:")

        # Add instruction if available
        if config and config.instruction:
            lines.append(f"  Instructions: {config.instruction}")

        lines.append(f"  Module: tools/{server_name}.py")
        lines.append(f"  Available tools:")

        for tool in tools:
            tool_line = f"    - {tool['name']}("

            # Add parameters
            if tool.get("parameters"):
                params = tool["parameters"]
                if isinstance(params, list):
                    tool_line += ", ".join(params)
                elif isinstance(params, dict):
                    param_strs = []
                    for pname, pinfo in params.items():
                        ptype = pinfo.get("type", "any")
                        required = pinfo.get("required", False)
                        if required:
                            param_strs.append(f"{pname}: {ptype}")
                        else:
                            default = pinfo.get("default", "None")
                            param_strs.append(f"{pname}: {ptype} = {default}")
                    tool_line += ", ".join(param_strs)

            tool_line += ")"

            # Add return type
            if tool.get("return_type"):
                tool_line += f" -> {tool['return_type']}"

            # Add description
            if tool.get("description"):
                tool_line += f": {tool['description']}"

            lines.append(tool_line)

    if not lines:
        return "\nNo MCP servers configured."

    return "\n".join(lines)


def build_code_generation_prompt(task: str, tool_summary: str) -> str:
    """Build complete code generation prompt.

    Args:
        task: User's task description
        tool_summary: Formatted summary of available tools

    Returns:
        Complete prompt string
    """
    return CODE_GENERATION_PROMPT.format(task=task, tool_summary=tool_summary)


def build_multi_turn_prompt(
    task: str,
    previous_code: str,
    error_message: str,
    stdout: str,
    tool_summary: str,
) -> str:
    """Build prompt for fixing errors in multi-turn execution.

    Args:
        task: Original task
        previous_code: Code that failed
        error_message: Error that occurred
        stdout: Standard output from failed execution
        tool_summary: Available tools

    Returns:
        Complete prompt string
    """
    return MULTI_TURN_PROMPT.format(
        task=task,
        previous_code=previous_code,
        error_message=error_message,
        stdout=stdout,
        tool_summary=tool_summary,
    )


def build_tool_discovery_prompt(task: str) -> str:
    """Build prompt for tool discovery.

    Args:
        task: User's task

    Returns:
        Complete prompt string
    """
    return TOOL_DISCOVERY_PROMPT.format(task=task)
