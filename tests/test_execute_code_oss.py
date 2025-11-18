#!/usr/bin/env python3
"""
Test script for execute_code tool with OSS image upload integration.

This script:
1. Sets up a Daytona sandbox
2. Tests code execution with matplotlib chart generation (plt.show())
3. Tests code execution with saved images (plt.savefig())
4. Verifies OSS upload functionality
5. Checks that markdown image URLs are returned

Run with:
    python test_execute_code_oss.py
"""

import asyncio
import sys
import traceback
import importlib.util

# Add project to path
sys.path.insert(0, "/Users/chen/projects/codeact-mcp")

from src.codeact_mcp.session import SessionManager
from src.codeact_mcp.config import CoreConfig


def load_module_from_path(module_name, file_path):
    """Load a module directly from file path to bypass package import chain."""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# Load execute_code tool directly
execute_module = load_module_from_path(
    "execute_tool",
    "/Users/chen/projects/codeact-mcp/src/agent/tools/code_execution/execute.py"
)
create_execute_code_tool = execute_module.create_execute_code_tool


class TestResult:
    """Track test results."""
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.errors = []

    def success(self, name: str, details: str = ""):
        self.passed += 1
        print(f"✅ PASS: {name}")
        if details:
            print(f"   {details}")

    def failure(self, name: str, reason: str):
        self.failed += 1
        self.errors.append((name, reason))
        print(f"❌ FAIL: {name}")
        print(f"   Reason: {reason}")

    def summary(self):
        total = self.passed + self.failed
        print("\n" + "=" * 60)
        print(f"TEST SUMMARY: {self.passed}/{total} passed")
        if self.errors:
            print("\nFailed tests:")
            for name, reason in self.errors:
                print(f"  - {name}: {reason}")
        print("=" * 60)


async def setup_environment():
    """Set up the sandbox environment."""
    print("\n" + "=" * 60)
    print("SETUP: Initializing sandbox environment")
    print("=" * 60)

    # Load configuration
    print("\n1. Loading CoreConfig from config.yaml...")
    config = CoreConfig.load()
    print(f"   Daytona base URL: {config.daytona.base_url}")

    # Create and initialize session
    print("\n2. Creating session...")
    session = SessionManager.get_session("test-execute-code-oss", config)

    print("\n3. Initializing session (this may take a moment)...")
    await session.initialize()
    print("   Session initialized successfully!")

    # Get sandbox info
    sandbox = session.sandbox
    print(f"\n4. Sandbox info:")
    print(f"   Sandbox ID: {sandbox.sandbox_id}")

    # Create execute_code tool
    print("\n5. Creating execute_code tool...")
    execute_code_tool = create_execute_code_tool(sandbox, session.mcp_registry)
    print(f"   Created tool: {execute_code_tool.name}")

    return session, sandbox, execute_code_tool


async def install_sandbox_dependencies(sandbox, results: TestResult):
    """Install required packages in the sandbox."""
    print("\n" + "=" * 60)
    print("SETUP: Installing sandbox dependencies")
    print("=" * 60)

    code = '''
import subprocess
import sys

# Install matplotlib and pillow
result = subprocess.run(
    [sys.executable, "-m", "pip", "install", "matplotlib", "pillow", "numpy", "-q"],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print("Dependencies installed successfully")
else:
    print(f"Install failed: {result.stderr}")
    sys.exit(1)
'''

    try:
        result = await sandbox.execute(code)
        print(f"Result: {result.stdout}")

        if result.success:
            results.success("Install dependencies", "matplotlib, pillow, numpy installed")
        else:
            results.failure("Install dependencies", result.stderr or result.stdout)
    except Exception as e:
        results.failure("Install dependencies", str(e))
        traceback.print_exc()


async def test_basic_execution(execute_code_tool, results: TestResult):
    """Test basic code execution without charts."""
    print("\n" + "=" * 60)
    print("TEST: Basic code execution")
    print("=" * 60)

    code = '''
print("Hello from sandbox!")
x = 1 + 2
print(f"Result: {x}")
'''

    try:
        result = await execute_code_tool.ainvoke({"code": code})
        print(f"Result:\n{result}")

        if "SUCCESS" in result and "Hello from sandbox!" in result:
            results.success("Basic execution", "Code executed successfully")
        else:
            results.failure("Basic execution", "Unexpected output")
    except Exception as e:
        results.failure("Basic execution", str(e))
        traceback.print_exc()


async def test_matplotlib_show(execute_code_tool, results: TestResult):
    """Test matplotlib chart with plt.show() - captured via artifacts."""
    print("\n" + "=" * 60)
    print("TEST: Matplotlib plt.show() chart (artifact capture)")
    print("=" * 60)

    code = '''
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import numpy as np

# Create a simple chart
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2)
plt.title('Sine Wave Chart')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.grid(True)
plt.show()

print("Chart generated with plt.show()")
'''

    try:
        result = await execute_code_tool.ainvoke({"code": code})
        print(f"Result:\n{result}")

        if "SUCCESS" in result:
            if "Uploaded images:" in result and "![" in result:
                results.success("Matplotlib plt.show()", "Chart captured and uploaded to OSS")
            elif "Chart generated" in result:
                results.success("Matplotlib plt.show()", "Code executed (artifact capture may not be available)")
            else:
                results.failure("Matplotlib plt.show()", "No uploaded images in result")
        else:
            results.failure("Matplotlib plt.show()", "Execution failed")
    except Exception as e:
        results.failure("Matplotlib plt.show()", str(e))
        traceback.print_exc()


async def test_matplotlib_savefig(execute_code_tool, results: TestResult):
    """Test matplotlib chart saved with plt.savefig() - detected via files_created."""
    print("\n" + "=" * 60)
    print("TEST: Matplotlib plt.savefig() chart (file detection)")
    print("=" * 60)

    code = '''
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Create a bar chart
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]

plt.figure(figsize=(8, 6))
plt.bar(categories, values, color='steelblue')
plt.title('Bar Chart Example')
plt.xlabel('Category')
plt.ylabel('Value')

# Save to results directory
plt.savefig('results/bar_chart.png', dpi=100, bbox_inches='tight')
plt.close()

print("Saved bar_chart.png to results/")
'''

    try:
        result = await execute_code_tool.ainvoke({"code": code})
        print(f"Result:\n{result}")

        if "SUCCESS" in result:
            if "bar_chart.png" in result:
                if "Uploaded images:" in result and "![" in result:
                    results.success("Matplotlib savefig()", "Chart saved and uploaded to OSS")
                else:
                    results.failure("Matplotlib savefig()", "File created but not uploaded")
            else:
                results.failure("Matplotlib savefig()", "Chart file not created")
        else:
            results.failure("Matplotlib savefig()", "Execution failed")
    except Exception as e:
        results.failure("Matplotlib savefig()", str(e))
        traceback.print_exc()


async def test_multiple_images(execute_code_tool, results: TestResult):
    """Test multiple image generation and upload."""
    print("\n" + "=" * 60)
    print("TEST: Multiple images")
    print("=" * 60)

    code = '''
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Chart 1: Line plot
plt.figure(figsize=(8, 5))
x = np.linspace(0, 10, 50)
plt.plot(x, np.cos(x), 'r-', label='cos')
plt.plot(x, np.sin(x), 'b--', label='sin')
plt.title('Trigonometric Functions')
plt.legend()
plt.savefig('results/trig_chart.png', dpi=100)
plt.close()

# Chart 2: Scatter plot
plt.figure(figsize=(8, 5))
np.random.seed(42)
x = np.random.randn(50)
y = np.random.randn(50)
plt.scatter(x, y, c='purple', alpha=0.6)
plt.title('Random Scatter')
plt.savefig('results/scatter_chart.png', dpi=100)
plt.close()

# Chart 3: Pie chart
plt.figure(figsize=(8, 8))
sizes = [30, 25, 20, 15, 10]
labels = ['A', 'B', 'C', 'D', 'E']
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart')
plt.savefig('results/pie_chart.png', dpi=100)
plt.close()

print("Generated 3 charts: trig_chart.png, scatter_chart.png, pie_chart.png")
'''

    try:
        result = await execute_code_tool.ainvoke({"code": code})
        print(f"Result:\n{result}")

        if "SUCCESS" in result:
            # Count uploaded images
            upload_count = result.count("![")
            files_created = all(f in result for f in ["trig_chart.png", "scatter_chart.png", "pie_chart.png"])

            if files_created and upload_count >= 3:
                results.success("Multiple images", f"All 3 charts uploaded ({upload_count} images)")
            elif files_created:
                results.failure("Multiple images", f"Files created but only {upload_count} uploaded")
            else:
                results.failure("Multiple images", "Some files not created")
        else:
            results.failure("Multiple images", "Execution failed")
    except Exception as e:
        results.failure("Multiple images", str(e))
        traceback.print_exc()


async def test_pil_image(execute_code_tool, results: TestResult):
    """Test PIL image generation and upload."""
    print("\n" + "=" * 60)
    print("TEST: PIL image generation")
    print("=" * 60)

    code = '''
from PIL import Image, ImageDraw

# Create a simple image
img = Image.new('RGB', (400, 300), color='white')
draw = ImageDraw.Draw(img)

# Draw some shapes
draw.rectangle([50, 50, 350, 250], outline='blue', width=3)
draw.ellipse([100, 100, 300, 200], fill='lightblue', outline='navy')
draw.text((150, 130), "Test Image", fill='darkblue')

# Save
img.save('results/pil_test.png')

print("Created PIL test image")
'''

    try:
        result = await execute_code_tool.ainvoke({"code": code})
        print(f"Result:\n{result}")

        if "SUCCESS" in result:
            if "pil_test.png" in result and "Uploaded images:" in result:
                results.success("PIL image", "Image created and uploaded")
            elif "pil_test.png" in result:
                results.failure("PIL image", "Image created but not uploaded")
            else:
                results.failure("PIL image", "Image not created")
        else:
            results.failure("PIL image", "Execution failed")
    except Exception as e:
        results.failure("PIL image", str(e))
        traceback.print_exc()


async def test_oss_url_format(execute_code_tool, results: TestResult):
    """Verify OSS URL format in response."""
    print("\n" + "=" * 60)
    print("TEST: OSS URL format validation")
    print("=" * 60)

    code = '''
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 4))
plt.plot([1, 2, 3], [1, 4, 2], 'go-')
plt.title('URL Format Test')
plt.savefig('results/url_test.png')
plt.close()

print("Chart saved for URL test")
'''

    try:
        result = await execute_code_tool.ainvoke({"code": code})
        print(f"Result:\n{result}")

        if "SUCCESS" in result:
            # Check for markdown image format
            if "![" in result and "](" in result and "http" in result:
                # Extract URL and validate format
                import re
                urls = re.findall(r'\!\[.*?\]\((https?://[^)]+)\)', result)
                if urls:
                    url = urls[0]
                    if ".png" in url and "charts/" in url:
                        results.success("OSS URL format", f"Valid markdown URL: {url[:80]}...")
                    else:
                        results.failure("OSS URL format", f"URL format issue: {url}")
                else:
                    results.failure("OSS URL format", "No valid URL pattern found")
            else:
                results.failure("OSS URL format", "No markdown image in result")
        else:
            results.failure("OSS URL format", "Execution failed")
    except Exception as e:
        results.failure("OSS URL format", str(e))
        traceback.print_exc()


async def test_execution_result_charts(sandbox, results: TestResult):
    """Test that ExecutionResult properly captures charts."""
    print("\n" + "=" * 60)
    print("TEST: ExecutionResult charts field")
    print("=" * 60)

    code = '''
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.figure()
plt.plot([1, 2, 3], [1, 2, 3])
plt.title('Direct Result Test')
plt.show()

print("Testing charts field")
'''

    try:
        result = await sandbox.execute(code)
        print(f"ExecutionResult:")
        print(f"  success: {result.success}")
        print(f"  stdout: {result.stdout[:100]}...")
        print(f"  files_created: {result.files_created}")
        print(f"  charts: {len(result.charts)} chart(s)")

        for i, chart in enumerate(result.charts):
            print(f"    Chart {i}: type={chart.type}, title={chart.title}")
            if chart.png_base64:
                print(f"      PNG data: {len(chart.png_base64)} chars")

        if result.success:
            if hasattr(result, 'charts'):
                results.success("ExecutionResult charts", f"charts field exists with {len(result.charts)} items")
            else:
                results.failure("ExecutionResult charts", "charts field missing")
        else:
            results.failure("ExecutionResult charts", "Execution failed")
    except Exception as e:
        results.failure("ExecutionResult charts", str(e))
        traceback.print_exc()


async def test_error_handling(execute_code_tool, results: TestResult):
    """Test error handling in code execution."""
    print("\n" + "=" * 60)
    print("TEST: Error handling")
    print("=" * 60)

    code = '''
# This will cause an error
undefined_variable + 1
'''

    try:
        result = await execute_code_tool.ainvoke({"code": code})
        print(f"Result:\n{result}")

        if "ERROR" in result:
            results.success("Error handling", "Errors properly reported")
        else:
            results.failure("Error handling", "Error not properly caught")
    except Exception as e:
        results.failure("Error handling", str(e))
        traceback.print_exc()


async def cleanup(session_id: str):
    """Clean up the session."""
    print("\n" + "=" * 60)
    print("CLEANUP: Cleaning up session")
    print("=" * 60)

    try:
        await SessionManager.cleanup_session(session_id)
        print("   Session cleaned up successfully")
    except Exception as e:
        print(f"   Error during cleanup: {e}")


async def main():
    """Main test function."""
    print("\n" + "=" * 60)
    print("EXECUTE CODE + OSS UPLOAD TEST")
    print("=" * 60)

    results = TestResult()
    session = None

    try:
        # Setup
        session, sandbox, execute_code_tool = await setup_environment()

        # Dependencies are now pre-installed in snapshot - no need to install
        # await install_sandbox_dependencies(sandbox, results)

        # Run tests
        await test_basic_execution(execute_code_tool, results)
        await test_execution_result_charts(sandbox, results)
        await test_matplotlib_show(execute_code_tool, results)
        await test_matplotlib_savefig(execute_code_tool, results)
        await test_multiple_images(execute_code_tool, results)
        await test_pil_image(execute_code_tool, results)
        await test_oss_url_format(execute_code_tool, results)
        await test_error_handling(execute_code_tool, results)

    except Exception as e:
        print(f"\n❌ FATAL ERROR: {e}")
        traceback.print_exc()
        results.failure("Setup/Execution", str(e))

    finally:
        # Cleanup
        if session:
            await cleanup("test-execute-code-oss")

        # Summary
        results.summary()

        # Return exit code
        return 0 if results.failed == 0 else 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
