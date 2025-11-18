"""Execute bash commands in the sandbox."""

from typing import Any, Optional

import structlog
from langchain_core.tools import tool

logger = structlog.get_logger(__name__)


def create_execute_bash_tool(sandbox: Any):
    """Factory function to create Bash tool with injected dependencies.

    Args:
        sandbox: CodeActSandbox instance for bash command execution

    Returns:
        Configured Bash tool function
    """

    @tool
    async def Bash(
        command: str,
        description: Optional[str] = None,
        timeout: Optional[int] = 120000,
        run_in_background: Optional[bool] = False,
        working_dir: Optional[str] = "/home/daytona",
    ) -> str:
        """Executes bash commands in a persistent shell session with proper handling and security measures.

        IMPORTANT: This tool is for terminal operations like git, npm, docker, etc.
        DO NOT use it for file operations (reading, writing, editing, searching, finding files)
        - use the specialized tools for those instead.

        Args:
            command: The bash command to execute
            description: Clear, concise description of what this command does (5-10 words, in active voice)
                        Examples: "List files in current directory", "Show working tree status"
            timeout: Optional timeout in milliseconds (max 600000 = 10 minutes, default 120000 = 2 minutes)
            run_in_background: Set to true to run this command in the background
            working_dir: Working directory for command execution (default: current directory)
                        Note: Try to maintain working directory using absolute paths instead of cd

        Returns:
            Command output (stdout and stderr), or ERROR message if execution failed.

        Path Handling:
            IMPORTANT: Always quote paths with spaces using double quotes
            ✅ cd "/Users/name/My Documents"
            ✅ python "/path/with spaces/script.py"
            ❌ cd /Users/name/My Documents  (will fail)

        Command Chaining:
            ✅ Sequential with dependency (use &&) - All commands must succeed
            mkdir new_dir && cd new_dir && touch file.txt

            ✅ Sequential without dependency (use ;) - Run regardless of previous command
            echo "start"; sleep 5; echo "end"

            ❌ NEVER use newlines to separate commands (newlines OK inside quoted strings)

        Examples:
            Package management:
            command = "pip install pytest"
            description = "Install pytest package"

            Running tests:
            command = "pytest tests/ -v"
            description = "Run test suite with verbose output"

            Git operations:
            command = "git status"
            description = "Show working tree status"

            Chain commands with &&:
            command = "mkdir results && cd results && touch output.txt"
            description = "Create directory and file"

            Background execution:
            command = "npm run dev"
            description = "Start development server"
            run_in_background = True

        Use THIS tool for:
        - Terminal operations (git, npm, docker, pip, pytest)
        - Directory operations (ls, mkdir, rmdir, file listing)
        - File discovery and search (find, locate)
        - File metadata (stat, file, wc -l)
        - File operations (cp, mv, chmod, rm)
        - System commands and utilities (grep, sed, awk, cut, du)
        - Text processing with Unix tools
        - Building and testing

        DO NOT use for file operations - use specialized tools instead:
        - Reading files → Use Read tool
        - Writing files → Use Write tool
        - Editing files → Use Edit tool
        - Finding files by pattern → Use Glob tool
        - Searching file contents → Use Grep tool
        """
        try:
            logger.info(
                "Executing bash command",
                command=command[:100],
                working_dir=working_dir,
                timeout=timeout,
                background=run_in_background,
            )

            # Convert timeout from milliseconds to seconds for sandbox
            timeout_seconds = timeout / 1000 if timeout else 120

            # Execute bash command in sandbox
            result = await sandbox.execute_bash_command(
                command,
                working_dir=working_dir,
                timeout=timeout_seconds,
                background=run_in_background,
            )

            if result["success"]:
                stdout = result.get("stdout", "")
                stderr = result.get("stderr", "")

                # Combine stdout and stderr for complete output
                output = stdout
                if stderr:
                    output += f"\n{stderr}" if output else stderr

                if output:
                    logger.info(
                        "Bash command executed successfully",
                        command=command[:50],
                        output_length=len(output),
                    )
                    return output
                else:
                    # Command succeeded but no output (e.g., mkdir)
                    logger.info(
                        "Bash command executed successfully (no output)",
                        command=command[:50],
                    )
                    return "Command completed successfully"

            else:
                # Command failed
                stderr = result.get("stderr", "Command execution failed")
                exit_code = result.get("exit_code", -1)

                logger.warning(
                    "Bash command failed",
                    command=command[:50],
                    exit_code=exit_code,
                    stderr_length=len(stderr),
                )

                return f"ERROR (exit code {exit_code})\n{stderr}"

        except Exception as e:
            error_msg = f"Failed to execute bash command: {str(e)}"
            logger.error(
                error_msg,
                command=command[:50],
                error=str(e),
                exc_info=True,
            )
            return f"ERROR: {error_msg}"

    return Bash
