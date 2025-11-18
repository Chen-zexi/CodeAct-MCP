"""Execute code tool for running Python code in the CodeAct sandbox."""

import base64
from pathlib import Path
from typing import Any

import structlog
from langchain_core.tools import tool

# Import OSS upload functions
from lib.oss_uploader import upload_bytes, get_public_url

logger = structlog.get_logger(__name__)

# Image extensions to detect for OSS upload
IMAGE_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.svg', '.gif', '.webp', '.bmp', '.tiff'}


def create_execute_code_tool(sandbox: Any, mcp_registry: Any):
    """Factory function to create execute_code tool with injected dependencies.

    Args:
        sandbox: CodeActSandbox instance for code execution
        mcp_registry: MCPRegistry instance with available MCP tools

    Returns:
        Configured execute_code tool function
    """

    @tool
    async def execute_code(code: str) -> str:
        """Execute Python code in the sandbox environment.

        Use this tool for complex operations that require Python logic, data processing,
        or interactions with MCP tools (tavily, github, etc.).

        The code executes in an isolated sandbox with:
        - MCP tools available via: from tools.{server_name} import {tool_name}
        - Workspace directories: results/, data/
        - Python standard library and common packages (pandas, requests, etc.)

        Args:
            code: Complete Python code to execute. Must be self-contained.
                  Print a summary of results (not full data) to stdout.

        Returns:
            Execution result containing SUCCESS/ERROR status, stdout, stderr, and files created.

        Example:
            code = '''
            from tools.tavily import tavily_search
            import json

            results = tavily_search(query="AI agents", max_results=5)
            filtered = [r for r in results if r.get('score', 0) > 0.7]

            with open('results/output.json', 'w') as f:
                json.dump(filtered, f, indent=2)

            print(f"Saved {len(filtered)} high-quality results")
            '''
        """
        if not sandbox:
            return "ERROR: Sandbox not initialized"

        try:
            logger.info("Executing code in sandbox", code_length=len(code))

            # Execute code in sandbox
            result = await sandbox.execute(code)

            if result.success:
                # Format success response
                parts = ["SUCCESS"]

                if result.stdout:
                    parts.append(result.stdout)

                if result.files_created:
                    # Extract file names from file objects
                    files = [
                        f.name if hasattr(f, "name") else str(f)
                        for f in result.files_created
                    ]
                    if files:
                        parts.append(f"Files created: {', '.join(files)}")

                # Upload images to OSS
                uploaded_images = []

                # 1. Upload charts from artifacts (matplotlib plt.show())
                if hasattr(result, 'charts') and result.charts:
                    for i, chart in enumerate(result.charts):
                        if chart.png_base64:
                            try:
                                # Decode base64 and upload
                                png_bytes = base64.b64decode(chart.png_base64)
                                oss_key = f"charts/{result.execution_id}/chart_{i}.png"
                                if upload_bytes(oss_key, png_bytes):
                                    url = get_public_url(oss_key)
                                    title = chart.title if chart.title else f"chart_{i}"
                                    uploaded_images.append(f"![{title}]({url})")
                                    logger.info(f"Uploaded artifact chart to OSS: {oss_key}")
                            except Exception as e:
                                logger.error(f"Failed to upload chart artifact: {e}")

                # 2. Upload saved image files from results/
                if result.files_created:
                    for file_path in result.files_created:
                        file_str = file_path.name if hasattr(file_path, "name") else str(file_path)
                        ext = Path(file_str).suffix.lower()
                        if ext in IMAGE_EXTENSIONS:
                            try:
                                # Download from sandbox
                                file_bytes = sandbox.download_file_bytes(file_str)
                                if file_bytes:
                                    # Upload to OSS
                                    filename = Path(file_str).name
                                    oss_key = f"charts/{result.execution_id}/{filename}"
                                    if upload_bytes(oss_key, file_bytes):
                                        url = get_public_url(oss_key)
                                        uploaded_images.append(f"![{file_str}]({url})")
                                        logger.info(f"Uploaded saved image to OSS: {oss_key}")
                            except Exception as e:
                                logger.error(f"Failed to upload saved image {file_str}: {e}")

                # Add uploaded images to response
                if uploaded_images:
                    parts.append("\nUploaded images:")
                    parts.extend(uploaded_images)

                response = "\n".join(parts)
                logger.info(
                    "Code executed successfully",
                    stdout_length=len(result.stdout),
                    images_uploaded=len(uploaded_images)
                )
                return response
            else:
                # Format error response
                # Python tracebacks often go to stdout in some environments
                # Show stderr if available, otherwise show stdout
                error_output = result.stderr if result.stderr else result.stdout

                logger.warning(
                    "Code execution failed",
                    stderr_length=len(result.stderr),
                    stdout_length=len(result.stdout),
                )

                return f"ERROR\n{error_output}"

        except Exception as e:
            logger.error("Code execution exception", error=str(e), exc_info=True)
            return f"ERROR: {str(e)}"

    return execute_code
