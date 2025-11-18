"""File operation tools: read, write, edit."""

from typing import Any, Optional

import structlog
from langchain_core.tools import tool

logger = structlog.get_logger(__name__)


def create_read_file_tool(sandbox: Any):
    """Factory function to create Read tool.

    Args:
        sandbox: CodeActSandbox instance

    Returns:
        Configured Read tool function
    """

    @tool
    async def Read(file_path: str, offset: Optional[int] = None, limit: Optional[int] = None) -> str:
        """Reads a file from the local filesystem.

        You can access any file directly by using this tool. Returns file contents with
        line numbers in cat -n format (starting at line 1).

        By default, it reads up to 2000 lines starting from the beginning of the file.
        You can optionally specify a line offset and limit (especially handy for long files).

        Args:
            file_path: Absolute path to the file to read (not relative)
                      Example: "/workspace/results/data.csv"
            offset: Line number to start reading from (optional, for large files)
            limit: Number of lines to read (optional, for large files)

        Returns:
            File contents with line numbers in cat -n format, or ERROR message if file not found.
            Line number format: spaces + line_number + → + content

        Example:
            Read entire file:
            file_path = "/workspace/config.yaml"

            Read specific lines (line 100-150):
            file_path = "/workspace/src/agent.py"
            offset = 100
            limit = 50

            Read a generated output:
            file_path = "/workspace/results/analysis.txt"
        """
        try:
            logger.info("Reading file", file_path=file_path, offset=offset, limit=limit)

            # Validate path if enabled
            if sandbox.config.filesystem.enable_path_validation and not sandbox.validate_path(file_path):
                error_msg = f"Access denied: {file_path} is not in allowed directories"
                logger.error(error_msg, file_path=file_path)
                return f"ERROR: {error_msg}"

            # Read file content with optional offset/limit
            if offset is not None or limit is not None:
                content = sandbox.read_file_range(file_path, offset or 0, limit or 2000)
            else:
                content = sandbox.read_file(file_path)

            if content is None:
                error_msg = f"File not found: {file_path}"
                logger.warning(error_msg, file_path=file_path)
                return f"ERROR: {error_msg}"

            # Format with line numbers in cat -n format
            lines = content.splitlines()
            start_line = (offset or 0) + 1
            formatted_lines = []

            for i, line in enumerate(lines):
                line_num = start_line + i
                # Format: "     1→content" (right-aligned line number with arrow)
                formatted_line = f"{line_num:>6}→{line}"
                formatted_lines.append(formatted_line)

            result = "\n".join(formatted_lines)

            logger.info(
                "File read successfully",
                file_path=file_path,
                size=len(content),
                lines=len(lines),
            )

            return result

        except Exception as e:
            error_msg = f"Failed to read file: {str(e)}"
            logger.error(error_msg, file_path=file_path, error=str(e), exc_info=True)
            return f"ERROR: {error_msg}"

    return Read


def create_write_file_tool(sandbox: Any):
    """Factory function to create Write tool.

    Args:
        sandbox: CodeActSandbox instance

    Returns:
        Configured Write tool function
    """

    @tool
    async def Write(file_path: str, content: str) -> str:
        """Writes a file to the local filesystem.

        This tool will overwrite the existing file if there is one at the provided path.
        ALWAYS prefer editing existing files with Edit tool over Write. Never write new files
        unless explicitly required.

        If this is an existing file, you MUST use the Read tool first to read the file's contents.

        Args:
            file_path: Absolute path to the file to write (must be absolute, not relative)
                      Example: "/workspace/results/output.txt"
            content: Complete content to write to the file

        Returns:
            Confirmation message, or ERROR message if operation failed.

        Example:
            Create a new file:
            file_path = "/workspace/results/summary.txt"
            content = "Analysis complete. Found 42 matches."

            Create a JSON configuration:
            file_path = "/workspace/config.json"
            content = '{"setting": "value", "enabled": true}'
        """
        try:
            logger.info("Writing file", file_path=file_path, size=len(content))

            # Validate path if enabled
            if sandbox.config.filesystem.enable_path_validation and not sandbox.validate_path(file_path):
                error_msg = f"Access denied: {file_path} is not in allowed directories"
                logger.error(error_msg, file_path=file_path)
                return f"ERROR: {error_msg}"

            # Write file
            success = sandbox.write_file(file_path, content)

            if success:
                bytes_written = len(content.encode('utf-8'))
                logger.info(
                    "File written successfully",
                    file_path=file_path,
                    bytes_written=bytes_written,
                )
                return f"Wrote {bytes_written} bytes to {file_path}"
            else:
                error_msg = "Write operation failed"
                logger.error(error_msg, file_path=file_path)
                return f"ERROR: {error_msg}"

        except Exception as e:
            error_msg = f"Failed to write file: {str(e)}"
            logger.error(error_msg, file_path=file_path, error=str(e), exc_info=True)
            return f"ERROR: {error_msg}"

    return Write


def create_edit_file_tool(sandbox: Any):
    """Factory function to create Edit tool.

    Args:
        sandbox: CodeActSandbox instance

    Returns:
        Configured Edit tool function
    """

    @tool
    async def Edit(file_path: str, old_string: str, new_string: str, replace_all: bool = False) -> str:
        """Performs exact string replacements in files (Claude Code standard).

        You must use the Read tool at least once before editing. This tool will error if you
        attempt an edit without reading the file.

        When editing text from Read tool output, ensure you preserve the exact indentation
        (tabs/spaces) as it appears AFTER the line number prefix. The line number prefix format
        is: spaces + line number + → + content. Everything after the arrow is the actual file
        content to match. Never include any part of the line number prefix in old_string or new_string.

        ALWAYS prefer editing existing files in the codebase. NEVER write new files unless explicitly required.

        The edit will FAIL if old_string is not unique in the file. Either provide a larger string
        with more surrounding context to make it unique or use replace_all to change every instance
        of old_string.

        Use replace_all for replacing and renaming strings across the file. This parameter is useful
        if you want to rename a variable for instance.

        Args:
            file_path: Absolute path to the file to modify (not relative)
            old_string: The exact text to replace (must exist and be unique unless replace_all=True)
            new_string: The text to replace it with (must be different from old_string)
            replace_all: Replace all occurrences (default: False)

        Returns:
            Confirmation message, or ERROR message if operation failed.

        Example:
            Single replacement - modify a function:
            file_path = "/workspace/src/agent.py"
            old_string = "def old_function():\\n    pass"
            new_string = "def old_function():\\n    return True"

            Replace all occurrences - rename a variable:
            file_path = "/workspace/src/agent.py"
            old_string = "old_var_name"
            new_string = "new_var_name"
            replace_all = True

            Multi-line replacement with exact indentation:
            file_path = "/workspace/config.yaml"
            old_string = "llm:\\n  name: \\"claude-sonnet\\"\\n  temperature: 0.7"
            new_string = "llm:\\n  name: \\"gpt-4o\\"\\n  temperature: 0.5"

            Add new lines to existing code:
            file_path = "/workspace/src/agent.py"
            old_string = "    def __init__(self):\\n        pass"
            new_string = "    def __init__(self):\\n        self.name = \\"agent\\"\\n        self.version = \\"1.0\\""
        """
        try:
            logger.info(
                "Editing file",
                file_path=file_path,
                old_string_preview=old_string[:50],
                replace_all=replace_all,
            )

            # Validate path if enabled
            if sandbox.config.filesystem.enable_path_validation and not sandbox.validate_path(file_path):
                error_msg = f"Access denied: {file_path} is not in allowed directories"
                logger.error(error_msg, file_path=file_path)
                return f"ERROR: {error_msg}"

            # Edit file
            result = sandbox.edit_file(file_path, old_string, new_string, replace_all)

            if not result.get("success", False):
                error_msg = result.get("error", "Edit operation failed")
                logger.error(error_msg, file_path=file_path)
                return f"ERROR: {error_msg}"

            # Return success message
            message = result.get("message", "File edited successfully")
            logger.info("File edited successfully", file_path=file_path)
            return message

        except Exception as e:
            error_msg = f"Failed to edit file: {str(e)}"
            logger.error(error_msg, file_path=file_path, error=str(e), exc_info=True)
            return f"ERROR: {error_msg}"

    return Edit
