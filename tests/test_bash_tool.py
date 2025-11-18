"""Tests for bash execution tool."""

import pytest
from unittest.mock import Mock, AsyncMock, MagicMock
from src.agent.tools.bash import create_execute_bash_tool


@pytest.fixture
def mock_sandbox():
    """Create a mock sandbox for testing."""
    sandbox = Mock()
    return sandbox


class TestExecuteBashTool:
    """Tests for execute_bash tool."""

    @pytest.mark.asyncio
    async def test_execute_bash_success_with_output(self, mock_sandbox):
        """Test successful bash command execution with output."""
        mock_sandbox.execute_bash_command = AsyncMock(return_value={
            "success": True,
            "stdout": "file1.txt\nfile2.txt\nfile3.txt",
            "stderr": "",
            "exit_code": 0
        })

        execute_bash = create_execute_bash_tool(mock_sandbox)
        result = await execute_bash.ainvoke({
            "command": "ls",
            "working_dir": "/workspace"
        })

        assert "SUCCESS" in result
        assert "file1.txt" in result
        assert "file2.txt" in result
        mock_sandbox.execute_bash_command.assert_called_once_with(
            "ls",
            working_dir="/workspace"
        )

    @pytest.mark.asyncio
    async def test_execute_bash_success_no_output(self, mock_sandbox):
        """Test successful bash command with no output (e.g., mkdir)."""
        mock_sandbox.execute_bash_command = AsyncMock(return_value={
            "success": True,
            "stdout": "",
            "stderr": "",
            "exit_code": 0
        })

        execute_bash = create_execute_bash_tool(mock_sandbox)
        result = await execute_bash.ainvoke({
            "command": "mkdir -p /workspace/testdir"
        })

        assert "SUCCESS" in result
        assert "Command completed successfully" in result

    @pytest.mark.asyncio
    async def test_execute_bash_command_failure(self, mock_sandbox):
        """Test bash command that fails."""
        mock_sandbox.execute_bash_command = AsyncMock(return_value={
            "success": False,
            "stdout": "",
            "stderr": "ls: cannot access '/nonexistent': No such file or directory",
            "exit_code": 2
        })

        execute_bash = create_execute_bash_tool(mock_sandbox)
        result = await execute_bash.ainvoke({
            "command": "ls /nonexistent"
        })

        assert "ERROR" in result
        assert "exit code 2" in result
        assert "No such file or directory" in result

    @pytest.mark.asyncio
    async def test_execute_bash_with_pipe(self, mock_sandbox):
        """Test bash command with pipe."""
        mock_sandbox.execute_bash_command = AsyncMock(return_value={
            "success": True,
            "stdout": "100 lines counted",
            "stderr": "",
            "exit_code": 0
        })

        execute_bash = create_execute_bash_tool(mock_sandbox)
        result = await execute_bash.ainvoke({
            "command": "cat file.txt | wc -l"
        })

        assert "SUCCESS" in result
        assert "100 lines counted" in result

    @pytest.mark.asyncio
    async def test_execute_bash_with_redirect(self, mock_sandbox):
        """Test bash command with output redirection."""
        mock_sandbox.execute_bash_command = AsyncMock(return_value={
            "success": True,
            "stdout": "",
            "stderr": "",
            "exit_code": 0
        })

        execute_bash = create_execute_bash_tool(mock_sandbox)
        result = await execute_bash.ainvoke({
            "command": "echo 'Hello World' > output.txt"
        })

        assert "SUCCESS" in result

    @pytest.mark.asyncio
    async def test_execute_bash_with_grep(self, mock_sandbox):
        """Test bash command with grep."""
        mock_sandbox.execute_bash_command = AsyncMock(return_value={
            "success": True,
            "stdout": "file1.py:def function1():\nfile2.py:def function2():",
            "stderr": "",
            "exit_code": 0
        })

        execute_bash = create_execute_bash_tool(mock_sandbox)
        result = await execute_bash.ainvoke({
            "command": "grep -r 'def ' *.py"
        })

        assert "SUCCESS" in result
        assert "file1.py" in result
        assert "function1" in result

    @pytest.mark.asyncio
    async def test_execute_bash_with_find(self, mock_sandbox):
        """Test bash command with find."""
        mock_sandbox.execute_bash_command = AsyncMock(return_value={
            "success": True,
            "stdout": "./file1.txt\n./subdir/file2.txt\n./subdir/file3.txt",
            "stderr": "",
            "exit_code": 0
        })

        execute_bash = create_execute_bash_tool(mock_sandbox)
        result = await execute_bash.ainvoke({
            "command": "find . -name '*.txt'"
        })

        assert "SUCCESS" in result
        assert "file1.txt" in result
        assert "subdir/file2.txt" in result

    @pytest.mark.asyncio
    async def test_execute_bash_with_multiple_commands(self, mock_sandbox):
        """Test bash command with multiple commands chained."""
        mock_sandbox.execute_bash_command = AsyncMock(return_value={
            "success": True,
            "stdout": "Directory created and file written",
            "stderr": "",
            "exit_code": 0
        })

        execute_bash = create_execute_bash_tool(mock_sandbox)
        result = await execute_bash.ainvoke({
            "command": "mkdir -p output && echo 'test' > output/file.txt && echo 'Directory created and file written'"
        })

        assert "SUCCESS" in result
        assert "Directory created and file written" in result

    @pytest.mark.asyncio
    async def test_execute_bash_with_working_dir(self, mock_sandbox):
        """Test bash command with custom working directory."""
        mock_sandbox.execute_bash_command = AsyncMock(return_value={
            "success": True,
            "stdout": "file.txt",
            "stderr": "",
            "exit_code": 0
        })

        execute_bash = create_execute_bash_tool(mock_sandbox)
        result = await execute_bash.ainvoke({
            "command": "ls",
            "working_dir": "/workspace/results"
        })

        assert "SUCCESS" in result
        mock_sandbox.execute_bash_command.assert_called_once_with(
            "ls",
            working_dir="/workspace/results"
        )

    @pytest.mark.asyncio
    async def test_execute_bash_with_wc(self, mock_sandbox):
        """Test bash command with wc (word count)."""
        mock_sandbox.execute_bash_command = AsyncMock(return_value={
            "success": True,
            "stdout": "  42  256 1824 file.txt",
            "stderr": "",
            "exit_code": 0
        })

        execute_bash = create_execute_bash_tool(mock_sandbox)
        result = await execute_bash.ainvoke({
            "command": "wc file.txt"
        })

        assert "SUCCESS" in result
        assert "42" in result  # line count

    @pytest.mark.asyncio
    async def test_execute_bash_with_du(self, mock_sandbox):
        """Test bash command with du (disk usage)."""
        mock_sandbox.execute_bash_command = AsyncMock(return_value={
            "success": True,
            "stdout": "4.5M\tresults/",
            "stderr": "",
            "exit_code": 0
        })

        execute_bash = create_execute_bash_tool(mock_sandbox)
        result = await execute_bash.ainvoke({
            "command": "du -sh results/"
        })

        assert "SUCCESS" in result
        assert "4.5M" in result

    @pytest.mark.asyncio
    async def test_execute_bash_exception(self, mock_sandbox):
        """Test bash command that raises an exception."""
        mock_sandbox.execute_bash_command = AsyncMock(
            side_effect=Exception("Sandbox connection error")
        )

        execute_bash = create_execute_bash_tool(mock_sandbox)
        result = await execute_bash.ainvoke({
            "command": "ls"
        })

        assert "ERROR" in result
        assert "Failed to execute bash command" in result
        assert "Sandbox connection error" in result

    @pytest.mark.asyncio
    async def test_execute_bash_with_cat(self, mock_sandbox):
        """Test bash command with cat."""
        mock_sandbox.execute_bash_command = AsyncMock(return_value={
            "success": True,
            "stdout": "Line 1\nLine 2\nLine 3",
            "stderr": "",
            "exit_code": 0
        })

        execute_bash = create_execute_bash_tool(mock_sandbox)
        result = await execute_bash.ainvoke({
            "command": "cat file.txt"
        })

        assert "SUCCESS" in result
        assert "Line 1" in result
        assert "Line 2" in result

    @pytest.mark.asyncio
    async def test_execute_bash_with_head(self, mock_sandbox):
        """Test bash command with head."""
        mock_sandbox.execute_bash_command = AsyncMock(return_value={
            "success": True,
            "stdout": "Line 1\nLine 2\nLine 3\nLine 4\nLine 5",
            "stderr": "",
            "exit_code": 0
        })

        execute_bash = create_execute_bash_tool(mock_sandbox)
        result = await execute_bash.ainvoke({
            "command": "head -5 file.txt"
        })

        assert "SUCCESS" in result
        assert "Line 1" in result

    @pytest.mark.asyncio
    async def test_execute_bash_with_awk(self, mock_sandbox):
        """Test bash command with awk."""
        mock_sandbox.execute_bash_command = AsyncMock(return_value={
            "success": True,
            "stdout": "value1\nvalue2\nvalue3",
            "stderr": "",
            "exit_code": 0
        })

        execute_bash = create_execute_bash_tool(mock_sandbox)
        result = await execute_bash.ainvoke({
            "command": "awk '{print $2}' data.txt"
        })

        assert "SUCCESS" in result
        assert "value1" in result
