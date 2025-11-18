# CodeAct MCP

A Python proof of concept implementation inspired by [Anthropic's engineering blog](https://www.anthropic.com/engineering/code-execution-with-mcp) and CodeAct agent pattern.

## Overview

### The Problem

Traditional MCP implementations suffer from token inefficiency:
- **Context overload**: Tool definitions consume excessive tokens before the model processes requests
- **Result duplication**: Intermediate outputs pass through the model repeatedly, bloating context usage

A simple workflow processing data between two services can consume 150,000+ tokens by passing intermediate results through the model.

### The Solution

CodeAct MCP implements the CodeAct pattern where agents generate executable Python code instead of JSON tool calls:

1. Agent generates code to interact with MCP tools
2. Code executes in an isolated sandbox
3. Data processing happens locally in the sandbox
4. Only summaries return to the LLM context

**Result: Significant token reduction and more dynamic and flexible workflow**

## Core Stack

- **LangGraph**: AI agent orchestration using the ReAct pattern
- **Daytona**: Secure sandbox execution environment
- **MCP**: Model Context Protocol for tool integration

## How It Works

```
User Task
    |
    v
+------------------+
|  CodeActAgent    |  Generates Python code
|  (LangGraph)     |
+------------------+
    |
    v
+------------------+
|  Daytona Sandbox |  Executes code locally
|                  |  Processes data in sandbox
+------------------+
    |
    v
+------------------+
|   MCP Servers    |  Alpha Vantage, Tavily, Tickertick, etc.
+------------------+
    |
    v
Summary returned to LLM (not raw data)
```

## Included MCP Servers

| Server | Description | Use Cases |
|--------|-------------|-----------|
| **Tavily** | Web search engine for finding current information online | News, research, real-time information, web queries |
| **Alpha Vantage** | Financial market data API | Stock quotes, historical prices, technical indicators, forex rates, crypto data, economic indicators |
| **Tickertick** | Financial news API | Ticker-specific news, curated market news, entity news about people and companies |

## MCP Tool Transformation

MCP tools are automatically converted to Python functions in daytona sandbox that agents can call. This transformation happens at session initialization.

### Schema to Python Mapping

MCP tool schemas (JSON Schema) are converted to Python type hints:

| JSON Schema Type | Python Type |
|-----------------|-------------|
| string          | str         |
| number          | float       |
| integer         | int         |
| boolean         | bool        |
| array           | List        |
| object          | Dict        |

### Function Generation

For each MCP tool, a Python function is generated with:
- **Proper parameter ordering**: Required parameters first, optional parameters with defaults
- **Type hints**: Based on the schema mapping above
- **Docstrings**: Including description, parameter docs, return type, and usage example

Example transformation:

**MCP Tool Schema:**
```json
{
  "name": "tavily_search",
  "description": "Search the web using Tavily",
  "inputSchema": {
    "type": "object",
    "properties": {
      "query": {"type": "string", "description": "Search query"},
      "max_results": {"type": "integer", "description": "Max results", "default": 10}
    },
    "required": ["query"]
  }
}
```

**Generated Python Function:**
```python
def tavily_search(query: str, max_results: Optional[int] = None) -> Any:
    """Search the web using Tavily

    Args:
        query (string) (required): Search query
        max_results (integer): Max results

    Returns:
        Tool execution result

    Example:
        result = tavily_search(query="example")
    """
    arguments = {
        "query": query,
        "max_results": max_results,
    }
    arguments = {k: v for k, v in arguments.items() if v is not None}
    return _call_mcp_tool("tavily", "tavily_search", arguments)
```

### Tool Organization in Sandbox

Generated tools are deployed to the sandbox filesystem:

```
./tools/
├── mcp_client.py           # MCP transport client (stdio/SSE/HTTP)
├── tavily.py               # Tavily MCP functions
├── filesystem.py           # Filesystem MCP functions
└── docs/
    ├── tavily_search.md    # Tool documentation
    └── read_file.md
```

The agent imports and calls these functions directly in generated code.

## Agent Behavior

### Progressive Tool Discovery

The agent discovers and uses tools on-demand rather than loading all tool schemas upfront:

1. **Initial context**: Agent receives a summary of available tools (names and brief descriptions only)
2. **On-demand exploration**: When a tool is needed, agent reads the detailed documentation from `./tools/docs/`
3. **Function import**: Agent imports and calls the specific function needed
4. **Iterative refinement**: If errors occur, agent reads documentation again or tries alternative approaches

This approach keeps the context window lean while allowing access to rich tool documentation when needed.

### Data Processing Workflow

The key to token efficiency is keeping data inside the sandbox:

**Step 1: Fetch Data**
```python
# Agent generates code to fetch data
from tools.tavily import tavily_search
results = tavily_search(query="AI agents research 2024", max_results=50)
```

**Step 2: Store in Sandbox**
```python
# Data stays in sandbox, not returned to LLM
import json
with open("results/search_results.json", "w") as f:
    json.dump(results, f)
print(f"Saved {len(results)} results to search_results.json")
```

**Step 3: Reuse for Further Processing**
```python
# Subsequent code loads from sandbox filesystem
import pandas as pd
with open("results/search_results.json") as f:
    data = json.load(f)

# Filter and analyze locally
df = pd.DataFrame(data)
filtered = df[df['score'] > 0.7]
filtered.to_csv("results/high_quality_results.csv")
print(f"Filtered to {len(filtered)} high-quality results")
```

### Multi-Turn State Persistence

Variables and files persist across multiple agent turns within a session:

- **Turn 1**: Fetch data and store in `results/data.json`
- **Turn 2**: Load `results/data.json`, analyze, save chart to `results/chart.png`
- **Turn 3**: Reference both files for final report

The sandbox maintains state, so the agent can build on previous work without re-fetching or re-processing data.

## Quick Start

### Prerequisites

- Python 3.12+
- Node.js (for MCP servers)
- [Daytona](https://app.daytona.io) account
- Anthropic API key or OpenAI API key

### Installation

```bash
# Clone repository
git clone <repository-url>
cd codeact-mcp

# Install dependencies
uv sync

# Set up environment
cp .env.example .env
# Edit .env with your API keys
```

### Environment Configuration

Edit `.env`:

```env
# Daytona (required)
DAYTONA_API_KEY=your_key_here

# LLM Provider
ANTHROPIC_API_KEY=your_key_here
# or
OPENAI_API_KEY=your_key_here

# MCP servers
TAVILY_API_KEY=your_key_here
ALPHA_VANTAGE_API_KEY=your_key_here
```

## Demo

See `CodeAct_Agent.ipynb` for an interactive demonstration that shows:
- Agent creation and configuration
- System prompt generation with tool summaries
- Multi-step task execution (research, analysis, visualization)
- Sandbox file tree before/after execution
- Result inspection and report generation

### API Server

Start a LangGraph API server for programmatic access:

```bash
uv run langgraph dev
```

This launches a local server where you can interact with the agent via HTTP API.

## Project Structure

```
codeact-mcp/
├── src/
│   ├── codeact_mcp/          # Core infrastructure
│   │   ├── sandbox.py        # Daytona sandbox management
│   │   ├── mcp_registry.py   # MCP server connections
│   │   ├── tool_generator.py # MCP to Python conversion
│   │   ├── session.py        # Session management
│   │   └── config.py         # Configuration
│   └── agent/                # Agent implementations
│       ├── agent.py          # CodeActAgent, CodeExecutor
│       ├── config.py         # Agent configuration
│       ├── backends/         # Daytona backend
│       ├── prompts/          # Prompt templates
│       ├── tools/            # Tool implementations
│       └── subagents/        # Sub-agent definitions
├── tests/                    # Test suite
├── config.yaml               # Main configuration
├── llms.json                 # LLM definitions
└── .env                      # API keys
```

## Configuration

### config.yaml

Main configuration for MCP servers, Daytona settings, filesystem access, and security:

```yaml
mcp:
  servers:
    - name: "filesystem"
      transport: "stdio"
      command: "npx"
      args: ["-y", "@anthropic/mcp-filesystem", "/workspace"]

daytona:
  target: "us"
  timeout: 60

security:
  max_execution_time: 300
  enable_code_validation: true
```

### llms.json

LLM provider definitions:

```json
{
  "claude-sonnet": {
    "model_id": "claude-sonnet-4-20250514",
    "provider": "anthropic",
    "sdk": "langchain_anthropic.ChatAnthropic",
    "api_key_env": "ANTHROPIC_API_KEY"
  }
}
```

## Running Tests

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_filesystem_tools.py

# Run with verbose output
pytest tests/ -v
```

## References

- [Anthropic: Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp)
- [CodeAct Paper (ICML 2024)](https://arxiv.org/abs/2402.01030)
- [MCP Specification](https://modelcontextprotocol.io/)
- [Daytona Documentation](https://www.daytona.io/docs/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)

## Acknowledgments

Special thanks to [Daytona](https://www.daytona.io/) for providing the secure sandbox infrastructure that makes this project possible. Their platform enables safe, isolated code execution with automatic cleanup, which is essential for the CodeAct pattern where AI agents generate and run arbitrary Python code.

## License

MIT License
