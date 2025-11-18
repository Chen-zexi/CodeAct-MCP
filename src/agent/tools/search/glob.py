"""Glob tool for file pattern matching."""

from typing import Any, Optional

import structlog
from langchain_core.tools import tool

logger = structlog.get_logger(__name__)


def create_glob_tool(sandbox: Any):
    """Factory function to create Glob tool.

    Args:
        sandbox: CodeActSandbox instance

    Returns:
        Configured Glob tool function
    """

    @tool
    async def Glob(pattern: str, path: Optional[str] = None) -> str:
        """Fast file pattern matching tool for finding files by name patterns.

        Works with any codebase size. Supports glob patterns like "**/*.js", "src/**/*.ts", "*.py".
        Returns matching file paths sorted by modification time.

        Use this tool when you need to find files by name patterns. For content-based searches,
        use the Grep tool instead.

        Args:
            pattern: Glob pattern to match files against
                    Examples: "**/*.py", "src/**/*.ts", "*.{js,ts}", "**/test_*.py"
            path: Optional directory to search in (defaults to current working directory if not specified).
                  IMPORTANT: Omit this parameter for default directory - don't enter "undefined" or "null"

        Returns:
            Matching file paths sorted by modification time, or error message if operation failed.

        Pattern Syntax:
            *       - Match anything except /
            **      - Match zero or more directories
            ?       - Match single character
            [...]   - Match character range
            {a,b}   - Match either pattern

        Examples:
            Find all Python files recursively:
            pattern = "**/*.py"

            Find all TypeScript files in src directory:
            pattern = "src/**/*.ts"
            path = "."

            Find all config files:
            pattern = "**/*.{yaml,yml,json}"

            Find test files:
            pattern = "**/test_*.py"
        """
        try:
            # Use current working directory if path not specified
            search_path = path if path is not None else "."

            logger.info("Globbing files", pattern=pattern, path=search_path)

            # Validate path if enabled
            if sandbox.config.filesystem.enable_path_validation and not sandbox.validate_path(search_path):
                error_msg = f"Access denied: {search_path} is not in allowed directories"
                logger.error(error_msg, path=search_path)
                return f"ERROR: {error_msg}"

            # Search for files matching the pattern
            # Note: This uses the sandbox's glob_files method which will be added in Phase 6
            # For now, we'll use search_files as a temporary implementation
            matches = sandbox.glob_files(pattern, search_path)

            if not matches:
                logger.info("No files found", pattern=pattern, path=search_path)
                return f"No files matching pattern '{pattern}' found in '{search_path}'"

            # Format output
            result = f"Found {len(matches)} file(s) matching '{pattern}':\n"
            for match in matches:
                result += f"{match}\n"

            logger.info(
                "Glob completed successfully",
                pattern=pattern,
                path=search_path,
                matches=len(matches),
            )

            return result.rstrip()

        except Exception as e:
            error_msg = f"Failed to glob files: {str(e)}"
            logger.error(error_msg, pattern=pattern, path=search_path, error=str(e), exc_info=True)
            return f"ERROR: {error_msg}"

    return Glob
