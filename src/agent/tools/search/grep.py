"""Grep tool for content searching with ripgrep."""

from typing import Any, Literal, Optional

import structlog
from langchain_core.tools import tool

logger = structlog.get_logger(__name__)


def create_grep_tool(sandbox: Any):
    """Factory function to create Grep tool.

    Args:
        sandbox: CodeActSandbox instance

    Returns:
        Configured Grep tool function
    """

    @tool
    async def Grep(
        pattern: str,
        path: Optional[str] = None,
        output_mode: Optional[Literal["files_with_matches", "content", "count"]] = "files_with_matches",
        glob: Optional[str] = None,
        type: Optional[str] = None,
        i: Optional[bool] = False,
        n: Optional[bool] = True,
        A: Optional[int] = None,
        B: Optional[int] = None,
        C: Optional[int] = None,
        multiline: Optional[bool] = False,
        head_limit: Optional[int] = None,
        offset: Optional[int] = 0,
    ) -> str:
        """Powerful search tool built on ripgrep for searching file contents with regex support.

        ALWAYS use Grep for search tasks. NEVER invoke `grep` or `rg` via Bash command.
        This tool has been optimized for correct permissions and access.

        Supports full regex syntax, file filtering, and multiple output modes.

        Args:
            pattern: Regular expression pattern to search for (ripgrep syntax)
                    Examples: "CodeActAgent", "log.*Error", "function\\s+\\w+", "interface\\{\\}"
            path: File or directory to search in (defaults to current working directory if not specified)
            output_mode: Output format (default: "files_with_matches")
                        "files_with_matches" - Show only file paths (quick check)
                        "content" - Show matching lines with context
                        "count" - Show match counts per file
            glob: Filter files by glob pattern (e.g., "*.js", "*.{ts,tsx}")
            type: File type to search (e.g., "js", "py", "rust", "go", "java", "cpp", "json", "yaml", "md")
            i: Case insensitive search (default: False)
            n: Show line numbers in content mode (default: True, ignored in other modes)
            A: Number of lines to show after each match (content mode only)
            B: Number of lines to show before each match (content mode only)
            C: Number of lines to show before and after each match (content mode only)
            multiline: Enable multiline mode where . matches newlines (default: False)
            head_limit: Limit output to first N lines/entries (default: None for unlimited)
            offset: Skip first N lines/entries before applying head_limit (default: 0)

        Returns:
            Search results in the specified format, or error message if operation failed.

        Pattern Syntax (Regex):
            .       - Any character
            .*      - Zero or more of any character
            \\s     - Whitespace
            \\w     - Word character
            \\d     - Digit
            [...]   - Character class
            \\{     - Literal brace (escaped for ripgrep)

        Examples:
            Find files containing "CodeActAgent":
            pattern = "CodeActAgent"

            Find with file content:
            pattern = "CodeActAgent"
            output_mode = "content"

            Case-insensitive search:
            pattern = "error"
            output_mode = "content"
            i = True

            Search only Python files:
            pattern = "async def"
            type = "py"
            output_mode = "content"

            Search with glob pattern:
            pattern = "import.*mcp"
            glob = "*.py"
            output_mode = "content"

            Search with context lines:
            pattern = "class.*Agent"
            output_mode = "content"
            C = 3

            Multiline search:
            pattern = "class.*\\{[\\s\\S]*?def.*init"
            multiline = True
            output_mode = "content"

            Count occurrences:
            pattern = "TODO"
            output_mode = "count"
        """
        try:
            # Use current working directory if path not specified
            search_path = path if path is not None else "."

            logger.info(
                "Grepping content",
                pattern=pattern,
                path=search_path,
                output_mode=output_mode,
                glob=glob,
                type=type,
                case_insensitive=i,
            )

            # Validate path if enabled
            if sandbox.config.filesystem.enable_path_validation and not sandbox.validate_path(search_path):
                error_msg = f"Access denied: {search_path} is not in allowed directories"
                logger.error(error_msg, path=search_path)
                return f"ERROR: {error_msg}"

            # Build grep options
            options = {
                "pattern": pattern,
                "path": search_path,
                "output_mode": output_mode,
                "glob": glob,
                "type": type,
                "case_insensitive": i,
                "show_line_numbers": n,
                "lines_after": A,
                "lines_before": B,
                "lines_context": C,
                "multiline": multiline,
                "head_limit": head_limit,
                "offset": offset,
            }

            # Search for content matching the pattern
            # Note: This uses the sandbox's grep_content method which will be added in Phase 6
            results = sandbox.grep_content(**options)

            if not results:
                logger.info("No matches found", pattern=pattern, path=search_path)
                return f"No matches found for pattern '{pattern}' in '{search_path}'"

            # Format output based on mode
            if output_mode == "files_with_matches":
                result = f"Found matches in {len(results)} file(s):\n"
                for file_path in results:
                    result += f"{file_path}\n"
            elif output_mode == "content":
                result = f"Matches for pattern '{pattern}':\n\n"
                for entry in results:
                    result += f"{entry}\n"
            elif output_mode == "count":
                result = f"Match counts for pattern '{pattern}':\n"
                for file_path, count in results:
                    result += f"{file_path}: {count}\n"
            else:
                result = str(results)

            logger.info(
                "Grep completed successfully",
                pattern=pattern,
                path=search_path,
                output_mode=output_mode,
                results_count=len(results),
            )

            return result.rstrip()

        except Exception as e:
            error_msg = f"Failed to grep content: {str(e)}"
            logger.error(
                error_msg,
                pattern=pattern,
                path=search_path,
                error=str(e),
                exc_info=True,
            )
            return f"ERROR: {error_msg}"

    return Grep
