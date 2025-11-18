"""Tests for filesystem tools."""

import pytest
from unittest.mock import Mock, AsyncMock, MagicMock
from src.agent.tools.filesystem import (
    create_read_file_tool,
    create_write_file_tool,
    create_edit_file_tool,
)


@pytest.fixture
def mock_sandbox():
    """Create a mock sandbox for testing."""
    sandbox = Mock()
    sandbox.config = Mock()
    sandbox.config.filesystem = Mock()
    sandbox.config.filesystem.enable_path_validation = True
    sandbox.config.filesystem.allowed_directories = ["/workspace", "/tmp"]

    return sandbox


class TestReadFileTool:
    """Tests for read_file tool."""

    @pytest.mark.asyncio
    async def test_read_file_success(self, mock_sandbox):
        """Test successful file read."""
        mock_sandbox.validate_path = Mock(return_value=True)
        mock_sandbox.read_file = Mock(return_value="Hello, world!")

        read_file = create_read_file_tool(mock_sandbox)
        result = await read_file.ainvoke({"filepath": "test.txt"})

        assert "SUCCESS" in result
        assert "Hello, world!" in result
        mock_sandbox.read_file.assert_called_once_with("test.txt")

    @pytest.mark.asyncio
    async def test_read_file_not_found(self, mock_sandbox):
        """Test reading non-existent file."""
        mock_sandbox.validate_path = Mock(return_value=True)
        mock_sandbox.read_file = Mock(return_value=None)

        read_file = create_read_file_tool(mock_sandbox)
        result = await read_file.ainvoke({"filepath": "missing.txt"})

        assert "ERROR" in result
        assert "File not found" in result

    @pytest.mark.asyncio
    async def test_read_file_access_denied(self, mock_sandbox):
        """Test reading file outside allowed directories."""
        mock_sandbox.validate_path = Mock(return_value=False)

        read_file = create_read_file_tool(mock_sandbox)
        result = await read_file.ainvoke({"filepath": "/etc/passwd"})

        assert "ERROR" in result
        assert "Access denied" in result


class TestWriteFileTool:
    """Tests for write_file tool."""

    @pytest.mark.asyncio
    async def test_write_file_success(self, mock_sandbox):
        """Test successful file write."""
        mock_sandbox.validate_path = Mock(return_value=True)
        mock_sandbox.write_file = Mock(return_value=True)

        write_file = create_write_file_tool(mock_sandbox)
        result = await write_file.ainvoke({
            "filepath": "output.txt",
            "content": "Test content"
        })

        assert "SUCCESS" in result
        assert "12 characters" in result  # len("Test content")
        mock_sandbox.write_file.assert_called_once_with("output.txt", "Test content")

    @pytest.mark.asyncio
    async def test_write_file_failure(self, mock_sandbox):
        """Test failed file write."""
        mock_sandbox.validate_path = Mock(return_value=True)
        mock_sandbox.write_file = Mock(return_value=False)

        write_file = create_write_file_tool(mock_sandbox)
        result = await write_file.ainvoke({
            "filepath": "output.txt",
            "content": "Test"
        })

        assert "ERROR" in result

    @pytest.mark.asyncio
    async def test_write_file_access_denied(self, mock_sandbox):
        """Test writing file outside allowed directories."""
        mock_sandbox.validate_path = Mock(return_value=False)

        write_file = create_write_file_tool(mock_sandbox)
        result = await write_file.ainvoke({
            "filepath": "/etc/test.txt",
            "content": "Test"
        })

        assert "ERROR" in result
        assert "Access denied" in result


class TestEditFileTool:
    """Tests for edit_file tool."""

    @pytest.mark.asyncio
    async def test_edit_file_success(self, mock_sandbox):
        """Test successful file edit."""
        mock_sandbox.validate_path = Mock(return_value=True)
        mock_sandbox.edit_file = Mock(return_value={
            "success": True,
            "changed": True,
            "message": "Successfully edited test.txt"
        })

        edit_file = create_edit_file_tool(mock_sandbox)
        result = await edit_file.ainvoke({
            "filepath": "test.txt",
            "pattern": "old",
            "replacement": "new"
        })

        assert "SUCCESS" in result
        assert "Successfully edited" in result

    @pytest.mark.asyncio
    async def test_edit_file_dry_run(self, mock_sandbox):
        """Test edit file in dry run mode."""
        mock_sandbox.validate_path = Mock(return_value=True)
        mock_sandbox.edit_file = Mock(return_value={
            "success": True,
            "changed": True,
            "dry_run": True,
            "preview": "new content here"
        })

        edit_file = create_edit_file_tool(mock_sandbox)
        result = await edit_file.ainvoke({
            "filepath": "test.txt",
            "pattern": "old",
            "replacement": "new",
            "dry_run": True
        })

        assert "DRY RUN" in result
        assert "Preview of changes" in result
        assert "new content here" in result


class TestListDirectoryTool:
    """Tests for list_directory tool."""

    @pytest.mark.asyncio
    async def test_list_directory_success(self, mock_sandbox):
        """Test successful directory listing."""
        mock_sandbox.validate_path = Mock(return_value=True)
        mock_sandbox.list_directory = Mock(return_value=[
            {"name": "file1.txt", "type": "file", "path": "file1.txt"},
            {"name": "subdir", "type": "directory", "path": "subdir"},
            {"name": "file2.csv", "type": "file", "path": "file2.csv"},
        ])

        list_dir = create_list_directory_tool(mock_sandbox)
        result = await list_dir.ainvoke({"path": "."})

        assert "SUCCESS" in result
        assert "3 items" in result
        assert "[DIR]  subdir" in result
        assert "[FILE] file1.txt" in result
        assert "[FILE] file2.csv" in result

    @pytest.mark.asyncio
    async def test_list_directory_empty(self, mock_sandbox):
        """Test listing empty directory."""
        mock_sandbox.validate_path = Mock(return_value=True)
        mock_sandbox.list_directory = Mock(return_value=[])

        list_dir = create_list_directory_tool(mock_sandbox)
        result = await list_dir.ainvoke({"path": "."})

        assert "SUCCESS" in result
        assert "empty" in result


class TestCreateDirectoryTool:
    """Tests for create_directory tool."""

    @pytest.mark.asyncio
    async def test_create_directory_success(self, mock_sandbox):
        """Test successful directory creation."""
        mock_sandbox.validate_path = Mock(return_value=True)
        mock_sandbox.create_directory = Mock(return_value=True)

        create_dir = create_create_directory_tool(mock_sandbox)
        result = await create_dir.ainvoke({"path": "newdir"})

        assert "SUCCESS" in result
        assert "Created directory 'newdir'" in result
        mock_sandbox.create_directory.assert_called_once_with("newdir")


class TestSearchFilesTool:
    """Tests for search_files tool."""

    @pytest.mark.asyncio
    async def test_search_files_found(self, mock_sandbox):
        """Test successful file search with results."""
        mock_sandbox.validate_path = Mock(return_value=True)
        mock_sandbox.search_files = Mock(return_value=[
            "file1.py",
            "subdir/file2.py",
            "test_file.py"
        ])

        search_files = create_search_files_tool(mock_sandbox)
        result = await search_files.ainvoke({
            "pattern": "*.py",
            "directory": "."
        })

        assert "SUCCESS" in result
        assert "Found 3 file(s)" in result
        assert "file1.py" in result
        assert "subdir/file2.py" in result

    @pytest.mark.asyncio
    async def test_search_files_not_found(self, mock_sandbox):
        """Test file search with no results."""
        mock_sandbox.validate_path = Mock(return_value=True)
        mock_sandbox.search_files = Mock(return_value=[])

        search_files = create_search_files_tool(mock_sandbox)
        result = await search_files.ainvoke({
            "pattern": "*.xyz",
            "directory": "."
        })

        assert "SUCCESS" in result
        assert "No files matching" in result


class TestGetFileInfoTool:
    """Tests for get_file_info tool."""

    @pytest.mark.asyncio
    async def test_get_file_info_success(self, mock_sandbox):
        """Test successful file info retrieval."""
        mock_sandbox.validate_path = Mock(return_value=True)
        mock_sandbox.get_file_info_detailed = Mock(return_value={
            "path": "test.txt",
            "exists": True,
            "size_bytes": 1024,
            "size_chars": 1000,
            "lines": 50,
            "max_line_length": 80,
            "is_empty": False
        })

        get_info = create_get_file_info_tool(mock_sandbox)
        result = await get_info.ainvoke({"filepath": "test.txt"})

        assert "SUCCESS" in result
        assert "1024 bytes" in result
        assert "50" in result  # lines

    @pytest.mark.asyncio
    async def test_get_file_info_not_found(self, mock_sandbox):
        """Test file info for non-existent file."""
        mock_sandbox.validate_path = Mock(return_value=True)
        mock_sandbox.get_file_info_detailed = Mock(return_value={
            "path": "missing.txt",
            "exists": False
        })

        get_info = create_get_file_info_tool(mock_sandbox)
        result = await get_info.ainvoke({"filepath": "missing.txt"})

        assert "ERROR" in result
        assert "File not found" in result


class TestMoveFileTool:
    """Tests for move_file tool."""

    @pytest.mark.asyncio
    async def test_move_file_success(self, mock_sandbox):
        """Test successful file move."""
        mock_sandbox.validate_path = Mock(return_value=True)
        mock_sandbox.move_file = Mock(return_value=True)

        move_file = create_move_file_tool(mock_sandbox)
        result = await move_file.ainvoke({
            "source": "old.txt",
            "destination": "new.txt"
        })

        assert "SUCCESS" in result
        assert "Moved file from 'old.txt' to 'new.txt'" in result
        mock_sandbox.move_file.assert_called_once_with("old.txt", "new.txt")

    @pytest.mark.asyncio
    async def test_move_file_source_denied(self, mock_sandbox):
        """Test moving file with source access denied."""
        def validate_side_effect(path):
            return path != "/forbidden/file.txt"

        mock_sandbox.validate_path = Mock(side_effect=validate_side_effect)

        move_file = create_move_file_tool(mock_sandbox)
        result = await move_file.ainvoke({
            "source": "/forbidden/file.txt",
            "destination": "/workspace/file.txt"
        })

        assert "ERROR" in result
        assert "Access denied" in result
        assert "source" in result
