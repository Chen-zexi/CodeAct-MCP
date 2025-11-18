# Daytona Documentation v0.0.0-dev
# Generated on: 2025-11-14


Daytona API keys are used to authenticate requests to the [Daytona API](https://www.daytona.io/docs/en/tools/api.md). You can view, create, or delete your API Keys on the [API Keys](https://app.daytona.io/dashboard/keys) page.

## Creating an API key

You can obtain an API key from the Daytona platform:

1. Navigate to [API Keys](https://app.daytona.io/dashboard/keys), on the [Daytona Dashboard](https://app.daytona.io/dashboard/).
2. Click the **`Create Key`** button.
3. In the open modal, create and copy a new key to your clipboard.

To use an API key in your application, set the `DAYTONA_API_KEY` environment variable as described on the [Configuration](https://www.daytona.io/docs/en/configuration.md) page.

## Permissions & Scopes

When creating a new API Key, you can select the specific permissions (scopes) it should have. Scopes control what actions the key can perform. Grant only the scopes you need for each key.

Below is a list of available scopes and their descriptions:

| Resource    | Scope                | Description                          |
|-------------|----------------------|--------------------------------------|
| Sandboxes   | `write:sandboxes`    | Create/modify sandboxes           |
|             | `delete:sandboxes`   | Delete sandboxes                     |
| Snapshots   | `write:snapshots`    | Create/modify snapshots           |
|             | `delete:snapshots`   | Delete snapshots                     |
| Registries  | `write:registries`   | Create/modify registries          |
|             | `delete:registries`  | Delete registries                    |
| Volumes     | `read:volumes`       | View volumes                         |
|             | `write:volumes`      | Create/modify volumes             |
|             | `delete:volumes`     | Delete volumes                       |
| Audit       | `read:audit_logs`    | View audit logs                      |

Daytona Audit Logs provide a detailed record of user and system activity across your organization. Use this feature to track sandbox lifecycle events, user access, system changes, and more.

You can access Audit Logs from the [Dashboard](https://app.daytona.io/dashboard/audit-logs).

## Prerequisites

Audit logs are available to:
- **Admins** - Full access to all audit logs
- **Members** - Access only if they have audit log permissions

Contact your organization admin if you cannot access audit logs.

## Real-Time Updates

Enable the **Real-Time Updates** toggle in the top-right corner of the Audit Logs page to automatically refresh logs as new events occur.

## Log Structure

Each log entry includes the following columns:

| Field     | Description                            |
|---------- |----------------------------------------|
| **Time**  | Timestamp of when the action occurred (UTC)  |
| **User**  | Email of the user who performed action  |
| **Action**| Operation executed                      |
| **Target**| Resource type affected                  |
| **Outcome**| Result status code and message         |

### Example

```text
Time:       5h ago (7/31/2025, 8:15:27 AM)
User:       janedoe@acme.com
Action:     create
Target:     sandbox (ID: 10f249ad-...)
Outcome:    Success (200)
```

## Use Cases

- **Security audits**: Monitor for unauthorized access or sandbox misuse
- **Debugging**: Understand sandbox lifecycle issues (e.g. failed starts)
- **Compliance Export**: Export logs for internal or external audits (Coming soon)

## Actions

Below is the complete list of actions logged by Daytona:

```text
create, read, update, delete, login,
set_default, update_access, update_quota,
suspend, unsuspend, accept, decline,
link_account, unlink_account, leave_organization,
regenerate_key_pair, update_scheduling,
start, stop, replace_labels, create_backup,
update_public_status, set_auto_stop_interval,
set_auto_archive_interval, set_auto_delete_interval, archive,
get_port_preview_url, set_general_status, activate, deactivate,
update_network_settings, get_webhook_app_portal_access,
send_webhook_message, initialize_webhooks,
update_sandbox_default_limited_network_egress,
create_ssh_access, revoke_ssh_access,
toolbox_delete_file, toolbox_download_file, toolbox_create_folder,
toolbox_move_file, toolbox_set_file_permissions, toolbox_replace_in_files,
toolbox_upload_file, toolbox_bulk_upload_files,
toolbox_git_add_files, toolbox_git_create_branch, toolbox_git_delete_branch,
toolbox_git_clone_repository, toolbox_git_commit_changes,
toolbox_git_pull_changes, toolbox_git_push_changes,
toolbox_git_checkout_branch, toolbox_execute_command,
toolbox_create_session, toolbox_session_execute_command,
toolbox_delete_session, toolbox_computer_use_start,
toolbox_computer_use_stop, toolbox_computer_use_restart_process
```

## Targets

Each action targets a specific resource type. Possible targets include:

```text
api_key, organization, organization_invitation,
organization_role, organization_user, docker_registry,
runner, sandbox, snapshot, user, volume
```

## Outcomes

The outcome field indicates the result of the action. Statuses follow standard HTTP semantics:

| Outcome | Description |
|---------|-------------|
| **Info** | Informational (1xx codes) |
| **Success** | Action succeeded (2xx codes) |
| **Redirect** | Redirects (3xx codes) |
| **Error** | Client/server error (4xx/5xx) |

Example errors may include:

- `400` – Sandbox is not started
- `403` – Unauthorized
- `500` – Internal error

{/* ## Filtering & Pagination

You can filter and search logs by:

- Action type
- Target resource
- Outcome status
- User email

Use the page size selector to change how many results are shown per page. */}

The [Billing](https://app.daytona.io/dashboard/billing) page in the Daytona Dashboard provides an overview of your Organization's billing, wallet, and usage details.

## Wallet Overview

The Wallet section shows the balance of the Organization's wallet and the amount of credits spent this month.

## Automatic Top-Up

Organizations can set automatic top-up rules for their wallets.

- **Threshold** — When the wallet balance drops to this amount, a top-up is triggered.  
- **Target** — The wallet balance is topped up to this amount.

Set both **Threshold** and **Target** to `0` to disable automatic top-up.

## Cost Breakdown

The Cost Breakdown chart shows a breakdown of costs per resource. Users can view consumption for CPU, RAM and Disk and toggle between area and bar charts.

**Computer Use** enables programmatic control of desktop environments within Daytona sandboxes. It provides mouse, keyboard, screenshot, and display operations for automating GUI interactions and testing desktop applications.

We recommend using this instance type for most tasks.

## Common Use Cases

- **GUI Application Testing** - Automate interactions with desktop applications, click buttons, fill forms, and validate UI behavior
- **Visual Testing & Screenshots** - Capture screenshots of applications, compare UI states, and perform visual regression testing  
- **Desktop Automation** - Automate repetitive desktop tasks, file management through GUI, and complex workflows
- **Human-in-the-Loop** - Access the VNC interface directly from the [Daytona Dashboard](https://app.daytona.io/dashboard/sandboxes) to manually control and interact with the desktop environment alongside automated scripts

## SDK References

Choose your preferred SDK to get started with computer use automation:

### TypeScript SDK
Complete API reference for computer use operations in TypeScript.

[View TypeScript SDK →](https://www.daytona.io/docs/en/typescript-sdk/computer-use.md)

### Python SDK  
Complete API reference for computer use operations in Python (sync & async).

[View Python SDK →](https://www.daytona.io/docs/en/python-sdk/sync/computer-use.md)

## Quick Example

    ```python
    from daytona import Daytona

    # Initialize using environment variables (recommended)
    daytona = Daytona()
    # Or explicitly configure:
    # daytona = Daytona(
    #     api_key=os.getenv('DAYTONA_API_KEY'),
    #     api_url=os.getenv('DAYTONA_API_URL', 'https://app.daytona.io/api')
    # )

    # Create sandbox from default snapshot (includes desktop environment)
    sandbox = daytona.create()

    # Start computer use processes
    result = sandbox.computer_use.start()
    print("Computer use started:", result.message)

    # Take a screenshot
    screenshot = sandbox.computer_use.screenshot.take_full_screen()

    # Click and type
    sandbox.computer_use.mouse.click(100, 200)
    sandbox.computer_use.keyboard.type('Hello, Linux!')
    sandbox.computer_use.keyboard.hotkey('ctrl+s')
    ```

    ```typescript
    import { Daytona } from '@daytonaio/sdk';

    // Initialize using environment variables (recommended)
    const daytona = new Daytona();
    // Or explicitly configure:
    // const daytona = new Daytona({
    //     apiKey: process.env.DAYTONA_API_KEY,
    //     apiUrl: process.env.DAYTONA_API_URL || 'https://app.daytona.io/api'
    // });

    // Create sandbox from default snapshot (includes desktop environment)
    const sandbox = await daytona.create();

    // Start computer use processes
    await sandbox.computerUse.start();

    // Take a screenshot
    const screenshot = await sandbox.computerUse.screenshot.takeFullScreen();

    // Click and type
    await sandbox.computerUse.mouse.click(100, 200);
    await sandbox.computerUse.keyboard.type('Hello, Linux!');
    await sandbox.computerUse.keyboard.hotkey('ctrl+s');
    ```

**Environment Variables (.env file):**
```bash
DAYTONA_API_KEY=your-api-key-here
DAYTONA_API_URL=https://app.daytona.io/api
```

## Related Documentation

- [Computer Use - Windows](https://www.daytona.io/docs/en/computer-use-windows.md)  
- [Computer Use - macOS](https://www.daytona.io/docs/en/computer-use-macos.md)

**Computer Use** enables programmatic control of desktop environments within Daytona sandboxes. It provides mouse, keyboard, screenshot, and display operations for automating GUI interactions and testing desktop applications.

We recommend using this instance type if you need to interact with macOS-only applications.

:::caution[Alpha Access Required]
macOS Computer Use is currently in **private alpha**. To request access, please fill out the [macOS Access Request Form](https://docs.google.com/forms/d/e/1FAIpQLSc9xlGZ49OjWNkyzDPC9Ip3InMRR0ZXY3tcoD-PFQj3ck6gzQ/viewform?usp=sharing&ouid=103304973264148733944).

Once submitted, our team will review your request and reach out with setup instructions and availability details.
:::

## Common Use Cases

- **GUI Application Testing** - Automate interactions with native macOS applications, click buttons, fill forms, and validate UI behavior
- **Visual Testing & Screenshots** - Capture screenshots of applications, compare UI states, and perform visual regression testing
- **Desktop Automation** - Automate repetitive macOS desktop tasks, file management through GUI, and complex workflows

## Getting Started

Once you have access to the macOS Computer Use alpha, you'll be able to programmatically control macOS desktop environments within your Daytona sandboxes. The functionality will include mouse operations, keyboard automation, screenshot capture, and display management specifically optimized for macOS environments.

## Related Documentation

- [Computer Use - Linux](https://www.daytona.io/docs/en/computer-use-linux.md)  
- [Computer Use - Windows](https://www.daytona.io/docs/en/computer-use-windows.md)

**Computer Use** enables programmatic control of desktop environments within Daytona sandboxes. It provides mouse, keyboard, screenshot, and display operations for automating GUI interactions and testing desktop applications.

We recommend using this instance type if you need to interact with Windows-only applications.

:::caution[Alpha Access Required]
Windows Computer Use is currently in **private alpha**. To request access, please fill out the [Access Request Form](https://docs.google.com/forms/d/e/1FAIpQLSfoK-77-VpfsMubw8F4f1opCxIL1AyJUgnM0ONYup5hZ0RTvQ/viewform?usp=dialog).

Once submitted, our team will review your request and reach out with setup instructions and availability details.
:::

## Common Use Cases

- **GUI Application Testing** - Automate interactions with Windows desktop applications, click buttons, fill forms, and validate UI behavior
- **Visual Testing & Screenshots** - Capture screenshots of applications, compare UI states, and perform visual regression testing
- **Desktop Automation** - Automate repetitive Windows desktop tasks, file management through GUI, and complex workflows

## Getting Started

Once you have access to the Windows Computer Use alpha, you'll be able to programmatically control Windows desktop environments within your Daytona sandboxes. The functionality will include mouse operations, keyboard automation, screenshot capture, and display management specifically optimized for Windows environments.

## Related Documentation

- [Computer Use - Linux](https://www.daytona.io/docs/en/computer-use-linux.md)  
- [Computer Use - macOS](https://www.daytona.io/docs/en/computer-use-macos.md)

## Configuration Methods

Daytona SDK supports multiple ways to configure your environment, in order of precedence:

1. [**Configuration in code**](#configuration-in-code)
2. [**Environment variables**](#environment-variables)
3. [**.env file**](#env-file)
4. [**Default values**](#default-values)

## Configuration in Code

Daytona SDK provides an option to configure settings using the `DaytonaConfig` class in Python and TypeScript. The `DaytonaConfig` class accepts the following parameters:

- `api_key`: Your Daytona [API Key](https://www.daytona.io/docs/api-keys.md)
- `api_url`: URL of your Daytona API
- `target`: Daytona Target to create the Sandboxes on.

```python
from daytona import DaytonaConfig

config = DaytonaConfig(
    api_key="your-api-key",
    api_url="your-api-url",
    target="us"
)

```
```typescript
import { DaytonaConfig } from '@daytonaio/sdk';

const config: DaytonaConfig = {
    apiKey: "your-api-key",          
    apiUrl: "your-api-url",     
    target: "us"                  
};
```


## Environment Variables

Daytona SDK supports environment variables for configuration. The SDK automatically looks for these environment variables:

| Variable              | Description                                | Optional |
| --------------------- | ------------------------------------------ | -------- |
| **`DAYTONA_API_KEY`** | Your Daytona API key.                      | No       |
| **`DAYTONA_API_URL`** | URL of your Daytona API.                   | Yes      |
| **`DAYTONA_TARGET`**  | Daytona Target to create the Sandboxes on. | Yes      |

Set environment variables in your shell:

    ```bash
    export DAYTONA_API_KEY=your-api-key
    export DAYTONA_API_URL=https://your-api-url
    export DAYTONA_TARGET=us
    ```
    ```bash 
    $env:DAYTONA_API_KEY="your-api-key"
    $env:DAYTONA_API_URL="https://your-api-url"
    $env:DAYTONA_TARGET="us"
    ```

You can also set these environment variables in a `.env` file.

## .env File

Create a `.env` file in your project root directory:

```bash
DAYTONA_API_KEY=your-api-key
DAYTONA_API_URL=https://your-api-url
DAYTONA_TARGET=us
```

The SDK will automatically read these values when initializing.

## Default Values

If no configuration is provided, Daytona SDK will use its built-in defaults:

| Option    | Default Value                       |
|-----------|-------------------------------------|
| API URL   | https://app.daytona.io/api          |
| Target    | Default region for the organization |

Daytona allows you to deploy your own custom preview proxy to handle preview URLs for sandboxes. This gives you complete control over the preview experience, including custom domains, authentication, error handling, and styling.

**What you can do with a custom preview proxy:**

- **Custom Domain:** Host your proxy under your own domain (e.g., `preview.yourcompany.com`)
- **User Authentication:** Implement custom authentication logic for private previews
- **Smart Sandbox Management:** Automatically start stopped sandboxes before forwarding users
- **Custom Error Pages:** Style error pages to match your brand
- **Preview Warning Control:** Disable Daytona's preview warning
- **CORS Management:** Override Daytona's default CORS settings

---

## How It Works

When a user visits a preview URL, your custom proxy receives the request and can:

1. **Authenticate the user** using custom logic
2. **Check sandbox status** and start it if needed
3. **Forward the request** to the actual sandbox
4. **Handle responses** with custom styling and error pages
5. **Send custom headers** to control Daytona's behavior

---

## Daytona Headers

Your proxy can send special headers to control Daytona's behavior:

#### Disable Preview Warning

To disable Daytona's preview warning page, send:

```
X-Daytona-Skip-Preview-Warning: true
```

#### Disable CORS

To override Daytona's default CORS settings, send:

```
X-Daytona-Disable-CORS: true
```

### Disable Last Activity Update

To prevent sandbox last activity updates when previewing, you can set the `X-Daytona-Skip-Last-Activity-Update` header to `true`.
This will stop Daytona from keeping sandboxes, that have [auto-stop enabled](https://www.daytona.io/docs/sandbox-management.md#auto-stop-interval), started:

```bash
curl -H "X-Daytona-Skip-Last-Activity-Update: true" \
https://3000-sandbox-123456.proxy.daytona.work
```

### Authentication

For private preview links, users should send:

```
X-Daytona-Preview-Token: {sandboxToken}
```

The `sandboxToken` can be fetched through the [Daytona SDK or API](https://www.daytona.io/docs/en/preview-and-authentication.md).

---

## Examples

You can find examples of custom preview proxies on our [Github](https://github.com/daytonaio/daytona-proxy-samples):

- [Typescript Example](https://github.com/daytonaio/daytona-proxy-samples/tree/main/typescript)
- [Golang Example](https://github.com/daytonaio/daytona-proxy-samples/tree/main/go)

import { Image } from 'astro:assets'

import chartImage from '../../../assets/docs/images/chart-0.png'

You can use Daytona Sandbox to run AI-generated code to analyze data. Here's how the AI data analysis workflow typically looks:

1. Your user has a dataset in CSV format or other formats.
2. You prompt the LLM to generate code (usually Python) based on the user's data.
3. The sandbox runs the AI-generated code and returns the results.
4. You display the results to the user.

---

## Build an AI Data Analyst with Daytona

This example shows how to build an AI-powered data analyst that automatically generates insights and visualizations from CSV data using Daytona's secure sandbox environment.

**What we'll build:** A system that analyzes a vehicle valuation dataset, identifies price relation to manufacturing year, and generates professional visualizations - all through natural language prompts to Claude.

### 1. Project Setup

#### 1.1 Install Dependencies

Install the Daytona SDK and Anthropic SDK to your project:

    `bash pip install daytona anthropic python-dotenv `

    `bash npm install @daytonaio/sdk @anthropic-ai/sdk dotenv `

#### 1.2 Configure Environment

Get your API keys and configure your environment:

1. **Daytona API key:** Get it from [Daytona Dashboard](https://app.daytona.io/dashboard/keys)
2. **Anthropic API key:** Get it from [Anthropic Console](https://console.anthropic.com/)

Create a `.env` file in your project:

```bash
DAYTONA_API_KEY=dtn_***
ANTHROPIC_API_KEY=sk-ant-***
```

### 2. Dataset Preparation

#### 2.1 Download Dataset

We'll be using a publicly available dataset of vehicle valuation. You can download it directly from:

[https://download.daytona.io/dataset.csv](https://download.daytona.io/dataset.csv)

Download the file and save it as `dataset.csv` in your project directory.

#### 2.2 Initialize Sandbox

Now create a Daytona sandbox and upload your dataset:

    ```python
    from dotenv import load_dotenv
    from daytona import Daytona
    import os

    load_dotenv()

    # Create sandbox

    daytona = Daytona()
    sandbox = daytona.create()

    # Upload the dataset to the sandbox

    sandbox.fs.upload_file("dataset.csv", "/home/daytona/dataset.csv")

    ```

    ```typescript
    import 'dotenv/config'
    import { Daytona } from '@daytonaio/sdk';

    // Create sandbox
    const daytona = new Daytona();
    const sandbox = await daytona.create()

    // Upload the dataset to the sandbox
    await sandbox.fs.uploadFile('dataset.csv', '/home/daytona/dataset.csv')
    ```

### 3. Building the AI Data Analyst

Now we'll create the core functionality that connects Claude with Daytona to analyze data and generate visualizations.

#### 3.1 Code Execution Handler

First, let's create a function to handle code execution and chart extraction:

    ```python
    import base64

    def run_ai_generated_code(sandbox, ai_generated_code):
      execution = sandbox.process.code_run(ai_generated_code)
      if execution.exit_code != 0:
        print('AI-generated code had an error.')
        print(execution.exit_code)
        print(execution.result)
        return

      # Check for charts in execution artifacts
      if not execution.artifacts or not execution.artifacts.charts:
        print('No charts found in execution artifacts')
        return

      result_idx = 0
      for result in execution.artifacts.charts:
        if result.png: # Save the png to a file (png is in base64 format)
          with open(f'chart-{result_idx}.png', 'wb') as f:
            f.write(base64.b64decode(result.png))
            print(f'Chart saved to chart-{result_idx}.png')
            result_idx += 1

    ```

    ```typescript
    import fs from 'fs'

    async function runAIGeneratedCode(sandbox, aiGeneratedCode: string) {
      const execution = await sandbox.process.codeRun(aiGeneratedCode)
      if (execution.exitCode != 0) {
        console.error('AI-generated code had an error.')
        console.log(execution.exitCode)
        console.log(execution.result)
        return
      }

      // Check for charts in execution artifacts
      if (!execution.artifacts || !execution.artifacts.charts) {
        console.log('No charts found in execution artifacts')
        return
      }

      let resultIdx = 0
      for (const result of execution.artifacts.charts) {
        if (result.png) {
          // Save the png to a file (png is in base64 format)
          fs.writeFileSync(`chart-${resultIdx}.png`, result.png, { encoding: 'base64' })
          console.log(`Chart saved to chart-${resultIdx}.png`)
          resultIdx++
        }
      }
    }
    ```

#### 3.2 Creating the Analysis Prompt

Next, we'll create the prompt that tells Claude about our dataset and what analysis we want. This prompt includes:

- Dataset schema and column descriptions
- The specific analysis request (vote average trends over time)
- Instructions for code generation

    ```python
    from anthropic import Anthropic

    prompt = f"""
    I have a CSV file with vehicle valuations saved in the sandbox at /home/daytona/dataset.csv.

    Relevant columns:
    - 'year': integer, the manufacturing year of the vehicle
    - 'price_in_euro': float, the listed price of the vehicle in Euros

    Analyze how price varies by manufacturing year.  
    Drop rows where 'year' or 'price_in_euro' is missing, non-numeric, or an outlier.  
    Create a line chart showing average price per year.
    Write Python code that analyzes the dataset based on my request and produces right chart accordingly.
    Finish with a plt.show()"""

    anthropic = Anthropic()
    print('Waiting for the model response...')

    ```

    ```typescript
    import Anthropic from '@anthropic-ai/sdk'

    const prompt = `
    I have a CSV file with vehicle valuations saved in the sandbox at /home/daytona/dataset.csv.

    Relevant columns:
    - 'year': integer, the manufacturing year of the vehicle
    - 'price_in_euro': float, the listed price of the vehicle in Euros

    Analyze how price varies by manufacturing year.  
    Drop rows where 'year' or 'price_in_euro' is missing, non-numeric, or an outlier.  
    Create a line chart showing average price per year.
    Write Python code that analyzes the dataset based on my request and produces right chart accordingly.
    Finish with a plt.show()`

    const anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY })
    console.log('Waiting for the model response...')
    ```

#### 3.3 Tool Calling Setup

Now we'll connect Claude to our Daytona sandbox using tool calling. This allows Claude to automatically execute the Python code it generates:

    ```python
    msg = anthropic.messages.create(
        model='claude-3-5-sonnet-20240620',
        max_tokens=1024,
        messages=[{'role': 'user', 'content': prompt}],
        tools=[
            {
                'name': 'run_python_code',
                'description': 'Run Python code',
                'input_schema': {
                    'type': 'object',
                    'properties': {
                        'code': {
                            'type': 'string',
                            'description': 'The Python code to run',
                        },
                    },
                    'required': ['code'],
                },
            },
        ],
    )
    ```

    ```typescript
    const msg = await anthropic.messages.create({
      model: 'claude-3-5-sonnet-20240620',
      max_tokens: 1024,
      messages: [{ role: 'user', content: prompt }],
      tools: [
        {
          name: 'run_python_code',
          description: 'Run Python code',
          input_schema: {
            type: 'object',
            properties: {
              code: {
                type: 'string',
                description: 'The Python code to run',
              },
            },
            required: ['code'],
          },
        },
      ],
    })
    ```

#### 3.4 Response Processing

Finally, we'll parse Claude's response and execute any generated code in our Daytona sandbox:

    ```python
    for content_block in msg.content:
        if content_block.type == 'tool_use':
            if content_block.name == 'run_python_code':
                code = content_block.input['code']
                print('Will run following code in the Sandbox:\n', code)
                # Execute the code in the sandbox
                run_ai_generated_code(sandbox, code)
    ```

    ```typescript
    interface CodeRunToolInput {
      code: string
    }

    for (const contentBlock of msg.content) {
      if (contentBlock.type === 'tool_use') {
        if (contentBlock.name === 'run_python_code') {
          const code = (contentBlock.input as CodeRunToolInput).code
          console.log('Will run following code in the Sandbox:\n', code)
          // Execute the code in the sandbox
          await runAIGeneratedCode(sandbox, code)
        }
      }
    }

    ```

That's it! The `run_ai_generated_code` function we created automatically handles saving charts. When Claude generates a visualization with `plt.show()`, Daytona captures it as a chart artifact and saves it as a PNG file.

**Key advantages of this approach:**

- **Secure execution:** Code runs in isolated Daytona sandboxes
- **Automatic artifact capture:** Charts, tables, and outputs are automatically extracted
- **Error handling:** Built-in error detection and logging
- **Language agnostic:** While we used Python here, Daytona supports multiple languages

### 4. Running Your Analysis

Now you can run the complete code to see the results.

    ```bash
    python data-analysis.py
    ```

    ```bash
    npx tsx data-analysis.ts
    ```

You should see the chart in your project directory that will look similar to this:

<Image src={chartImage} alt="Vehicle valuation by manufacturing year chart" width={600} style="max-width: 100%; height: auto; margin: 1rem 0;" />

### 5. Complete Implementation

Here are the complete, ready-to-run examples:

    ```python
    import base64
    from dotenv import load_dotenv
    from daytona import Daytona, Sandbox
    from anthropic import Anthropic


    def main():
        load_dotenv()
        # Create sandbox
        daytona = Daytona()
        sandbox = daytona.create()
        
        # Upload the dataset to the sandbox
        sandbox.fs.upload_file("dataset.csv", "/home/daytona/dataset.csv")
        
        prompt = f"""
    I have a CSV file with vehicle valuations saved in the sandbox at /home/daytona/dataset.csv.

    Relevant columns:
    - 'year': integer, the manufacturing year of the vehicle
    - 'price_in_euro': float, the listed price of the vehicle in Euros

    Analyze how price varies by manufacturing year.  
    Drop rows where 'year' or 'price_in_euro' is missing, non-numeric, or an outlier.  
    Create a line chart showing average price per year.
    Write Python code that analyzes the dataset based on my request and produces right chart accordingly.
    Finish with a plt.show()"""

        anthropic = Anthropic()
        print('Waiting for the model response...')
        msg = anthropic.messages.create(
            model='claude-3-5-sonnet-20240620',
            max_tokens=1024,
            messages=[{'role': 'user', 'content': prompt}],
            tools=[
                {
                    'name': 'run_python_code',
                    'description': 'Run Python code',
                    'input_schema': {
                        'type': 'object',
                        'properties': {
                            'code': {
                                'type': 'string',
                                'description': 'The Python code to run',
                            },
                        },
                        'required': ['code'],
                    },
                },
            ],
        )

        for content_block in msg.content:
            if content_block.type == 'tool_use':
                if content_block.name == 'run_python_code':
                    code = content_block.input['code']
                    print('Will run following code in the Sandbox:\n', code)
                    # Execute the code in the sandbox
                    run_ai_generated_code(sandbox, code)


    def run_ai_generated_code(sandbox: Sandbox, ai_generated_code: str):
        execution = sandbox.process.code_run(ai_generated_code)
        if execution.exit_code != 0:
            print('AI-generated code had an error.')
            print(execution.exit_code)
            print(execution.result)
            return
        
        # Iterate over all the results and specifically check for png files that will represent the chart.
        if not execution.artifacts or not execution.artifacts.charts:
            print('No charts found in execution artifacts')
            print(execution.artifacts)
            return

        result_idx = 0
        for result in execution.artifacts.charts:
            if result.png:
                # Save the png to a file
                # The png is in base64 format.
                with open(f'chart-{result_idx}.png', 'wb') as f:
                    f.write(base64.b64decode(result.png))
                print(f'Chart saved to chart-{result_idx}.png')
                result_idx += 1


    if __name__ == "__main__":
        main()
    ```

    ```typescript
    import 'dotenv/config'
    import fs from 'fs'
    import Anthropic from '@anthropic-ai/sdk'
    import { Daytona, Sandbox } from '@daytonaio/sdk';


    async function main() {
      // Create sandbox
      const daytona = new Daytona();
      const sandbox = await daytona.create()

      // Upload the dataset to the sandbox
      await sandbox.fs.uploadFile('dataset.csv', '/home/daytona/dataset.csv')

      const prompt = `
    I have a CSV file with vehicle valuations saved in the sandbox at /home/daytona/dataset.csv.

    Relevant columns:
    - 'year': integer, the manufacturing year of the vehicle
    - 'price_in_euro': float, the listed price of the vehicle in Euros

    Analyze how price varies by manufacturing year.  
    Drop rows where 'year' or 'price_in_euro' is missing, non-numeric, or an outlier.  
    Create a line chart showing average price per year.
    Write Python code that analyzes the dataset based on my request and produces right chart accordingly.
    Finish with a plt.show()`

      const anthropic = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY })
      console.log('Waiting for the model response...')
      const msg = await anthropic.messages.create({
        model: 'claude-3-5-sonnet-20240620',
        max_tokens: 1024,
        messages: [{ role: 'user', content: prompt }],
        tools: [
          {
            name: 'run_python_code',
            description: 'Run Python code',
            input_schema: {
              type: 'object',
              properties: {
                code: {
                  type: 'string',
                  description: 'The Python code to run',
                },
              },
              required: ['code'],
            },
          },
        ],
      })

      interface CodeRunToolInput {
        code: string
      }

      for (const contentBlock of msg.content) {
        if (contentBlock.type === 'tool_use') {
          if (contentBlock.name === 'run_python_code') {
            const code = (contentBlock.input as CodeRunToolInput).code
            console.log('Will run following code in the Sandbox:\n', code)
            // Execute the code in the sandbox
            await runAIGeneratedCode(sandbox, code)
          }
        }
      }
    }

    async function runAIGeneratedCode(sandbox: Sandbox, aiGeneratedCode: string) {
      const execution = await sandbox.process.codeRun(aiGeneratedCode)
      if (execution.exitCode != 0) {
        console.error('AI-generated code had an error.')
        console.log(execution.exitCode)
        console.log(execution.result)
        process.exit(1)
      }
      // Iterate over all the results and specifically check for png files that will represent the chart.
      if (!execution.artifacts || !execution.artifacts.charts) {
        console.log('No charts found in execution artifacts')
        console.log(execution.artifacts)
        return
      }

      let resultIdx = 0
      for (const result of execution.artifacts.charts) {
        if (result.png) {
          // Save the png to a file
          // The png is in base64 format.
          fs.writeFileSync(`chart-${resultIdx}.png`, result.png, { encoding: 'base64' })
          console.log(`Chart saved to chart-${resultIdx}.png`)
          resultIdx++
        }
      }
    }

    main().catch(console.error);
    ```

Daytona's declarative builder provides a powerful, code-first approach to defining dependencies for Sandboxes. Instead of importing images from a container registry, you can programmatically define them using the SDK.

## Overview

The declarative builder system supports two primary workflows:

1. [**Declarative Images**](#declarative-image-building): Build images with varying dependencies _on demand_ when creating Sandboxes
2. [**Pre-built Snapshots**](#creating-pre-built-snapshots): Create and register _ready-to-use_ [Snapshots](https://www.daytona.io/docs/snapshots.md) that can be shared across multiple Sandboxes

### Declarative Image Building

You can create declarative images on-the-fly when creating Sandboxes. This is ideal for iterating quickly without creating separate Snapshots.

Declarative images are cached for 24 hours, and will be automatically reused when running the same script. Thus, subsequent runs on the same Runner will be almost instantaneous.

```python
# Define a simple declarative image with Python packages
declarative_image = (
    Image.debian_slim("3.12")
    .pip_install(["requests", "pytest"])
    .workdir("/home/daytona")
)

# Create a new Sandbox with the declarative image and stream the build logs
sandbox = daytona.create(
    CreateSandboxFromImageParams(image=declarative_image),
    timeout=0,
    on_snapshot_create_logs=print,
)
```
```typescript
// Define a simple declarative image with Python packages
const declarativeImage = Image.debianSlim('3.12')
  .pipInstall(['requests', 'pytest'])
  .workdir('/home/daytona')

// Create a new Sandbox with the declarative image and stream the build logs
const sandbox = await daytona.create(
  {
    image: declarativeImage,
  },
  {
    timeout: 0,
    onSnapshotCreateLogs: console.log,
  }
)
```

See: [CreateSandboxFromImageParams (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/daytona.md#createsandboxfromimageparams), [CreateSandboxFromImageParams (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/daytona.md#createsandboxfromimageparams)

### Creating Pre-built Snapshots

For images that will be reused across multiple Sandboxes, create a pre-built Snapshot. This Snapshot will remain visible in the Daytona dashboard and be permanently cached, ensuring instant availability without rebuilding.

```python
# Create a simple Python data science image
snapshot_name = "data-science-snapshot"

image = (
    Image.debian_slim("3.12")
    .pip_install(["pandas", "numpy"])
    .workdir("/home/daytona")
)

# Create the Snapshot and stream the build logs
daytona.snapshot.create(
    CreateSnapshotParams(
        name=snapshot_name,
        image=image,
    ),
    on_logs=print,
)

# Create a new Sandbox using the pre-built Snapshot
sandbox = daytona.create(
  CreateSandboxFromSnapshotParams(snapshot=snapshot_name)
)
```
```typescript
// Create a simple Python data science image
const snapshotName = 'data-science-snapshot'

const image = Image.debianSlim('3.12')
  .pipInstall(['pandas', 'numpy'])
  .workdir('/home/daytona')

// Create the Snapshot and stream the build logs
await daytona.snapshot.create(
  {
      name: snapshotName,
      image,
  },
  {
      onLogs: console.log,
  }
)

// Create a new Sandbox using the pre-built Snapshot
const sandbox = await daytona.create({
  snapshot: snapshotName,
})
```

See: [CreateSnapshotParams (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/snapshot.md#createsnapshotparams), [CreateSnapshotParams (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/snapshot.md#createsnapshotparams)

## Image Configuration

The Daytona SDK provides methods to define images programmatically using the Daytona SDK. You can specify base images, install packages, add files, set environment variables, and more.

For a complete API reference and method signatures, check the [Python](https://www.daytona.io/docs/python-sdk/common/image.md) and [TypeScript](https://www.daytona.io/docs/typescript-sdk/image.md) SDK references.

### Base Image Selection

These examples demonstrate how to select and configure base images:

```python
# Create an image from a base
image = Image.base("python:3.12-slim-bookworm")

# Use a Debian slim image with Python 3.12
image = Image.debian_slim("3.12")
```
```typescript
// Create an image from a base
const image = Image.base('python:3.12-slim-bookworm')

// Use a Debian slim image with Python 3.12
const image = Image.debianSlim('3.12')
```

See: [base (Python SDK)](https://www.daytona.io/docs/python-sdk/common/image.md#imagebase), [debian_slim (Python SDK)](https://www.daytona.io/docs/python-sdk/common/image.md#imagedebian_slim), [base (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/image.md#base), [debianSlim (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/image.md#debianslim)

### Package Management

Use these methods to install Python packages and dependencies:

```python
# Add pip packages
image = Image.debian_slim("3.12").pip_install("requests", "pandas")

# Install from requirements.txt
image = Image.debian_slim("3.12").pip_install_from_requirements("requirements.txt")

# Install from pyproject.toml (with optional dependencies)
image = Image.debian_slim("3.12").pip_install_from_pyproject("pyproject.toml", optional_dependencies=["dev"])
```
```typescript
// Add pip packages
const image = Image.debianSlim('3.12').pipInstall(['requests', 'pandas'])

// Install from requirements.txt
const image = Image.debianSlim('3.12').pipInstallFromRequirements('requirements.txt')

// Install from pyproject.toml (with optional dependencies)
const image = Image.debianSlim('3.12').pipInstallFromPyproject('pyproject.toml', { 
  optionalDependencies: ['dev'] 
})
```

See: [pip_install (Python SDK)](https://www.daytona.io/docs/python-sdk/common/image.md#imagepip_install), [pip_install_from_requirements (Python SDK)](https://www.daytona.io/docs/python-sdk/common/image.md#imagepip_install_from_requirements), [pip_install_from_pyproject (Python SDK)](https://www.daytona.io/docs/python-sdk/common/image.md#imagepip_install_from_pyproject), [pipInstall (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/image.md#pipinstall), [pipInstallFromRequirements (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/image.md#pipinstallfromrequirements), [pipInstallFromPyproject (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/image.md#pipinstallfrompyproject)

### File System Operations

These examples show how to add files and directories to your image:

```python
# Add a local file
image = Image.debian_slim("3.12").add_local_file("package.json", "/home/daytona/package.json")

# Add a local directory
image = Image.debian_slim("3.12").add_local_dir("src", "/home/daytona/src")
```
```typescript
// Add a local file
const image = Image.debianSlim('3.12').addLocalFile('package.json', '/home/daytona/package.json')

// Add a local directory
const image = Image.debianSlim('3.12').addLocalDir('src', '/home/daytona/src')
```

See: [add_local_file (Python SDK)](https://www.daytona.io/docs/python-sdk/common/image.md#imageadd_local_file), [add_local_dir (Python SDK)](https://www.daytona.io/docs/python-sdk/common/image.md#imageadd_local_dir), [addLocalFile (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/image.md#addlocalfile), [addLocalDir (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/image.md#addlocaldir)

### Environment Configuration

Configure environment variables and working directories with these methods:

```python
# Set environment variables
image = Image.debian_slim("3.12").env({"PROJECT_ROOT": "/home/daytona"})

# Set working directory
image = Image.debian_slim("3.12").workdir("/home/daytona")
```
```typescript
// Set environment variables
const image = Image.debianSlim('3.12').env({ PROJECT_ROOT: '/home/daytona' })

// Set working directory
const image = Image.debianSlim('3.12').workdir('/home/daytona')
```

See: [env (Python SDK)](https://www.daytona.io/docs/python-sdk/common/image.md#imageenv), [workdir (Python SDK)](https://www.daytona.io/docs/python-sdk/common/image.md#imageworkdir), [env (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/image.md#env), [workdir (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/image.md#workdir)

### Commands and Entrypoints

Execute commands during build and configure container startup behavior:

```python
# Run shell commands during build
image = Image.debian_slim("3.12").run_commands(
    'apt-get update && apt-get install -y git',
    'groupadd -r daytona && useradd -r -g daytona -m daytona',
    'mkdir -p /home/daytona/workspace'
)

# Set entrypoint
image = Image.debian_slim("3.12").entrypoint(["/bin/bash"])

# Set default command
image = Image.debian_slim("3.12").cmd(["/bin/bash"])
```
```typescript
// Run shell commands during build
const image = Image.debianSlim('3.12').runCommands(
    'apt-get update && apt-get install -y git',
    'groupadd -r daytona && useradd -r -g daytona -m daytona',
    'mkdir -p /home/daytona/workspace'
)

// Set entrypoint
const image = Image.debianSlim('3.12').entrypoint(['/bin/bash'])

// Set default command
const image = Image.debianSlim('3.12').cmd(['/bin/bash'])
```

See: [run_commands (Python SDK)](https://www.daytona.io/docs/python-sdk/common/image.md#imagerun_commands), [entrypoint (Python SDK)](https://www.daytona.io/docs/python-sdk/common/image.md#imageentrypoint), [cmd (Python SDK)](https://www.daytona.io/docs/python-sdk/common/image.md#imagecmd), [runCommands (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/image.md#runcommands), [entrypoint (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/image.md#entrypoint), [cmd (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/image.md#cmd)

### Dockerfile Integration

Integrate existing Dockerfiles or add custom Dockerfile commands:

```python
# Add custom Dockerfile commands
image = Image.debian_slim("3.12").dockerfile_commands(["RUN echo 'Hello, world!'"])

# Use an existing Dockerfile
image = Image.from_dockerfile("Dockerfile")

# Extend an existing Dockerfile
image = Image.from_dockerfile("app/Dockerfile").pip_install(["numpy"])
```
```typescript
// Add custom Dockerfile commands
const image = Image.debianSlim('3.12').dockerfileCommands(['RUN echo "Hello, world!"'])

// Use an existing Dockerfile
const image = Image.fromDockerfile('Dockerfile')

// Extend an existing Dockerfile
const image = Image.fromDockerfile("app/Dockerfile").pipInstall(['numpy'])
```

See: [dockerfile_commands (Python SDK)](https://www.daytona.io/docs/python-sdk/common/image.md#imagedockerfile_commands), [from_dockerfile (Python SDK)](https://www.daytona.io/docs/python-sdk/common/image.md#imagefrom_dockerfile), [dockerfileCommands (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/image.md#dockerfilecommands), [fromDockerfile (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/image.md#fromdockerfile)

## Best Practices

Use the following best practices when working with the declarative builder:

1. **Layer Optimization**: Group related operations to minimize Docker layers
2. **Cache Utilization**: Identical build commands and context will be cached and subsequent builds will be almost instant
3. **Security**: Create non-root users for application workloads
4. **Resource Efficiency**: Use slim base images when appropriate
5. **Context Minimization**: Only include necessary files in the build context

The Daytona SDK provides comprehensive file system operations through the `fs` module in Sandboxes. This guide covers all available file system operations and best practices.

## Basic Operations

Daytona SDK provides an option to interact with the file system in Sandboxes. You can perform various operations like listing files, creating directories, reading and writing files, and more.

File operations assume you are operating in the Sandbox user's home directory (e.g. `workspace` implies `/home/[username]/workspace`). Use a leading `/` when providing absolute paths.

### Listing Files and Directories

Daytona SDK provides an option to list files and directories in a Sandbox using Python and TypeScript.

```python
# List files in a directory
files = sandbox.fs.list_files("workspace")

for file in files:
    print(f"Name: {file.name}")
    print(f"Is directory: {file.is_dir}")
    print(f"Size: {file.size}")
    print(f"Modified: {file.mod_time}")

```
```typescript
// List files in a directory
const files = await sandbox.fs.listFiles("workspace")

files.forEach(file => {
    console.log(`Name: ${file.name}`)
    console.log(`Is directory: ${file.isDir}`)
    console.log(`Size: ${file.size}`)
    console.log(`Modified: ${file.modTime}`)
})
```


See: [list_files (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/file-system.md#filesystemlist_files), [listFiles (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/file-system.md#listfiles)

### Creating Directories

Daytona SDK provides an option to create directories with specific permissions using Python and TypeScript.

```python
# Create with specific permissions
sandbox.fs.create_folder("workspace/new-dir", "755")
```
```typescript
// Create with specific permissions
await sandbox.fs.createFolder("workspace/new-dir", "755")
```


See: [create_folder (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/file-system.md#filesystemcreate_folder), [createFolder (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/file-system.md#createfolder)

### Uploading Files

Daytona SDK provides options to read, write, upload, download, and delete files in Sandboxes using Python and TypeScript.

#### Uploading a Single File

The following example shows how to upload a single file:

```python
# Upload a single file
with open("local_file.txt", "rb") as f:
    content = f.read()
sandbox.fs.upload_file(content, "remote_file.txt")
```
```typescript
// Upload a single file
const fileContent = Buffer.from('Hello, World!')
await sandbox.fs.uploadFile(fileContent, "data.txt")
```


See: [upload_file (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/file-system.md#filesystemupload_file), [uploadFile (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/file-system.md#uploadfile)

#### Uploading Multiple Files

The following example shows how to efficiently upload multiple files with a single method call.

```python
# Upload multiple files at once
files_to_upload = []

with open("file1.txt", "rb") as f1:
    files_to_upload.append(FileUpload(
        source=f1.read(),
        destination="data/file1.txt",
    ))

with open("file2.txt", "rb") as f2:
    files_to_upload.append(FileUpload(
        source=f2.read(),
        destination="data/file2.txt",
    ))

with open("settings.json", "rb") as f3:
    files_to_upload.append(FileUpload(
        source=f3.read(),
        destination="config/settings.json",
    ))

sandbox.fs.upload_files(files_to_upload)

```
```typescript
// Upload multiple files at once
const files = [
    {
        source: Buffer.from('Content of file 1'),
        destination: 'data/file1.txt',
    },
    {
        source: Buffer.from('Content of file 2'),
        destination: 'data/file2.txt',
    },
    {
        source: Buffer.from('{"key": "value"}'),
        destination: 'config/settings.json',
    }
]

await sandbox.fs.uploadFiles(files)
```


See: [upload_files (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/file-system.md#filesystemupload_files), [uploadFiles (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/file-system.md#uploadfiles)

### Downloading Files

#### Downloading a Single File

The following commands downloads a single file `file1.txt` from the Sandbox working directory and prints out the content:

```python

content = sandbox.fs.download_file("file1.txt")

with open("local_file.txt", "wb") as f:
    f.write(content)

print(content.decode('utf-8'))

```
```typescript

const downloadedFile = await sandbox.fs.downloadFile("file1.txt")

console.log('File content:', downloadedFile.toString())

```


See: [download_file (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/file-system.md#filesystemdownload_file), [downloadFile (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/file-system.md#downloadfile)

#### Downloading Multiple Files

The following example shows how to efficiently download multiple files with a single method call.

```python
# Download multiple files at once
files_to_download = [
    FileDownloadRequest(source="data/file1.txt"), # No destination - download to memory
    FileDownloadRequest(source="data/file2.txt", destination="local_file2.txt"), # Download to local file
]

results = sandbox.fs.download_files(files_to_download)

for result in results:
    if result.error:
        print(f"Error downloading {result.source}: {result.error}")
    elif result.result:
        print(f"Downloaded {result.source} to {result.result}")

```
```typescript
// Download multiple files at once
const files = [
    { source: "data/file1.txt" }, // No destination - download to memory
    { source: "data/file2.txt", destination: "local_file2.txt" }, // Download to local file
]

const results = await sandbox.fs.downloadFiles(files)

results.forEach(result => {
    if (result.error) {
        console.error(`Error downloading ${result.source}: ${result.error}`)
    } else if (result.result) {
        console.log(`Downloaded ${result.source} to ${result.result}`)
    }
})
```

See: [download_files (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/file-system.md#filesystemdownload_files), [downloadFiles (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/file-system.md#downloadfiles)

### Deleting files

The following example shows how to delete a file:

```python

sandbox.fs.delete_file("workspace/file.txt")

```
```typescript

await sandbox.fs.deleteFile("workspace/file.txt")
```


See: [delete_file (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/file-system.md#filesystemdelete_file), [deleteFile (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/file-system.md#deletefile)

## Advanced Operations

Daytona SDK provides advanced file system operations like file permissions, search and replace, and more.

### File Permissions

Daytona SDK provides an option to set file permissions, get file permissions, and set directory permissions recursively using Python and TypeScript.

```python
# Set file permissions
sandbox.fs.set_file_permissions("workspace/file.txt", "644")

# Get file permissions

file_info = sandbox.fs.get_file_info("workspace/file.txt")
print(f"Permissions: {file_info.permissions}")

```
```typescript
// Set file permissions
await sandbox.fs.setFilePermissions("workspace/file.txt", { mode: "644" })

// Get file permissions
const fileInfo = await sandbox.fs.getFileDetails("workspace/file.txt")
console.log(`Permissions: ${fileInfo.permissions}`)
```


See: [set_file_permissions (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/file-system.md#filesystemset_file_permissions), [setFilePermissions (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/file-system.md#setfilepermissions)

### File Search and Replace

Daytona SDK provides an option to search for text in files and replace text in files using Python and TypeScript.

```python
# Search for text in files; if a folder is specified, the search is recursive
results = sandbox.fs.find_files(
    path="workspace/src",
    pattern="text-of-interest"
)
for match in results:
    print(f"Absolute file path: {match.file}")
    print(f"Line number: {match.line}")
    print(f"Line content: {match.content}")
    print("\n")

# Replace text in files

sandbox.fs.replace_in_files(
    files=["workspace/file1.txt", "workspace/file2.txt"],
    pattern="old_text",
    new_value="new_text"
)

```
```typescript
// Search for text in files; if a folder is specified, the search is recursive
const results = await sandbox.fs.findFiles({
    path="workspace/src",
    pattern: "text-of-interest"
})
results.forEach(match => {
    console.log('Absolute file path:', match.file)
    console.log('Line number:', match.line)
    console.log('Line content:', match.content)
})

// Replace text in files
await sandbox.fs.replaceInFiles(
    ["workspace/file1.txt", "workspace/file2.txt"],
    "old_text",
    "new_text"
)
```


See: [find_files (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/file-system.md#filesystemfind_files), [replace_in_files (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/file-system.md#filesystemreplace_in_files), [findFiles (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/file-system.md#findfiles), [replaceInFiles (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/file-system.md#replaceinfiles)

The Daytona SDK provides official [Python](https://www.daytona.io/docs/en/python-sdk.md) and [TypeScript](https://www.daytona.io/docs/en/typescript-sdk.md) interfaces for interacting with Daytona, enabling you to programmatically manage development environments and execute code. [Python SDK](https://www.daytona.io/docs/en/python-sdk.md) supports both sync and async programming models where async classes are prefixed with `Async`.

Follow the step-by-step guide to create and run your first Daytona Sandbox for an AI Agent.

For steps on additional configuration, including setting environment variables as well as accessing experimental features on our staging deployment, visit [Configuration](https://www.daytona.io/docs/en/configuration.md).

## Install the Daytona SDK

Daytona provides official Python and TypeScript SDKs for interacting with the Daytona platform. Install the SDK using your preferred method:

    ```bash
    pip install daytona
    ```

    ```bash
    # Using npm
    npm install @daytonaio/sdk

    # Using yarn

    yarn add @daytonaio/sdk

    # Using pnpm

    pnpm add @daytonaio/sdk

    ```

## Run Code Inside a Sandbox

Run the following code to create a Daytona Sandbox and execute commands:

    ```python
    from daytona import Daytona, DaytonaConfig

    # Initialize the Daytona client
    daytona = Daytona(DaytonaConfig(api_key="YOUR_API_KEY"))

    # Create the Sandbox instance
    sandbox = daytona.create()

    # Run code securely inside the Sandbox
    response = sandbox.process.code_run('print("Sum of 3 and 4 is " + str(3 + 4))')
    if response.exit_code != 0:
        print(f"Error running code: {response.exit_code} {response.result}")
    else:
        print(response.result)

    # Clean up the Sandbox
    sandbox.delete()
    ```

    ```typescript
    import { Daytona } from '@daytonaio/sdk'

    async function main() {
      // Initialize the Daytona client
      const daytona = new Daytona({
        apiKey: 'YOUR_API_KEY',
      })

      let sandbox;
      try {
        // Create the Sandbox instance
        sandbox = await daytona.create({
          language: "python",
        });
        // Run code securely inside the Sandbox
        const response = await sandbox.process.codeRun(
          'print("Sum of 3 and 4 is " + str(3 + 4))'
        );
        if (response.exitCode !== 0) {
          console.error("Error running code:", response.exitCode, response.result);
        } else {
          console.log(response.result);
        }
      } catch (error) {
        console.error("Sandbox flow error:", error);
      } finally {
        // Clean up the Sandbox
        if (sandbox) {
          await sandbox.delete();
        }
      }
    }

    main().catch(console.error)

    ```

    ```bash
    python main.py
    ```

    ```bash
    npx tsx ./index.ts
    ```

## Preview Your App

The following snippet uploads a file containing a simple Flask app to a Daytona Sandbox. The web server runs on port `3000` and is accessible through the provided preview URL:

    ```python
    from daytona import Daytona, DaytonaConfig, SessionExecuteRequest

    daytona = Daytona(DaytonaConfig(api_key="YOUR_API_KEY"))

    sandbox = daytona.create()

    app_code = b'''
    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def hello():
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Hello World</title>
            <link rel="icon" href="https://www.daytona.io/favicon.ico">
        </head>
        <body style="display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background-color: #0a0a0a; font-family: Arial, sans-serif;">
            <div style="text-align: center; padding: 2rem; border-radius: 10px; background-color: white; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                <img src="https://raw.githubusercontent.com/daytonaio/daytona/main/assets/images/Daytona-logotype-black.png" alt="Daytona Logo" style="width: 180px; margin: 10px 0px;">
                <p>This web app is running in a Daytona sandbox!</p>
            </div>
        </body>
        </html>
        """

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=3000)
    '''

    # Save the Flask app to a file

    sandbox.fs.upload_file(app_code, "app.py")

    # Create a new session and execute a command

    exec_session_id = "python-app-session"
    sandbox.process.create_session(exec_session_id)

    sandbox.process.execute_session_command(exec_session_id, SessionExecuteRequest(
        command="python /app.py",
        var_async=True
    ))

    # Get the preview link for the Flask app

    preview_info = sandbox.get_preview_link(3000)
    print(f"Flask app is available at: {preview_info.url}")

    ```

    ```typescript
    import { Daytona } from '@daytonaio/sdk';

    const daytona = new Daytona(({
      apiKey: "YOUR_API_KEY"
    }));

    async function main() {
      const sandbox = await daytona.create();

      const appCode = Buffer.from(`
    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def hello():
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Hello World</title>
            <link rel="icon" href="https://www.daytona.io/favicon.ico">
        </head>
        <body style="display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background-color: #0a0a0a; font-family: Arial, sans-serif;">
            <div style="text-align: center; padding: 2rem; border-radius: 10px; background-color: white; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                <img src="https://raw.githubusercontent.com/daytonaio/daytona/main/assets/images/Daytona-logotype-black.png" alt="Daytona Logo" style="width: 180px; margin: 10px 0px;">
                <p>This web app is running in a Daytona sandbox!</p>
            </div>
        </body>
        </html>
        """

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=3000)
      `);

      // Save the Flask app to a file
      await sandbox.fs.uploadFile(appCode, "app.py");

      // Create a new session and execute a command
      const execSessionId = "python-app-session";
      await sandbox.process.createSession(execSessionId);

      await sandbox.process.executeSessionCommand(execSessionId, ({
        command: `python app.py`,
        async: true,
      }));

      // Get the preview link for the Flask app
      const previewInfo = await sandbox.getPreviewLink(3000);
      console.log(`Flask app is available at: ${previewInfo.url}`);
    }

    main().catch(error => console.error("Error:", error));

    ```

Need to access this endpoint programmatically? Learn more about [Preview & Authentication](https://www.daytona.io/docs/en/preview-and-authentication.md).

:::tip
You can access the Sandbox [Web Terminal](https://www.daytona.io/docs/en/web-terminal.md) by printing out the preview URL for port `22222` or by simply going to Dashboard -> Sandboxes and clicking on the Terminal input sign.
:::

## Connect to an LLM

The following snippet connects to an LLM using the Anthropic API and asks Claude to generate code for getting the factorial of 25 and then executes it inside of a Daytona Sandbox:

    ````python
    import os
    import re
    import requests
    from daytona import Daytona, DaytonaConfig
    from dotenv import load_dotenv

    load_dotenv()

    daytona = Daytona(DaytonaConfig())

    sandbox = daytona.create()

    def get_claude_response(api_key, prompt):
        url = "https://api.anthropic.com/v1/messages"
        headers = {
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json"
        }
        data = {
            "model": "claude-3-7-sonnet-latest",
            "max_tokens": 256,
            "messages": [{"role": "user", "content": prompt}]
        }
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            content = response.json().get("content", [])
            return "".join([item["text"] for item in content if item["type"] == "text"])
        else:
            return f"Error {response.status_code}: {response.text}"

    prompt = "Python code that returns the factorial of 25. Output only the code. No explanation. No intro. No comments. Just raw code in a single code block."

    result = get_claude_response(os.environ["ANTHROPIC_API_KEY"], prompt)

    code_match = re.search(r"```python\n(.*?)```", result, re.DOTALL)

    code = code_match.group(1) if code_match else result
    code = code.replace('\\', '\\\\')

    # Run Python code inside the Sandbox and get the output

    response = sandbox.process.code_run(code)
    print("The factorial of 25 is", response.result)

    ````

    Running the snippet:

    ```bash
    ANTHROPIC_API_KEY="your-anthropic-api-key"
    DAYTONA_API_KEY="your-daytona-api-key"
    DAYTONA_TARGET=us
    python claude-example.py
    ```

    ```bash
    > The factorial of 25 is 15511210043330985984000000
    ```

    ````typescript
    import { Daytona } from '@daytonaio/sdk'
    import * as dotenv from 'dotenv'
    import axios from 'axios'

    dotenv.config()

    const daytona = new Daytona()

    async function getClaudeResponse(apiKey: string, prompt: string): Promise<string> {
      const url = "https://api.anthropic.com/v1/messages"
      const headers = {
        "x-api-key": apiKey,
        "anthropic-version": "2023-06-01",
        "Content-Type": "application/json"
      }
      const data = {
        "model": "claude-3-7-sonnet-latest",
        "max_tokens": 256,
        "messages": [{"role": "user", "content": prompt}]
      }

      try {
        const response = await axios.post(url, data, { headers })
        if (response.status === 200) {
          const content = response.data.content || []
          return content
            .filter((item: any) => item.type === "text")
            .map((item: any) => item.text)
            .join("")
        } else {
          return `Error ${response.status}: ${response.statusText}`
        }
      } catch (error: any) {
        return `Error: ${error.message}`
      }
    }

    async function main() {
      const sandbox = await daytona.create()

      const prompt = "Python code that returns the factorial of 25. Output only the code. No explanation. No intro. No comments. Just raw code in a single code block."
      
      const result = await getClaudeResponse(process.env.ANTHROPIC_API_KEY || "", prompt)
      
      // Extract code from the response using regex
      const codeMatch = result.match(/```python\n(.*?)```/s)
      
      let code = codeMatch ? codeMatch[1] : result
      code = code.replace(/\\/g, '\\\\')
      
      // Run the extracted code in the sandbox
      const response = await sandbox.process.codeRun(code)
      console.log("The factorial of 25 is", response.result)
    }

    main().catch(console.error)

    ````

    Running the snippet:

    ```bash
    ANTHROPIC_API_KEY="your-anthropic-api-key"
    DAYTONA_API_KEY="your-daytona-api-key"
    DAYTONA_TARGET=us
    npx ts-node claude-example.ts
    ```

    ```bash
    > The factorial of 25 is 15511210043330985984000000
    ```

## Additional Examples

Use the Daytona SDK [Python examples](https://github.com/daytonaio/daytona/tree/main/examples/python) or [TypeScript/JavaScript examples](https://github.com/daytonaio/daytona/tree/main/examples/typescript) to create a Sandbox and run your code.

Speed up your development on Daytona using LLMs. Copy the /llms.txt files and include them into your projects or chat context: [llms-full.txt](https://www.daytona.io/docs/llms-full.txt.md) or [llms.txt](https://www.daytona.io/docs/llms.txt.md)

Learn more by checking out the Daytona SDK repository on [GitHub](https://github.com/daytonaio/daytona).

## Multiple Runtime Support

The Daytona TypeScript SDK works across multiple JavaScript runtimes including Node.js, Deno, Bun, browsers, and serverless platforms (Cloudflare Workers, AWS Lambda, Azure Functions, etc.).

:::note[Browser and Framework Configuration]
When using the SDK in browser-based environments or frameworks like Vite and Next.js, you'll need to configure node polyfills. See the sections below for setup instructions.
:::

### Daytona in Vite Projects

When using Daytona SDK in a Vite-based project, you need to configure node polyfills to ensure compatibility. Add the following configuration to your `vite.config.ts` file in the plugins array:

```typescript
import { nodePolyfills } from 'vite-plugin-node-polyfills'

  plugins: [
    // ... other plugins
    nodePolyfills({
      globals: { global: true, process: true, Buffer: true },
      overrides: {
        path: 'path-browserify-win32',
      },
    }),
  ],
  // ... rest of your config
})
```

### Daytona in Next.js Projects

When using Daytona SDK in a Next.js project, you need to configure node polyfills to ensure compatibility with Webpack and Turbopack bundlers (depending on what you're using). Add the following configuration to your `next.config.ts` file:

```typescript
import type { NextConfig } from 'next'
import NodePolyfillPlugin from 'node-polyfill-webpack-plugin'
import { env, nodeless } from 'unenv'

const { alias: turbopackAlias } = env(nodeless, {})

const nextConfig: NextConfig = {
  // Turbopack
  experimental: {
    turbo: {
      resolveAlias: {
        ...turbopackAlias,
      },
    },
  },
  // Webpack
  webpack: (config, { isServer }) => {
    if (!isServer) {
      config.plugins.push(new NodePolyfillPlugin())
    }
    return config
  },
}

```

## Setting up the Daytona CLI

If you want to use [images from your local device](https://www.daytona.io/docs/en/snapshots.md#using-a-local-image) or simply prefer managing your Sandboxes using the command line interface, install the Daytona CLI by running:

    ```bash
    brew install daytonaio/cli/daytona
    ```

    ```bash
    powershell -Command "irm https://get.daytona.io/windows | iex"
    ```

The Daytona SDK provides built-in Git support through the `git` module in Sandboxes. This guide covers all available Git operations and best practices.

## Basic Operations

Daytona SDK provides an option to clone, check status, and manage Git repositories in Sandboxes. You can interact with Git repositories using the `git` module.

Similarly to file operations the starting cloning dir is the current Sandbox working directory. Uses the WORKDIR specified in
the Dockerfile if present, or falling back to the user's home directory if not - e.g. `workspace/repo` implies `/my-work-dir/workspace/repo`, but you are free to provide an absolute workDir path as well (by starting the path with `/`).

### Cloning Repositories

Daytona SDK provides an option to clone Git repositories into Sandboxes using Python and TypeScript. You can clone public or private repositories, specific branches, and authenticate using personal access tokens.

```python
# Basic clone
sandbox.git.clone(
    url="https://github.com/user/repo.git",
    path="workspace/repo"
)

# Clone with authentication

sandbox.git.clone(
    url="https://github.com/user/repo.git",
    path="workspace/repo",
    username="git",
    password="personal_access_token"
)

# Clone specific branch

sandbox.git.clone(
    url="https://github.com/user/repo.git",
    path="workspace/repo",
    branch="develop"
)

```
```typescript
// Basic clone
await sandbox.git.clone(
    "https://github.com/user/repo.git",
    "workspace/repo"
);

// Clone with authentication
await sandbox.git.clone(
    "https://github.com/user/repo.git",
    "workspace/repo",
    undefined,
    undefined,
    "git",
    "personal_access_token"
);

// Clone specific branch
await sandbox.git.clone(
    "https://github.com/user/repo.git",
    "workspace/repo",
    "develop"
);
```


See: [clone (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/git.md#gitclone), [clone (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/git.md#clone)

### Repository Status

Daytona SDK provides an option to check the status of Git repositories in Sandboxes. You can get the current branch, modified files, number of commits ahead and behind main branch using Python and TypeScript.

```python
# Get repository status
status = sandbox.git.status("workspace/repo")
print(f"Current branch: {status.current_branch}")
print(f"Commits ahead: {status.ahead}")
print(f"Commits behind: {status.behind}")
for file in status.file_status:
    print(f"File: {file.name}")

# List branches

response = sandbox.git.branches("workspace/repo")
for branch in response.branches:
    print(f"Branch: {branch}")

```
```typescript
// Get repository status
const status = await sandbox.git.status("workspace/repo");
console.log(`Current branch: ${status.currentBranch}`);
console.log(`Commits ahead: ${status.ahead}`);
console.log(`Commits behind: ${status.behind}`);
status.fileStatus.forEach(file => {
    console.log(`File: ${file.name}`);
});

// List branches
const response = await sandbox.git.branches("workspace/repo");
response.branches.forEach(branch => {
    console.log(`Branch: ${branch}`);
});
```


See: [status (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/git.md#gitstatus), [status (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/git.md#status)

## Branch Operations

Daytona SDK provides an option to manage branches in Git repositories. You can create, switch, and delete branches.

### Managing Branches

Daytona SDK provides an option to create, switch, and delete branches in Git repositories using Python and TypeScript.

```python
# Create new branch
sandbox.git.create_branch("workspace/repo", "feature/new-feature")

# Switch branch

sandbox.git.checkout_branch("workspace/repo", "feature/new-feature")

# Delete branch

sandbox.git.delete_branch("workspace/repo", "feature/old-feature")

```
```typescript
// Create new branch
await sandbox.git.createBranch("workspace/repo", "feature/new-feature");

// Switch branch
await sandbox.git.checkoutBranch("workspace/repo", "feature/new-feature");

// Delete branch
await sandbox.git.deleteBranch("workspace/repo", "feature/old-feature");
```


See: [create_branch (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/git.md#gitcreate_branch), [checkout_branch (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/git.md#gitcheckout_branch), [delete_branch (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/git.md#gitdelete_branch), [createBranch (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/git.md#createbranch), [checkoutBranch (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/git.md#checkoutbranch), [deleteBranch (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/git.md#deletebranch)

## Staging and Committing

Daytona SDK provides an option to stage and commit changes in Git repositories. You can stage specific files, all changes, and commit with a message using Python and TypeScript.

### Working with Changes

```python
# Stage specific files
sandbox.git.add("workspace/repo", ["file1.txt", "file2.txt"])

# Stage all changes

sandbox.git.add("workspace/repo", ["."])

# Commit changes

sandbox.git.commit("workspace/repo", "feat: add new feature", "John Doe", "john@example.com")

```
```typescript
// Stage specific files
await sandbox.git.add("workspace/repo", ["file1.txt", "file2.txt"]);

// Stage all changes
await sandbox.git.add("workspace/repo", ["."]);

// Commit changes
await sandbox.git.commit("workspace/repo", "feat: add new feature", "John Doe", "john@example.com");
```


See: [add (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/git.md#gitadd), [commit (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/git.md#gitcommit), [add (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/git.md#add), [commit (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/git.md#commit)

## Remote Operations

Daytona SDK provides an option to work with remote repositories in Git.

### Working with Remotes

Daytona SDK provides an option to push and pull changes using Python and TypeScript.

```python
# Push changes
sandbox.git.push("workspace/repo")

# Pull changes
sandbox.git.pull("workspace/repo")

```
```typescript
// Push changes
await sandbox.git.push("workspace/repo");

// Pull changes
await sandbox.git.pull("workspace/repo");
```


See: [push (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/git.md#gitpush), [pull (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/git.md#gitpull), [push (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/git.md#push), [pull (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/git.md#pull)

The Daytona SDK provides official Python and TypeScript interfaces for interacting with Daytona,
enabling you to programmatically manage development environments and execute code.

### Quick Start

Run your first line of code in a Daytona Sandbox. Use our [LLMs context files](https://www.daytona.io/docs/en/getting-started.md#additional-examples) for faster development with AI assistants.

#### 1. Get Your API Key

- Go to the Daytona [Dashboard](https://app.daytona.io/dashboard).
- Create a new [API key](https://app.daytona.io/dashboard/keys). Make sure to save it securely,
  as it won't be shown again.

#### 2. Install the SDK

    ```bash
    pip install daytona
    ```

    ```bash
    npm install @daytonaio/sdk
    ```

#### 3. Write Your Code

    Create a file named: `main.py`

    ```python
    from daytona import Daytona, DaytonaConfig

    # Define the configuration

    config = DaytonaConfig(api_key="your-api-key")

    # Initialize the Daytona client

    daytona = Daytona(config)

    # Create the Sandbox instance

    sandbox = daytona.create()

    # Run the code securely inside the Sandbox

    response = sandbox.process.code_run('print("Hello World from code!")')
    if response.exit_code != 0:
      print(f"Error: {response.exit_code} {response.result}")
    else:
        print(response.result)

    # Clean up

    sandbox.delete()

    ```

    Create a file named: `index.mts`

    ```typescript
    import { Daytona } from '@daytonaio/sdk';

    // Initialize the Daytona client
    const daytona = new Daytona({ apiKey: 'your-api-key' });

    // Create the Sandbox instance
    const sandbox = await daytona.create({
      language: 'typescript',
    });

    // Run the code securely inside the Sandbox
    const response = await sandbox.process.codeRun('console.log("Hello World from code!")')
    console.log(response.result);

    // Clean up
    await sandbox.delete()
    ```

:::note
Replace `your-api-key` with the value from your Daytona dashboard.
:::

#### 4. Run It

    ```bash
    python main.py
    ```

    ```bash
    npx tsx index.mts
    ```

#### ✅ What You Just Did

- Installed the Daytona SDK.
- Created a secure sandbox environment.
- Executed code remotely inside that sandbox.
- Retrieved and displayed the output locally.

You're now ready to use Daytona for secure, isolated code execution.

<ExploreMore />

import { Image } from 'astro:assets'

import chartImage from '../../../assets/docs/images/langchain-data-analysis-chart.png'

This package provides the `DaytonaDataAnalysisTool` - LangChain tool integration that enables agents to perform secure Python data analysis in a sandboxed environment. It supports multi-step workflows, file uploads/downloads, and custom result handling, making it ideal for automating data analysis tasks with LangChain agents.

This page demonstrates the use of this tool with a basic example analyzing a vehicle valuations dataset. Our goal is to analyze how vehicle prices vary by manufacturing year and create a line chart showing average price per year.

---

### 1. Workflow Overview

You upload your dataset and provide a natural language prompt describing the analysis you want. The agent reasons about your request, determines how to use the `DaytonaDataAnalysisTool` to perform the task on your dataset, and executes the analysis securely in a Daytona sandbox.

You provide the data and describe what insights you need - the agent handles the rest.

### 2. Project Setup

#### 2.1 Install Dependencies

:::note[Python Version Requirement]
This example requires **Python 3.10 or higher** because it uses LangChain 1.0+ syntax. It's recommended to use a virtual environment (e.g., `venv` or `poetry`) to isolate project dependencies.
:::

Install the required packages for this example:

    ```bash
    pip install -U langchain langchain-anthropic langchain-daytona-data-analysis python-dotenv
    ```

    The packages include:
    - `langchain`: LangChain framework for building AI agents
    - `langchain-anthropic`: Integration package connecting Claude (Anthropic) APIs and LangChain
    - `langchain-daytona-data-analysis`: Provides the `DaytonaDataAnalysisTool` for LangChain agents
    - `python-dotenv`: Used for loading environment variables from `.env` file

#### 2.2 Configure Environment

Get your API keys and configure your environment:

1. **Daytona API key:** Get it from [Daytona Dashboard](https://app.daytona.io/dashboard/keys)
2. **Anthropic API key:** Get it from [Anthropic Console](https://console.anthropic.com/)

Create a `.env` file in your project:

```bash
DAYTONA_API_KEY=dtn_***
ANTHROPIC_API_KEY=sk-ant-***
```

### 3. Download Dataset

We'll be using a publicly available dataset of vehicle valuation. You can download it directly from:

[https://download.daytona.io/dataset.csv](https://download.daytona.io/dataset.csv)

Download the file and save it as `vehicle-dataset.csv` in your project directory.

### 4. Initialize the Language Model

Models are the reasoning engine of LangChain agents - they drive decision-making, determine which tools to call, and interpret results.

In this example, we'll use Anthropic's Claude model, which excels at code generation and analytical tasks.

Configure the Claude model with the following parameters:

    ```python
    from langchain_anthropic import ChatAnthropic

    model = ChatAnthropic(
        model_name="claude-sonnet-4-5-20250929",
        temperature=0,
        max_tokens_to_sample=1024,
        timeout=None,
        max_retries=2,
        stop=None
    )
    ```

    **Parameters explained:**
    - `model_name`: Specifies the Claude model to use
    - `temperature`: Tunes the degree of randomness in generation
    - `max_tokens_to_sample`: Number of tokens to predict per generation
    - `max_retries`: Number of retries allowed for Anthropic API requests

:::tip[Learn More About Models]
For detailed information about LangChain models, different providers, and how to choose the right model for your use case, visit the [LangChain Models documentation](https://docs.langchain.com/oss/python/langchain/models).
:::

### 5. Define the Result Handler

When the agent executes Python code in the sandbox, it generates artifacts like charts and output logs. We can define a handler function to process these results.

This function will extract chart data from the execution artifacts and save them as PNG files:

    ```python
    import base64
    from daytona import ExecutionArtifacts

    def process_data_analysis_result(result: ExecutionArtifacts):
        # Print the standard output from code execution
        print("Result stdout", result.stdout)
        
        result_idx = 0
        for chart in result.charts:
            if chart.png:
                # Charts are returned in base64 format
                # Decode and save them as PNG files
                with open(f'chart-{result_idx}.png', 'wb') as f:
                    f.write(base64.b64decode(chart.png))
                print(f'Chart saved to chart-{result_idx}.png')
                result_idx += 1
    ```

    This handler processes execution artifacts by:
    - Logging stdout output from the executed code
    - Extracting chart data from the artifacts
    - Decoding base64-encoded PNG charts
    - Saving them to local files

### 6. Configure the Data Analysis Tool

Now we'll initialize the `DaytonaDataAnalysisTool` and upload our dataset.

    ```python
    from langchain_daytona_data_analysis import DaytonaDataAnalysisTool

    # Initialize the tool with our result handler
    DataAnalysisTool = DaytonaDataAnalysisTool(
        on_result=process_data_analysis_result
    )
    
    try:
      # Upload the dataset with metadata describing its structure
      with open("./vehicle-dataset.csv", "rb") as f:
          DataAnalysisTool.upload_file(
              f,
              description=(
                  "This is a CSV file containing vehicle valuations. "
                  "Relevant columns:\n"
                  "- 'year': integer, the manufacturing year of the vehicle\n"
                  "- 'price_in_euro': float, the listed price of the vehicle in Euros\n"
                  "Drop rows where 'year' or 'price_in_euro' is missing, non-numeric, or an outlier."
              )
          )
    ```

    **Key points:**
    - The `on_result` parameter connects our custom result handler
    - The `description` provides context about the dataset structure to the agent
    - Column descriptions help the agent understand how to process the data
    - Data cleaning instructions ensure quality analysis

### 7. Create and Run the Agent

Finally, we'll create the LangChain agent with our configured model and tool, then invoke it with our analysis request.

    ```python
    from langchain.agents import create_agent

    # Create the agent with the model and data analysis tool
    agent = create_agent(model, tools=[DataAnalysisTool], debug=True)

        # Invoke the agent with our analysis request
        agent_response = agent.invoke({
            "messages": [{
                "role": "user",
                "content": "Analyze how vehicles price varies by manufacturing year. Create a line chart showing average price per year."
            }]
        })
    finally:
        # Always close the tool to clean up sandbox resources
        DataAnalysisTool.close()
    ```

    **What happens here:**
    1. The agent receives your natural language request
    2. It determines it needs to use the `DaytonaDataAnalysisTool`
    3. Agent generates Python code to analyze the data
    4. Code executes securely in the Daytona sandbox
    5. Results are processed by our handler function
    6. Charts are saved to your local directory
    7. Sandbox resources are cleaned up in the `finally` block

### 8. Running Your Analysis

Now you can run the complete code to see the results.

    ```bash
    python data-analysis.py
    ```

#### Understanding the Agent's Execution Flow

When you run the code, the agent works through your request step by step. Here's what happens in the background:

**Step 1: Agent receives and interprets the request**

The agent acknowledges your analysis request:

```
AI Message: "I'll analyze how vehicle prices vary by manufacturing year and create a line chart showing the average price per year."
```

**Step 2: Agent generates Python code**

The agent generates Python code to explore the dataset first:

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv('/home/daytona/vehicle-dataset.csv')

# Display basic info about the dataset
print("Dataset shape:", df.shape)
print("\nFirst few rows:")
print(df.head())
print("\nColumn names:")
print(df.columns.tolist())
print("\nData types:")
print(df.dtypes)
```

**Step 3: Code executes in Daytona sandbox**

The tool runs this code in a secure sandbox and returns the output:

```
Result stdout Dataset shape: (100000, 15)

First few rows:
   Unnamed: 0  ...                               offer_description
0       75721  ...  ST-Line Hybrid Adapt.LED+Head-Up-Display Klima
1       80184  ...             blue Trend,Viele Extras,Top-Zustand
2       19864  ...    35 e-tron S line/Matrix/Pano/ACC/SONOS/LM 21
3       76699  ...           2.0 Lifestyle Plus Automatik Navi FAP
4       92991  ...                    1.6 T 48V 2WD Spirit LED, WR

[5 rows x 15 columns]

Column names:
['Unnamed: 0', 'brand', 'model', 'color', 'registration_date', 'year', 
 'price_in_euro', 'power_kw', 'power_ps', 'transmission_type', 'fuel_type', 
 'fuel_consumption_l_100km', 'fuel_consumption_g_km', 'mileage_in_km', 
 'offer_description']

Data types:
Unnamed: 0                    int64
brand                        object
model                        object
color                        object
registration_date            object
year                         object
price_in_euro                object
power_kw                     object
power_ps                     object
transmission_type            object
fuel_type                    object
fuel_consumption_l_100km     object
fuel_consumption_g_km        object
mileage_in_km               float64
offer_description            object
dtype: object
```

**Step 4: Agent generates detailed analysis code**

Based on the initial dataset information, the agent generates more specific code to examine the key columns:

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv('/home/daytona/vehicle-dataset.csv')

print("Dataset shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())

# Check for year and price_in_euro columns
print("\nChecking 'year' column:")
print(df['year'].describe())
print("\nMissing values in 'year':", df['year'].isna().sum())

print("\nChecking 'price_in_euro' column:")
print(df['price_in_euro'].describe())
print("\nMissing values in 'price_in_euro':", df['price_in_euro'].isna().sum())
```

**Step 5: Execution results from sandbox**

The code executes and returns column statistics:

```
Result stdout Dataset shape: (100000, 15)

Column names:
['Unnamed: 0', 'brand', 'model', 'color', 'registration_date', 'year', 
 'price_in_euro', 'power_kw', 'power_ps', 'transmission_type', 'fuel_type', 
 'fuel_consumption_l_100km', 'fuel_consumption_g_km', 'mileage_in_km', 
 'offer_description']

Checking 'year' column:
count     100000
unique        49
top         2019
freq       12056
Name: year, dtype: object

Missing values in 'year': 0

Checking 'price_in_euro' column:
count     100000
unique     11652
top        19990
freq         665
Name: price_in_euro, dtype: object

Missing values in 'price_in_euro': 0
```

**Step 6: Agent generates final analysis and visualization code**

Now that the agent understands the data structure, it generates the complete analysis code with data cleaning, processing, and visualization:

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv('/home/daytona/vehicle-dataset.csv')

print("Original dataset shape:", df.shape)

# Clean the data - remove rows with missing values in year or price_in_euro
df_clean = df.dropna(subset=['year', 'price_in_euro'])
print(f"After removing missing values: {df_clean.shape}")

# Convert to numeric and remove non-numeric values
df_clean['year'] = pd.to_numeric(df_clean['year'], errors='coerce')
df_clean['price_in_euro'] = pd.to_numeric(df_clean['price_in_euro'], errors='coerce')

# Remove rows where conversion failed
df_clean = df_clean.dropna(subset=['year', 'price_in_euro'])
print(f"After removing non-numeric values: {df_clean.shape}")

# Remove outliers using IQR method for both year and price
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

df_clean = remove_outliers(df_clean, 'year')
print(f"After removing year outliers: {df_clean.shape}")

df_clean = remove_outliers(df_clean, 'price_in_euro')
print(f"After removing price outliers: {df_clean.shape}")

print("\nCleaned data summary:")
print(df_clean[['year', 'price_in_euro']].describe())

# Calculate average price per year
avg_price_by_year = df_clean.groupby('year')['price_in_euro'].mean().sort_index()

print("\nAverage price by year:")
print(avg_price_by_year)

# Create line chart
plt.figure(figsize=(14, 7))
plt.plot(avg_price_by_year.index, avg_price_by_year.values, marker='o', 
         linewidth=2, markersize=6, color='#2E86AB')
plt.xlabel('Manufacturing Year', fontsize=12, fontweight='bold')
plt.ylabel('Average Price (€)', fontsize=12, fontweight='bold')
plt.title('Average Vehicle Price by Manufacturing Year', fontsize=14, 
          fontweight='bold', pad=20)
plt.grid(True, alpha=0.3, linestyle='--')
plt.xticks(rotation=45)

# Format y-axis to show currency
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'€{x:,.0f}'))

plt.tight_layout()
plt.show()

# Additional statistics
print(f"\nTotal number of vehicles analyzed: {len(df_clean)}")
print(f"Year range: {int(df_clean['year'].min())} - {int(df_clean['year'].max())}")
print(f"Price range: €{df_clean['price_in_euro'].min():.2f} - €{df_clean['price_in_euro'].max():.2f}")
print(f"Overall average price: €{df_clean['price_in_euro'].mean():.2f}")
```

This comprehensive code performs data cleaning, outlier removal, calculates averages by year, and creates a professional visualization.

**Step 7: Final execution and chart generation**

The code executes successfully in the sandbox, processes the data, and generates the visualization:

```
Result stdout Original dataset shape: (100000, 15)
After removing missing values: (100000, 15)
After removing non-numeric values: (99946, 15)
After removing year outliers: (96598, 15)
After removing price outliers: (90095, 15)

Cleaned data summary:
               year  price_in_euro
count  90095.000000   90095.000000
mean    2016.698563   22422.266707
std        4.457647   12964.727116
min     2005.000000     150.000000
25%     2014.000000   12980.000000
50%     2018.000000   19900.000000
75%     2020.000000   29500.000000
max     2023.000000   62090.000000

Average price by year:
year
2005.0     5968.124319
2006.0     6870.881523
2007.0     8015.234473
2008.0     8788.644495
2009.0     8406.198576
2010.0    10378.815972
2011.0    11540.640435
2012.0    13306.642261
2013.0    14512.707025
2014.0    15997.682899
2015.0    18563.864358
2016.0    20124.556294
2017.0    22268.083322
2018.0    24241.123673
2019.0    26757.469111
2020.0    29400.163494
2021.0    30720.168646
2022.0    33861.717552
2023.0    33119.840175
Name: price_in_euro, dtype: float64

Total number of vehicles analyzed: 90095
Year range: 2005 - 2023
Price range: €150.00 - €62090.00
Overall average price: €22422.27

Chart saved to chart-0.png
```

The agent successfully completed the analysis, showing that vehicle prices generally increased from 2005 (€5,968) to 2022 (€33,862), with a slight decrease in 2023. The result handler captured the generated chart and saved it as `chart-0.png`.

You should see the chart in your project directory that will look similar to this:

<Image src={chartImage} alt="Vehicle valuation by manufacturing year chart" width={600} style="max-width: 100%; height: auto; margin: 1rem 0;" />

### 9. Complete Implementation

Here is the complete, ready-to-run example:

    ```python
  import base64
  from dotenv import load_dotenv
  from langchain.agents import create_agent
  from langchain_anthropic import ChatAnthropic
  from daytona import ExecutionArtifacts
  from langchain_daytona_data_analysis import DaytonaDataAnalysisTool

  load_dotenv()

  model = ChatAnthropic(
      model_name="claude-sonnet-4-5-20250929",
      temperature=0,
      max_tokens_to_sample=1024,
      timeout=None,
      max_retries=2,
      stop=None
  )

  def process_data_analysis_result(result: ExecutionArtifacts):
      # Print the standard output from code execution
      print("Result stdout", result.stdout)
      result_idx = 0
      for chart in result.charts:
          if chart.png:
              # Save the png to a file
              # The png is in base64 format.
              with open(f'chart-{result_idx}.png', 'wb') as f:
                  f.write(base64.b64decode(chart.png))
              print(f'Chart saved to chart-{result_idx}.png')
              result_idx += 1

  def main():
      DataAnalysisTool = DaytonaDataAnalysisTool(
          on_result=process_data_analysis_result
      )

      try:
          with open("./vehicle-dataset.csv", "rb") as f:
              DataAnalysisTool.upload_file(
                  f,
                  description=(
                      "This is a CSV file containing vehicle valuations. "
                      "Relevant columns:\n"
                      "- 'year': integer, the manufacturing year of the vehicle\n"
                      "- 'price_in_euro': float, the listed price of the vehicle in Euros\n"
                      "Drop rows where 'year' or 'price_in_euro' is missing, non-numeric, or an outlier."
                  )
              )

          agent = create_agent(model, tools=[DataAnalysisTool], debug=True)

          agent_response = agent.invoke(
              {"messages": [{"role": "user", "content": "Analyze how vehicles price varies by manufacturing year. Create a line chart showing average price per year."}]}
          )
      finally:
          DataAnalysisTool.close()

  if __name__ == "__main__":
      main()
    ```

**Key advantages of this approach:**

- **Secure execution:** Code runs in isolated Daytona sandbox
- **Automatic artifact capture:** Charts, tables, and outputs are automatically extracted
- **Natural language interface:** Describe analysis tasks in plain English
- **Framework integration:** Seamlessly works with LangChain's agent ecosystem

### 10. API Reference

The following public methods are available on `DaytonaDataAnalysisTool`:

#### download_file

```python
def download_file(remote_path: str) -> bytes
```

Downloads a file from the sandbox by its remote path.

**Arguments**:

- `remote_path` - str: Path to the file in the sandbox.

**Returns**:

- `bytes` - File contents.

**Example**:

```python
# Download a file from the sandbox
file_bytes = tool.download_file("/home/daytona/results.csv")
```

#### upload_file

```python
def upload_file(file: IO, description: str) -> SandboxUploadedFile
```

Uploads a file to the sandbox. The file is placed in `/home/daytona/`.

**Arguments**:

- `file` - IO: File-like object to upload.
- `description` - str: Description of the file, explaining its purpose and the type of data it contains.

**Returns**:

- [`SandboxUploadedFile`](#sandboxuploadedfile) - Metadata about the uploaded file.

**Example**:

Suppose you want to analyze sales data for a retail business. You have a CSV file named `sales_q3_2025.csv` containing columns like `transaction_id`, `date`, `product`, `quantity`, and `revenue`. You want to upload this file and provide a description that gives context for the analysis.

```python
with open("sales_q3_2025.csv", "rb") as f:
    uploaded = tool.upload_file(
        f,
        "CSV file containing Q3 2025 retail sales transactions. Columns: transaction_id, date, product, quantity, revenue."
    )
```

#### remove_uploaded_file

```python
def remove_uploaded_file(uploaded_file: SandboxUploadedFile) -> None
```

Removes a previously uploaded file from the sandbox.

**Arguments**:

- `uploaded_file` - [`SandboxUploadedFile`](#sandboxuploadedfile): The file to remove.

**Returns**:

- None

**Example**:

```python
# Remove an uploaded file
tool.remove_uploaded_file(uploaded)
```

#### get_sandbox

```python
def get_sandbox() -> Sandbox
```

Gets the current sandbox instance.

This method provides access to the Daytona sandbox instance, allowing you to inspect sandbox properties and metadata, as well as perform any sandbox-related operations. For details on available attributes and methods, see the [Sandbox](#sandbox) data structure section below.

**Arguments**:

- None

**Returns**:

- [`Sandbox`](#sandbox) - Sandbox instance.

**Example**:

```python
sandbox = tool.get_sandbox()
```

#### install_python_packages

```python
def install_python_packages(package_names: str | list[str]) -> None
```

Installs one or more Python packages in the sandbox using pip.

**Arguments**:

- `package_names` - str | list[str]: Name(s) of the package(s) to install.

**Returns**:

- None

:::note
The list of preinstalled packages in a sandbox can be found at [Daytona's Default Snapshot documentation](https://www.daytona.io/docs/en/snapshots.md#default-snapshot).
:::

**Example**:

```python
# Install a single package
tool.install_python_packages("pandas")

# Install multiple packages
tool.install_python_packages(["numpy", "matplotlib"])
```

#### close

```python
def close() -> None
```

Closes and deletes the sandbox environment.

**Arguments**:

- None

**Returns**:

- None

:::note
Call this method when you are finished with all data analysis tasks to properly clean up resources and avoid unnecessary usage.
:::

**Example**:

```python
# Close the sandbox and clean up
tool.close()
```

### 11. Data Structures

#### SandboxUploadedFile
Represents metadata about a file uploaded to the sandbox.

- `name`: `str` - Name of the uploaded file in the sandbox
- `remote_path`: `str` - Full path to the file in the sandbox
- `description`: `str` - Description provided during upload

#### Sandbox
Represents a Daytona sandbox instance.

See the full structure and API in the [Daytona Python SDK Sandbox documentation](https://www.daytona.io/docs/en/python-sdk/sync/sandbox.md#sandbox).

The Daytona SDK provides Language Server Protocol (LSP) support through Sandbox instances. This enables advanced language features like code completion, diagnostics, and more.

## Creating LSP Servers

Daytona SDK provides an option to create LSP servers in Python and TypeScript. The `path_to_project` argument is relative to the current Sandbox working directory when no leading `/` is used. The working directory is specified by WORKDIR when it is present in the Dockerfile, and otherwise falls back to the user's home directory.

```python
from daytona import Daytona, LspLanguageId

# Create Sandbox
daytona = Daytona()
sandbox = daytona.create()

# Create LSP server for Python
lsp_server = sandbox.create_lsp_server(
    language_id=LspLanguageId.PYTHON,
    path_to_project="workspace/project"
)

```
```typescript
import { Daytona, LspLanguageId } from '@daytonaio/sdk'

// Create sandbox
const daytona = new Daytona()
const sandbox = await daytona.create({
    language: 'typescript'
})

// Create LSP server for TypeScript
const lspServer = await sandbox.createLspServer(
    LspLanguageId.TYPESCRIPT,
    "workspace/project"
)
```


See: [create_lsp_server (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/sandbox.md#sandboxcreate_lsp_server), [createLspServer (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/sandbox.md#createlspserver)

### Supported Languages

The supported languages for creating LSP servers with the Daytona SDK are defined by the `LspLanguageId` enum:

| Enum Value                   | Description                         |
|------------------------------|-------------------------------------|
| `LspLanguageId.PYTHON`       | Python language server.             |
| `LspLanguageId.TYPESCRIPT`   | TypeScript/JavaScript language server. |

See: [LspLanguageId (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/lsp-server.md#lsplanguageid), [LspLanguageId (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/lsp-server.md#lsplanguageid)

## LSP Features

Daytona SDK provides LSP features for code analysis and editing.

### Code Completion

Daytona SDK provides an option to get code completions for a specific position in a file using Python and TypeScript.

```python
completions = lsp_server.completions(
    path="workspace/project/main.py",
    position={"line": 10, "character": 15}
)
print(f"Completions: {completions}")
```
```typescript
const completions = await lspServer.completions(
    "workspace/project/main.ts",
    { line: 10, character: 15 }
)
console.log('Completions:', completions)
```

See: [completions (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/lsp-server.md#lspservercompletions), [completions (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/lsp-server.md#completions)

Daytona enforces resource limits to ensure fair usage and stability across all organizations. Your organization has access to a compute pool consisting of:

- **vCPU** — Total CPU cores available
- **Memory** — Total RAM available
- **Storage** — Total disk space available

Resources are shared across all running Sandboxes, so the number of Sandboxes you can run at once depends on their individual usage.

You can see default values and how to configure usage under [Sandbox Resources](https://www.daytona.io/docs/en/sandbox-management.md#sandbox-resources). Check your current usage and limits in the [Dashboard](https://app.daytona.io/dashboard/limits).

## Tiers & Limit Increases

Organizations are automatically placed into a Tier based on verification status.\
You can unlock higher limits by completing the following steps:

| Tier   | Resources (vCPU / RAM / Storage) | Access Requirements                                                                                                     |
| ------ | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Tier 1 | 10 / 10GiB / 30GiB               | Email verified                                                                                                          |
| Tier 2 | 100 / 200GiB / 300GiB            | Credit card linked, $25 top-up, [GitHub connected](https://www.daytona.io/docs/en/linked-accounts.md#how-to-link-an-account). |
| Tier 3 | 250 / 500GiB / 2000GiB           | Business email verified, Phone verified, $500 top-up.                                                                   |
| Tier 4 | 500 / 1000GiB / 5000GiB          | $2000 top-up every 30 days.                                                                                             |
| Custom | Custom limits                    | Contact [support@daytona.io](mailto:support@daytona.io)                                                                 |

Once you meet the criteria for a higher tier, make sure to Upgrade by clicking the "Upgrade" button in the [Dashboard](https://app.daytona.io/dashboard/limits).

## Manage usage dynamically

You can manage your resource usage by [changing the state](http://localhost:4321/docs/sandbox-management#sandbox-lifecycle) of your Sandboxes. The table below summarizes how each state affects resource usage:

| State      | vCPU | Memory | Storage | Notes                                                      |
|------------|:-------:|:--------:|:------:|------------------------------------------------------------|
| Running |   ✅    |   ✅     |  ✅   | Counts against all limits                                  |
| Stopped |   ❌    |   ❌     |  ✅   | Frees CPU & memory, but storage is still used                 |
| Archived|   ❌    |   ❌     |  ❌   | Data moved to cold storage, no quota impact                |
| Deleted |   ❌    |   ❌     |  ❌   | All resources freed                                        |

See [Sandbox Management](https://www.daytona.io/docs/en/sandbox-management.md) for more information.

## Need More?

If you need higher or specialized limits, reach out to [support@daytona.io](mailto:support@daytona.io).

Daytona supports the linking of user accounts from various identity providers. At the moment, the following providers are supported:

- Google
- GitHub

You can log into your Daytona account using any linked provider.

:::tip

#### Unlock higher usage limits

Linking your GitHub account is one of the requirements to automatically upgrade to Tier 2.

:::

## Linking/Unlinking Accounts

To link or unlink an account:
1. Visit the [Linked Accounts](https://app.daytona.io/dashboard/user/linked-accounts) page in the Daytona dashboard.
2. Use the "Link Account" or "Unlink" button next to the provider you wish to manage.

## Need More?

If you need support for other identity providers, reach out to [support@daytona.io](mailto:support@daytona.io).

When executing long-running processes in a sandbox, you’ll often want to access and process their logs in **real-time**.

The Daytona SDK supports both:

- `Fetching log snapshot` — retrieve all logs up to a certain point.
- `Log streaming` — stream logs as they are being produced, while the process is still running.

This guide covers how to use log streaming in both asynchronous and synchronous modes.
Real-time streaming is especially useful for **debugging**, **monitoring**, or integrating with **observability tools**.

:::note
Starting with version `0.27.0`, you can retrieve session command logs in two distinct streams: **stdout** and **stderr**.
:::

## Streaming Logs with Callbacks

If your sandboxed process is part of a larger system and is expected to run for an extended period (or indefinitely),
you can process logs asynchronously **in the background**, while the rest of your system continues executing.

This is ideal for:

- Continuous monitoring
- Debugging long-running jobs
- Live log forwarding or visualizations


  ```python
  import asyncio
  from daytona import Daytona, SessionExecuteRequest

  async def main():
    daytona = Daytona()
    sandbox = daytona.create()

    session_id = "streaming-session"
    sandbox.process.create_session(session_id)

    command = sandbox.process.execute_session_command(
      session_id,
      SessionExecuteRequest(
        command='for i in {1..5}; do echo "Step $i"; echo "Error $i" >&2; sleep 1; done',
        var_async=True,
      ),
    )

    # Stream logs with separate callbacks
    logs_task = asyncio.create_task(
      sandbox.process.get_session_command_logs_async(
        session_id,
        command.cmd_id,
        lambda stdout: print(f"[STDOUT]: {stdout}"),
        lambda stderr: print(f"[STDERR]: {stderr}"),
      )
    )

    print("Continuing execution while logs are streaming...")
    await asyncio.sleep(3)
    print("Other operations completed!")

    # Wait for the logs to complete
    await logs_task

    sandbox.delete()
    
  if __name__ == "__main__":
      asyncio.run(main())

  ```
  ```typescript
  import { Daytona, SessionExecuteRequest } from '@daytonaio/sdk'

  async function main() {
    const daytona = new Daytona()
    const sandbox = await daytona.create()
    const sessionId = "exec-session-1"
    await sandbox.process.createSession(sessionId)

    const command = await sandbox.process.executeSessionCommand(
      sessionId,
      {
        command: 'for i in {1..5}; do echo "Step $i"; echo "Error $i" >&2; sleep 1; done',
        runAsync: true,
      },
    )

    // Stream logs with separate callbacks
    const logsTask = sandbox.process.getSessionCommandLogs(
      sessionId,
      command.cmdId!,
      (stdout) => console.log('[STDOUT]:', stdout),
      (stderr) => console.log('[STDERR]:', stderr),
    )

    console.log('Continuing execution while logs are streaming...')
    await new Promise((resolve) => setTimeout(resolve, 3000))
    console.log('Other operations completed!')

    // Wait for the logs to complete
    await logsTask

    await sandbox.delete()
  }

  main()
  ```


See: [get_session_command_logs_async (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/process.md#processget_session_command_logs_async), [getSessionCommandLogs (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/process.md#getsessioncommandlogs)

## Retrieve All Existing Logs

If the command has a predictable duration, or if you don't need to run it in the background but want to
periodically check all existing logs, you can use the following example to get the logs up to the current point in time.

  ```python
  import time
  from daytona import Daytona, SessionExecuteRequest

  daytona = Daytona()
  sandbox = daytona.create()
  session_id = "exec-session-1"
  sandbox.process.create_session(session_id)

  # Execute a blocking command and wait for the result
  command = sandbox.process.execute_session_command(
    session_id, SessionExecuteRequest(command="echo 'Hello from stdout' && echo 'Hello from stderr' >&2")
  )
  print(f"[STDOUT]: {command.stdout}")
  print(f"[STDERR]: {command.stderr}")
  print(f"[OUTPUT]: {command.output}")

  # Or execute command in the background and get the logs later
  command = sandbox.process.execute_session_command(
    session_id, 
    SessionExecuteRequest(
      command='while true; do if (( RANDOM % 2 )); then echo "All good at $(date)"; else echo "Oops, an error at $(date)" >&2; fi; sleep 1; done',
      run_async=True
    )
  )
  time.sleep(5)
  # Get the logs up to the current point in time
  logs = sandbox.process.get_session_command_logs(session_id, command.cmd_id)
  print(f"[STDOUT]: {logs.stdout}")
  print(f"[STDERR]: {logs.stderr}")
  print(f"[OUTPUT]: {logs.output}")

  sandbox.delete()
  ```
  ```typescript
  import { Daytona, SessionExecuteRequest } from '@daytonaio/sdk'

  async function main() {
    const daytona = new Daytona()
    const sandbox = await daytona.create()
    const sessionId = "exec-session-1"
    await sandbox.process.createSession(sessionId)

    // Execute a blocking command and wait for the result
    const command = await sandbox.process.executeSessionCommand(
      sessionId,
      {
        command: 'echo "Hello from stdout" && echo "Hello from stderr" >&2',
      },
    )
    console.log(`[STDOUT]: ${command.stdout}`)
    console.log(`[STDERR]: ${command.stderr}`)
    console.log(`[OUTPUT]: ${command.output}`)

    // Or execute command in the background and get the logs later
    const command2 = await sandbox.process.executeSessionCommand(
      sessionId,
      {
        command: 'while true; do if (( RANDOM % 2 )); then echo "All good at $(date)"; else echo "Oops, an error at $(date)" >&2; fi; sleep 1; done',
        runAsync: true,
      },
    )
    await new Promise((resolve) => setTimeout(resolve, 5000))
    // Get the logs up to the current point in time
    const logs = await sandbox.process.getSessionCommandLogs(sessionId, command2.cmdId!)
    console.log(`[STDOUT]: ${logs.stdout}`)
    console.log(`[STDERR]: ${logs.stderr}`)
    console.log(`[OUTPUT]: ${logs.output}`)

    await sandbox.delete()
  }

  main()
  ```


See: [get_session_command_logs_async (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/process.md#processget_session_command_logs_async), [getSessionCommandLogs (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/process.md#getsessioncommandlogs)

The Daytona Model Context Protocol (MCP) Server enables AI agents to interact with Daytona's features programmatically. This guide covers how to set up and use the MCP server with various AI agents.

## Prerequisites

Before getting started, ensure you have:

- A Daytona account
- Daytona CLI installed
- A compatible AI agent (Claude Desktop App, Claude Code, Cursor, or Windsurf)

## Installation and Setup

### 1. Install Daytona CLI

```bash
brew install daytonaio/cli/daytona
```

```bash
powershell -Command "irm https://get.daytona.io/windows | iex"
```

### 2. Authenticate with Daytona

```bash
daytona login
```

### 3. Initialize MCP Server

Initialize the Daytona MCP server with your preferred AI agent:

```bash
daytona mcp init [claude/cursor/windsurf]
```

### 4. Open Your AI Agent

After initialization, open your AI agent application to begin using Daytona features.

## Integration with Other AI Agents

To integrate Daytona MCP with other AI agents, follow these steps:

1. Generate the MCP configuration:

```bash
daytona mcp config
```

This command outputs a JSON configuration that you can copy into your agent's settings:

```json
{
  "mcpServers": {
    "daytona-mcp": {
      "command": "daytona",
      "args": ["mcp", "start"],
      "env": {
        "HOME": "${HOME}",
        "PATH": "${HOME}:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/homebrew/bin"
      },
      "logFile": "${HOME}/Library/Logs/daytona/daytona-mcp-server.log"
    }
  }
}
```

:::note
For Windows users, add the following to the `env` field:

```json
"APPDATA": "${APPDATA}"
```

:::

2. Open or restart your AI agent to apply the configuration.

## Available Tools

### Sandbox Management

- **Create Sandbox**

  - Creates a new Daytona sandbox
  - Parameters:
    - `name`: Name of the sandbox (optional)
    - `target`: Target region (optional)
    - `snapshot`: Snapshot for the sandbox (optional)
    - `auto_stop_interval` (default: "15"): Auto-stop interval in minutes (0 disables)
    - `auto_archive_interval` (default: "10080"): Auto-archive interval in minutes (0 means the maximum interval will be used)
    - `auto_delete_interval` (default: "-1"): Auto-delete interval in minutes (negative value means disabled, 0 means delete immediately upon stopping)
    - `volumes`: Volumes to attach to the sandbox (optional)
    - `network_block_all`: Whether to block all network access for the sandbox (optional)
    - `network_allow_list`: Comma-separated list of allowed CIDR network addresses for the sandbox (optional)
    - `public`: Whether the sandbox http preview is publicly accessible (optional)
    - `cpu`: CPU cores allocated to the sandbox (optional)
    - `gpu`: GPU units allocated to the sandbox (optional)
    - `memory`: Memory allocated to the sandbox in GB (optional)
    - `disk`: Disk space allocated to the sandbox in GB (optional)
    - `user`: User associated with the sandbox (optional)
    - `build_info`: Build information for the sandbox (optional)
    - `env`: Environment variables for the sandbox (optional)
    - `labels`: Labels for the sandbox (optional)

- **Destroy Sandbox**
  - Removes an existing Daytona sandbox
  - Parameters:
    - `id`: ID of the sandbox to destroy

### File Operations

- **Download File**

  - Downloads a file from the Daytona sandbox
  - Returns content as text or base64 encoded image
  - Parameters:
    - `id`: ID of the sandbox to download the file from
    - `file_path`: Path to the file

- **Upload File**

  - Uploads a file to the Daytona sandbox
  - Supports text or base64-encoded binary content
  - Creates necessary parent directories automatically
  - Files persist during the session with appropriate permissions
  - Supports overwrite controls and maintains original file formats
  - Parameters:
    - `id`: ID of the sandbox to upload the file to
    - `file_path`: Path to the file to upload
    - `content`: Content of the file to upload
    - `encoding`: Encoding of the file to upload
    - `overwrite`: Overwrite the file if it already exists

- **Create Folder**

  - Creates a new directory in the sandbox
  - Parameters:
    - `id`: ID of the sandbox to create the folder in
    - `folder_path`: Path to create
    - `mode`: Directory permissions (default: 0755)

- **Get File Info**

  - Retrieves information about a file
  - Parameters:
    - `id`: ID of the sandbox to get the file information from
    - `file_path`: Path to the file

- **List Files**

  - Lists contents of a directory
  - Parameters:
    - `id`: ID of the sandbox to list the files from
    - `path`: Directory path (defaults to current directory)

- **Move File**

  - Moves or renames a file
  - Parameters:
    - `id`: ID of the sandbox to move the file in
    - `source_path`: Source location
    - `dest_path`: Destination location

- **Delete File**
  - Removes a file or directory
  - Parameters:
    - `id`: ID of the sandbox to delete the file in
    - `file_path`: Path to delete

### Preview

- **Preview Link**
  - Generates accessible preview URLs for web applications
  - Creates secure tunnels to expose local ports externally
  - Validates server status on specified ports
  - Provides diagnostic information for troubleshooting
  - Supports custom descriptions and metadata for service organization
  - Parameters:
    - `id`: ID of the sandbox to preview the link from
    - `port`: Port to expose
    - `description`: Description of the service
    - `check_server`: Check if a server is running on the port

### Git Operations

- **Git Clone**
  - Clones a Git repository
  - Parameters:
    - `id`: ID of the sandbox to clone the repository in
    - `url`: Repository URL
    - `path`: Target directory (defaults to current)
    - `branch`: Branch to clone
    - `commit_id`: Specific commit to clone
    - `username`: Git username
    - `password`: Git password

### Command Execution

- **Execute Command**
  - Runs shell commands in the Daytona environment
  - Returns stdout, stderr, and exit code
  - Commands run with sandbox user permissions
  - Parameters:
    - `id`: ID of the sandbox to execute the command in
    - `command`: Command to execute

## Troubleshooting

Common issues and solutions:

- **Authentication Issues**

  - Run `daytona login` to refresh credentials

- **Connection Errors**

  - Verify MCP server configuration
  - Check server status

- **Sandbox Errors**
  - Use `daytona sandbox list` to check sandbox status

## Support

For additional assistance:

- Visit [daytona.io](https://daytona.io)
- Contact support at support@daytona.io

Daytona provides network egress limiting for sandboxes to control internet access. This feature can be automatically applied based on your organization's billing tier or manually configured for specific sandboxes.

## Tier-Based Network Restrictions

Network limits are automatically applied to sandboxes based on your organization's billing tier. This provides secure and controlled internet access for development environments:

- **Tier 1 & Tier 2**: Network access is restricted and cannot be overridden at the sandbox level
- **Tier 3 & Tier 4**: Full internet access is available by default, with the ability to configure custom network settings

:::note
**Tier 1 & 2**: Organization-level network restrictions take precedence over sandbox-level settings. Even if you specify `networkAllowList` when creating a sandbox, the organization's network restrictions will still apply.
:::

To learn more about organization tiers and limits, see the [Limits documentation](https://www.daytona.io/docs/limits.md).

## Managing Network Access

### Creating Sandboxes with Network Restrictions

You can control network access when creating sandboxes using the `networkAllowList` and `networkBlockAll` parameters:


```python
from daytona import CreateSandboxFromSnapshotParams, Daytona

daytona = Daytona()

# Allow access to specific IP addresses (Wikipedia, X/Twitter, private network)
sandbox = daytona.create(CreateSandboxFromSnapshotParams(
    network_allow_list='208.80.154.232/32,199.16.156.103/32,192.168.1.0/24'
))

# Or block all network access
sandbox = daytona.create(CreateSandboxFromSnapshotParams(
    network_block_all=True
))
```


```typescript
import { Daytona } from '@daytonaio/sdk'

const daytona = new Daytona()

// Allow access to specific IP addresses (Wikipedia, X/Twitter, private network)
const sandbox = await daytona.create({
  networkAllowList: '208.80.154.232/32,199.16.156.103/32,192.168.1.0/24'
})

// Or block all network access
const sandbox = await daytona.create({
  networkBlockAll: true
})
```



:::note
If both `networkBlockAll` and `networkAllowList` are specified, `networkBlockAll` takes precedence and all network access will be blocked, ignoring the allow list.
:::


### Network Allow List Format

The `networkAllowList` accepts up to 5 CIDR network blocks separated by commas:

- **Single IP**: `208.80.154.232/32` (Wikipedia)
- **Subnet**: `192.168.1.0/24` (Private network)
- **Multiple networks**: `208.80.154.232/32,199.16.156.103/32,10.0.0.0/8`

:::note
**Essential Services**: Services that are essential for development are accessible on all tiers, including package registries, container registries, Git repositories, CDN services, platform services, system package managers etc.\
If you experience issues with any essential development services, please contact [support@daytona.io](mailto:support@daytona.io) for assistance as these should be accessible on all tiers.

For a complete list of whitelisted services, see [Essential Services](#essential-services) below.
:::

## Organization Configuration

The network access policies for your organization are set automatically depending on your organization's limits tier and cannot be modified by organization administrators. These policies determine the default network behavior for all sandboxes in your organization.

## Testing Network Access

To test network connectivity from your sandbox:

```bash
# Test HTTP connectivity to allowed addresses
curl -I https://208.80.154.232

# Test package manager access (allowed on all tiers)
apt update  # For Ubuntu/Debian
npm ping    # For Node.js
pip install --dry-run requests  # For Python
```

## Security Benefits

Network limits provide several security advantages:

- **Prevents data exfiltration** from sandboxes
- **Reduces attack surface** by limiting external connections
- **Complies with security policies** for development environments
- **Enables fine-grained control** over network access

:::caution
Enabling unrestricted network access may pose security risks when executing untrusted code. It is recommended to whitelist specific network addresses using `networkAllowList` or block all network access using `networkBlockAll` instead.

Test network connectivity before starting critical development work and consider upgrading your tier if you need access to many external services.
:::


## Essential Services

The following services are whitelisted and accessible on all tiers:

- Package registries:
  - npm: `registry.npmjs.org`, `registry.npmjs.com`, `nodejs.org`, `nodesource.com`, `npm.pkg.github.com`
  - yarn: `classic.yarnpkg.com`, `registry.yarnpkg.com`, `repo.yarnpkg.com`, `releases.yarnpkg.com`, `yarn.npmjs.org`, `yarnpkg.netlify.com`, `dl.yarnpkg.com`, `yarnpkg.com`
  - PyPI: `pypi.org`, `pypi.python.org`, `files.pythonhosted.org`, `bootstrap.pypa.io`
  - Maven: `repo1.maven.org`, `repo.maven.apache.org`
- Container registries:
  - Docker: `download.docker.com`, `registry-1.docker.io`, `registry.docker.io`, `auth.docker.io`, `index.docker.io`, `hub.docker.com`, `docker.io`
  - Google: `gcr.io`, `asia.gcr.io`, `eu.gcr.io`, `us.gcr.io`, `marketplace.gcr.io`, `registry.cloud.google.com`
  - Microsoft: `mcr.microsoft.com`
  - Quay: `quay.io`, `quay-registry.s3.amazonaws.com`
  - Kubernetes: `registry.k8s.io`
- Git repositories:
  - GitHub: `github.com`, `api.github.com`, `raw.githubusercontent.com`, `github-releases.githubusercontent.com`, `codeload.github.com`, `ghcr.io`, `packages.github.com`
  - GitLab: `gitlab.com`, `registry.gitlab.com`
  - Bitbucket: `bitbucket.org`
- System package managers:
  - Ubuntu: `archive.ubuntu.com`, `security.ubuntu.com`
  - Debian: `deb.debian.org`, `security.debian.org`, `cdn-fastly.deb.debian.org`, `ftp.debian.org`
- CDN services:
  - Cloudflare: `cloudflare.com`
  - Fastly: `fastly.com`
  - JavaScript CDNs: `unpkg.com`, `jsdelivr.net`
- AI/ML services:
  - Anthropic: `api.anthropic.com`
- Platform services:
  - Daytona: `app.daytona.io`


## Getting Help

If you encounter network access issues or need unrestricted network access

1. Check your **organization tier** in the [Dashboard](https://app.daytona.io/dashboard/limits)
2. Upgrade your **organization tier** by completing the required verification steps to unlock higher limits tiers automatically
3. Verify your **network allow list** configuration
4. Contact support at [support@daytona.io](mailto:support@daytona.io) for assistance

Organizations in Daytona are used to group resources and enable collaboration. Users can work individually in their Personal Organization or together in a Collaborative Organization.

### Personal vs Collaborative Organizations

Every Daytona user starts with a **Personal Organization**, ideal for solo use and experimentation. **Collaborative Organizations** are created manually and designed for company-wide collaboration with shared access and controls.

| Feature            | Personal Organization            | Collaborative Organization                     |
| ------------------ | -------------------------------- | ---------------------------------------------- |
| **Creation**       | Automatic on signup              | Manually by a user                             |
| **Members**        | Single user only                 | Multiple users (invite-based)                  |
| **Access Control** | No roles or permissions          | Roles with granular resource-based Assignments |
| **Billing**        | Tied to individual user          | Shared across team members                     |
| **Use Case**       | Personal testing, small projects | Company/team development and production        |
| **Quota Scope**    | Per user                         | Shared across all members                      |
| **Deletable**      | ❌ No                            | ✅ Yes (by Owner)                              |

Users can switch between their Personal and Collaborative Organizations using the dropdown in the sidebar. Each Organization has its own sandboxes, API keys, and resource quotas.

## Managing Members

### Organization Roles

Users within an Organization can have one of two different Roles:
- **Owners** have full
administrative access to the Organization and its resources. Organization Owners can perform administrative actions such as:
- **Members** have no administrative access
to the Organization, while their access to Organization resources is based on [**Assignments**](#available-assignments).

### Administrative Actions

Organization Owners can perform administrative actions such as:

- [Invite new users to the Organization](#inviting-new-users)
- [Manage pending invitations](#managing-invitations)
- Change [Role](#organization-roles) of a user in the Organization
- Update [Assignments](#available-assignments) for an Organization Member
- Remove user from the Organization
- Inspect audit logs
- [Delete Organization](#organization-settings)

### Inviting New Users

As an Organization **Owner**, to invite a new user to your Organization:

1. Navigate to the _Members page_.
2. Click on _Invite Member_.
3. Enter the email address of the user you want to invite.
4. Choose a [Role](#organization-roles) for the new user. If you select the `Member` role, define their [Assignments](#available-assignments).

### Available Assignments

The list of available **Assignments** includes:

| Assignment              | Description                                                         |
| ----------------------- | ------------------------------------------------------------------- |
| **`Viewer (required)`** | Grants read access to all resources in the organization             |
| **`Developer`**         | Grants the ability to create sandboxes and keys in the organization |
| **`Sandboxes Admin`**   | Grants admin access to sandboxes in the organization                |
| **`Snapshots Admin`**   | Grants admin access to snapshots in the organization                |
| **`Registries Admin`**  | Grants admin access to registries in the organization               |
| **`Volumes Admin`**     | Grants admin access to volumes in the organization                  |
| **`Super Admin`**       | Grants full access to all resources in the organization             |
| **`Auditor`**           | Grants access to audit logs in the organization                     |

### Managing Invitations

To view their pending invitations to join other Organizations, users can navigate to the _Invitations
page_ by expanding the dropdown at the bottom of the sidebar, and clicking on _Invitations_. Once a user
accepts an invitation to join an Organization, they get access to resource quotas assigned to that
Organization and they may proceed by issuing a new [API key](https://www.daytona.io/docs/en/api-keys.md) and creating sandboxes.

## Organization Settings

The [Settings](https://app.daytona.io/dashboard/settings) subpage in the Dashboard allows you to view the Organization ID and Name and to delete the Organization if you don't need it anymore. This action is irreversible, so please proceed with caution. Personal Organizations are there by default and cannot be deleted.

This guide will walk you through running Daytona Open Source locally using Docker Compose.

The compose file can be found in the [docker](https://github.com/daytonaio/daytona/tree/main/docker) folder of the Daytona repository.

:::caution

- This setup is still in development and is **not safe to use in production**
- A separate deployment guide will be provided for production scenarios
  :::

## Overview

The Docker Compose configuration includes all the necessary services to run Daytona:

- **API**: Main Daytona application server
- **Proxy**: Request proxy service
- **Runner**: Service that hosts the Daytona Runner
- **SSH Gateway**: Service that handles sandbox SSH access
- **Database**: PostgreSQL database for data persistence
- **Redis**: In-memory data store for caching and sessions
- **Dex**: OIDC authentication provider
- **Registry**: Docker image registry with web UI
- **MinIO**: S3-compatible object storage
- **MailDev**: Email testing service
- **Jaeger**: Distributed tracing
- **PgAdmin**: Database administration interface

## Quick Start

1. Clone the [Daytona repository](https://github.com/daytonaio/daytona)
2. [Install Docker and Docker Compose](https://docs.docker.com/get-docker/)
3. Run the following command (from the root of the Daytona repo) to start all services:

   ```bash
   docker compose -f docker/docker-compose.yaml up -d
   ```

4. Access the services:
   - Daytona Dashboard: http://localhost:3000
     - Access Credentials: dev@daytona.io `password`
     - Make sure that the default snapshot is active at http://localhost:3000/dashboard/snapshots
   - PgAdmin: http://localhost:5050
   - Registry UI: http://localhost:5100
   - MinIO Console: http://localhost:9001 (minioadmin / minioadmin)

## DNS Setup for Proxy URLs

For local development, you need to resolve `*.proxy.localhost` domains to `127.0.0.1`:

```bash
./scripts/setup-proxy-dns.sh
```

This configures dnsmasq with `address=/proxy.localhost/127.0.0.1`.

**Without this setup**, SDK examples and direct proxy access won't work.

## Development Notes

- The setup uses shared networking for simplified service communication
- Database and storage data is persisted in Docker volumes
- The registry is configured to allow image deletion for testing
- Sandbox resource limits are disabled due to inability to partition cgroups in DinD environment where the sock is not mounted

## Additional Network Options

### HTTP Proxy

To configurate an outbound HTTP proxy for the Daytona services, you can set the following environment variables in the `docker-compose.yaml` file for each service that requires proxy access (the API service is the only that requires outbound access to pull images):

- `HTTP_PROXY`: URL of the HTTP proxy server
- `HTTPS_PROXY`: URL of the HTTPS proxy server
- `NO_PROXY`: Comma-separated list of hostnames or IP addresses that should bypass the proxy

The baseline configuration for the API service should be as follows:

```yaml
environment:
  - HTTP_PROXY=<your-proxy>
  - HTTPS_PROXY=<your-proxy>
  - NO_PROXY=localhost,runner,dex,registry,minio,jaeger,otel-collector,<your-proxy>
```

### Extra CA Certificates

To configure extra CA certificates (for example, paired with `DB_TLS` env vars), set the following environment variable in the API service:

```yaml
environment:
  - NODE_EXTRA_CA_CERTS=/path/to/your/cert-bundle.pembundle
```

The provided file is a cert bundle. Meaning it can contain multiple CA certificates in PEM format.

## Environment Variables

You can customize the deployment by modifying environment variables in the `docker-compose.yaml` file.
Below is a full list of environment variables with their default values:

### API Service

| Variable                                   | Type    | Default Value                                        | Description                                                                                          |
| ------------------------------------------ | ------- | ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `PORT`                                     | number  | `3000`                                               | API service port                                                                                     |
| `DB_HOST`                                  | string  | `db`                                                 | PostgreSQL database hostname                                                                         |
| `DB_PORT`                                  | number  | `5432`                                               | PostgreSQL database port                                                                             |
| `DB_USERNAME`                              | string  | `user`                                               | PostgreSQL database username                                                                         |
| `DB_PASSWORD`                              | string  | `pass`                                               | PostgreSQL database password                                                                         |
| `DB_DATABASE`                              | string  | `daytona`                                            | PostgreSQL database name                                                                             |
| `DB_TLS_ENABLED`                           | boolean | `false`                                              | Enable TLS for database connection                                                                   |
| `DB_TLS_REJECT_UNAUTHORIZED`               | boolean | `true`                                               | Reject unauthorized TLS certificates                                                                 |
| `REDIS_HOST`                               | string  | `redis`                                              | Redis server hostname                                                                                |
| `REDIS_PORT`                               | number  | `6379`                                               | Redis server port                                                                                    |
| `OIDC_CLIENT_ID`                           | string  | `daytona`                                            | OIDC client identifier                                                                               |
| `OIDC_ISSUER_BASE_URL`                     | string  | `http://dex:5556/dex`                                | OIDC issuer base URL                                                                                 |
| `PUBLIC_OIDC_DOMAIN`                       | string  | `http://localhost:5556/dex`                          | Public OIDC domain                                                                                   |
| `OIDC_AUDIENCE`                            | string  | `daytona`                                            | OIDC audience identifier                                                                             |
| `OIDC_MANAGEMENT_API_ENABLED`              | boolean | (empty)                                              | Enable OIDC management API                                                                           |
| `OIDC_MANAGEMENT_API_CLIENT_ID`            | string  | (empty)                                              | OIDC management API client ID                                                                        |
| `OIDC_MANAGEMENT_API_CLIENT_SECRET`        | string  | (empty)                                              | OIDC management API client secret                                                                    |
| `OIDC_MANAGEMENT_API_AUDIENCE`             | string  | (empty)                                              | OIDC management API audience                                                                         |
| `DEFAULT_SNAPSHOT`                         | string  | `daytonaio/sandbox:0.4.3`                            | Default sandbox snapshot image                                                                       |
| `DASHBOARD_URL`                            | string  | `http://localhost:3000/dashboard`                    | Dashboard URL                                                                                        |
| `DASHBOARD_BASE_API_URL`                   | string  | `http://localhost:3000`                              | Dashboard base API URL                                                                               |
| `POSTHOG_API_KEY`                          | string  | `phc_bYtEsdMDrNLydXPD4tufkBrHKgfO2zbycM30LOowYNv`    | PostHog API key for analytics                                                                        |
| `POSTHOG_HOST`                             | string  | `https://d18ag4dodbta3l.cloudfront.net`              | PostHog host URL                                                                                     |
| `POSTHOG_ENVIRONMENT`                      | string  | `local`                                              | PostHog environment identifier                                                                       |
| `TRANSIENT_REGISTRY_URL`                   | string  | `http://registry:6000`                               | Transient registry URL                                                                               |
| `TRANSIENT_REGISTRY_ADMIN`                 | string  | `admin`                                              | Transient registry admin username                                                                    |
| `TRANSIENT_REGISTRY_PASSWORD`              | string  | `password`                                           | Transient registry admin password                                                                    |
| `TRANSIENT_REGISTRY_PROJECT_ID`            | string  | `daytona`                                            | Transient registry project ID                                                                        |
| `INTERNAL_REGISTRY_URL`                    | string  | `http://registry:6000`                               | Internal registry URL                                                                                |
| `INTERNAL_REGISTRY_ADMIN`                  | string  | `admin`                                              | Internal registry admin username                                                                     |
| `INTERNAL_REGISTRY_PASSWORD`               | string  | `password`                                           | Internal registry admin password                                                                     |
| `INTERNAL_REGISTRY_PROJECT_ID`             | string  | `daytona`                                            | Internal registry project ID                                                                         |
| `SMTP_HOST`                                | string  | `maildev`                                            | SMTP server hostname                                                                                 |
| `SMTP_PORT`                                | number  | `1025`                                               | SMTP server port                                                                                     |
| `SMTP_USER`                                | string  | (empty)                                              | SMTP username                                                                                        |
| `SMTP_PASSWORD`                            | string  | (empty)                                              | SMTP password                                                                                        |
| `SMTP_SECURE`                              | boolean | (empty)                                              | Enable SMTP secure connection                                                                        |
| `SMTP_EMAIL_FROM`                          | string  | `"Daytona Team <no-reply@daytona.io>"`               | SMTP sender email address                                                                            |
| `S3_ENDPOINT`                              | string  | `http://minio:9000`                                  | S3-compatible storage endpoint                                                                       |
| `S3_STS_ENDPOINT`                          | string  | `http://minio:9000/minio/v1/assume-role`             | S3 STS endpoint                                                                                      |
| `S3_REGION`                                | string  | `us-east-1`                                          | S3 region                                                                                            |
| `S3_ACCESS_KEY`                            | string  | `minioadmin`                                         | S3 access key                                                                                        |
| `S3_SECRET_KEY`                            | string  | `minioadmin`                                         | S3 secret key                                                                                        |
| `S3_DEFAULT_BUCKET`                        | string  | `daytona`                                            | S3 default bucket name                                                                               |
| `S3_ACCOUNT_ID`                            | string  | `/`                                                  | S3 account ID                                                                                        |
| `S3_ROLE_NAME`                             | string  | `/`                                                  | S3 role name                                                                                         |
| `ENVIRONMENT`                              | string  | `dev`                                                | Application environment                                                                              |
| `MAX_AUTO_ARCHIVE_INTERVAL`                | number  | `43200`                                              | Maximum auto-archive interval (seconds)                                                              |
| `OTEL_ENABLED`                             | boolean | `true`                                               | Enable OpenTelemetry tracing                                                                         |
| `OTEL_COLLECTOR_URL`                       | string  | `http://jaeger:4318/v1/traces`                       | OpenTelemetry collector URL                                                                          |
| `MAINTENANCE_MODE`                         | boolean | `false`                                              | Enable maintenance mode                                                                              |
| `PROXY_DOMAIN`                             | string  | `proxy.localhost:4000`                               | Proxy domain                                                                                         |
| `PROXY_PROTOCOL`                           | string  | `http`                                               | Proxy protocol                                                                                       |
| `PROXY_API_KEY`                            | string  | `super_secret_key`                                   | Proxy API key                                                                                        |
| `PROXY_TEMPLATE_URL`                       | string  | `http://{{PORT}}-{{sandboxId}}.proxy.localhost:4000` | Proxy template URL pattern                                                                           |
| `PROXY_TOOLBOX_BASE_URL`                   | string  | `{PROXY_PROTOCOL}://{PROXY_DOMAIN}`                  | Proxy base URL for toolbox requests                                                                  |
| `DEFAULT_RUNNER_DOMAIN`                    | string  | `runner:3003`                                        | Default runner domain                                                                                |
| `DEFAULT_RUNNER_API_URL`                   | string  | `http://runner:3003`                                 | Default runner API URL                                                                               |
| `DEFAULT_RUNNER_PROXY_URL`                 | string  | `http://runner:3003`                                 | Default runner proxy URL                                                                             |
| `DEFAULT_RUNNER_API_KEY`                   | string  | `secret_api_token`                                   | Default runner API key                                                                               |
| `DEFAULT_RUNNER_CPU`                       | number  | `4`                                                  | Default runner CPU allocation                                                                        |
| `DEFAULT_RUNNER_MEMORY`                    | number  | `8`                                                  | Default runner memory allocation (GB)                                                                |
| `DEFAULT_RUNNER_DISK`                      | number  | `50`                                                 | Default runner disk allocation (GB)                                                                  |
| `DEFAULT_RUNNER_GPU`                       | number  | `0`                                                  | Default runner GPU allocation                                                                        |
| `DEFAULT_RUNNER_GPU_TYPE`                  | string  | `none`                                               | Default runner GPU type                                                                              |
| `DEFAULT_RUNNER_CAPACITY`                  | number  | `100`                                                | Default runner capacity                                                                              |
| `DEFAULT_RUNNER_REGION`                    | string  | `us`                                                 | Default runner region                                                                                |
| `DEFAULT_RUNNER_CLASS`                     | string  | `small`                                              | Default runner class                                                                                 |
| `DEFAULT_ORG_QUOTA_TOTAL_CPU_QUOTA`        | number  | `10000`                                              | Default organization total CPU quota                                                                 |
| `DEFAULT_ORG_QUOTA_TOTAL_MEMORY_QUOTA`     | number  | `10000`                                              | Default organization total memory quota                                                              |
| `DEFAULT_ORG_QUOTA_TOTAL_DISK_QUOTA`       | number  | `100000`                                             | Default organization total disk quota                                                                |
| `DEFAULT_ORG_QUOTA_MAX_CPU_PER_SANDBOX`    | number  | `100`                                                | Default organization max CPU per sandbox                                                             |
| `DEFAULT_ORG_QUOTA_MAX_MEMORY_PER_SANDBOX` | number  | `100`                                                | Default organization max memory per sandbox                                                          |
| `DEFAULT_ORG_QUOTA_MAX_DISK_PER_SANDBOX`   | number  | `1000`                                               | Default organization max disk per sandbox                                                            |
| `DEFAULT_ORG_QUOTA_SNAPSHOT_QUOTA`         | number  | `1000`                                               | Default organization snapshot quota                                                                  |
| `DEFAULT_ORG_QUOTA_MAX_SNAPSHOT_SIZE`      | number  | `1000`                                               | Default organization max snapshot size                                                               |
| `DEFAULT_ORG_QUOTA_VOLUME_QUOTA`           | number  | `10000`                                              | Default organization volume quota                                                                    |
| `SSH_GATEWAY_API_KEY`                      | string  | `ssh_secret_api_token`                               | SSH gateway API key                                                                                  |
| `SSH_GATEWAY_COMMAND`                      | string  | `ssh -p 2222 {{TOKEN}}@localhost`                    | SSH gateway command template                                                                         |
| `RUNNER_DECLARATIVE_BUILD_SCORE_THRESHOLD` | number  | `10`                                                 | Runner declarative build score threshold                                                             |
| `RUNNER_AVAILABILITY_SCORE_THRESHOLD`      | number  | `10`                                                 | Runner availability score threshold                                                                  |
| `RUN_MIGRATIONS`                           | boolean | `true`                                               | Enable database migrations on startup                                                                |
| `ADMIN_API_KEY`                            | string  | (empty)                                              | Admin API key, auto-generated if empty, used only upon initial setup, not recommended for production |
| `ADMIN_TOTAL_CPU_QUOTA`                    | number  | `0`                                                  | Admin total CPU quota, used only upon initial setup                                                  |
| `ADMIN_TOTAL_MEMORY_QUOTA`                 | number  | `0`                                                  | Admin total memory quota, used only upon initial setup                                               |
| `ADMIN_TOTAL_DISK_QUOTA`                   | number  | `0`                                                  | Admin total disk quota, used only upon initial setup                                                 |
| `ADMIN_MAX_CPU_PER_SANDBOX`                | number  | `0`                                                  | Admin max CPU per sandbox, used only upon initial setup                                              |
| `ADMIN_MAX_MEMORY_PER_SANDBOX`             | number  | `0`                                                  | Admin max memory per sandbox, used only upon initial setup                                           |
| `ADMIN_MAX_DISK_PER_SANDBOX`               | number  | `0`                                                  | Admin max disk per sandbox, used only upon initial setup                                             |
| `ADMIN_SNAPSHOT_QUOTA`                     | number  | `100`                                                | Admin snapshot quota, used only upon initial setup                                                   |
| `ADMIN_MAX_SNAPSHOT_SIZE`                  | number  | `100`                                                | Admin max snapshot size, used only upon initial setup                                                |
| `ADMIN_VOLUME_QUOTA`                       | number  | `0`                                                  | Admin volume quota, used only upon initial setup                                                     |
| `SKIP_USER_EMAIL_VERIFICATION`             | boolean | `true`                                               | Skip user email verification process                                                                 |

### Runner

| Variable                   | Type    | Default Value                     | Description                           |
| -------------------------- | ------- | --------------------------------- | ------------------------------------- |
| `VERSION`                  | string  | `0.0.1`                           | Runner service version                |
| `ENVIRONMENT`              | string  | `development`                     | Application environment               |
| `API_PORT`                 | number  | `3003`                            | Runner API service port               |
| `API_TOKEN`                | string  | `secret_api_token`                | Runner API authentication token       |
| `LOG_FILE_PATH`            | string  | `/home/daytona/runner/runner.log` | Path to runner log file               |
| `RESOURCE_LIMITS_DISABLED` | boolean | `true`                            | Disable resource limits for sandboxes |
| `AWS_ENDPOINT_URL`         | string  | `http://minio:9000`               | AWS S3-compatible storage endpoint    |
| `AWS_REGION`               | string  | `us-east-1`                       | AWS region                            |
| `AWS_ACCESS_KEY_ID`        | string  | `minioadmin`                      | AWS access key ID                     |
| `AWS_SECRET_ACCESS_KEY`    | string  | `minioadmin`                      | AWS secret access key                 |
| `AWS_DEFAULT_BUCKET`       | string  | `daytona`                         | AWS default bucket name               |
| `SERVER_URL`               | string  | `http://api:3000/api`             | Daytona API server URL                |

### SSH Gateway

| Variable           | Type   | Default Value                        | Description                |
| ------------------ | ------ | ------------------------------------ | -------------------------- |
| `API_URL`          | string | `http://api:3000/api`                | Daytona API URL            |
| `API_KEY`          | string | `ssh_secret_api_token`               | API authentication key     |
| `SSH_PRIVATE_KEY`  | string | (Base64-encoded OpenSSH private key) | SSH private key for auth   |
| `SSH_HOST_KEY`     | string | (Base64-encoded OpenSSH host key)    | SSH host key for server    |
| `SSH_GATEWAY_PORT` | number | `2222`                               | SSH gateway listening port |

### Proxy

| Variable             | Type    | Default Value               | Description                    |
| -------------------- | ------- | --------------------------- | ------------------------------ |
| `DAYTONA_API_URL`    | string  | `http://api:3000/api`       | Daytona API URL                |
| `PROXY_PORT`         | number  | `4000`                      | Proxy service port             |
| `PROXY_DOMAIN`       | string  | `proxy.localhost:4000`      | Proxy domain                   |
| `PROXY_API_KEY`      | string  | `super_secret_key`          | Proxy API authentication key   |
| `PROXY_PROTOCOL`     | string  | `http`                      | Proxy protocol (http or https) |
| `OIDC_CLIENT_ID`     | string  | `daytona`                   | OIDC client identifier         |
| `OIDC_CLIENT_SECRET` | string  | (empty)                     | OIDC client secret             |
| `OIDC_DOMAIN`        | string  | `http://dex:5556/dex`       | OIDC domain                    |
| `OIDC_PUBLIC_DOMAIN` | string  | `http://localhost:5556/dex` | OIDC public domain             |
| `OIDC_AUDIENCE`      | string  | `daytona`                   | OIDC audience identifier       |
| `REDIS_HOST`         | string  | `redis`                     | Redis server hostname          |
| `REDIS_PORT`         | number  | `6379`                      | Redis server port              |
| `TOOLBOX_ONLY_MODE`  | boolean | `false`                     | Allow only toolbox requests    |

## [OPTIONAL] Configure Auth0 for Authentication

The default compose setup uses a local Dex OIDC provider for authentication. However, you can configure Auth0 as an alternative OIDC provider by following these steps:

### Step 1: Create Your Auth0 Tenant

Begin by navigating to https://auth0.com/signup and start the signup process. Choose your account type based on your use case - select `Company` for business applications or `Personal` for individual projects.\
On the "Let's get setup" page, you'll need to enter your application name such as `My Daytona` and select `Single Page Application (SPA)` as the application type. For authentication methods, you can start with `Email and Password` since additional social providers like Google, GitHub, or Facebook can be added later. Once you've configured these settings, click `Create Application` in the bottom right corner.

### Step 2: Configure Your Single Page Application

Navigate to `Applications` > `Applications` in the left sidebar and select the application you just created. Click the `Settings` tab and scroll down to find the `Application URIs` section where you'll configure the callback and origin URLs.
In the `Allowed Callback URIs` field, add the following URLs:

```
http://localhost:3000
http://localhost:3000/api/oauth2-redirect.html
http://localhost:4000/callback
http://proxy.localhost:4000/callback
```

For `Allowed Logout URIs`, add:

```
http://localhost:3000
```

And for `Allowed Web Origins`, add:

```
http://localhost:3000
```

Remember to click `Save Changes` at the bottom of the page to apply these configurations.

### Step 3: Create Machine-to-Machine Application

You'll need a Machine-to-Machine application to interact with Auth0's Management API. Go to `Applications` > `Applications` and click `Create Application`. Choose `Machine to Machine Applications` as the type and provide a descriptive name like `My Management API M2M`.
After creating the application, navigate to the `APIs` tab within your new M2M application. Find and authorize the `Auth0 Management API` by clicking the toggle or authorize button.\
Once authorized, click the dropdown arrow next to the Management API to configure permissions. Grant the following permissions to your M2M application:

```
read:users
update:users
read:connections
create:guardian_enrollment_tickets
read:connections_options
```

Click `Save` to apply these permission changes.

### Step 4: Set Up Custom API

Your Daytona application will need a custom API to handle authentication and authorization. Navigate to `Applications` > `APIs` in the left sidebar and click `Create API`. Enter a descriptive name such as `My Daytona API` and provide an identifier like `my-daytona-api`. The identifier should be a unique string that will be used in your application configuration.\
After creating the API, go to the `Permissions` tab to define the scopes your application will use. Add each of the following permissions with their corresponding descriptions:

| Permission                  | Description                              |
| --------------------------- | ---------------------------------------- |
| `read:node`                 | Get workspace node info                  |
| `create:node`               | Create new workspace node record         |
| `create:user`               | Create user account                      |
| `read:users`                | Get all user accounts                    |
| `regenerate-key-pair:users` | Regenerate user SSH key-pair             |
| `read:workspaces`           | Read workspaces (user scope)             |
| `create:registry`           | Create a new docker registry auth record |
| `read:registries`           | Get all docker registry records          |
| `read:registry`             | Get docker registry record               |
| `write:registry`            | Create or update docker registry record  |

### Step 5: Configure Environment Variables

Once you've completed all the Auth0 setup steps, you'll need to configure environment variables in your Daytona deployment. These variables connect your application to the Auth0 services you've just configured.

#### Finding Your Configuration Values

You can find the necessary values in the Auth0 dashboard. For your SPA application settings, go to `Applications` > `Applications`, select your SPA app, and click the `Settings` tab. For your M2M application, follow the same path but select your Machine-to-Machine app instead. Custom API settings are located under `Applications` > `APIs`, then select your custom API and go to `Settings`.

#### API Service Configuration

Configure the following environment variables for your API service:

```bash
OIDC_CLIENT_ID=your_spa_app_client_id
OIDC_ISSUER_BASE_URL=your_spa_app_domain
OIDC_AUDIENCE=your_custom_api_identifier
OIDC_MANAGEMENT_API_ENABLED=true
OIDC_MANAGEMENT_API_CLIENT_ID=your_m2m_app_client_id
OIDC_MANAGEMENT_API_CLIENT_SECRET=your_m2m_app_client_secret
OIDC_MANAGEMENT_API_AUDIENCE=your_auth0_managment_api_identifier
```

#### Proxy Service Configuration

For your proxy service, configure these environment variables:

```bash
OIDC_CLIENT_ID=your_spa_app_client_id
OIDC_CLIENT_SECRET=
OIDC_DOMAIN=your_spa_app_domain
OIDC_AUDIENCE=your_custom_api_identifier (with trailing slash)
```

Note that `OIDC_CLIENT_SECRET` should remain empty for your proxy environment.

The Daytona SDK provides a method to generate preview links for Sandboxes. A preview link's schema consists of the port and Sandbox ID (e.g.
`https://3000-sandboxid.proxy.daytona.works`).

Any process listening for HTTP traffic on ports 3000–9999 can be previewed.

## Fetching a Preview Link

To fetch the preview link and the authorization token for a specific port, you can simply use the SDK method:

```python

preview_info = sandbox.get_preview_link(3000)

print(f"Preview link url: {preview_info.url}")
print(f"Preview link token: {preview_info.token}")

```

```typescript

const previewInfo = await sandbox.getPreviewUrl(3000);

console.log(`Preview link url: ${previewInfo.url}`);
console.log(`Preview link token: ${previewInfo.token}`);

```


:::tip
If you want to serve the previews under your own domain instead of using Daytona's URLs, check out the [Custom Domain/Authentication](https://www.daytona.io/docs/en/custom-domain-authentication.md) section.
:::

See: [get_preview_link (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/sandbox.md#sandboxget_preview_link), [getPreviewLink (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/sandbox.md#getpreviewlink)

## Authentication

If the Sandbox has its `public` property set to `true`, these links will be publicly accessible, otherwise the preview link will be available only to the Sandbox Organization users.

For programmatic access, use the authorization token to access the preview URL:

```bash
curl -H "x-daytona-preview-token: vg5c0ylmcimr8b_v1ne0u6mdnvit6gc0" \
https://3000-sandbox-123456.proxy.daytona.work
```

## Warning Page

When opening the preview link in a browser, a warning page will be shown for the first time.
This warning serves as a security measure to inform users about the potential risks of visiting the preview URL.

The warning page will only be shown when loading the preview link in a browser.

To avoid this warning you can do one of the following:

- Send the `X-Daytona-Skip-Preview-Warning: true` header
- Upgrade to [Tier 3](https://www.daytona.io/docs/en/limits.md)
- Deploy your own [custom preview proxy](https://www.daytona.io/docs/en/custom-domain-authentication.md)

The Daytona SDK provides powerful process and code execution capabilities through the `process` module in Sandboxes. This guide covers all available process operations and best practices.

## Code Execution

Daytona SDK provides an option to execute code in Python and TypeScript.

### Running Code

Daytona SDK provides an option to run code snippets in Python and TypeScript. You can execute code with input, timeout, and environment variables.

```python
# Run Python code
response = sandbox.process.code_run('''
def greet(name):
    return f"Hello, {name}!"

print(greet("Daytona"))
''')

print(response.result)

```
```typescript
// Run TypeScript code
let response = await sandbox.process.codeRun(`
function greet(name: string): string {
    return \`Hello, \${name}!\`;
}

console.log(greet("Daytona"));
`);
console.log(response.result);

// Run code with argv and environment variables
response = await sandbox.process.codeRun(
    `
    console.log(\`Hello, \${process.argv[2]}!\`);
    console.log(\`FOO: \${process.env.FOO}\`);
    `,
    { 
      argv: ["Daytona"],
      env: { FOO: "BAR" }
    }
);
console.log(response.result);

// Run code with timeout
response = await sandbox.process.codeRun(
    'setTimeout(() => console.log("Done"), 2000);',
    undefined,
    5000
);
console.log(response.result);
```


See: [code_run (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/process.md#processcode_run), [codeRun (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/process.md#coderun)

## Process Execution

Daytona SDK provides an option to execute shell commands and manage background processes in Sandboxes. The workDir for executing defaults to the current Sandbox working directory. Uses the WORKDIR specified in
the Dockerfile if present, or falling back to the user's home directory if not - e.g. `workspace/repo` implies `/my-work-dir/workspace/repo`, but you can override it with an absolute path (by starting the path with `/`).

### Running Commands

Daytona SDK provides an option to execute shell commands in Python and TypeScript. You can run commands with input, timeout, and environment variables.

```python
# Execute any shell command
response = sandbox.process.exec("ls -la")
print(response.result)

# Setting a working directory and a timeout

response = sandbox.process.exec("sleep 3", cwd="workspace/src", timeout=5)
print(response.result)

# Passing environment variables

response = sandbox.process.exec("echo $CUSTOM_SECRET", env={
        "CUSTOM_SECRET": "DAYTONA"
    }
)
print(response.result)

```
```typescript

// Execute any shell command
const response = await sandbox.process.executeCommand("ls -la");
console.log(response.result);

// Setting a working directory and a timeout
const response2 = await sandbox.process.executeCommand("sleep 3", "workspace/src", undefined, 5);
console.log(response2.result);

// Passing environment variables
const response3 = await sandbox.process.executeCommand("echo $CUSTOM_SECRET", ".", {
        "CUSTOM_SECRET": "DAYTONA"
    }
);
console.log(response3.result);

```


See: [exec (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/process.md#processexec), [executeCommand (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/process.md#executecommand)

## Sessions (Background Processes)

Daytona SDK provides an option to start, stop, and manage background process sessions in Sandboxes. You can run long-running commands, monitor process status, and list all running processes.

### Managing Long-Running Processes

Daytona SDK provides an option to start and stop background processes. You can run long-running commands and monitor process status.

```python
# Check session's executed commands
session = sandbox.process.get_session(session_id)
print(f"Session {process_id}:")
for command in session.commands:
    print(f"Command: {command.command}, Exit Code: {command.exit_code}")

# List all running sessions

sessions = sandbox.process.list_sessions()
for session in sessions:
    print(f"PID: {session.id}, Commands: {session.commands}")

```
```typescript
// Check session's executed commands
const session = await sandbox.process.getSession(sessionId);
console.log(`Session ${sessionId}:`);
for (const command of session.commands) {
    console.log(`Command: ${command.command}, Exit Code: ${command.exitCode}`);
}

// List all running sessions
const sessions = await sandbox.process.listSessions();
for (const session of sessions) {
    console.log(`PID: ${session.id}, Commands: ${session.commands}`);
}

```


See: [get_session (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/process.md#processget_session), [list_sessions (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/process.md#processlist_sessions), [getSession (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/process.md#getsession), [listSessions (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/process.md#listsessions)

## Best Practices

Use the following best practices when working with process and code execution in Daytona SDK.

### Resource Management

The following best practices apply to managing resources when executing processes:

1. Use [sessions](#sessions-background-processes) for long-running operations
2. Clean up sessions after execution
3. Handle session exceptions properly

   ```python
   # Python - Clean up session
   session_id = "long-running-cmd"
   try:
       sandbox.process.create_session(session_id)
       session = sandbox.process.get_session(session_id)
       # Do work...
   finally:
       sandbox.process.delete_session(session.session_id)
   ```
   ```typescript
   // TypeScript - Clean up session
   const sessionId = "long-running-cmd";
   try {
       await sandbox.process.createSession(sessionId);
       const session = await sandbox.process.getSession(sessionId);
       // Do work...
   } finally {
       await sandbox.process.deleteSession(session.sessionId);
   }
   ```

See: [create_session (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/process.md#processcreate_session), [delete_session (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/process.md#processdelete_session), [createSession (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/process.md#createsession), [deleteSession (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/process.md#deletesession)

### Error Handling

The following best practices apply to error handling when executing processes:

- Handle process exceptions properly
- Log error details for debugging
- Use try-catch blocks for error handling

```python
try:
    response = sandbox.process.code_run("invalid python code")
except ProcessExecutionError as e:
    print(f"Execution failed: {e}")
    print(f"Exit code: {e.exit_code}")
    print(f"Error output: {e.stderr}")
```
```typescript
try {
    const response = await sandbox.process.codeRun("invalid typescript code");
} catch (e) {
    if (e instanceof ProcessExecutionError) {
        console.error("Execution failed:", e);
        console.error("Exit code:", e.exitCode);
        console.error("Error output:", e.stderr);
    }
}
```

## Common Issues

To troubleshoot common issues related to process and code execution, refer to the following table:

| Issue | Solutions |
|-------|-----------|
| `Process Execution Failed` | • Check command syntax<br/>• Verify required dependencies<br/>• Ensure sufficient permissions |
| `Process Timeout` | • Adjust timeout settings<br/>• Optimize long-running operations<br/>• Consider using background processes |
| `Resource Limits` | • Monitor process memory usage<br/>• Handle process cleanup properly<br/>• Use appropriate resource constraints |

The Daytona SDK provides powerful pseudo terminal (PTY) capabilities through the `process` module in Sandboxes. PTY sessions allow you to create interactive terminal sessions that can execute commands, handle user input, and manage terminal operations.

## What is PTY?

A PTY (Pseudo Terminal) is a virtual terminal interface that allows programs to interact with a shell as if they were connected to a real terminal. PTY sessions in Daytona enable:

- Interactive command execution with real-time input/output
- Terminal resizing capabilities
- Process management with kill operations
- Real-time data streaming from terminal sessions

## Interactive Commands with PTY

PTY sessions excel at handling interactive commands that require user input and can be resized during execution.

```python
import time
from daytona import Daytona, Sandbox
from daytona.common.pty import PtySize

def handle_pty_data(data: bytes):
text = data.decode("utf-8", errors="replace")
print(text, end="")

# Create PTY session

pty_handle = sandbox.process.create_pty_session(
id="interactive-session",
pty_size=PtySize(cols=300, rows=100)
)

# Send interactive command

pty_handle.send_input('printf "Are you accepting the terms and conditions? (y/n): " && read confirm && if [ "$confirm" = "y" ]; then echo "You accepted"; else echo "You did not accept"; fi\n')
time.sleep(1)
pty_handle.send_input("y\n")

# Resize terminal

pty_session_info = pty_handle.resize(PtySize(cols=210, rows=110))
print(f"PTY session resized to {pty_session_info.cols}x{pty_session_info.rows}")

# Exit the session

pty_handle.send_input('exit\n')

# Handle output using iterator

for data in pty_handle:
handle_pty_data(data)

print(f"Session completed with exit code: {pty_handle.exit_code}")

````
```typescript
import { Daytona, Sandbox } from '@daytonaio/sdk'

// Create PTY session
const ptyHandle = await sandbox.process.createPty({
  id: 'interactive-session',
  cols: 300,
  rows: 100,
  onData: (data) => {
    const text = new TextDecoder().decode(data)
    process.stdout.write(text)
  },
})

await ptyHandle.waitForConnection()

// Send interactive command
await ptyHandle.sendInput('printf "Are you accepting the terms and conditions? (y/n): " && read confirm && if [ "$confirm" = "y" ]; then echo "You accepted"; else echo "You did not accept"; fi\n')
await new Promise(resolve => setTimeout(resolve, 1000))
await ptyHandle.sendInput('y\n')

// Resize terminal
const ptySessionInfo = await sandbox.process.resizePtySession(ptySessionId, 210, 110)
console.log(`\nPTY session resized to ${ptySessionInfo.cols}x${ptySessionInfo.rows}`)

// Exit the session
await ptyHandle.sendInput('exit\n')

// Wait for completion
const result = await ptyHandle.wait()
console.log(`Session completed with exit code: ${result.exitCode}`)
````


## Long-Running Processes with PTY

PTY sessions are perfect for managing long-running processes that need to be monitored or terminated.

```python
import time
from daytona import Daytona, Sandbox
from daytona.common.pty import PtySize

def handle_pty_data(data: bytes):
text = data.decode("utf-8", errors="replace")
print(text, end="")

# Create PTY session

pty_handle = sandbox.process.create_pty_session(
id="long-running-session",
pty_size=PtySize(cols=120, rows=30)
)

# Start a long-running process

pty_handle.send_input('while true; do echo "Running... $(date)"; sleep 1; done\n')

# Using thread and wait() method to handle PTY output

thread = threading.Thread(target=pty_handle.wait, args=(handle_pty_data, 10))
thread.start()

time.sleep(3) # Let it run for a bit

print("Killing long-running process...")
pty_handle.kill()

thread.join()

print(f"\nProcess terminated with exit code: {result.exit_code}")
if result.error:
print(f"Termination reason: {result.error}")

````
```typescript
import { Daytona, Sandbox } from '@daytonaio/sdk'

// Create PTY session
const ptyHandle = await sandbox.process.createPty({
  id: 'long-running-session',
  cols: 120,
  rows: 30,
  onData: (data) => {
    const text = new TextDecoder().decode(data)
    process.stdout.write(text)
  },
})

await ptyHandle.waitForConnection()

// Start a long-running process
await ptyHandle.sendInput('while true; do echo "Running... $(date)"; sleep 1; done\n')
await new Promise(resolve => setTimeout(resolve, 3000)) // Let it run for a bit

console.log('Killing long-running process...')
await ptyHandle.kill()

// Wait for termination
const result = await ptyHandle.wait()
console.log(`\nProcess terminated with exit code: ${result.exitCode}`)
if (result.error) {
    console.log(`Termination reason: ${result.error}`)
}
````


## Best Practices

### Resource Management

Always clean up PTY sessions to prevent resource leaks:

```python
# Python: Use try/finally
pty_handle = None
try:
    pty_handle = sandbox.process.create_pty_session(id="session", pty_size=PtySize(cols=120, rows=30))
    # Do work...
finally:
    if pty_handle:
        pty_handle.kill()
```
```typescript
// TypeScript: Use try/finally
let ptyHandle
try {
  ptyHandle = await sandbox.process.createPty({
    id: 'session',
    cols: 120,
    rows: 30,
  })
  // Do work...
} finally {
  if (ptyHandle) await ptyHandle.kill()
}
```

### Error Handling

Monitor exit codes and handle errors appropriately:

```python
# Python: Check exit codes
result = pty_handle.wait()
if result.exit_code != 0:
    print(f"Command failed: {result.exit_code}")
    print(f"Error: {result.error}")
```
```typescript
// TypeScript: Check exit codes
const result = await ptyHandle.wait()
if (result.exitCode !== 0) {
  console.log(`Command failed: ${result.exitCode}`)
  console.log(`Error: ${result.error}`)
}
```

## Common Use Cases

- **Interactive Development**: REPLs, debuggers, and development tools
- **Build Processes**: Running and monitoring compilation, testing, or deployment
- **System Administration**: Remote server management and configuration
- **User Interfaces**: Terminal-based applications requiring user interaction

## Troubleshooting

**Connection Issues**: Verify sandbox status, network connectivity, and proper session IDs.
**Performance Issues**: Use appropriate terminal dimensions and efficient data handlers.
**Process Management**: Use explicit `kill()` calls and proper timeout handling for long-running processes.

## AsyncComputerUse

```python
class AsyncComputerUse()
```

Computer Use functionality for interacting with the desktop environment.

Provides access to mouse, keyboard, screenshot, and display operations
for automating desktop interactions within a sandbox.

**Attributes**:

- `mouse` _AsyncMouse_ - Mouse operations interface.
- `keyboard` _AsyncKeyboard_ - Keyboard operations interface.
- `screenshot` _AsyncScreenshot_ - Screenshot operations interface.
- `display` _AsyncDisplay_ - Display operations interface.

#### AsyncComputerUse.start

```python
@intercept_errors(message_prefix="Failed to start computer use: ")
async def start() -> ComputerUseStartResponse
```

Starts all computer use processes (Xvfb, xfce4, x11vnc, novnc).

**Returns**:

- `ComputerUseStartResponse` - Computer use start response.
  

**Example**:

```python
result = await sandbox.computer_use.start()
print("Computer use processes started:", result.message)
```

#### AsyncComputerUse.stop

```python
@intercept_errors(message_prefix="Failed to stop computer use: ")
async def stop() -> ComputerUseStopResponse
```

Stops all computer use processes.

**Returns**:

- `ComputerUseStopResponse` - Computer use stop response.
  

**Example**:

```python
result = await sandbox.computer_use.stop()
print("Computer use processes stopped:", result.message)
```

#### AsyncComputerUse.get\_status

```python
@intercept_errors(message_prefix="Failed to get computer use status: ")
async def get_status() -> ComputerUseStatusResponse
```

Gets the status of all computer use processes.

**Returns**:

- `ComputerUseStatusResponse` - Status information about all VNC desktop processes.
  

**Example**:

```python
response = await sandbox.computer_use.get_status()
print("Computer use status:", response.status)
```

#### AsyncComputerUse.get\_process\_status

```python
@intercept_errors(message_prefix="Failed to get process status: ")
async def get_process_status(process_name: str) -> ProcessStatusResponse
```

Gets the status of a specific VNC process.

**Arguments**:

- `process_name` _str_ - Name of the process to check.
  

**Returns**:

- `ProcessStatusResponse` - Status information about the specific process.
  

**Example**:

```python
xvfb_status = await sandbox.computer_use.get_process_status("xvfb")
no_vnc_status = await sandbox.computer_use.get_process_status("novnc")
```

#### AsyncComputerUse.restart\_process

```python
@intercept_errors(message_prefix="Failed to restart process: ")
async def restart_process(process_name: str) -> ProcessRestartResponse
```

Restarts a specific VNC process.

**Arguments**:

- `process_name` _str_ - Name of the process to restart.
  

**Returns**:

- `ProcessRestartResponse` - Process restart response.
  

**Example**:

```python
result = await sandbox.computer_use.restart_process("xfce4")
print("XFCE4 process restarted:", result.message)
```

#### AsyncComputerUse.get\_process\_logs

```python
@intercept_errors(message_prefix="Failed to get process logs: ")
async def get_process_logs(process_name: str) -> ProcessLogsResponse
```

Gets logs for a specific VNC process.

**Arguments**:

- `process_name` _str_ - Name of the process to get logs for.
  

**Returns**:

- `ProcessLogsResponse` - Process logs.
  

**Example**:

```python
logs = await sandbox.computer_use.get_process_logs("novnc")
print("NoVNC logs:", logs)
```

#### AsyncComputerUse.get\_process\_errors

```python
@intercept_errors(message_prefix="Failed to get process errors: ")
async def get_process_errors(process_name: str) -> ProcessErrorsResponse
```

Gets error logs for a specific VNC process.

**Arguments**:

- `process_name` _str_ - Name of the process to get error logs for.
  

**Returns**:

- `ProcessErrorsResponse` - Process error logs.
  

**Example**:

```python
errors = await sandbox.computer_use.get_process_errors("x11vnc")
print("X11VNC errors:", errors)
```


## AsyncMouse

```python
class AsyncMouse()
```

Mouse operations for computer use functionality.

#### AsyncMouse.get\_position

```python
@intercept_errors(message_prefix="Failed to get mouse position: ")
async def get_position() -> MousePositionResponse
```

Gets the current mouse cursor position.

**Returns**:

- `MousePositionResponse` - Current mouse position with x and y coordinates.
  

**Example**:

```python
position = await sandbox.computer_use.mouse.get_position()
print(f"Mouse is at: {position.x}, {position.y}")
```

#### AsyncMouse.move

```python
@intercept_errors(message_prefix="Failed to move mouse: ")
async def move(x: int, y: int) -> MousePositionResponse
```

Moves the mouse cursor to the specified coordinates.

**Arguments**:

- `x` _int_ - The x coordinate to move to.
- `y` _int_ - The y coordinate to move to.
  

**Returns**:

- `MousePositionResponse` - Position after move.
  

**Example**:

```python
result = await sandbox.computer_use.mouse.move(100, 200)
print(f"Mouse moved to: {result.x}, {result.y}")
```

#### AsyncMouse.click

```python
@intercept_errors(message_prefix="Failed to click mouse: ")
async def click(x: int,
                y: int,
                button: str = "left",
                double: bool = False) -> MouseClickResponse
```

Clicks the mouse at the specified coordinates.

**Arguments**:

- `x` _int_ - The x coordinate to click at.
- `y` _int_ - The y coordinate to click at.
- `button` _str_ - The mouse button to click ('left', 'right', 'middle').
- `double` _bool_ - Whether to perform a double-click.
  

**Returns**:

- `MouseClickResponse` - Click operation result.
  

**Example**:

```python
# Single left click
result = await sandbox.computer_use.mouse.click(100, 200)

# Double click
double_click = await sandbox.computer_use.mouse.click(100, 200, "left", True)

# Right click
right_click = await sandbox.computer_use.mouse.click(100, 200, "right")
```

#### AsyncMouse.drag

```python
@intercept_errors(message_prefix="Failed to drag mouse: ")
async def drag(start_x: int,
               start_y: int,
               end_x: int,
               end_y: int,
               button: str = "left") -> MouseDragResponse
```

Drags the mouse from start coordinates to end coordinates.

**Arguments**:

- `start_x` _int_ - The starting x coordinate.
- `start_y` _int_ - The starting y coordinate.
- `end_x` _int_ - The ending x coordinate.
- `end_y` _int_ - The ending y coordinate.
- `button` _str_ - The mouse button to use for dragging.
  

**Returns**:

- `MouseDragResponse` - Drag operation result.
  

**Example**:

```python
result = await sandbox.computer_use.mouse.drag(50, 50, 150, 150)
print(f"Dragged from {result.from_x},{result.from_y} to {result.to_x},{result.to_y}")
```

#### AsyncMouse.scroll

```python
@intercept_errors(message_prefix="Failed to scroll mouse: ")
async def scroll(x: int, y: int, direction: str, amount: int = 1) -> bool
```

Scrolls the mouse wheel at the specified coordinates.

**Arguments**:

- `x` _int_ - The x coordinate to scroll at.
- `y` _int_ - The y coordinate to scroll at.
- `direction` _str_ - The direction to scroll ('up' or 'down').
- `amount` _int_ - The amount to scroll.
  

**Returns**:

- `bool` - Whether the scroll operation was successful.
  

**Example**:

```python
# Scroll up
scroll_up = await sandbox.computer_use.mouse.scroll(100, 200, "up", 3)

# Scroll down
scroll_down = await sandbox.computer_use.mouse.scroll(100, 200, "down", 5)
```

## AsyncKeyboard

```python
class AsyncKeyboard()
```

Keyboard operations for computer use functionality.

#### AsyncKeyboard.type

```python
@intercept_errors(message_prefix="Failed to type text: ")
async def type(text: str, delay: Optional[int] = None) -> None
```

Types the specified text.

**Arguments**:

- `text` _str_ - The text to type.
- `delay` _int_ - Delay between characters in milliseconds.
  

**Raises**:

- `DaytonaError` - If the type operation fails.
  

**Example**:

```python
try:
    await sandbox.computer_use.keyboard.type("Hello, World!")
    print(f"Operation success")
except Exception as e:
    print(f"Operation failed: {e}")

# With delay between characters
try:
    await sandbox.computer_use.keyboard.type("Slow typing", 100)
    print(f"Operation success")
except Exception as e:
    print(f"Operation failed: {e}")
```

#### AsyncKeyboard.press

```python
@intercept_errors(message_prefix="Failed to press key: ")
async def press(key: str, modifiers: Optional[List[str]] = None) -> None
```

Presses a key with optional modifiers.

**Arguments**:

- `key` _str_ - The key to press (e.g., 'Enter', 'Escape', 'Tab', 'a', 'A').
- `modifiers` _List[str]_ - Modifier keys ('ctrl', 'alt', 'meta', 'shift').
  

**Raises**:

- `DaytonaError` - If the press operation fails.
  

**Example**:

```python
# Press Enter
try:
    await sandbox.computer_use.keyboard.press("Return")
    print(f"Operation success")
except Exception as e:
    print(f"Operation failed: {e}")

# Press Ctrl+C
try:
    await sandbox.computer_use.keyboard.press("c", ["ctrl"])
    print(f"Operation success")

# Press Ctrl+Shift+T
try:
    await sandbox.computer_use.keyboard.press("t", ["ctrl", "shift"])
    print(f"Operation success")
except Exception as e:
    print(f"Operation failed: {e}")
```

#### AsyncKeyboard.hotkey

```python
@intercept_errors(message_prefix="Failed to press hotkey: ")
async def hotkey(keys: str) -> None
```

Presses a hotkey combination.

**Arguments**:

- `keys` _str_ - The hotkey combination (e.g., 'ctrl+c', 'alt+tab', 'cmd+shift+t').
  

**Raises**:

- `DaytonaError` - If the hotkey operation fails.
  

**Example**:

```python
# Copy
try:
    await sandbox.computer_use.keyboard.hotkey("ctrl+c")
    print(f"Operation success")
except Exception as e:
    print(f"Operation failed: {e}")

# Paste
try:
    await sandbox.computer_use.keyboard.hotkey("ctrl+v")
    print(f"Operation success")
except Exception as e:
    print(f"Operation failed: {e}")

# Alt+Tab
try:
    await sandbox.computer_use.keyboard.hotkey("alt+tab")
    print(f"Operation success")
except Exception as e:
    print(f"Operation failed: {e}")
```

## AsyncScreenshot

```python
class AsyncScreenshot()
```

Screenshot operations for computer use functionality.

#### AsyncScreenshot.take\_full\_screen

```python
@intercept_errors(message_prefix="Failed to take screenshot: ")
async def take_full_screen(show_cursor: bool = False) -> ScreenshotResponse
```

Takes a screenshot of the entire screen.

**Arguments**:

- `show_cursor` _bool_ - Whether to show the cursor in the screenshot.
  

**Returns**:

- `ScreenshotResponse` - Screenshot data with base64 encoded image.
  

**Example**:

```python
screenshot = await sandbox.computer_use.screenshot.take_full_screen()
print(f"Screenshot size: {screenshot.width}x{screenshot.height}")

# With cursor visible
with_cursor = await sandbox.computer_use.screenshot.take_full_screen(True)
```

#### AsyncScreenshot.take\_region

```python
@intercept_errors(message_prefix="Failed to take region screenshot: ")
async def take_region(region: ScreenshotRegion,
                      show_cursor: bool = False) -> ScreenshotResponse
```

Takes a screenshot of a specific region.

**Arguments**:

- `region` _ScreenshotRegion_ - The region to capture.
- `show_cursor` _bool_ - Whether to show the cursor in the screenshot.
  

**Returns**:

- `ScreenshotResponse` - Screenshot data with base64 encoded image.
  

**Example**:

```python
region = ScreenshotRegion(x=100, y=100, width=300, height=200)
screenshot = await sandbox.computer_use.screenshot.take_region(region)
print(f"Captured region: {screenshot.region.width}x{screenshot.region.height}")
```

#### AsyncScreenshot.take\_compressed

```python
@intercept_errors(message_prefix="Failed to take compressed screenshot: ")
async def take_compressed(
        options: Optional[ScreenshotOptions] = None) -> ScreenshotResponse
```

Takes a compressed screenshot of the entire screen.

**Arguments**:

- `options` _ScreenshotOptions_ - Compression and display options.
  

**Returns**:

- `ScreenshotResponse` - Compressed screenshot data.
  

**Example**:

```python
# Default compression
screenshot = await sandbox.computer_use.screenshot.take_compressed()

# High quality JPEG
jpeg = await sandbox.computer_use.screenshot.take_compressed(
    ScreenshotOptions(format="jpeg", quality=95, show_cursor=True)
)

# Scaled down PNG
scaled = await sandbox.computer_use.screenshot.take_compressed(
    ScreenshotOptions(format="png", scale=0.5)
)
```

#### AsyncScreenshot.take\_compressed\_region

```python
@intercept_errors(
    message_prefix="Failed to take compressed region screenshot: ")
async def take_compressed_region(
        region: ScreenshotRegion,
        options: Optional[ScreenshotOptions] = None) -> ScreenshotResponse
```

Takes a compressed screenshot of a specific region.

**Arguments**:

- `region` _ScreenshotRegion_ - The region to capture.
- `options` _ScreenshotOptions_ - Compression and display options.
  

**Returns**:

- `ScreenshotResponse` - Compressed screenshot data.
  

**Example**:

```python
region = ScreenshotRegion(x=0, y=0, width=800, height=600)
screenshot = await sandbox.computer_use.screenshot.take_compressed_region(
    region,
    ScreenshotOptions(format="webp", quality=80, show_cursor=True)
)
print(f"Compressed size: {screenshot.size_bytes} bytes")
```

## AsyncDisplay

```python
class AsyncDisplay()
```

Display operations for computer use functionality.

#### AsyncDisplay.get\_info

```python
@intercept_errors(message_prefix="Failed to get display info: ")
async def get_info() -> DisplayInfoResponse
```

Gets information about the displays.

**Returns**:

- `DisplayInfoResponse` - Display information including primary display and all available displays.
  

**Example**:

```python
info = await sandbox.computer_use.display.get_info()
print(f"Primary display: {info.primary_display.width}x{info.primary_display.height}")
print(f"Total displays: {info.total_displays}")
for i, display in enumerate(info.displays):
    print(f"Display {i}: {display.width}x{display.height} at {display.x},{display.y}")
```

#### AsyncDisplay.get\_windows

```python
@intercept_errors(message_prefix="Failed to get windows: ")
async def get_windows() -> WindowsResponse
```

Gets the list of open windows.

**Returns**:

- `WindowsResponse` - List of open windows with their IDs and titles.
  

**Example**:

```python
windows = await sandbox.computer_use.display.get_windows()
print(f"Found {windows.count} open windows:")
for window in windows.windows:
    print(f"- {window.title} (ID: {window.id})")
```

## ScreenshotRegion

```python
class ScreenshotRegion()
```

Region coordinates for screenshot operations.

**Attributes**:

- `x` _int_ - X coordinate of the region.
- `y` _int_ - Y coordinate of the region.
- `width` _int_ - Width of the region.
- `height` _int_ - Height of the region.

## ScreenshotOptions

```python
class ScreenshotOptions()
```

Options for screenshot compression and display.

**Attributes**:

- `show_cursor` _bool_ - Whether to show the cursor in the screenshot.
- `fmt` _str_ - Image format (e.g., 'png', 'jpeg', 'webp').
- `quality` _int_ - Compression quality (0-100).
- `scale` _float_ - Scale factor for the screenshot.

## AsyncDaytona

```python
class AsyncDaytona()
```

Main class for interacting with the Daytona API.

This class provides asynchronous methods to create, manage, and interact with Daytona Sandboxes.
It can be initialized either with explicit configuration or using environment variables.

**Attributes**:

- `volume` _AsyncVolumeService_ - Service for managing volumes.
- `snapshot` _AsyncSnapshotService_ - Service for managing snapshots.
  

**Example**:

  Using environment variables:
```python
async with AsyncDaytona() as daytona:  # Uses DAYTONA_API_KEY, DAYTONA_API_URL
    sandbox = await daytona.create()
```
  
  Using explicit configuration:
```python
config = DaytonaConfig(
    api_key="your-api-key",
    api_url="https://your-api.com",
    target="us"
)
try:
    daytona = AsyncDaytona(config)
    sandbox = await daytona.create()
finally:
    await daytona.close()
```

#### AsyncDaytona.\_\_init\_\_

```python
def __init__(config: Optional[DaytonaConfig] = None)
```

Initializes Daytona instance with optional configuration.

If no config is provided, reads from environment variables:
- `DAYTONA_API_KEY`: Required API key for authentication
- `DAYTONA_API_URL`: Required api URL
- `DAYTONA_TARGET`: Optional target environment (if not provided, default region for the organization is used)

**Arguments**:

- `config` _Optional[DaytonaConfig]_ - Object containing api_key, api_url, and target.
  

**Raises**:

- `DaytonaError` - If API key is not provided either through config or environment variables
  

**Example**:

```python
from daytona import Daytona, DaytonaConfig
# Using environment variables
daytona1 = AsyncDaytona()
await daytona1.close()
# Using explicit configuration
config = DaytonaConfig(
    api_key="your-api-key",
    api_url="https://your-api.com",
    target="us"
)
daytona2 = AsyncDaytona(config)
await daytona2.close()
```

#### AsyncDaytona.\_\_aenter\_\_

```python
async def __aenter__()
```

Async context manager entry.

#### AsyncDaytona.\_\_aexit\_\_

```python
async def __aexit__(exc_type, exc_value, traceback)
```

Async context manager exit - ensures proper cleanup.

#### AsyncDaytona.close

```python
async def close()
```

Close the HTTP session and clean up resources.

This method should be called when you're done using the AsyncDaytona instance
to properly close the underlying HTTP sessions and avoid resource leaks.

**Example**:

```python
daytona = AsyncDaytona()
try:
    sandbox = await daytona.create()
    # ... use sandbox ...
finally:
    await daytona.close()
```
  
  Or better yet, use as async context manager:
```python
async with AsyncDaytona() as daytona:
    sandbox = await daytona.create()
    # ... use sandbox ...
# Automatically closed
```

#### AsyncDaytona.create

```python
@overload
async def create(params: Optional[CreateSandboxFromSnapshotParams] = None,
                 *,
                 timeout: Optional[float] = 60) -> AsyncSandbox
```

Creates Sandboxes from specified or default snapshot. You can specify various parameters,
including language, image, environment variables, and volumes.

**Arguments**:

- `params` _Optional[CreateSandboxFromSnapshotParams]_ - Parameters for Sandbox creation. If not provided,
  defaults to default Daytona snapshot and Python language.
- `timeout` _Optional[float]_ - Timeout (in seconds) for sandbox creation. 0 means no timeout.
  Default is 60 seconds.
  

**Returns**:

- `Sandbox` - The created Sandbox instance.
  

**Raises**:

- `DaytonaError` - If timeout, auto_stop_interval or auto_archive_interval is negative;
  If sandbox fails to start or times out
  

**Example**:

  Create a default Python Sandbox:
```python
sandbox = await daytona.create()
```
  
  Create a custom Sandbox:
```python
params = CreateSandboxFromSnapshotParams(
    language="python",
    snapshot="my-snapshot-id",
    env_vars={"DEBUG": "true"},
    auto_stop_interval=0,
    auto_archive_interval=60,
    auto_delete_interval=120
)
sandbox = await daytona.create(params, timeout=40)
```

#### AsyncDaytona.create

```python
@overload
async def create(
        params: Optional[CreateSandboxFromImageParams] = None,
        *,
        timeout: Optional[float] = 60,
        on_snapshot_create_logs: Callable[[str], None] = None) -> AsyncSandbox
```

Creates Sandboxes from specified image available on some registry or declarative Daytona Image.
You can specify various parameters, including resources, language, image, environment variables,
and volumes. Daytona creates snapshot from provided image and uses it to create Sandbox.

**Arguments**:

- `params` _Optional[CreateSandboxFromImageParams]_ - Parameters for Sandbox creation from image.
- `timeout` _Optional[float]_ - Timeout (in seconds) for sandbox creation. 0 means no timeout.
  Default is 60 seconds.
- `on_snapshot_create_logs` _Callable[[str], None]_ - This callback function handles snapshot creation logs.
  

**Returns**:

- `Sandbox` - The created Sandbox instance.
  

**Raises**:

- `DaytonaError` - If timeout, auto_stop_interval or auto_archive_interval is negative;
  If sandbox fails to start or times out
  

**Example**:

  Create a default Python Sandbox from image:
```python
sandbox = await daytona.create(CreateSandboxFromImageParams(image="debian:12.9"))
```
  
  Create a custom Sandbox from declarative Image definition:
```python
declarative_image = (
    Image.base("alpine:3.18")
    .pipInstall(["numpy", "pandas"])
    .env({"MY_ENV_VAR": "My Environment Variable"})
)
params = CreateSandboxFromImageParams(
    language="python",
    image=declarative_image,
    env_vars={"DEBUG": "true"},
    resources=Resources(cpu=2, memory=4),
    auto_stop_interval=0,
    auto_archive_interval=60,
    auto_delete_interval=120
)
sandbox = await daytona.create(
    params,
    timeout=40,
    on_snapshot_create_logs=lambda chunk: print(chunk, end=""),
)
```

#### AsyncDaytona.delete

```python
async def delete(sandbox: AsyncSandbox, timeout: Optional[float] = 60) -> None
```

Deletes a Sandbox.

**Arguments**:

- `sandbox` _Sandbox_ - The Sandbox instance to delete.
- `timeout` _Optional[float]_ - Timeout (in seconds) for sandbox deletion. 0 means no timeout.
  Default is 60 seconds.
  

**Raises**:

- `DaytonaError` - If sandbox fails to delete or times out
  

**Example**:

```python
sandbox = await daytona.create()
# ... use sandbox ...
await daytona.delete(sandbox)  # Clean up when done
```

#### AsyncDaytona.get

```python
@intercept_errors(message_prefix="Failed to get sandbox: ")
async def get(sandbox_id_or_name: str) -> AsyncSandbox
```

Gets a Sandbox by its ID or name.

**Arguments**:

- `sandbox_id_or_name` _str_ - The ID or name of the Sandbox to retrieve.
  

**Returns**:

- `Sandbox` - The Sandbox instance.
  

**Raises**:

- `DaytonaError` - If sandbox_id_or_name is not provided.
  

**Example**:

```python
sandbox = await daytona.get("my-sandbox-id-or-name")
print(sandbox.state)
```

#### AsyncDaytona.find\_one

```python
@intercept_errors(message_prefix="Failed to find sandbox: ")
async def find_one(sandbox_id_or_name: Optional[str] = None,
                   labels: Optional[Dict[str, str]] = None) -> AsyncSandbox
```

Finds a Sandbox by its ID or name or labels.

**Arguments**:

- `sandbox_id_or_name` _Optional[str]_ - The ID or name of the Sandbox to retrieve.
- `labels` _Optional[Dict[str, str]]_ - Labels to filter Sandboxes.
  

**Returns**:

- `Sandbox` - First Sandbox that matches the ID or name or labels.
  

**Raises**:

- `DaytonaError` - If no Sandbox is found.
  

**Example**:

```python
sandbox = await daytona.find_one(labels={"my-label": "my-value"})
print(f"Sandbox ID: {sandbox.id} State: {sandbox.state}")
```

#### AsyncDaytona.list

```python
@intercept_errors(message_prefix="Failed to list sandboxes: ")
async def list(labels: Optional[Dict[str, str]] = None,
               page: Optional[int] = None,
               limit: Optional[int] = None) -> AsyncPaginatedSandboxes
```

Returns paginated list of Sandboxes filtered by labels.

**Arguments**:

- `labels` _Optional[Dict[str, str]]_ - Labels to filter Sandboxes.
- `page` _Optional[int]_ - Page number for pagination (starting from 1).
- `limit` _Optional[int]_ - Maximum number of items per page.
  

**Returns**:

- `AsyncPaginatedSandboxes` - Paginated list of Sandbox instances that match the labels.
  

**Example**:

```python
result = await daytona.list(labels={"my-label": "my-value"}, page=2, limit=10)
for sandbox in result.items:
    print(f"{sandbox.id}: {sandbox.state}")
```

#### AsyncDaytona.start

```python
async def start(sandbox: AsyncSandbox, timeout: Optional[float] = 60) -> None
```

Starts a Sandbox and waits for it to be ready.

**Arguments**:

- `sandbox` _Sandbox_ - The Sandbox to start.
- `timeout` _Optional[float]_ - Optional timeout in seconds to wait for the Sandbox to start.
  0 means no timeout. Default is 60 seconds.
  

**Raises**:

- `DaytonaError` - If timeout is negative; If Sandbox fails to start or times out

#### AsyncDaytona.stop

```python
async def stop(sandbox: AsyncSandbox, timeout: Optional[float] = 60) -> None
```

Stops a Sandbox and waits for it to be stopped.

**Arguments**:

- `sandbox` _Sandbox_ - The sandbox to stop
- `timeout` _Optional[float]_ - Optional timeout (in seconds) for sandbox stop.
  0 means no timeout. Default is 60 seconds.
  

**Raises**:

- `DaytonaError` - If timeout is negative; If Sandbox fails to stop or times out


## CodeLanguage

```python
@dataclass
class CodeLanguage(Enum)
```

Programming languages supported by Daytona

**Enum Members**:
    - `PYTHON` ("python")
    - `TYPESCRIPT` ("typescript")
    - `JAVASCRIPT` ("javascript")

## DaytonaConfig

```python
class DaytonaConfig(BaseModel)
```

Configuration options for initializing the Daytona client.

**Attributes**:

- `api_key` _Optional[str]_ - API key for authentication with the Daytona API. If not set, it must be provided
  via the environment variable `DAYTONA_API_KEY`, or a JWT token must be provided instead.
- `jwt_token` _Optional[str]_ - JWT token for authentication with the Daytona API. If not set, it must be provided
  via the environment variable `DAYTONA_JWT_TOKEN`, or an API key must be provided instead.
- `organization_id` _Optional[str]_ - Organization ID used for JWT-based authentication. Required if a JWT token
  is provided, and must be set either here or in the environment variable `DAYTONA_ORGANIZATION_ID`.
- `api_url` _Optional[str]_ - URL of the Daytona API. Defaults to `'https://app.daytona.io/api'` if not set
  here or in the environment variable `DAYTONA_API_URL`.
- `server_url` _Optional[str]_ - Deprecated. Use `api_url` instead. This property will be removed
  in a future version.
- `target` _Optional[str]_ - Target runner location for the Sandbox. Default region for the organization is used 
  if not set here or in the environment variable `DAYTONA_TARGET`.
  

**Example**:

```python
config = DaytonaConfig(api_key="your-api-key")
```
```python
config = DaytonaConfig(jwt_token="your-jwt-token", organization_id="your-organization-id")
```

## CreateSandboxBaseParams

```python
class CreateSandboxBaseParams(BaseModel)
```

Base parameters for creating a new Sandbox.

**Attributes**:

- `name` _Optional[str]_ - Name of the Sandbox.
- `language` _Optional[CodeLanguage]_ - Programming language for the Sandbox. Defaults to "python".
- `os_user` _Optional[str]_ - OS user for the Sandbox.
- `env_vars` _Optional[Dict[str, str]]_ - Environment variables to set in the Sandbox.
- `labels` _Optional[Dict[str, str]]_ - Custom labels for the Sandbox.
- `public` _Optional[bool]_ - Whether the Sandbox should be public.
- `timeout` _Optional[float]_ - Timeout in seconds for Sandbox to be created and started.
- `auto_stop_interval` _Optional[int]_ - Interval in minutes after which Sandbox will
  automatically stop if no Sandbox event occurs during that time. Default is 15 minutes.
  0 means no auto-stop.
- `auto_archive_interval` _Optional[int]_ - Interval in minutes after which a continuously stopped Sandbox will
  automatically archive. Default is 7 days.
  0 means the maximum interval will be used.
- `auto_delete_interval` _Optional[int]_ - Interval in minutes after which a continuously stopped Sandbox will
  automatically be deleted. By default, auto-delete is disabled.
  Negative value means disabled, 0 means delete immediately upon stopping.
- `volumes` _Optional[List[VolumeMount]]_ - List of volumes mounts to attach to the Sandbox.
- `network_block_all` _Optional[bool]_ - Whether to block all network access for the Sandbox.
- `network_allow_list` _Optional[str]_ - Comma-separated list of allowed CIDR network addresses for the Sandbox.
- `ephemeral` _Optional[bool]_ - Whether the Sandbox should be ephemeral.
  If True, auto_delete_interval will be set to 0.

## CreateSandboxFromImageParams

```python
class CreateSandboxFromImageParams(CreateSandboxBaseParams)
```

Parameters for creating a new Sandbox from an image.

**Attributes**:

- `image` _Union[str, Image]_ - Custom Docker image to use for the Sandbox. If an Image object is provided,
  the image will be dynamically built.
- `resources` _Optional[Resources]_ - Resource configuration for the Sandbox. If not provided, sandbox will
  have default resources.

## CreateSandboxFromSnapshotParams

```python
class CreateSandboxFromSnapshotParams(CreateSandboxBaseParams)
```

Parameters for creating a new Sandbox from a snapshot.

**Attributes**:

- `snapshot` _Optional[str]_ - Name of the snapshot to use for the Sandbox.

## AsyncFileSystem

```python
class AsyncFileSystem()
```

Provides file system operations within a Sandbox.

This class implements a high-level interface to file system operations that can
be performed within a Daytona Sandbox.

#### AsyncFileSystem.\_\_init\_\_

```python
def __init__(api_client: FileSystemApi,
             ensure_toolbox_url: Callable[[], Awaitable[None]])
```

Initializes a new FileSystem instance.

**Arguments**:

- `api_client` _FileSystemApi_ - API client for Sandbox file system operations.
- `ensure_toolbox_url` _Callable[[], Awaitable[None]]_ - Ensures the toolbox API URL is initialized.
  Must be called before invoking any private methods on the API client.

#### AsyncFileSystem.create\_folder

```python
@intercept_errors(message_prefix="Failed to create folder: ")
async def create_folder(path: str, mode: str) -> None
```

Creates a new directory in the Sandbox at the specified path with the given
permissions.

**Arguments**:

- `path` _str_ - Path where the folder should be created. Relative paths are resolved based
  on the sandbox working directory.
- `mode` _str_ - Folder permissions in octal format (e.g., "755" for rwxr-xr-x).
  

**Example**:

```python
# Create a directory with standard permissions
await sandbox.fs.create_folder("workspace/data", "755")

# Create a private directory
await sandbox.fs.create_folder("workspace/secrets", "700")
```

#### AsyncFileSystem.delete\_file

```python
@intercept_errors(message_prefix="Failed to delete file: ")
async def delete_file(path: str, recursive: bool = False) -> None
```

Deletes a file from the Sandbox.

**Arguments**:

- `path` _str_ - Path to the file to delete. Relative paths are resolved based on the sandbox working directory.
- `recursive` _bool_ - If the file is a directory, this must be true to delete it.
  

**Example**:

```python
# Delete a file
await sandbox.fs.delete_file("workspace/data/old_file.txt")
```

#### AsyncFileSystem.download\_file

```python
@overload
async def download_file(remote_path: str, timeout: int = 30 * 60) -> bytes
```

Downloads a file from the Sandbox. Returns the file contents as a bytes object.
This method is useful when you want to load the file into memory without saving it to disk.
It can only be used for smaller files.

**Arguments**:

- `remote_path` _str_ - Path to the file in the Sandbox. Relative paths are resolved based
  on the sandbox working directory.
- `timeout` _int_ - Timeout for the download operation in seconds. 0 means no timeout. Default is 30 minutes.
  

**Returns**:

- `bytes` - The file contents as a bytes object.
  

**Example**:

```python
# Download and save a file locally
content = await sandbox.fs.download_file("workspace/data/file.txt")
with open("local_copy.txt", "wb") as f:
    f.write(content)

# Download and process text content
content = await sandbox.fs.download_file("workspace/data/config.json")
config = json.loads(content.decode('utf-8'))
```

#### AsyncFileSystem.download\_file

```python
@overload
async def download_file(remote_path: str,
                        local_path: str,
                        timeout: int = 30 * 60) -> None
```

Downloads a file from the Sandbox and saves it to a local file using stream.
This method is useful when you want to download larger files that may not fit into memory.

**Arguments**:

- `remote_path` _str_ - Path to the file in the Sandbox. Relative paths are resolved based
  on the sandbox working directory.
- `local_path` _str_ - Path to save the file locally.
- `timeout` _int_ - Timeout for the download operation in seconds. 0 means no timeout. Default is 30 minutes.
  

**Example**:

```python
local_path = "local_copy.txt"
await sandbox.fs.download_file("tmp/large_file.txt", local_path)
size_mb = os.path.getsize(local_path) / 1024 / 1024
print(f"Size of the downloaded file {local_path}: {size_mb} MB")
```

#### AsyncFileSystem.download\_files

```python
@intercept_errors(message_prefix="Failed to download files: ")
async def download_files(files: List[FileDownloadRequest],
                         timeout: int = 30 * 60) -> List[FileDownloadResponse]
```

Downloads multiple files from the Sandbox. If the files already exist locally, they will be overwritten.

**Arguments**:

- `files` _List[FileDownloadRequest]_ - List of files to download.
- `timeout` _int_ - Timeout for the download operation in seconds. 0 means no timeout. Default is 30 minutes.
  

**Returns**:

- `List[FileDownloadResponse]` - List of download results.
  

**Raises**:

- `Exception` - Only if the request itself fails (network issues, invalid request/response, etc.). Individual
  file download errors are returned in the `FileDownloadResponse.error` field.
  

**Example**:

```python
# Download multiple files
results = await sandbox.fs.download_files([
    FileDownloadRequest(source="tmp/data.json"),
    FileDownloadRequest(source="tmp/config.json", destination="local_config.json")
])
for result in results:
    if result.error:
        print(f"Error downloading {result.source}: {result.error}")
    elif result.result:
        print(f"Downloaded {result.source} to {result.result}")
```

#### AsyncFileSystem.find\_files

```python
@intercept_errors(message_prefix="Failed to find files: ")
async def find_files(path: str, pattern: str) -> List[Match]
```

Searches for files containing a pattern, similar to
the grep command.

**Arguments**:

- `path` _str_ - Path to the file or directory to search. If the path is a directory,
  the search will be performed recursively. Relative paths are resolved based
  on the sandbox working directory.
- `pattern` _str_ - Search pattern to match against file contents.
  

**Returns**:

- `List[Match]` - List of matches found in files. Each Match object includes:
  - file: Path to the file containing the match
  - line: The line number where the match was found
  - content: The matching line content
  

**Example**:

```python
# Search for TODOs in Python files
matches = await sandbox.fs.find_files("workspace/src", "TODO:")
for match in matches:
    print(f"{match.file}:{match.line}: {match.content.strip()}")
```

#### AsyncFileSystem.get\_file\_info

```python
@intercept_errors(message_prefix="Failed to get file info: ")
async def get_file_info(path: str) -> FileInfo
```

Gets detailed information about a file or directory, including its
size, permissions, and timestamps.

**Arguments**:

- `path` _str_ - Path to the file or directory. Relative paths are resolved based
  on the sandbox working directory.
  

**Returns**:

- `FileInfo` - Detailed file information including:
  - name: File name
  - is_dir: Whether the path is a directory
  - size: File size in bytes
  - mode: File permissions
  - mod_time: Last modification timestamp
  - permissions: File permissions in octal format
  - owner: File owner
  - group: File group
  

**Example**:

```python
# Get file metadata
info = await sandbox.fs.get_file_info("workspace/data/file.txt")
print(f"Size: {info.size} bytes")
print(f"Modified: {info.mod_time}")
print(f"Mode: {info.mode}")

# Check if path is a directory
info = await sandbox.fs.get_file_info("workspace/data")
if info.is_dir:
    print("Path is a directory")
```

#### AsyncFileSystem.list\_files

```python
@intercept_errors(message_prefix="Failed to list files: ")
async def list_files(path: str) -> List[FileInfo]
```

Lists files and directories in a given path and returns their information, similar to the ls -l command.

**Arguments**:

- `path` _str_ - Path to the directory to list contents from. Relative paths are resolved
  based on the sandbox working directory.
  

**Returns**:

- `List[FileInfo]` - List of file and directory information. Each FileInfo
  object includes the same fields as described in get_file_info().
  

**Example**:

```python
# List directory contents
files = await sandbox.fs.list_files("workspace/data")

# Print files and their sizes
for file in files:
    if not file.is_dir:
        print(f"{file.name}: {file.size} bytes")

# List only directories
dirs = [f for f in files if f.is_dir]
print("Subdirectories:", ", ".join(d.name for d in dirs))
```

#### AsyncFileSystem.move\_files

```python
@intercept_errors(message_prefix="Failed to move files: ")
async def move_files(source: str, destination: str) -> None
```

Moves or renames a file or directory. The parent directory of the destination must exist.

**Arguments**:

- `source` _str_ - Path to the source file or directory. Relative paths are resolved
  based on the sandbox working directory.
- `destination` _str_ - Path to the destination. Relative paths are resolved based on
  the sandbox working directory.
  

**Example**:

```python
# Rename a file
await sandbox.fs.move_files(
    "workspace/data/old_name.txt",
    "workspace/data/new_name.txt"
)

# Move a file to a different directory
await sandbox.fs.move_files(
    "workspace/data/file.txt",
    "workspace/archive/file.txt"
)

# Move a directory
await sandbox.fs.move_files(
    "workspace/old_dir",
    "workspace/new_dir"
)
```

#### AsyncFileSystem.replace\_in\_files

```python
@intercept_errors(message_prefix="Failed to replace in files: ")
async def replace_in_files(files: List[str], pattern: str,
                           new_value: str) -> List[ReplaceResult]
```

Performs search and replace operations across multiple files.

**Arguments**:

- `files` _List[str]_ - List of file paths to perform replacements in. Relative paths are
  resolved based on the sandbox working directory.
- `pattern` _str_ - Pattern to search for.
- `new_value` _str_ - Text to replace matches with.
  

**Returns**:

- `List[ReplaceResult]` - List of results indicating replacements made in
  each file. Each ReplaceResult includes:
  - file: Path to the modified file
  - success: Whether the operation was successful
  - error: Error message if the operation failed
  

**Example**:

```python
# Replace in specific files
results = await sandbox.fs.replace_in_files(
    files=["workspace/src/file1.py", "workspace/src/file2.py"],
    pattern="old_function",
    new_value="new_function"
)

# Print results
for result in results:
    if result.success:
        print(f"{result.file}: {result.success}")
    else:
        print(f"{result.file}: {result.error}")
```

#### AsyncFileSystem.search\_files

```python
@intercept_errors(message_prefix="Failed to search files: ")
async def search_files(path: str, pattern: str) -> SearchFilesResponse
```

Searches for files and directories whose names match the
specified pattern. The pattern can be a simple string or a glob pattern.

**Arguments**:

- `path` _str_ - Path to the root directory to start search from. Relative paths are resolved
  based on the sandbox working directory.
- `pattern` _str_ - Pattern to match against file names. Supports glob
  patterns (e.g., "*.py" for Python files).
  

**Returns**:

- `SearchFilesResponse` - Search results containing:
  - files: List of matching file and directory paths
  

**Example**:

```python
# Find all Python files
result = await sandbox.fs.search_files("workspace", "*.py")
for file in result.files:
    print(file)

# Find files with specific prefix
result = await sandbox.fs.search_files("workspace/data", "test_*")
print(f"Found {len(result.files)} test files")
```

#### AsyncFileSystem.set\_file\_permissions

```python
@intercept_errors(message_prefix="Failed to set file permissions: ")
async def set_file_permissions(path: str,
                               mode: str = None,
                               owner: str = None,
                               group: str = None) -> None
```

Sets permissions and ownership for a file or directory. Any of the parameters can be None
to leave that attribute unchanged.

**Arguments**:

- `path` _str_ - Path to the file or directory. Relative paths are resolved based on
  the sandbox working directory.
- `mode` _Optional[str]_ - File mode/permissions in octal format
  (e.g., "644" for rw-r--r--).
- `owner` _Optional[str]_ - User owner of the file.
- `group` _Optional[str]_ - Group owner of the file.
  

**Example**:

```python
# Make a file executable
await sandbox.fs.set_file_permissions(
    path="workspace/scripts/run.sh",
    mode="755"  # rwxr-xr-x
)

# Change file owner
await sandbox.fs.set_file_permissions(
    path="workspace/data/file.txt",
    owner="daytona",
    group="daytona"
)
```

#### AsyncFileSystem.upload\_file

```python
@overload
async def upload_file(file: bytes,
                      remote_path: str,
                      timeout: int = 30 * 60) -> None
```

Uploads a file to the specified path in the Sandbox. If a file already exists at
the destination path, it will be overwritten. This method is useful when you want to upload
small files that fit into memory.

**Arguments**:

- `file` _bytes_ - File contents as a bytes object.
- `remote_path` _str_ - Path to the destination file. Relative paths are resolved based on
  the sandbox working directory.
- `timeout` _int_ - Timeout for the upload operation in seconds. 0 means no timeout. Default is 30 minutes.
  

**Example**:

```python
# Upload a text file
content = b"Hello, World!"
await sandbox.fs.upload_file(content, "tmp/hello.txt")

# Upload a local file
with open("local_file.txt", "rb") as f:
    content = f.read()
await sandbox.fs.upload_file(content, "tmp/file.txt")

# Upload binary data
import json
data = {"key": "value"}
content = json.dumps(data).encode('utf-8')
await sandbox.fs.upload_file(content, "tmp/config.json")
```

#### AsyncFileSystem.upload\_file

```python
@overload
async def upload_file(local_path: str,
                      remote_path: str,
                      timeout: int = 30 * 60) -> None
```

Uploads a file from the local file system to the specified path in the Sandbox.
If a file already exists at the destination path, it will be overwritten. This method uses
streaming to upload the file, so it is useful when you want to upload larger files that may
not fit into memory.

**Arguments**:

- `local_path` _str_ - Path to the local file to upload.
- `remote_path` _str_ - Path to the destination file in the Sandbox. Relative paths are
  resolved based on the sandbox working directory.
- `timeout` _int_ - Timeout for the upload operation in seconds. 0 means no timeout. Default is 30 minutes.
  

**Example**:

```python
await sandbox.fs.upload_file("local_file.txt", "tmp/large_file.txt")
```

#### AsyncFileSystem.upload\_files

```python
@intercept_errors(message_prefix="Failed to upload files: ")
async def upload_files(files: List[FileUpload],
                       timeout: int = 30 * 60) -> None
```

Uploads multiple files to the Sandbox. If files already exist at the destination paths,
they will be overwritten.

**Arguments**:

- `files` _List[FileUpload]_ - List of files to upload.
- `timeout` _int_ - Timeout for the upload operation in seconds. 0 means no timeout. Default is 30 minutes.

**Example**:

```python
# Upload multiple text files
files = [
    FileUpload(
        source=b"Content of file 1",
        destination="/tmp/file1.txt"
    ),
    FileUpload(
        source="workspace/data/file2.txt",
        destination="/tmp/file2.txt"
    ),
    FileUpload(
        source=b'{"key": "value"}',
        destination="/tmp/config.json"
    )
]
await sandbox.fs.upload_files(files)
```


## FileUpload

```python
@dataclass
class FileUpload()
```

Represents a file to be uploaded to the Sandbox.

**Attributes**:

- `source` _Union[bytes, str]_ - File contents as a bytes object or a local file path. If a bytes object is provided,
  make sure it fits into memory, otherwise use the local file path which content will be streamed to the Sandbox.
- `destination` _str_ - Absolute destination path in the Sandbox. Relative paths are resolved based on
  the sandbox working directory.

## FileDownloadRequest

```python
@dataclass
class FileDownloadRequest()
```

Represents a request to download a single file from the Sandbox.

**Attributes**:

- `source` _str_ - Source path in the Sandbox. Relative paths are resolved based on the user's
  root directory.
- `destination` _Optional[str]_ - Destination path in the local filesystem where the file content will be
  streamed to. If not provided, the file will be downloaded in the bytes buffer
  (might cause memory issues if the file is large).

## FileDownloadResponse

```python
@dataclass
class FileDownloadResponse()
```

Represents the response to a single file download request.

**Attributes**:

- `source` _str_ - The original source path requested for download.
- `result` _Union[str, bytes, None]_ - The download result - file path (if destination provided in the request)
  or bytes content (if no destination in the request), None if failed or no data received.
- `error` _Optional[str]_ - Error message if the download failed, None if successful.

## AsyncGit

```python
class AsyncGit()
```

Provides Git operations within a Sandbox.

**Example**:

```python
# Clone a repository
await sandbox.git.clone(
    url="https://github.com/user/repo.git",
    path="workspace/repo"
)

# Check repository status
status = await sandbox.git.status("workspace/repo")
print(f"Modified files: {status.modified}")

# Stage and commit changes
await sandbox.git.add("workspace/repo", ["file.txt"])
await sandbox.git.commit(
    path="workspace/repo",
    message="Update file",
    author="John Doe",
    email="john@example.com"
)
```

#### AsyncGit.\_\_init\_\_

```python
def __init__(api_client: GitApi)
```

Initializes a new Git handler instance.

**Arguments**:

- `api_client` _GitApi_ - API client for Sandbox Git operations.

#### AsyncGit.add

```python
@intercept_errors(message_prefix="Failed to add files: ")
async def add(path: str, files: List[str]) -> None
```

Stages the specified files for the next commit, similar to
running 'git add' on the command line.

**Arguments**:

- `path` _str_ - Path to the Git repository root. Relative paths are resolved based on
  the sandbox working directory.
- `files` _List[str]_ - List of file paths or directories to stage, relative to the repository root.
  

**Example**:

```python
# Stage a single file
await sandbox.git.add("workspace/repo", ["file.txt"])

# Stage multiple files
await sandbox.git.add("workspace/repo", [
    "src/main.py",
    "tests/test_main.py",
    "README.md"
])
```

#### AsyncGit.branches

```python
@intercept_errors(message_prefix="Failed to list branches: ")
async def branches(path: str) -> ListBranchResponse
```

Lists branches in the repository.

**Arguments**:

- `path` _str_ - Path to the Git repository root. Relative paths are resolved based on
  the sandbox working directory.
  

**Returns**:

- `ListBranchResponse` - List of branches in the repository.
  

**Example**:

```python
response = await sandbox.git.branches("workspace/repo")
print(f"Branches: {response.branches}")
```

#### AsyncGit.clone

```python
@intercept_errors(message_prefix="Failed to clone repository: ")
async def clone(url: str,
                path: str,
                branch: Optional[str] = None,
                commit_id: Optional[str] = None,
                username: Optional[str] = None,
                password: Optional[str] = None) -> None
```

Clones a Git repository into the specified path. It supports
cloning specific branches or commits, and can authenticate with the remote
repository if credentials are provided.

**Arguments**:

- `url` _str_ - Repository URL to clone from.
- `path` _str_ - Path where the repository should be cloned. Relative paths are resolved
  based on the sandbox working directory.
- `branch` _Optional[str]_ - Specific branch to clone. If not specified,
  clones the default branch.
- `commit_id` _Optional[str]_ - Specific commit to clone. If specified,
  the repository will be left in a detached HEAD state at this commit.
- `username` _Optional[str]_ - Git username for authentication.
- `password` _Optional[str]_ - Git password or token for authentication.
  

**Example**:

```python
# Clone the default branch
await sandbox.git.clone(
    url="https://github.com/user/repo.git",
    path="workspace/repo"
)

# Clone a specific branch with authentication
await sandbox.git.clone(
    url="https://github.com/user/private-repo.git",
    path="workspace/private",
    branch="develop",
    username="user",
    password="token"
)

# Clone a specific commit
await sandbox.git.clone(
    url="https://github.com/user/repo.git",
    path="workspace/repo-old",
    commit_id="abc123"
)
```

#### AsyncGit.commit

```python
@intercept_errors(message_prefix="Failed to commit changes: ")
async def commit(path: str,
                 message: str,
                 author: str,
                 email: str,
                 allow_empty: bool = False) -> GitCommitResponse
```

Creates a new commit with the staged changes. Make sure to stage
changes using the add() method before committing.

**Arguments**:

- `path` _str_ - Path to the Git repository root. Relative paths are resolved based on
  the sandbox working directory.
- `message` _str_ - Commit message describing the changes.
- `author` _str_ - Name of the commit author.
- `email` _str_ - Email address of the commit author.
- `allow_empty` _bool, optional_ - Allow creating an empty commit when no changes are staged. Defaults to False.
  

**Example**:

```python
# Stage and commit changes
await sandbox.git.add("workspace/repo", ["README.md"])
await sandbox.git.commit(
    path="workspace/repo",
    message="Update documentation",
    author="John Doe",
    email="john@example.com",
    allow_empty=True
)
```

#### AsyncGit.push

```python
@intercept_errors(message_prefix="Failed to push changes: ")
async def push(path: str,
               username: Optional[str] = None,
               password: Optional[str] = None) -> None
```

Pushes all local commits on the current branch to the remote
repository. If the remote repository requires authentication, provide
username and password/token.

**Arguments**:

- `path` _str_ - Path to the Git repository root. Relative paths are resolved based on
  the sandbox working directory.
- `username` _Optional[str]_ - Git username for authentication.
- `password` _Optional[str]_ - Git password or token for authentication.
  

**Example**:

```python
# Push without authentication (for public repos or SSH)
await sandbox.git.push("workspace/repo")

# Push with authentication
await sandbox.git.push(
    path="workspace/repo",
    username="user",
    password="github_token"
)
```

#### AsyncGit.pull

```python
@intercept_errors(message_prefix="Failed to pull changes: ")
async def pull(path: str,
               username: Optional[str] = None,
               password: Optional[str] = None) -> None
```

Pulls changes from the remote repository. If the remote repository requires authentication,
provide username and password/token.

**Arguments**:

- `path` _str_ - Path to the Git repository root. Relative paths are resolved based on
  the sandbox working directory.
- `username` _Optional[str]_ - Git username for authentication.
- `password` _Optional[str]_ - Git password or token for authentication.
  

**Example**:

```python
# Pull without authentication
await sandbox.git.pull("workspace/repo")

# Pull with authentication
await sandbox.git.pull(
    path="workspace/repo",
    username="user",
    password="github_token"
)
```

#### AsyncGit.status

```python
@intercept_errors(message_prefix="Failed to get status: ")
async def status(path: str) -> GitStatus
```

Gets the current Git repository status.

**Arguments**:

- `path` _str_ - Path to the Git repository root. Relative paths are resolved based on
  the sandbox working directory.
  

**Returns**:

- `GitStatus` - Repository status information including:
  - current_branch: Current branch name
  - file_status: List of file statuses
  - ahead: Number of local commits not pushed to remote
  - behind: Number of remote commits not pulled locally
  - branch_published: Whether the branch has been published to the remote repository
  

**Example**:

```python
status = await sandbox.git.status("workspace/repo")
print(f"On branch: {status.current_branch}")
print(f"Commits ahead: {status.ahead}")
print(f"Commits behind: {status.behind}")
```

#### AsyncGit.checkout\_branch

```python
@intercept_errors(message_prefix="Failed to checkout branch: ")
async def checkout_branch(path: str, branch: str) -> None
```

Checkout branch in the repository.

**Arguments**:

- `path` _str_ - Path to the Git repository root. Relative paths are resolved based on
  the sandbox working directory.
- `branch` _str_ - Name of the branch to checkout
  

**Example**:

```python
# Checkout a branch
await sandbox.git.checkout_branch("workspace/repo", "feature-branch")
```

#### AsyncGit.create\_branch

```python
@intercept_errors(message_prefix="Failed to create branch: ")
async def create_branch(path: str, name: str) -> None
```

Create branch in the repository.

**Arguments**:

- `path` _str_ - Path to the Git repository root. Relative paths are resolved based on
  the sandbox working directory.
- `name` _str_ - Name of the new branch to create
  

**Example**:

```python
# Create a new branch
await sandbox.git.create_branch("workspace/repo", "new-feature")
```

#### AsyncGit.delete\_branch

```python
@intercept_errors(message_prefix="Failed to delete branch: ")
async def delete_branch(path: str, name: str) -> None
```

Delete branch in the repository.

**Arguments**:

- `path` _str_ - Path to the Git repository root. Relative paths are resolved based on
  the sandbox working directory.
- `name` _str_ - Name of the branch to delete
  

**Example**:

```python
# Delete a branch
await sandbox.git.delete_branch("workspace/repo", "old-feature")
```


## GitCommitResponse

```python
class GitCommitResponse()
```

Response from the git commit.

**Attributes**:

- `sha` _str_ - The SHA of the commit

## AsyncLspServer

```python
class AsyncLspServer()
```

Provides Language Server Protocol functionality for code intelligence to provide
IDE-like features such as code completion, symbol search, and more.

#### AsyncLspServer.\_\_init\_\_

```python
def __init__(language_id: LspLanguageId, path_to_project: str,
             api_client: LspApi)
```

Initializes a new LSP server instance.

**Arguments**:

- `language_id` _LspLanguageId_ - The language server type (e.g., LspLanguageId.TYPESCRIPT).
- `path_to_project` _str_ - Absolute path to the project root directory.
- `api_client` _LspApi_ - API client for Sandbox operations.
- `instance` _SandboxInstance_ - The Sandbox instance this server belongs to.

#### AsyncLspServer.start

```python
@intercept_errors(message_prefix="Failed to start LSP server: ")
async def start() -> None
```

Starts the language server.

This method must be called before using any other LSP functionality.
It initializes the language server for the specified language and project.

**Example**:

```python
lsp = sandbox.create_lsp_server("typescript", "workspace/project")
await lsp.start()  # Initialize the server
# Now ready for LSP operations
```

#### AsyncLspServer.stop

```python
@intercept_errors(message_prefix="Failed to stop LSP server: ")
async def stop() -> None
```

Stops the language server.

This method should be called when the LSP server is no longer needed to
free up system resources.

**Example**:

```python
# When done with LSP features
await lsp.stop()  # Clean up resources
```

#### AsyncLspServer.did\_open

```python
@intercept_errors(message_prefix="Failed to open file: ")
async def did_open(path: str) -> None
```

Notifies the language server that a file has been opened.

This method should be called when a file is opened in the editor to enable
language features like diagnostics and completions for that file. The server
will begin tracking the file's contents and providing language features.

**Arguments**:

- `path` _str_ - Path to the opened file. Relative paths are resolved based on the project path
  set in the LSP server constructor.
  

**Example**:

```python
# When opening a file for editing
await lsp.did_open("workspace/project/src/index.ts")
# Now can get completions, symbols, etc. for this file
```

#### AsyncLspServer.did\_close

```python
@intercept_errors(message_prefix="Failed to close file: ")
async def did_close(path: str) -> None
```

Notify the language server that a file has been closed.

This method should be called when a file is closed in the editor to allow
the language server to clean up any resources associated with that file.

**Arguments**:

- `path` _str_ - Path to the closed file. Relative paths are resolved based on the project path
  set in the LSP server constructor.
  

**Example**:

```python
# When done editing a file
await lsp.did_close("workspace/project/src/index.ts")
```

#### AsyncLspServer.document\_symbols

```python
@intercept_errors(message_prefix="Failed to get symbols from document: ")
async def document_symbols(path: str) -> List[LspSymbol]
```

Gets symbol information (functions, classes, variables, etc.) from a document.

**Arguments**:

- `path` _str_ - Path to the file to get symbols from. Relative paths are resolved based on the project path
  set in the LSP server constructor.
  

**Returns**:

- `List[LspSymbol]` - List of symbols in the document. Each symbol includes:
  - name: The symbol's name
  - kind: The symbol's kind (function, class, variable, etc.)
  - location: The location of the symbol in the file
  

**Example**:

```python
# Get all symbols in a file
symbols = await lsp.document_symbols("workspace/project/src/index.ts")
for symbol in symbols:
    print(f"{symbol.kind} {symbol.name}: {symbol.location}")
```

#### AsyncLspServer.workspace\_symbols

```python
@deprecated(
    reason=
    "Method is deprecated. Use `sandbox_symbols` instead. This method will be removed in a future version."
)
async def workspace_symbols(query: str) -> List[LspSymbol]
```

Searches for symbols matching the query string across all files
in the Sandbox.

**Arguments**:

- `query` _str_ - Search query to match against symbol names.
  

**Returns**:

- `List[LspSymbol]` - List of matching symbols from all files.

#### AsyncLspServer.sandbox\_symbols

```python
@intercept_errors(message_prefix="Failed to get symbols from sandbox: ")
async def sandbox_symbols(query: str) -> List[LspSymbol]
```

Searches for symbols matching the query string across all files
in the Sandbox.

**Arguments**:

- `query` _str_ - Search query to match against symbol names.
  

**Returns**:

- `List[LspSymbol]` - List of matching symbols from all files. Each symbol
  includes:
  - name: The symbol's name
  - kind: The symbol's kind (function, class, variable, etc.)
  - location: The location of the symbol in the file
  

**Example**:

```python
# Search for all symbols containing "User"
symbols = await lsp.sandbox_symbols("User")
for symbol in symbols:
    print(f"{symbol.name} in {symbol.location}")
```

#### AsyncLspServer.completions

```python
@intercept_errors(message_prefix="Failed to get completions: ")
async def completions(path: str,
                      position: LspCompletionPosition) -> CompletionList
```

Gets completion suggestions at a position in a file.

**Arguments**:

- `path` _str_ - Path to the file. Relative paths are resolved based on the project path
  set in the LSP server constructor.
- `position` _LspCompletionPosition_ - Cursor position to get completions for.
  

**Returns**:

- `CompletionList` - List of completion suggestions. The list includes:
  - isIncomplete: Whether more items might be available
  - items: List of completion items, each containing:
  - label: The text to insert
  - kind: The kind of completion
  - detail: Additional details about the item
  - documentation: Documentation for the item
  - sortText: Text used to sort the item in the list
  - filterText: Text used to filter the item
  - insertText: The actual text to insert (if different from label)
  

**Example**:

```python
# Get completions at a specific position
pos = LspCompletionPosition(line=10, character=15)
completions = await lsp.completions("workspace/project/src/index.ts", pos)
for item in completions.items:
    print(f"{item.label} ({item.kind}): {item.detail}")
```


## LspLanguageId

```python
class LspLanguageId(Enum)
```

Language IDs for Language Server Protocol (LSP).

**Enum Members**:
    - `PYTHON` ("python")
    - `TYPESCRIPT` ("typescript")
    - `JAVASCRIPT` ("javascript")

## LspCompletionPosition

```python
class LspCompletionPosition()
```

Represents a zero-based completion position in a text document,
specified by line number and character offset.

**Attributes**:

- `line` _int_ - Zero-based line number in the document.
- `character` _int_ - Zero-based character offset on the line.

#### LspCompletionPosition.\_\_init\_\_

```python
def __init__(line: int, character: int)
```

Initialize a new LspCompletionPosition instance.

**Arguments**:

- `line` _int_ - Zero-based line number in the document.
- `character` _int_ - Zero-based character offset on the line.

## AsyncObjectStorage

```python
class AsyncObjectStorage()
```

AsyncObjectStorage class for interacting with object storage services.

**Attributes**:

- `endpoint_url` _str_ - The endpoint URL for the object storage service.
- `aws_access_key_id` _str_ - The access key ID for the object storage service.
- `aws_secret_access_key` _str_ - The secret access key for the object storage service.
- `aws_session_token` _str_ - The session token for the object storage service. Used for temporary credentials.
- `bucket_name` _str_ - The name of the bucket to use. Defaults to "daytona-volume-builds".

#### AsyncObjectStorage.upload

```python
async def upload(path: str,
                 organization_id: str,
                 archive_base_path: str | None = None) -> str
```

Uploads a file to the object storage service.

**Arguments**:

- `path` _str_ - The path to the file to upload.
- `organization_id` _str_ - The organization ID to use.
- `archive_base_path` _str_ - The base path to use for the archive.
  

**Returns**:

- `str` - The hash of the uploaded file.

## AsyncSandbox

```python
class AsyncSandbox(SandboxDto)
```

Represents a Daytona Sandbox.

**Attributes**:

- `fs` _AsyncFileSystem_ - File system operations interface.
- `git` _AsyncGit_ - Git operations interface.
- `process` _AsyncProcess_ - Process execution interface.
- `computer_use` _AsyncComputerUse_ - Computer use operations interface for desktop automation.
- `id` _str_ - Unique identifier for the Sandbox.
- `name` _str_ - Name of the Sandbox.
- `organization_id` _str_ - Organization ID of the Sandbox.
- `snapshot` _str_ - Daytona snapshot used to create the Sandbox.
- `user` _str_ - OS user running in the Sandbox.
- `env` _Dict[str, str]_ - Environment variables set in the Sandbox.
- `labels` _Dict[str, str]_ - Custom labels attached to the Sandbox.
- `public` _bool_ - Whether the Sandbox is publicly accessible.
- `target` _str_ - Target location of the runner where the Sandbox runs.
- `cpu` _int_ - Number of CPUs allocated to the Sandbox.
- `gpu` _int_ - Number of GPUs allocated to the Sandbox.
- `memory` _int_ - Amount of memory allocated to the Sandbox in GiB.
- `disk` _int_ - Amount of disk space allocated to the Sandbox in GiB.
- `state` _SandboxState_ - Current state of the Sandbox (e.g., "started", "stopped").
- `error_reason` _str_ - Error message if Sandbox is in error state.
- `backup_state` _SandboxBackupStateEnum_ - Current state of Sandbox backup.
- `backup_created_at` _str_ - When the backup was created.
- `auto_stop_interval` _int_ - Auto-stop interval in minutes.
- `auto_archive_interval` _int_ - Auto-archive interval in minutes.
- `auto_delete_interval` _int_ - Auto-delete interval in minutes.
- `volumes` _List[str]_ - Volumes attached to the Sandbox.
- `build_info` _str_ - Build information for the Sandbox if it was created from dynamic build.
- `created_at` _str_ - When the Sandbox was created.
- `updated_at` _str_ - When the Sandbox was last updated.
- `network_block_all` _bool_ - Whether to block all network access for the Sandbox.
- `network_allow_list` _str_ - Comma-separated list of allowed CIDR network addresses for the Sandbox.

#### AsyncSandbox.\_\_init\_\_

```python
def __init__(sandbox_dto: SandboxDto, toolbox_api: ApiClient,
             sandbox_api: SandboxApi, code_toolbox: SandboxCodeToolbox,
             get_toolbox_base_url: Callable[[], Awaitable[str]])
```

Initialize a new Sandbox instance.

**Arguments**:

- `sandbox_dto` _SandboxDto_ - The sandbox data from the API.
- `toolbox_api` _ApiClient_ - API client for toolbox operations.
- `sandbox_api` _SandboxApi_ - API client for Sandbox operations.
- `code_toolbox` _SandboxCodeToolbox_ - Language-specific toolbox implementation.
- `get_toolbox_base_url` _Callable[[], Awaitable[str]]_ - Function to get the toolbox base URL.

#### AsyncSandbox.refresh\_data

```python
@intercept_errors(message_prefix="Failed to refresh sandbox data: ")
async def refresh_data() -> None
```

Refreshes the Sandbox data from the API.

**Example**:

```python
await sandbox.refresh_data()
print(f"Sandbox {sandbox.id}:")
print(f"State: {sandbox.state}")
print(f"Resources: {sandbox.cpu} CPU, {sandbox.memory} GiB RAM")
```

#### AsyncSandbox.get\_user\_home\_dir

```python
@intercept_errors(message_prefix="Failed to get user home directory: ")
async def get_user_home_dir() -> str
```

Gets the user's home directory path inside the Sandbox.

**Returns**:

- `str` - The absolute path to the user's home directory inside the Sandbox.
  

**Example**:

```python
user_home_dir = await sandbox.get_user_home_dir()
print(f"Sandbox user home: {user_home_dir}")
```

#### AsyncSandbox.get\_work\_dir

```python
@intercept_errors(message_prefix="Failed to get working directory path: ")
async def get_work_dir() -> str
```

Gets the working directory path inside the Sandbox.

**Returns**:

- `str` - The absolute path to the Sandbox working directory. Uses the WORKDIR specified in
  the Dockerfile if present, or falling back to the user's home directory if not.
  

**Example**:

```python
work_dir = await sandbox.get_work_dir()
print(f"Sandbox working directory: {work_dir}")
```

#### AsyncSandbox.create\_lsp\_server

```python
def create_lsp_server(language_id: LspLanguageId,
                      path_to_project: str) -> AsyncLspServer
```

Creates a new Language Server Protocol (LSP) server instance.

The LSP server provides language-specific features like code completion,
diagnostics, and more.

**Arguments**:

- `language_id` _LspLanguageId_ - The language server type (e.g., LspLanguageId.PYTHON).
- `path_to_project` _str_ - Path to the project root directory. Relative paths are resolved
  based on the sandbox working directory.
  

**Returns**:

- `LspServer` - A new LSP server instance configured for the specified language.
  

**Example**:

```python
lsp = sandbox.create_lsp_server("python", "workspace/project")
```

#### AsyncSandbox.set\_labels

```python
@intercept_errors(message_prefix="Failed to set labels: ")
async def set_labels(labels: Dict[str, str]) -> Dict[str, str]
```

Sets labels for the Sandbox.

Labels are key-value pairs that can be used to organize and identify Sandboxes.

**Arguments**:

- `labels` _Dict[str, str]_ - Dictionary of key-value pairs representing Sandbox labels.
  

**Returns**:

  Dict[str, str]: Dictionary containing the updated Sandbox labels.
  

**Example**:

```python
new_labels = sandbox.set_labels({
    "project": "my-project",
    "environment": "development",
    "team": "backend"
})
print(f"Updated labels: {new_labels}")
```

#### AsyncSandbox.start

```python
@intercept_errors(message_prefix="Failed to start sandbox: ")
@with_timeout(error_message=lambda self, timeout: (
    f"Sandbox {self.id} failed to start within the {timeout} seconds timeout period"
))
async def start(timeout: Optional[float] = 60)
```

Starts the Sandbox and waits for it to be ready.

**Arguments**:

- `timeout` _Optional[float]_ - Maximum time to wait in seconds. 0 means no timeout. Default is 60 seconds.
  

**Raises**:

- `DaytonaError` - If timeout is negative. If sandbox fails to start or times out.
  

**Example**:

```python
sandbox = daytona.get_current_sandbox("my-sandbox")
sandbox.start(timeout=40)  # Wait up to 40 seconds
print("Sandbox started successfully")
```

#### AsyncSandbox.stop

```python
@intercept_errors(message_prefix="Failed to stop sandbox: ")
@with_timeout(error_message=lambda self, timeout: (
    f"Sandbox {self.id} failed to stop within the {timeout} seconds timeout period"
))
async def stop(timeout: Optional[float] = 60)
```

Stops the Sandbox and waits for it to be fully stopped.

**Arguments**:

- `timeout` _Optional[float]_ - Maximum time to wait in seconds. 0 means no timeout. Default is 60 seconds.
  

**Raises**:

- `DaytonaError` - If timeout is negative; If sandbox fails to stop or times out
  

**Example**:

```python
sandbox = daytona.get_current_sandbox("my-sandbox")
sandbox.stop()
print("Sandbox stopped successfully")
```

#### AsyncSandbox.delete

```python
@intercept_errors(message_prefix="Failed to remove sandbox: ")
async def delete(timeout: Optional[float] = 60) -> None
```

Deletes the Sandbox.

**Arguments**:

- `timeout` _Optional[float]_ - Timeout (in seconds) for sandbox deletion. 0 means no timeout.
  Default is 60 seconds.

#### AsyncSandbox.wait\_for\_sandbox\_start

```python
@intercept_errors(
    message_prefix="Failure during waiting for sandbox to start: ")
@with_timeout(error_message=lambda self, timeout: (
    f"Sandbox {self.id} failed to become ready within the {timeout} seconds timeout period"
))
async def wait_for_sandbox_start(timeout: Optional[float] = 60) -> None
```

Waits for the Sandbox to reach the 'started' state. Polls the Sandbox status until it
reaches the 'started' state, encounters an error or times out.

**Arguments**:

- `timeout` _Optional[float]_ - Maximum time to wait in seconds. 0 means no timeout. Default is 60 seconds.
  

**Raises**:

- `DaytonaError` - If timeout is negative; If Sandbox fails to start or times out

#### AsyncSandbox.wait\_for\_sandbox\_stop

```python
@intercept_errors(
    message_prefix="Failure during waiting for sandbox to stop: ")
@with_timeout(error_message=lambda self, timeout: (
    f"Sandbox {self.id} failed to become stopped within the {timeout} seconds timeout period"
))
async def wait_for_sandbox_stop(timeout: Optional[float] = 60) -> None
```

Waits for the Sandbox to reach the 'stopped' state. Polls the Sandbox status until it
reaches the 'stopped' state, encounters an error or times out. It will wait up to 60 seconds
for the Sandbox to stop.
Treats destroyed as stopped to cover ephemeral sandboxes that are automatically deleted after stopping.

**Arguments**:

- `timeout` _Optional[float]_ - Maximum time to wait in seconds. 0 means no timeout. Default is 60 seconds.
  

**Raises**:

- `DaytonaError` - If timeout is negative. If Sandbox fails to stop or times out.

#### AsyncSandbox.set\_autostop\_interval

```python
@intercept_errors(message_prefix="Failed to set auto-stop interval: ")
async def set_autostop_interval(interval: int) -> None
```

Sets the auto-stop interval for the Sandbox.

The Sandbox will automatically stop after being idle (no new events) for the specified interval.
Events include any state changes or interactions with the Sandbox through the SDK.
Interactions using Sandbox Previews are not included.

**Arguments**:

- `interval` _int_ - Number of minutes of inactivity before auto-stopping.
  Set to 0 to disable auto-stop. Defaults to 15.
  

**Raises**:

- `DaytonaError` - If interval is negative
  

**Example**:

```python
# Auto-stop after 1 hour
sandbox.set_autostop_interval(60)
# Or disable auto-stop
sandbox.set_autostop_interval(0)
```

#### AsyncSandbox.set\_auto\_archive\_interval

```python
@intercept_errors(message_prefix="Failed to set auto-archive interval: ")
async def set_auto_archive_interval(interval: int) -> None
```

Sets the auto-archive interval for the Sandbox.

The Sandbox will automatically archive after being continuously stopped for the specified interval.

**Arguments**:

- `interval` _int_ - Number of minutes after which a continuously stopped Sandbox will be auto-archived.
  Set to 0 for the maximum interval. Default is 7 days.
  

**Raises**:

- `DaytonaError` - If interval is negative
  

**Example**:

```python
# Auto-archive after 1 hour
sandbox.set_auto_archive_interval(60)
# Or use the maximum interval
sandbox.set_auto_archive_interval(0)
```

#### AsyncSandbox.set\_auto\_delete\_interval

```python
@intercept_errors(message_prefix="Failed to set auto-delete interval: ")
async def set_auto_delete_interval(interval: int) -> None
```

Sets the auto-delete interval for the Sandbox.

The Sandbox will automatically delete after being continuously stopped for the specified interval.

**Arguments**:

- `interval` _int_ - Number of minutes after which a continuously stopped Sandbox will be auto-deleted.
  Set to negative value to disable auto-delete. Set to 0 to delete immediately upon stopping.
  By default, auto-delete is disabled.
  

**Example**:

```python
# Auto-delete after 1 hour
sandbox.set_auto_delete_interval(60)
# Or delete immediately upon stopping
sandbox.set_auto_delete_interval(0)
# Or disable auto-delete
sandbox.set_auto_delete_interval(-1)
```

#### AsyncSandbox.get\_preview\_link

```python
@intercept_errors(message_prefix="Failed to get preview link: ")
async def get_preview_link(port: int) -> PortPreviewUrl
```

Retrieves the preview link for the sandbox at the specified port. If the port is closed,
it will be opened automatically. For private sandboxes, a token is included to grant access
to the URL.

**Arguments**:

- `port` _int_ - The port to open the preview link on.
  

**Returns**:

- `PortPreviewUrl` - The response object for the preview link, which includes the `url`
  and the `token` (to access private sandboxes).
  

**Example**:

```python
preview_link = sandbox.get_preview_link(3000)
print(f"Preview URL: {preview_link.url}")
print(f"Token: {preview_link.token}")
```

#### AsyncSandbox.archive

```python
@intercept_errors(message_prefix="Failed to archive sandbox: ")
async def archive() -> None
```

Archives the sandbox, making it inactive and preserving its state. When sandboxes are
archived, the entire filesystem state is moved to cost-effective object storage, making it
possible to keep sandboxes available for an extended period. The tradeoff between archived
and stopped states is that starting an archived sandbox takes more time, depending on its size.
Sandbox must be stopped before archiving.

#### AsyncSandbox.create\_ssh\_access

```python
@intercept_errors(message_prefix="Failed to create SSH access: ")
async def create_ssh_access(
        expires_in_minutes: Optional[int] = None) -> SshAccessDto
```

Creates an SSH access token for the sandbox.

**Arguments**:

- `expires_in_minutes` _Optional[int]_ - The number of minutes the SSH access token will be valid for.

#### AsyncSandbox.revoke\_ssh\_access

```python
@intercept_errors(message_prefix="Failed to revoke SSH access: ")
async def revoke_ssh_access(token: str) -> None
```

Revokes an SSH access token for the sandbox.

**Arguments**:

- `token` _str_ - The token to revoke.

#### AsyncSandbox.validate\_ssh\_access

```python
@intercept_errors(message_prefix="Failed to validate SSH access: ")
async def validate_ssh_access(token: str) -> SshAccessValidationDto
```

Validates an SSH access token for the sandbox.

**Arguments**:

- `token` _str_ - The token to validate.


## AsyncPaginatedSandboxes

```python
class AsyncPaginatedSandboxes(PaginatedSandboxesDto)
```

Represents a paginated list of Daytona Sandboxes.

**Attributes**:

- `items` _List[AsyncSandbox]_ - List of Sandbox instances in the current page.
- `total` _int_ - Total number of Sandboxes across all pages.
- `page` _int_ - Current page number.
- `total_pages` _int_ - Total number of pages available.

## Resources

```python
@dataclass
class Resources()
```

Resources configuration for Sandbox.

**Attributes**:

- `cpu` _Optional[int]_ - Number of CPU cores to allocate.
- `memory` _Optional[int]_ - Amount of memory in GiB to allocate.
- `disk` _Optional[int]_ - Amount of disk space in GiB to allocate.
- `gpu` _Optional[int]_ - Number of GPUs to allocate.
  

**Example**:

```python
resources = Resources(
    cpu=2,
    memory=4,  # 4GiB RAM
    disk=20,   # 20GiB disk
    gpu=1
)
params = CreateSandboxFromImageParams(
    image=Image.debian_slim("3.12"),
    language="python",
    resources=resources
)
```

## Snapshot

```python
class Snapshot(SnapshotDto)
```

Represents a Daytona Snapshot which is a pre-configured sandbox.

**Attributes**:

- `id` _StrictStr_ - Unique identifier for the Snapshot.
- `organization_id` _Optional[StrictStr]_ - Organization ID of the Snapshot.
- `general` _Optional[bool]_ - Whether the Snapshot is general.
- `name` _StrictStr_ - Name of the Snapshot.
- `image_name` _StrictStr_ - Name of the Image of the Snapshot.
- `state` _StrictStr_ - State of the Snapshot.
- `size` _Optional[Union[StrictFloat, StrictInt]]_ - Size of the Snapshot.
- `entrypoint` _Optional[List[str]]_ - Entrypoint of the Snapshot.
- `cpu` _Union[StrictFloat, StrictInt]_ - CPU of the Snapshot.
- `gpu` _Union[StrictFloat, StrictInt]_ - GPU of the Snapshot.
- `mem` _Union[StrictFloat, StrictInt]_ - Memory of the Snapshot in GiB.
- `disk` _Union[StrictFloat, StrictInt]_ - Disk of the Snapshot in GiB.
- `error_reason` _Optional[StrictStr]_ - Error reason of the Snapshot.
- `created_at` _StrictStr_ - Timestamp when the Snapshot was created.
- `updated_at` _StrictStr_ - Timestamp when the Snapshot was last updated.
- `last_used_at` _StrictStr_ - Timestamp when the Snapshot was last used.


## AsyncSnapshotService

```python
class AsyncSnapshotService()
```

Service for managing Daytona Snapshots. Can be used to list, get, create and delete Snapshots.

#### AsyncSnapshotService.list

```python
@intercept_errors(message_prefix="Failed to list snapshots: ")
async def list(page: Optional[int] = None,
               limit: Optional[int] = None) -> PaginatedSnapshots
```

Returns paginated list of Snapshots.

**Arguments**:

- `page` _Optional[int]_ - Page number for pagination (starting from 1).
- `limit` _Optional[int]_ - Maximum number of items per page.
  

**Returns**:

- `PaginatedSnapshots` - Paginated list of Snapshots.
  

**Example**:

```python
async with AsyncDaytona() as daytona:
    result = await daytona.snapshot.list(page=2, limit=10)
    for snapshot in result.items:
        print(f"{snapshot.name} ({snapshot.image_name})")
```

#### AsyncSnapshotService.delete

```python
@intercept_errors(message_prefix="Failed to delete snapshot: ")
async def delete(snapshot: Snapshot) -> None
```

Delete a Snapshot.

**Arguments**:

- `snapshot` _Snapshot_ - Snapshot to delete.
  

**Example**:

```python
async with AsyncDaytona() as daytona:
    snapshot = await daytona.snapshot.get("test-snapshot")
    await daytona.snapshot.delete(snapshot)
    print("Snapshot deleted")
```

#### AsyncSnapshotService.get

```python
@intercept_errors(message_prefix="Failed to get snapshot: ")
async def get(name: str) -> Snapshot
```

Get a Snapshot by name.

**Arguments**:

- `name` _str_ - Name of the Snapshot to get.
  

**Returns**:

- `Snapshot` - The Snapshot object.
  

**Example**:

```python
async with AsyncDaytona() as daytona:
    snapshot = await daytona.snapshot.get("test-snapshot-name")
    print(f"{snapshot.name} ({snapshot.image_name})")
```

#### AsyncSnapshotService.create

```python
@intercept_errors(message_prefix="Failed to create snapshot: ")
@with_timeout(error_message=lambda self, timeout: (
    f"Failed to create snapshot within {timeout} seconds timeout period."))
async def create(params: CreateSnapshotParams,
                 *,
                 on_logs: Callable[[str], None] = None,
                 timeout: Optional[float] = 0) -> Snapshot
```

Creates and registers a new snapshot from the given Image definition.

**Arguments**:

- `params` _CreateSnapshotParams_ - Parameters for snapshot creation.
- `on_logs` _Callable[[str], None]_ - This callback function handles snapshot creation logs.
- `timeout` _Optional[float]_ - Default is no timeout. Timeout in seconds (0 means no timeout).

**Example**:

```python
image = Image.debianSlim('3.12').pipInstall('numpy')
daytona.snapshot.create(
    CreateSnapshotParams(name='my-snapshot', image=image),
    on_logs=lambda chunk: print(chunk, end=""),
)
```

#### AsyncSnapshotService.activate

```python
async def activate(snapshot: Snapshot) -> Snapshot
```

Activate a snapshot.

**Arguments**:

- `snapshot` _Snapshot_ - The Snapshot instance.

**Returns**:

- `Snapshot` - The activated Snapshot instance.

#### AsyncSnapshotService.process\_image\_context

```python
@staticmethod
async def process_image_context(object_storage_api: ObjectStorageApi,
                                image: Image) -> List[str]
```

Processes the image context by uploading it to object storage.

**Arguments**:

- `image` _Image_ - The Image instance.

**Returns**:

- `List[str]` - List of context hashes stored in object storage.

## PaginatedSnapshots

```python
class PaginatedSnapshots(PaginatedSnapshotsDto)
```

Represents a paginated list of Daytona Snapshots.

**Attributes**:

- `items` _List[Snapshot]_ - List of Snapshot instances in the current page.
- `total` _int_ - Total number of Snapshots across all pages.
- `page` _int_ - Current page number.
- `total_pages` _int_ - Total number of pages available.

## CreateSnapshotParams

```python
class CreateSnapshotParams(BaseModel)
```

Parameters for creating a new snapshot.

**Attributes**:

- `name` _Optional[str]_ - Name of the snapshot.
- `image` _Union[str, Image]_ - Image of the snapshot. If a string is provided,
  it should be available on some registry. If an Image instance is provided,
  it will be used to create a new image in Daytona.
- `resources` _Optional[Resources]_ - Resources of the snapshot.
- `entrypoint` _Optional[List[str]]_ - Entrypoint of the snapshot.

## Volume

```python
class Volume(VolumeDto)
```

Represents a Daytona Volume which is a shared storage volume for Sandboxes.

**Attributes**:

- `id` _StrictStr_ - Unique identifier for the Volume.
- `name` _StrictStr_ - Name of the Volume.
- `organization_id` _StrictStr_ - Organization ID of the Volume.
- `state` _StrictStr_ - State of the Volume.
- `created_at` _StrictStr_ - Date and time when the Volume was created.
- `updated_at` _StrictStr_ - Date and time when the Volume was last updated.
- `last_used_at` _StrictStr_ - Date and time when the Volume was last used.


## AsyncVolumeService

```python
class AsyncVolumeService()
```

Service for managing Daytona Volumes. Can be used to list, get, create and delete Volumes.

#### AsyncVolumeService.list

```python
async def list() -> List[Volume]
```

List all Volumes.

**Returns**:

- `List[Volume]` - List of all Volumes.
  

**Example**:

```python
async with AsyncDaytona() as daytona:
    volumes = await daytona.volume.list()
    for volume in volumes:
        print(f"{volume.name} ({volume.id})")
```

#### AsyncVolumeService.get

```python
async def get(name: str, create: bool = False) -> Volume
```

Get a Volume by name.

**Arguments**:

- `name` _str_ - Name of the Volume to get.
- `create` _bool_ - If True, create a new Volume if it doesn't exist.
  

**Returns**:

- `Volume` - The Volume object.
  

**Example**:

```python
async with AsyncDaytona() as daytona:
    volume = await daytona.volume.get("test-volume-name", create=True)
    print(f"{volume.name} ({volume.id})")
```

#### AsyncVolumeService.create

```python
async def create(name: str) -> Volume
```

Create a new Volume.

**Arguments**:

- `name` _str_ - Name of the Volume to create.
  

**Returns**:

- `Volume` - The Volume object.
  

**Example**:

```python
async with AsyncDaytona() as daytona:
    volume = await daytona.volume.create("test-volume")
    print(f"{volume.name} ({volume.id}); state: {volume.state}")
```

#### AsyncVolumeService.delete

```python
async def delete(volume: Volume) -> None
```

Delete a Volume.

**Arguments**:

- `volume` _Volume_ - Volume to delete.
  

**Example**:

```python
async with AsyncDaytona() as daytona:
    volume = await daytona.volume.get("test-volume")
    await daytona.volume.delete(volume)
    print("Volume deleted")
```

## Chart

```python
class Chart()
```

Represents a chart with metadata from matplotlib.

**Attributes**:

- `type` _ChartType_ - The type of chart
- `title` _str_ - The title of the chart
- `elements` _List[Any]_ - The elements of the chart
- `png` _Optional[str]_ - The PNG representation of the chart encoded in base64


## ChartType

```python
class ChartType(str, Enum)
```

Chart types

**Enum Members**:
    - `LINE` ("line")
    - `SCATTER` ("scatter")
    - `BAR` ("bar")
    - `PIE` ("pie")
    - `BOX_AND_WHISKER` ("box_and_whisker")
    - `COMPOSITE_CHART` ("composite_chart")
    - `UNKNOWN` ("unknown")

## Chart2D

```python
class Chart2D(Chart)
```

Represents a 2D chart with metadata.

**Attributes**:

- `x_label` _Optional[str]_ - The label of the x-axis
- `y_label` _Optional[str]_ - The label of the y-axis

## PointData

```python
class PointData()
```

Represents a point in a 2D chart.

**Attributes**:

- `label` _str_ - The label of the point
- `points` _List[Tuple[Union[str, float], Union[str, float]]]_ - The points of the chart

## PointChart

```python
class PointChart(Chart2D)
```

Represents a point chart with metadata.

**Attributes**:

- `x_ticks` _List[Union[str, float]]_ - The ticks of the x-axis
- `x_tick_labels` _List[str]_ - The labels of the x-axis
- `x_scale` _str_ - The scale of the x-axis
- `y_ticks` _List[Union[str, float]]_ - The ticks of the y-axis
- `y_tick_labels` _List[str]_ - The labels of the y-axis
- `y_scale` _str_ - The scale of the y-axis
- `elements` _List[PointData]_ - The points of the chart

## LineChart

```python
class LineChart(PointChart)
```

Represents a line chart with metadata.

**Attributes**:

- `type` _ChartType_ - The type of chart

## ScatterChart

```python
class ScatterChart(PointChart)
```

Represents a scatter chart with metadata.

**Attributes**:

- `type` _ChartType_ - The type of chart

## BarData

```python
class BarData()
```

Represents a bar in a bar chart.

**Attributes**:

- `label` _str_ - The label of the bar
- `group` _str_ - The group of the bar
- `value` _str_ - The value of the bar

## BarChart

```python
class BarChart(Chart2D)
```

Represents a bar chart with metadata.

**Attributes**:

- `type` _ChartType_ - The type of chart
- `elements` _List[BarData]_ - The bars of the chart

## PieData

```python
class PieData()
```

Represents a pie slice in a pie chart.

**Attributes**:

- `label` _str_ - The label of the pie slice
- `angle` _float_ - The angle of the pie slice
- `radius` _float_ - The radius of the pie slice
- `autopct` _float_ - The autopct value of the pie slice

## PieChart

```python
class PieChart(Chart)
```

Represents a pie chart with metadata.

**Attributes**:

- `type` _ChartType_ - The type of chart
- `elements` _List[PieData]_ - The pie slices of the chart

## BoxAndWhiskerData

```python
class BoxAndWhiskerData()
```

Represents a box and whisker in a box and whisker chart.

**Attributes**:

- `label` _str_ - The label of the box and whisker
- `min` _float_ - The minimum value of the box and whisker
- `first_quartile` _float_ - The first quartile of the box and whisker
- `median` _float_ - The median of the box and whisker
- `third_quartile` _float_ - The third quartile of the box and whisker
- `max` _float_ - The maximum value of the box and whisker
- `outliers` _List[float]_ - The outliers of the box and whisker

## BoxAndWhiskerChart

```python
class BoxAndWhiskerChart(Chart2D)
```

Represents a box and whisker chart with metadata.

**Attributes**:

- `type` _ChartType_ - The type of chart
- `elements` _List[BoxAndWhiskerData]_ - The box and whiskers of the chart

## CompositeChart

```python
class CompositeChart(Chart)
```

Represents a composite chart with metadata. A composite chart is a chart
that contains multiple charts (subplots).

**Attributes**:

- `type` _ChartType_ - The type of chart
- `elements` _List[Chart]_ - The charts (subplots) of the composite chart

## DaytonaError

```python
class DaytonaError(Exception)
```

Base error for Daytona SDK.


## DaytonaNotFoundError

```python
class DaytonaNotFoundError(DaytonaError)
```

Error for when a resource is not found.

## Image

```python
class Image(BaseModel)
```

Represents an image definition for a Daytona sandbox.
Do not construct this class directly. Instead use one of its static factory methods,
such as `Image.base()`, `Image.debian_slim()`, or `Image.from_dockerfile()`.

#### Image.dockerfile

```python
def dockerfile() -> str
```

Returns a generated Dockerfile for the image.

#### Image.pip\_install

```python
def pip_install(*packages: Union[str, list[str]],
                find_links: Optional[list[str]] = None,
                index_url: Optional[str] = None,
                extra_index_urls: Optional[list[str]] = None,
                pre: bool = False,
                extra_options: str = "") -> "Image"
```

Adds commands to install packages using pip.

**Arguments**:

- `*packages` - The packages to install.
- `find_links` - Optional[list[str]]: The find-links to use.
- `index_url` - Optional[str]: The index URL to use.
- `extra_index_urls` - Optional[list[str]]: The extra index URLs to use.
- `pre` - bool = False: Whether to install pre-release packages.
- `extra_options` - str = "": Additional options to pass to pip. Given string is passed
  directly to the pip install command.
  

**Returns**:

- `Image` - The image with the pip install commands added.
  

**Example**:

```python
image = Image.debian_slim("3.12").pip_install("requests", "pandas")
```

#### Image.pip\_install\_from\_requirements

```python
def pip_install_from_requirements(requirements_txt: str,
                                  find_links: Optional[list[str]] = None,
                                  index_url: Optional[str] = None,
                                  extra_index_urls: Optional[list[str]] = None,
                                  pre: bool = False,
                                  extra_options: str = "") -> "Image"
```

Installs dependencies from a requirements.txt file.

**Arguments**:

- `requirements_txt` - str: The path to the requirements.txt file.
- `find_links` - Optional[list[str]]: The find-links to use.
- `index_url` - Optional[str]: The index URL to use.
- `extra_index_urls` - Optional[list[str]]: The extra index URLs to use.
- `pre` - bool = False: Whether to install pre-release packages.
- `extra_options` - str = "": Additional options to pass to pip.
  

**Returns**:

- `Image` - The image with the pip install commands added.
  

**Example**:

```python
image = Image.debian_slim("3.12").pip_install_from_requirements("requirements.txt")
```

#### Image.pip\_install\_from\_pyproject

```python
def pip_install_from_pyproject(pyproject_toml: str,
                               optional_dependencies: list[str],
                               find_links: Optional[str] = None,
                               index_url: Optional[str] = None,
                               extra_index_url: Optional[str] = None,
                               pre: bool = False,
                               extra_options: str = "") -> "Image"
```

Installs dependencies from a pyproject.toml file.

**Arguments**:

- `pyproject_toml` - str: The path to the pyproject.toml file.
- `optional_dependencies` - list[str] = []: The optional dependencies to install from the pyproject.toml file.
- `find_links` - Optional[str] = None: The find-links to use.
- `index_url` - Optional[str] = None: The index URL to use.
- `extra_index_url` - Optional[str] = None: The extra index URL to use.
- `pre` - bool = False: Whether to install pre-release packages.
- `extra_options` - str = "": Additional options to pass to pip. Given string is passed
  directly to the pip install command.
  

**Returns**:

- `Image` - The image with the pip install commands added.
  

**Example**:

```python
image = Image.debian_slim("3.12")                 .pip_install_from_pyproject("pyproject.toml", optional_dependencies=["dev"])
```

#### Image.add\_local\_file

```python
def add_local_file(local_path: Union[str, Path], remote_path: str) -> "Image"
```

Adds a local file to the image.

**Arguments**:

- `local_path` - Union[str, Path]: The path to the local file.
- `remote_path` - str: The path to the file in the image.
  

**Returns**:

- `Image` - The image with the local file added.
  

**Example**:

```python
image = Image.debian_slim("3.12").add_local_file("package.json", "/home/daytona/package.json")
```

#### Image.add\_local\_dir

```python
def add_local_dir(local_path: Union[str, Path], remote_path: str) -> "Image"
```

Adds a local directory to the image.

**Arguments**:

- `local_path` - Union[str, Path]: The path to the local directory.
- `remote_path` - str: The path to the directory in the image.
  

**Returns**:

- `Image` - The image with the local directory added.
  

**Example**:

```python
image = Image.debian_slim("3.12").add_local_dir("src", "/home/daytona/src")
```

#### Image.run\_commands

```python
def run_commands(*commands: Union[str, list[str]]) -> "Image"
```

Runs commands in the image.

**Arguments**:

- `*commands` - The commands to run.
  

**Returns**:

- `Image` - The image with the commands added.
  

**Example**:

```python
image = Image.debian_slim("3.12").run_commands(
    'echo "Hello, world!"',
    ['bash', '-c', 'echo Hello, world, again!']
)
```

#### Image.env

```python
def env(env_vars: dict[str, str]) -> "Image"
```

Sets environment variables in the image.

**Arguments**:

- `env_vars` - dict[str, str]: The environment variables to set.
  

**Returns**:

- `Image` - The image with the environment variables added.
  

**Example**:

```python
image = Image.debian_slim("3.12").env({"PROJECT_ROOT": "/home/daytona"})
```

#### Image.workdir

```python
def workdir(path: Union[str, Path]) -> "Image"
```

Sets the working directory in the image.

**Arguments**:

- `path` - Union[str, Path]: The path to the working directory.
  

**Returns**:

- `Image` - The image with the working directory added.
  

**Example**:

```python
image = Image.debian_slim("3.12").workdir("/home/daytona")
```

#### Image.entrypoint

```python
def entrypoint(entrypoint_commands: list[str]) -> "Image"
```

Sets the entrypoint for the image.

**Arguments**:

- `entrypoint_commands` - list[str]: The commands to set as the entrypoint.
  

**Returns**:

- `Image` - The image with the entrypoint added.
  

**Example**:

```python
image = Image.debian_slim("3.12").entrypoint(["/bin/bash"])
```

#### Image.cmd

```python
def cmd(cmd: list[str]) -> "Image"
```

Sets the default command for the image.

**Arguments**:

- `cmd` - list[str]: The commands to set as the default command.
  

**Returns**:

- `Image` - The image with the default command added.
  

**Example**:

```python
image = Image.debian_slim("3.12").cmd(["/bin/bash"])
```

#### Image.dockerfile\_commands

```python
def dockerfile_commands(
        dockerfile_commands: list[str],
        context_dir: Optional[Union[Path, str]] = None) -> "Image"
```

Adds arbitrary Dockerfile-like commands to the image.

**Arguments**:

- `*dockerfile_commands` - The commands to add to the Dockerfile.
- `context_dir` - Optional[Union[Path, str]]: The path to the context directory.
  

**Returns**:

- `Image` - The image with the Dockerfile commands added.
  

**Example**:

```python
image = Image.debian_slim("3.12").dockerfile_commands(["RUN echo 'Hello, world!'"])
```

#### Image.from\_dockerfile

```python
@staticmethod
def from_dockerfile(path: Union[str, Path]) -> "Image"
```

Creates an Image from an existing Dockerfile.

**Arguments**:

- `path` - Union[str, Path]: The path to the Dockerfile.
  

**Returns**:

- `Image` - The image with the Dockerfile added.
  

**Example**:

```python
image = Image.from_dockerfile("Dockerfile")
```

#### Image.base

```python
@staticmethod
def base(image: str) -> "Image"
```

Creates an Image from an existing base image.

**Arguments**:

- `image` - str: The base image to use.
  

**Returns**:

- `Image` - The image with the base image added.
  

**Example**:

```python
image = Image.base("python:3.12-slim-bookworm")
```

#### Image.debian\_slim

```python
@staticmethod
def debian_slim(
        python_version: Optional[SupportedPythonSeries] = None) -> "Image"
```

Creates a Debian slim image based on the official Python Docker image.

**Arguments**:

- `python_version` - Optional[SupportedPythonSeries]: The Python version to use.
  

**Returns**:

- `Image` - The image with the Debian slim image added.
  

**Example**:

```python
image = Image.debian_slim("3.12")
```


## Context

```python
class Context(BaseModel)
```

Context for an image.

**Attributes**:

- `source_path` _str_ - The path to the source file or directory.
- `archive_path` _Optional[str]_ - The path inside the archive file in object storage.

The Daytona Python SDK provides a robust interface for programmatically interacting with Daytona Sandboxes.

## Installation

Install the Daytona Python SDK using pip:

```bash
pip install daytona
```

Or using poetry:

```bash
poetry add daytona
```

## Getting Started

Here's a simple example to help you get started with the Daytona Python SDK:

    ```python
    from daytona import Daytona

    def main():
        # Initialize the SDK (uses environment variables by default)
        daytona = Daytona()

        # Create a new sandbox
        sandbox = daytona.create()

        # Execute a command
        response = sandbox.process.exec("echo 'Hello, World!'")
        print(response.result)

    if __name__ == "__main__":
        main()
    ```

    ```python
    import asyncio
    from daytona import AsyncDaytona

    async def main():
        # Initialize the SDK (uses environment variables by default)
        async with AsyncDaytona() as daytona:
            # Create a new sandbox
            sandbox = await daytona.create()

            # Execute a command
            response = await sandbox.process.exec("echo 'Hello, World!'")
            print(response.result)

    if __name__ == "__main__":
        asyncio.run(main())
    ```

## Configuration

The SDK can be configured using environment variables or by passing options to the constructor:

    ```python
    from daytona import Daytona, DaytonaConfig

    # Using environment variables (DAYTONA_API_KEY, DAYTONA_API_URL, DAYTONA_TARGET)
    daytona = Daytona()

    # Using explicit configuration
    config = DaytonaConfig(
        api_key="your-api-key",
        api_url="https://app.daytona.io/api",
        target="us"
    )
    daytona = Daytona(config)
    ```

    ```python
    import asyncio
    from daytona import AsyncDaytona, DaytonaConfig

    async def main():
        try:
            # Using environment variables (DAYTONA_API_KEY, DAYTONA_API_URL, DAYTONA_TARGET)
            daytona = AsyncDaytona()
            # Your async code here
            pass
        finally:
            await daytona.close()

        # Using explicit configuration
        config = DaytonaConfig(
            api_key="your-api-key",
            api_url="https://app.daytona.io/api",
            target="us"
        )
        async with AsyncDaytona(config) as daytona:
            # Your code here
            pass

    if __name__ == "__main__":
        asyncio.run(main())
    ```

## ComputerUse

```python
class ComputerUse()
```

Computer Use functionality for interacting with the desktop environment.

Provides access to mouse, keyboard, screenshot, and display operations
for automating desktop interactions within a sandbox.

**Attributes**:

- `mouse` _Mouse_ - Mouse operations interface.
- `keyboard` _Keyboard_ - Keyboard operations interface.
- `screenshot` _Screenshot_ - Screenshot operations interface.
- `display` _Display_ - Display operations interface.

#### ComputerUse.start

```python
@intercept_errors(message_prefix="Failed to start computer use: ")
def start() -> ComputerUseStartResponse
```

Starts all computer use processes (Xvfb, xfce4, x11vnc, novnc).

**Returns**:

- `ComputerUseStartResponse` - Computer use start response.
  

**Example**:

```python
result = sandbox.computer_use.start()
print("Computer use processes started:", result.message)
```

#### ComputerUse.stop

```python
@intercept_errors(message_prefix="Failed to stop computer use: ")
def stop() -> ComputerUseStopResponse
```

Stops all computer use processes.

**Returns**:

- `ComputerUseStopResponse` - Computer use stop response.
  

**Example**:

```python
result = sandbox.computer_use.stop()
print("Computer use processes stopped:", result.message)
```

#### ComputerUse.get\_status

```python
@intercept_errors(message_prefix="Failed to get computer use status: ")
def get_status() -> ComputerUseStatusResponse
```

Gets the status of all computer use processes.

**Returns**:

- `ComputerUseStatusResponse` - Status information about all VNC desktop processes.
  

**Example**:

```python
response = sandbox.computer_use.get_status()
print("Computer use status:", response.status)
```

#### ComputerUse.get\_process\_status

```python
@intercept_errors(message_prefix="Failed to get process status: ")
def get_process_status(process_name: str) -> ProcessStatusResponse
```

Gets the status of a specific VNC process.

**Arguments**:

- `process_name` _str_ - Name of the process to check.
  

**Returns**:

- `ProcessStatusResponse` - Status information about the specific process.
  

**Example**:

```python
xvfb_status = sandbox.computer_use.get_process_status("xvfb")
no_vnc_status = sandbox.computer_use.get_process_status("novnc")
```

#### ComputerUse.restart\_process

```python
@intercept_errors(message_prefix="Failed to restart process: ")
def restart_process(process_name: str) -> ProcessRestartResponse
```

Restarts a specific VNC process.

**Arguments**:

- `process_name` _str_ - Name of the process to restart.
  

**Returns**:

- `ProcessRestartResponse` - Process restart response.
  

**Example**:

```python
result = sandbox.computer_use.restart_process("xfce4")
print("XFCE4 process restarted:", result.message)
```

#### ComputerUse.get\_process\_logs

```python
@intercept_errors(message_prefix="Failed to get process logs: ")
def get_process_logs(process_name: str) -> ProcessLogsResponse
```

Gets logs for a specific VNC process.

**Arguments**:

- `process_name` _str_ - Name of the process to get logs for.
  

**Returns**:

- `ProcessLogsResponse` - Process logs.
  

**Example**:

```python
logs = sandbox.computer_use.get_process_logs("novnc")
print("NoVNC logs:", logs)
```

#### ComputerUse.get\_process\_errors

```python
@intercept_errors(message_prefix="Failed to get process errors: ")
def get_process_errors(process_name: str) -> ProcessErrorsResponse
```

Gets error logs for a specific VNC process.

**Arguments**:

- `process_name` _str_ - Name of the process to get error logs for.
  

**Returns**:

- `ProcessErrorsResponse` - Process error logs.
  

**Example**:

```python
errors = sandbox.computer_use.get_process_errors("x11vnc")
print("X11VNC errors:", errors)
```


## Mouse

```python
class Mouse()
```

Mouse operations for computer use functionality.

#### Mouse.get\_position

```python
@intercept_errors(message_prefix="Failed to get mouse position: ")
def get_position() -> MousePositionResponse
```

Gets the current mouse cursor position.

**Returns**:

- `MousePositionResponse` - Current mouse position with x and y coordinates.
  

**Example**:

```python
position = sandbox.computer_use.mouse.get_position()
print(f"Mouse is at: {position.x}, {position.y}")
```

#### Mouse.move

```python
@intercept_errors(message_prefix="Failed to move mouse: ")
def move(x: int, y: int) -> MousePositionResponse
```

Moves the mouse cursor to the specified coordinates.

**Arguments**:

- `x` _int_ - The x coordinate to move to.
- `y` _int_ - The y coordinate to move to.
  

**Returns**:

- `MousePositionResponse` - Position after move.
  

**Example**:

```python
result = sandbox.computer_use.mouse.move(100, 200)
print(f"Mouse moved to: {result.x}, {result.y}")
```

#### Mouse.click

```python
@intercept_errors(message_prefix="Failed to click mouse: ")
def click(x: int,
          y: int,
          button: str = "left",
          double: bool = False) -> MouseClickResponse
```

Clicks the mouse at the specified coordinates.

**Arguments**:

- `x` _int_ - The x coordinate to click at.
- `y` _int_ - The y coordinate to click at.
- `button` _str_ - The mouse button to click ('left', 'right', 'middle').
- `double` _bool_ - Whether to perform a double-click.
  

**Returns**:

- `MouseClickResponse` - Click operation result.
  

**Example**:

```python
# Single left click
result = sandbox.computer_use.mouse.click(100, 200)

# Double click
double_click = sandbox.computer_use.mouse.click(100, 200, "left", True)

# Right click
right_click = sandbox.computer_use.mouse.click(100, 200, "right")
```

#### Mouse.drag

```python
@intercept_errors(message_prefix="Failed to drag mouse: ")
def drag(start_x: int,
         start_y: int,
         end_x: int,
         end_y: int,
         button: str = "left") -> MouseDragResponse
```

Drags the mouse from start coordinates to end coordinates.

**Arguments**:

- `start_x` _int_ - The starting x coordinate.
- `start_y` _int_ - The starting y coordinate.
- `end_x` _int_ - The ending x coordinate.
- `end_y` _int_ - The ending y coordinate.
- `button` _str_ - The mouse button to use for dragging.
  

**Returns**:

- `MouseDragResponse` - Drag operation result.
  

**Example**:

```python
result = sandbox.computer_use.mouse.drag(50, 50, 150, 150)
print(f"Dragged from {result.from_x},{result.from_y} to {result.to_x},{result.to_y}")
```

#### Mouse.scroll

```python
@intercept_errors(message_prefix="Failed to scroll mouse: ")
def scroll(x: int, y: int, direction: str, amount: int = 1) -> bool
```

Scrolls the mouse wheel at the specified coordinates.

**Arguments**:

- `x` _int_ - The x coordinate to scroll at.
- `y` _int_ - The y coordinate to scroll at.
- `direction` _str_ - The direction to scroll ('up' or 'down').
- `amount` _int_ - The amount to scroll.
  

**Returns**:

- `bool` - Whether the scroll operation was successful.
  

**Example**:

```python
# Scroll up
scroll_up = sandbox.computer_use.mouse.scroll(100, 200, "up", 3)

# Scroll down
scroll_down = sandbox.computer_use.mouse.scroll(100, 200, "down", 5)
```

## Keyboard

```python
class Keyboard()
```

Keyboard operations for computer use functionality.

#### Keyboard.type

```python
@intercept_errors(message_prefix="Failed to type text: ")
def type(text: str, delay: Optional[int] = None) -> None
```

Types the specified text.

**Arguments**:

- `text` _str_ - The text to type.
- `delay` _int_ - Delay between characters in milliseconds.
  

**Raises**:

- `DaytonaError` - If the type operation fails.
  

**Example**:

```python
try:
    sandbox.computer_use.keyboard.type("Hello, World!")
    print(f"Operation success")
except Exception as e:
    print(f"Operation failed: {e}")

# With delay between characters
try:
    sandbox.computer_use.keyboard.type("Slow typing", 100)
    print(f"Operation success")
except Exception as e:
    print(f"Operation failed: {e}")
```

#### Keyboard.press

```python
@intercept_errors(message_prefix="Failed to press key: ")
def press(key: str, modifiers: Optional[List[str]] = None) -> None
```

Presses a key with optional modifiers.

**Arguments**:

- `key` _str_ - The key to press (e.g., 'Enter', 'Escape', 'Tab', 'a', 'A').
- `modifiers` _List[str]_ - Modifier keys ('ctrl', 'alt', 'meta', 'shift').
  

**Raises**:

- `DaytonaError` - If the press operation fails.
  

**Example**:

```python
# Press Enter
try:
    sandbox.computer_use.keyboard.press("Return")
    print(f"Operation success")
except Exception as e:
    print(f"Operation failed: {e}")

# Press Ctrl+C
try:
    sandbox.computer_use.keyboard.press("c", ["ctrl"])
    print(f"Operation success")

# Press Ctrl+Shift+T
try:
    sandbox.computer_use.keyboard.press("t", ["ctrl", "shift"])
    print(f"Operation success")
except Exception as e:
    print(f"Operation failed: {e}")
```

#### Keyboard.hotkey

```python
@intercept_errors(message_prefix="Failed to press hotkey: ")
def hotkey(keys: str) -> None
```

Presses a hotkey combination.

**Arguments**:

- `keys` _str_ - The hotkey combination (e.g., 'ctrl+c', 'alt+tab', 'cmd+shift+t').
  

**Raises**:

- `DaytonaError` - If the hotkey operation fails.
  

**Example**:

```python
# Copy
try:
    sandbox.computer_use.keyboard.hotkey("ctrl+c")
    print(f"Operation success")
except Exception as e:
    print(f"Operation failed: {e}")

# Paste
try:
    sandbox.computer_use.keyboard.hotkey("ctrl+v")
    print(f"Operation success")
except Exception as e:
    print(f"Operation failed: {e}")

# Alt+Tab
try:
    sandbox.computer_use.keyboard.hotkey("alt+tab")
    print(f"Operation success")
except Exception as e:
    print(f"Operation failed: {e}")
```

## Screenshot

```python
class Screenshot()
```

Screenshot operations for computer use functionality.

#### Screenshot.take\_full\_screen

```python
@intercept_errors(message_prefix="Failed to take screenshot: ")
def take_full_screen(show_cursor: bool = False) -> ScreenshotResponse
```

Takes a screenshot of the entire screen.

**Arguments**:

- `show_cursor` _bool_ - Whether to show the cursor in the screenshot.
  

**Returns**:

- `ScreenshotResponse` - Screenshot data with base64 encoded image.
  

**Example**:

```python
screenshot = sandbox.computer_use.screenshot.take_full_screen()
print(f"Screenshot size: {screenshot.width}x{screenshot.height}")

# With cursor visible
with_cursor = sandbox.computer_use.screenshot.take_full_screen(True)
```

#### Screenshot.take\_region

```python
@intercept_errors(message_prefix="Failed to take region screenshot: ")
def take_region(region: ScreenshotRegion,
                show_cursor: bool = False) -> ScreenshotResponse
```

Takes a screenshot of a specific region.

**Arguments**:

- `region` _ScreenshotRegion_ - The region to capture.
- `show_cursor` _bool_ - Whether to show the cursor in the screenshot.
  

**Returns**:

- `ScreenshotResponse` - Screenshot data with base64 encoded image.
  

**Example**:

```python
region = ScreenshotRegion(x=100, y=100, width=300, height=200)
screenshot = sandbox.computer_use.screenshot.take_region(region)
print(f"Captured region: {screenshot.region.width}x{screenshot.region.height}")
```

#### Screenshot.take\_compressed

```python
@intercept_errors(message_prefix="Failed to take compressed screenshot: ")
def take_compressed(
        options: Optional[ScreenshotOptions] = None) -> ScreenshotResponse
```

Takes a compressed screenshot of the entire screen.

**Arguments**:

- `options` _ScreenshotOptions_ - Compression and display options.
  

**Returns**:

- `ScreenshotResponse` - Compressed screenshot data.
  

**Example**:

```python
# Default compression
screenshot = sandbox.computer_use.screenshot.take_compressed()

# High quality JPEG
jpeg = sandbox.computer_use.screenshot.take_compressed(
    ScreenshotOptions(format="jpeg", quality=95, show_cursor=True)
)

# Scaled down PNG
scaled = sandbox.computer_use.screenshot.take_compressed(
    ScreenshotOptions(format="png", scale=0.5)
)
```

#### Screenshot.take\_compressed\_region

```python
@intercept_errors(
    message_prefix="Failed to take compressed region screenshot: ")
def take_compressed_region(
        region: ScreenshotRegion,
        options: Optional[ScreenshotOptions] = None) -> ScreenshotResponse
```

Takes a compressed screenshot of a specific region.

**Arguments**:

- `region` _ScreenshotRegion_ - The region to capture.
- `options` _ScreenshotOptions_ - Compression and display options.
  

**Returns**:

- `ScreenshotResponse` - Compressed screenshot data.
  

**Example**:

```python
region = ScreenshotRegion(x=0, y=0, width=800, height=600)
screenshot = sandbox.computer_use.screenshot.take_compressed_region(
    region,
    ScreenshotOptions(format="webp", quality=80, show_cursor=True)
)
print(f"Compressed size: {screenshot.size_bytes} bytes")
```

## Display

```python
class Display()
```

Display operations for computer use functionality.

#### Display.get\_info

```python
@intercept_errors(message_prefix="Failed to get display info: ")
def get_info() -> DisplayInfoResponse
```

Gets information about the displays.

**Returns**:

- `DisplayInfoResponse` - Display information including primary display and all available displays.
  

**Example**:

```python
info = sandbox.computer_use.display.get_info()
print(f"Primary display: {info.primary_display.width}x{info.primary_display.height}")
print(f"Total displays: {info.total_displays}")
for i, display in enumerate(info.displays):
    print(f"Display {i}: {display.width}x{display.height} at {display.x},{display.y}")
```

#### Display.get\_windows

```python
@intercept_errors(message_prefix="Failed to get windows: ")
def get_windows() -> WindowsResponse
```

Gets the list of open windows.

**Returns**:

- `WindowsResponse` - List of open windows with their IDs and titles.
  

**Example**:

```python
windows = sandbox.computer_use.display.get_windows()
print(f"Found {windows.count} open windows:")
for window in windows.windows:
    print(f"- {window.title} (ID: {window.id})")
```

## ScreenshotRegion

```python
class ScreenshotRegion()
```

Region coordinates for screenshot operations.

**Attributes**:

- `x` _int_ - X coordinate of the region.
- `y` _int_ - Y coordinate of the region.
- `width` _int_ - Width of the region.
- `height` _int_ - Height of the region.

## ScreenshotOptions

```python
class ScreenshotOptions()
```

Options for screenshot compression and display.

**Attributes**:

- `show_cursor` _bool_ - Whether to show the cursor in the screenshot.
- `fmt` _str_ - Image format (e.g., 'png', 'jpeg', 'webp').
- `quality` _int_ - Compression quality (0-100).
- `scale` _float_ - Scale factor for the screenshot.

## Daytona

```python
class Daytona()
```

Main class for interacting with the Daytona API.

This class provides methods to create, manage, and interact with Daytona Sandboxes.
It can be initialized either with explicit configuration or using environment variables.

**Attributes**:

- `volume` _VolumeService_ - Service for managing volumes.
- `snapshot` _SnapshotService_ - Service for managing snapshots.
  

**Example**:

  Using environment variables:
```python
daytona = Daytona()  # Uses DAYTONA_API_KEY, DAYTONA_API_URL
sandbox = daytona.create()
```
  
  Using explicit configuration:
```python
config = DaytonaConfig(
    api_key="your-api-key",
    api_url="https://your-api.com",
    target="us"
)
daytona = Daytona(config)
sandbox = daytona.create()
```

#### Daytona.\_\_init\_\_

```python
def __init__(config: Optional[DaytonaConfig] = None)
```

Initializes Daytona instance with optional configuration.

If no config is provided, reads from environment variables:
- `DAYTONA_API_KEY`: Required API key for authentication
- `DAYTONA_API_URL`: Required api URL
- `DAYTONA_TARGET`: Optional target environment (if not provided, default region for the organization is used)

**Arguments**:

- `config` _Optional[DaytonaConfig]_ - Object containing api_key, api_url, and target.
  

**Raises**:

- `DaytonaError` - If API key is not provided either through config or environment variables
  

**Example**:

```python
from daytona import Daytona, DaytonaConfig
# Using environment variables
daytona1 = Daytona()

# Using explicit configuration
config = DaytonaConfig(
    api_key="your-api-key",
    api_url="https://your-api.com",
    target="us"
)
daytona2 = Daytona(config)

```

#### Daytona.create

```python
@overload
def create(params: Optional[CreateSandboxFromSnapshotParams] = None,
           *,
           timeout: Optional[float] = 60) -> Sandbox
```

Creates Sandboxes from specified or default snapshot. You can specify various parameters,
including language, image, environment variables, and volumes.

**Arguments**:

- `params` _Optional[CreateSandboxFromSnapshotParams]_ - Parameters for Sandbox creation. If not provided,
  defaults to default Daytona snapshot and Python language.
- `timeout` _Optional[float]_ - Timeout (in seconds) for sandbox creation. 0 means no timeout.
  Default is 60 seconds.
  

**Returns**:

- `Sandbox` - The created Sandbox instance.
  

**Raises**:

- `DaytonaError` - If timeout, auto_stop_interval or auto_archive_interval is negative;
  If sandbox fails to start or times out
  

**Example**:

  Create a default Python Sandbox:
```python
sandbox = daytona.create()
```
  
  Create a custom Sandbox:
```python
params = CreateSandboxFromSnapshotParams(
    language="python",
    snapshot="my-snapshot-id",
    env_vars={"DEBUG": "true"},
    auto_stop_interval=0,
    auto_archive_interval=60,
    auto_delete_interval=120
)
sandbox = daytona.create(params, timeout=40)
```

#### Daytona.create

```python
@overload
def create(params: Optional[CreateSandboxFromImageParams] = None,
           *,
           timeout: Optional[float] = 60,
           on_snapshot_create_logs: Callable[[str], None] = None) -> Sandbox
```

Creates Sandboxes from specified image available on some registry or declarative Daytona Image.
You can specify various parameters, including resources, language, image, environment variables,
and volumes. Daytona creates snapshot from provided image and uses it to create Sandbox.

**Arguments**:

- `params` _Optional[CreateSandboxFromImageParams]_ - Parameters for Sandbox creation from image.
- `timeout` _Optional[float]_ - Timeout (in seconds) for sandbox creation. 0 means no timeout.
  Default is 60 seconds.
- `on_snapshot_create_logs` _Callable[[str], None]_ - This callback function handles snapshot creation logs.
  

**Returns**:

- `Sandbox` - The created Sandbox instance.
  

**Raises**:

- `DaytonaError` - If timeout, auto_stop_interval or auto_archive_interval is negative;
  If sandbox fails to start or times out
  

**Example**:

  Create a default Python Sandbox from image:
```python
sandbox = daytona.create(CreateSandboxFromImageParams(image="debian:12.9"))
```
  
  Create a custom Sandbox from declarative Image definition:
```python
declarative_image = (
    Image.base("alpine:3.18")
    .pipInstall(["numpy", "pandas"])
    .env({"MY_ENV_VAR": "My Environment Variable"})
)
params = CreateSandboxFromImageParams(
    language="python",
    image=declarative_image,
    env_vars={"DEBUG": "true"},
    resources=Resources(cpu=2, memory=4),
    auto_stop_interval=0,
    auto_archive_interval=60,
    auto_delete_interval=120
)
sandbox = daytona.create(
    params,
    timeout=40,
    on_snapshot_create_logs=lambda chunk: print(chunk, end=""),
)
```

#### Daytona.delete

```python
def delete(sandbox: Sandbox, timeout: Optional[float] = 60) -> None
```

Deletes a Sandbox.

**Arguments**:

- `sandbox` _Sandbox_ - The Sandbox instance to delete.
- `timeout` _Optional[float]_ - Timeout (in seconds) for sandbox deletion. 0 means no timeout.
  Default is 60 seconds.
  

**Raises**:

- `DaytonaError` - If sandbox fails to delete or times out
  

**Example**:

```python
sandbox = daytona.create()
# ... use sandbox ...
daytona.delete(sandbox)  # Clean up when done
```

#### Daytona.get

```python
@intercept_errors(message_prefix="Failed to get sandbox: ")
def get(sandbox_id_or_name: str) -> Sandbox
```

Gets a Sandbox by its ID or name.

**Arguments**:

- `sandbox_id_or_name` _str_ - The ID or name of the Sandbox to retrieve.
  

**Returns**:

- `Sandbox` - The Sandbox instance.
  

**Raises**:

- `DaytonaError` - If sandbox_id_or_name is not provided.
  

**Example**:

```python
sandbox = daytona.get("my-sandbox-id-or-name")
print(sandbox.state)
```

#### Daytona.find\_one

```python
@intercept_errors(message_prefix="Failed to find sandbox: ")
def find_one(sandbox_id_or_name: Optional[str] = None,
             labels: Optional[Dict[str, str]] = None) -> Sandbox
```

Finds a Sandbox by its ID or name or labels.

**Arguments**:

- `sandbox_id_or_name` _Optional[str]_ - The ID or name of the Sandbox to retrieve.
- `labels` _Optional[Dict[str, str]]_ - Labels to filter Sandboxes.
  

**Returns**:

- `Sandbox` - First Sandbox that matches the ID or name or labels.
  

**Raises**:

- `DaytonaError` - If no Sandbox is found.
  

**Example**:

```python
sandbox = daytona.find_one(labels={"my-label": "my-value"})
print(f"Sandbox ID: {sandbox.id} State: {sandbox.state}")
```

#### Daytona.list

```python
@intercept_errors(message_prefix="Failed to list sandboxes: ")
def list(labels: Optional[Dict[str, str]] = None,
         page: Optional[int] = None,
         limit: Optional[int] = None) -> PaginatedSandboxes
```

Returns paginated list of Sandboxes filtered by labels.

**Arguments**:

- `labels` _Optional[Dict[str, str]]_ - Labels to filter Sandboxes.
- `page` _Optional[int]_ - Page number for pagination (starting from 1).
- `limit` _Optional[int]_ - Maximum number of items per page.
  

**Returns**:

- `PaginatedSandboxes` - Paginated list of Sandbox instances that match the labels.
  

**Example**:

```python
result = daytona.list(labels={"my-label": "my-value"}, page=2, limit=10)
for sandbox in result.items:
    print(f"{sandbox.id}: {sandbox.state}")
```

#### Daytona.start

```python
def start(sandbox: Sandbox, timeout: Optional[float] = 60) -> None
```

Starts a Sandbox and waits for it to be ready.

**Arguments**:

- `sandbox` _Sandbox_ - The Sandbox to start.
- `timeout` _Optional[float]_ - Optional timeout in seconds to wait for the Sandbox to start.
  0 means no timeout. Default is 60 seconds.
  

**Raises**:

- `DaytonaError` - If timeout is negative; If Sandbox fails to start or times out

#### Daytona.stop

```python
def stop(sandbox: Sandbox, timeout: Optional[float] = 60) -> None
```

Stops a Sandbox and waits for it to be stopped.

**Arguments**:

- `sandbox` _Sandbox_ - The sandbox to stop
- `timeout` _Optional[float]_ - Optional timeout (in seconds) for sandbox stop.
  0 means no timeout. Default is 60 seconds.
  

**Raises**:

- `DaytonaError` - If timeout is negative; If Sandbox fails to stop or times out


## CodeLanguage

```python
@dataclass
class CodeLanguage(Enum)
```

Programming languages supported by Daytona

**Enum Members**:
    - `PYTHON` ("python")
    - `TYPESCRIPT` ("typescript")
    - `JAVASCRIPT` ("javascript")

## DaytonaConfig

```python
class DaytonaConfig(BaseModel)
```

Configuration options for initializing the Daytona client.

**Attributes**:

- `api_key` _Optional[str]_ - API key for authentication with the Daytona API. If not set, it must be provided
  via the environment variable `DAYTONA_API_KEY`, or a JWT token must be provided instead.
- `jwt_token` _Optional[str]_ - JWT token for authentication with the Daytona API. If not set, it must be provided
  via the environment variable `DAYTONA_JWT_TOKEN`, or an API key must be provided instead.
- `organization_id` _Optional[str]_ - Organization ID used for JWT-based authentication. Required if a JWT token
  is provided, and must be set either here or in the environment variable `DAYTONA_ORGANIZATION_ID`.
- `api_url` _Optional[str]_ - URL of the Daytona API. Defaults to `'https://app.daytona.io/api'` if not set
  here or in the environment variable `DAYTONA_API_URL`.
- `server_url` _Optional[str]_ - Deprecated. Use `api_url` instead. This property will be removed
  in a future version.
- `target` _Optional[str]_ - Target runner location for the Sandbox. Default region for the organization is used 
  if not set here or in the environment variable `DAYTONA_TARGET`.
  

**Example**:

```python
config = DaytonaConfig(api_key="your-api-key")
```
```python
config = DaytonaConfig(jwt_token="your-jwt-token", organization_id="your-organization-id")
```

## CreateSandboxBaseParams

```python
class CreateSandboxBaseParams(BaseModel)
```

Base parameters for creating a new Sandbox.

**Attributes**:

- `name` _Optional[str]_ - Name of the Sandbox.
- `language` _Optional[CodeLanguage]_ - Programming language for the Sandbox. Defaults to "python".
- `os_user` _Optional[str]_ - OS user for the Sandbox.
- `env_vars` _Optional[Dict[str, str]]_ - Environment variables to set in the Sandbox.
- `labels` _Optional[Dict[str, str]]_ - Custom labels for the Sandbox.
- `public` _Optional[bool]_ - Whether the Sandbox should be public.
- `timeout` _Optional[float]_ - Timeout in seconds for Sandbox to be created and started.
- `auto_stop_interval` _Optional[int]_ - Interval in minutes after which Sandbox will
  automatically stop if no Sandbox event occurs during that time. Default is 15 minutes.
  0 means no auto-stop.
- `auto_archive_interval` _Optional[int]_ - Interval in minutes after which a continuously stopped Sandbox will
  automatically archive. Default is 7 days.
  0 means the maximum interval will be used.
- `auto_delete_interval` _Optional[int]_ - Interval in minutes after which a continuously stopped Sandbox will
  automatically be deleted. By default, auto-delete is disabled.
  Negative value means disabled, 0 means delete immediately upon stopping.
- `volumes` _Optional[List[VolumeMount]]_ - List of volumes mounts to attach to the Sandbox.
- `network_block_all` _Optional[bool]_ - Whether to block all network access for the Sandbox.
- `network_allow_list` _Optional[str]_ - Comma-separated list of allowed CIDR network addresses for the Sandbox.
- `ephemeral` _Optional[bool]_ - Whether the Sandbox should be ephemeral.
  If True, auto_delete_interval will be set to 0.

## CreateSandboxFromImageParams

```python
class CreateSandboxFromImageParams(CreateSandboxBaseParams)
```

Parameters for creating a new Sandbox from an image.

**Attributes**:

- `image` _Union[str, Image]_ - Custom Docker image to use for the Sandbox. If an Image object is provided,
  the image will be dynamically built.
- `resources` _Optional[Resources]_ - Resource configuration for the Sandbox. If not provided, sandbox will
  have default resources.

## CreateSandboxFromSnapshotParams

```python
class CreateSandboxFromSnapshotParams(CreateSandboxBaseParams)
```

Parameters for creating a new Sandbox from a snapshot.

**Attributes**:

- `snapshot` _Optional[str]_ - Name of the snapshot to use for the Sandbox.

## FileSystem

```python
class FileSystem()
```

Provides file system operations within a Sandbox.

This class implements a high-level interface to file system operations that can
be performed within a Daytona Sandbox.

#### FileSystem.\_\_init\_\_

```python
def __init__(api_client: FileSystemApi, ensure_toolbox_url: Callable[[],
                                                                     None])
```

Initializes a new FileSystem instance.

**Arguments**:

- `api_client` _FileSystemApi_ - API client for Sandbox file system operations.
- `ensure_toolbox_url` _Callable[[], None]_ - Ensures the toolbox API URL is initialized.
  Must be called before invoking any private methods on the API client.

#### FileSystem.create\_folder

```python
@intercept_errors(message_prefix="Failed to create folder: ")
def create_folder(path: str, mode: str) -> None
```

Creates a new directory in the Sandbox at the specified path with the given
permissions.

**Arguments**:

- `path` _str_ - Path where the folder should be created. Relative paths are resolved based
  on the sandbox working directory.
- `mode` _str_ - Folder permissions in octal format (e.g., "755" for rwxr-xr-x).
  

**Example**:

```python
# Create a directory with standard permissions
sandbox.fs.create_folder("workspace/data", "755")

# Create a private directory
sandbox.fs.create_folder("workspace/secrets", "700")
```

#### FileSystem.delete\_file

```python
@intercept_errors(message_prefix="Failed to delete file: ")
def delete_file(path: str, recursive: bool = False) -> None
```

Deletes a file from the Sandbox.

**Arguments**:

- `path` _str_ - Path to the file to delete. Relative paths are resolved based on the sandbox working directory.
- `recursive` _bool_ - If the file is a directory, this must be true to delete it.
  

**Example**:

```python
# Delete a file
sandbox.fs.delete_file("workspace/data/old_file.txt")
```

#### FileSystem.download\_file

```python
@overload
def download_file(remote_path: str, timeout: int = 30 * 60) -> bytes
```

Downloads a file from the Sandbox. Returns the file contents as a bytes object.
This method is useful when you want to load the file into memory without saving it to disk.
It can only be used for smaller files.

**Arguments**:

- `remote_path` _str_ - Path to the file in the Sandbox. Relative paths are resolved based
  on the sandbox working directory.
- `timeout` _int_ - Timeout for the download operation in seconds. 0 means no timeout. Default is 30 minutes.
  

**Returns**:

- `bytes` - The file contents as a bytes object.
  

**Example**:

```python
# Download and save a file locally
content = sandbox.fs.download_file("workspace/data/file.txt")
with open("local_copy.txt", "wb") as f:
    f.write(content)

# Download and process text content
content = sandbox.fs.download_file("workspace/data/config.json")
config = json.loads(content.decode('utf-8'))
```

#### FileSystem.download\_file

```python
@overload
def download_file(remote_path: str,
                  local_path: str,
                  timeout: int = 30 * 60) -> None
```

Downloads a file from the Sandbox and saves it to a local file using stream.
This method is useful when you want to download larger files that may not fit into memory.

**Arguments**:

- `remote_path` _str_ - Path to the file in the Sandbox. Relative paths are resolved based
  on the sandbox working directory.
- `local_path` _str_ - Path to save the file locally.
- `timeout` _int_ - Timeout for the download operation in seconds. 0 means no timeout. Default is 30 minutes.
  

**Example**:

```python
local_path = "local_copy.txt"
sandbox.fs.download_file("tmp/large_file.txt", local_path)
size_mb = os.path.getsize(local_path) / 1024 / 1024
print(f"Size of the downloaded file {local_path}: {size_mb} MB")
```

#### FileSystem.download\_files

```python
@intercept_errors(message_prefix="Failed to download files: ")
def download_files(files: List[FileDownloadRequest],
                   timeout: int = 30 * 60) -> List[FileDownloadResponse]
```

Downloads multiple files from the Sandbox. If the files already exist locally, they will be overwritten.

**Arguments**:

- `files` _List[FileDownloadRequest]_ - List of files to download.
- `timeout` _int_ - Timeout for the download operation in seconds. 0 means no timeout. Default is 30 minutes.
  

**Returns**:

- `List[FileDownloadResponse]` - List of download results.
  

**Raises**:

- `Exception` - Only if the request itself fails (network issues, invalid request/response, etc.). Individual
  file download errors are returned in the `FileDownloadResponse.error` field.
  

**Example**:

```python
# Download multiple files
results = sandbox.fs.download_files([
    FileDownloadRequest(source="tmp/data.json"),
    FileDownloadRequest(source="tmp/config.json", destination="local_config.json")
])
for result in results:
    if result.error:
        print(f"Error downloading {result.source}: {result.error}")
    elif result.result:
        print(f"Downloaded {result.source} to {result.result}")
```

#### FileSystem.find\_files

```python
@intercept_errors(message_prefix="Failed to find files: ")
def find_files(path: str, pattern: str) -> List[Match]
```

Searches for files containing a pattern, similar to
the grep command.

**Arguments**:

- `path` _str_ - Path to the file or directory to search. If the path is a directory,
  the search will be performed recursively. Relative paths are resolved based
  on the sandbox working directory.
- `pattern` _str_ - Search pattern to match against file contents.
  

**Returns**:

- `List[Match]` - List of matches found in files. Each Match object includes:
  - file: Path to the file containing the match
  - line: The line number where the match was found
  - content: The matching line content
  

**Example**:

```python
# Search for TODOs in Python files
matches = sandbox.fs.find_files("workspace/src", "TODO:")
for match in matches:
    print(f"{match.file}:{match.line}: {match.content.strip()}")
```

#### FileSystem.get\_file\_info

```python
@intercept_errors(message_prefix="Failed to get file info: ")
def get_file_info(path: str) -> FileInfo
```

Gets detailed information about a file or directory, including its
size, permissions, and timestamps.

**Arguments**:

- `path` _str_ - Path to the file or directory. Relative paths are resolved based
  on the sandbox working directory.
  

**Returns**:

- `FileInfo` - Detailed file information including:
  - name: File name
  - is_dir: Whether the path is a directory
  - size: File size in bytes
  - mode: File permissions
  - mod_time: Last modification timestamp
  - permissions: File permissions in octal format
  - owner: File owner
  - group: File group
  

**Example**:

```python
# Get file metadata
info = sandbox.fs.get_file_info("workspace/data/file.txt")
print(f"Size: {info.size} bytes")
print(f"Modified: {info.mod_time}")
print(f"Mode: {info.mode}")

# Check if path is a directory
info = sandbox.fs.get_file_info("workspace/data")
if info.is_dir:
    print("Path is a directory")
```

#### FileSystem.list\_files

```python
@intercept_errors(message_prefix="Failed to list files: ")
def list_files(path: str) -> List[FileInfo]
```

Lists files and directories in a given path and returns their information, similar to the ls -l command.

**Arguments**:

- `path` _str_ - Path to the directory to list contents from. Relative paths are resolved
  based on the sandbox working directory.
  

**Returns**:

- `List[FileInfo]` - List of file and directory information. Each FileInfo
  object includes the same fields as described in get_file_info().
  

**Example**:

```python
# List directory contents
files = sandbox.fs.list_files("workspace/data")

# Print files and their sizes
for file in files:
    if not file.is_dir:
        print(f"{file.name}: {file.size} bytes")

# List only directories
dirs = [f for f in files if f.is_dir]
print("Subdirectories:", ", ".join(d.name for d in dirs))
```

#### FileSystem.move\_files

```python
@intercept_errors(message_prefix="Failed to move files: ")
def move_files(source: str, destination: str) -> None
```

Moves or renames a file or directory. The parent directory of the destination must exist.

**Arguments**:

- `source` _str_ - Path to the source file or directory. Relative paths are resolved
  based on the sandbox working directory.
- `destination` _str_ - Path to the destination. Relative paths are resolved based on
  the sandbox working directory.
  

**Example**:

```python
# Rename a file
sandbox.fs.move_files(
    "workspace/data/old_name.txt",
    "workspace/data/new_name.txt"
)

# Move a file to a different directory
sandbox.fs.move_files(
    "workspace/data/file.txt",
    "workspace/archive/file.txt"
)

# Move a directory
sandbox.fs.move_files(
    "workspace/old_dir",
    "workspace/new_dir"
)
```

#### FileSystem.replace\_in\_files

```python
@intercept_errors(message_prefix="Failed to replace in files: ")
def replace_in_files(files: List[str], pattern: str,
                     new_value: str) -> List[ReplaceResult]
```

Performs search and replace operations across multiple files.

**Arguments**:

- `files` _List[str]_ - List of file paths to perform replacements in. Relative paths are
  resolved based on the sandbox working directory.
- `pattern` _str_ - Pattern to search for.
- `new_value` _str_ - Text to replace matches with.
  

**Returns**:

- `List[ReplaceResult]` - List of results indicating replacements made in
  each file. Each ReplaceResult includes:
  - file: Path to the modified file
  - success: Whether the operation was successful
  - error: Error message if the operation failed
  

**Example**:

```python
# Replace in specific files
results = sandbox.fs.replace_in_files(
    files=["workspace/src/file1.py", "workspace/src/file2.py"],
    pattern="old_function",
    new_value="new_function"
)

# Print results
for result in results:
    if result.success:
        print(f"{result.file}: {result.success}")
    else:
        print(f"{result.file}: {result.error}")
```

#### FileSystem.search\_files

```python
@intercept_errors(message_prefix="Failed to search files: ")
def search_files(path: str, pattern: str) -> SearchFilesResponse
```

Searches for files and directories whose names match the
specified pattern. The pattern can be a simple string or a glob pattern.

**Arguments**:

- `path` _str_ - Path to the root directory to start search from. Relative paths are resolved
  based on the sandbox working directory.
- `pattern` _str_ - Pattern to match against file names. Supports glob
  patterns (e.g., "*.py" for Python files).
  

**Returns**:

- `SearchFilesResponse` - Search results containing:
  - files: List of matching file and directory paths
  

**Example**:

```python
# Find all Python files
result = sandbox.fs.search_files("workspace", "*.py")
for file in result.files:
    print(file)

# Find files with specific prefix
result = sandbox.fs.search_files("workspace/data", "test_*")
print(f"Found {len(result.files)} test files")
```

#### FileSystem.set\_file\_permissions

```python
@intercept_errors(message_prefix="Failed to set file permissions: ")
def set_file_permissions(path: str,
                         mode: str = None,
                         owner: str = None,
                         group: str = None) -> None
```

Sets permissions and ownership for a file or directory. Any of the parameters can be None
to leave that attribute unchanged.

**Arguments**:

- `path` _str_ - Path to the file or directory. Relative paths are resolved based on
  the sandbox working directory.
- `mode` _Optional[str]_ - File mode/permissions in octal format
  (e.g., "644" for rw-r--r--).
- `owner` _Optional[str]_ - User owner of the file.
- `group` _Optional[str]_ - Group owner of the file.
  

**Example**:

```python
# Make a file executable
sandbox.fs.set_file_permissions(
    path="workspace/scripts/run.sh",
    mode="755"  # rwxr-xr-x
)

# Change file owner
sandbox.fs.set_file_permissions(
    path="workspace/data/file.txt",
    owner="daytona",
    group="daytona"
)
```

#### FileSystem.upload\_file

```python
@overload
def upload_file(file: bytes, remote_path: str, timeout: int = 30 * 60) -> None
```

Uploads a file to the specified path in the Sandbox. If a file already exists at
the destination path, it will be overwritten. This method is useful when you want to upload
small files that fit into memory.

**Arguments**:

- `file` _bytes_ - File contents as a bytes object.
- `remote_path` _str_ - Path to the destination file. Relative paths are resolved based on
  the sandbox working directory.
- `timeout` _int_ - Timeout for the upload operation in seconds. 0 means no timeout. Default is 30 minutes.
  

**Example**:

```python
# Upload a text file
content = b"Hello, World!"
sandbox.fs.upload_file(content, "tmp/hello.txt")

# Upload a local file
with open("local_file.txt", "rb") as f:
    content = f.read()
sandbox.fs.upload_file(content, "tmp/file.txt")

# Upload binary data
import json
data = {"key": "value"}
content = json.dumps(data).encode('utf-8')
sandbox.fs.upload_file(content, "tmp/config.json")
```

#### FileSystem.upload\_file

```python
@overload
def upload_file(local_path: str,
                remote_path: str,
                timeout: int = 30 * 60) -> None
```

Uploads a file from the local file system to the specified path in the Sandbox.
If a file already exists at the destination path, it will be overwritten. This method uses
streaming to upload the file, so it is useful when you want to upload larger files that may
not fit into memory.

**Arguments**:

- `local_path` _str_ - Path to the local file to upload.
- `remote_path` _str_ - Path to the destination file in the Sandbox. Relative paths are
  resolved based on the sandbox working directory.
- `timeout` _int_ - Timeout for the upload operation in seconds. 0 means no timeout. Default is 30 minutes.
  

**Example**:

```python
sandbox.fs.upload_file("local_file.txt", "tmp/large_file.txt")
```

#### FileSystem.upload\_files

```python
@intercept_errors(message_prefix="Failed to upload files: ")
def upload_files(files: List[FileUpload], timeout: int = 30 * 60) -> None
```

Uploads multiple files to the Sandbox. If files already exist at the destination paths,
they will be overwritten.

**Arguments**:

- `files` _List[FileUpload]_ - List of files to upload.
- `timeout` _int_ - Timeout for the upload operation in seconds. 0 means no timeout. Default is 30 minutes.

**Example**:

```python
# Upload multiple text files
files = [
    FileUpload(
        source=b"Content of file 1",
        destination="/tmp/file1.txt"
    ),
    FileUpload(
        source="workspace/data/file2.txt",
        destination="/tmp/file2.txt"
    ),
    FileUpload(
        source=b'{"key": "value"}',
        destination="/tmp/config.json"
    )
]
sandbox.fs.upload_files(files)
```


## FileUpload

```python
@dataclass
class FileUpload()
```

Represents a file to be uploaded to the Sandbox.

**Attributes**:

- `source` _Union[bytes, str]_ - File contents as a bytes object or a local file path. If a bytes object is provided,
  make sure it fits into memory, otherwise use the local file path which content will be streamed to the Sandbox.
- `destination` _str_ - Absolute destination path in the Sandbox. Relative paths are resolved based on
  the sandbox working directory.

## FileDownloadRequest

```python
@dataclass
class FileDownloadRequest()
```

Represents a request to download a single file from the Sandbox.

**Attributes**:

- `source` _str_ - Source path in the Sandbox. Relative paths are resolved based on the user's
  root directory.
- `destination` _Optional[str]_ - Destination path in the local filesystem where the file content will be
  streamed to. If not provided, the file will be downloaded in the bytes buffer
  (might cause memory issues if the file is large).

## FileDownloadResponse

```python
@dataclass
class FileDownloadResponse()
```

Represents the response to a single file download request.

**Attributes**:

- `source` _str_ - The original source path requested for download.
- `result` _Union[str, bytes, None]_ - The download result - file path (if destination provided in the request)
  or bytes content (if no destination in the request), None if failed or no data received.
- `error` _Optional[str]_ - Error message if the download failed, None if successful.

## Git

```python
class Git()
```

Provides Git operations within a Sandbox.

**Example**:

```python
# Clone a repository
sandbox.git.clone(
    url="https://github.com/user/repo.git",
    path="workspace/repo"
)

# Check repository status
status = sandbox.git.status("workspace/repo")
print(f"Modified files: {status.modified}")

# Stage and commit changes
sandbox.git.add("workspace/repo", ["file.txt"])
sandbox.git.commit(
    path="workspace/repo",
    message="Update file",
    author="John Doe",
    email="john@example.com"
)
```

#### Git.\_\_init\_\_

```python
def __init__(api_client: GitApi)
```

Initializes a new Git handler instance.

**Arguments**:

- `api_client` _GitApi_ - API client for Sandbox Git operations.

#### Git.add

```python
@intercept_errors(message_prefix="Failed to add files: ")
def add(path: str, files: List[str]) -> None
```

Stages the specified files for the next commit, similar to
running 'git add' on the command line.

**Arguments**:

- `path` _str_ - Path to the Git repository root. Relative paths are resolved based on
  the sandbox working directory.
- `files` _List[str]_ - List of file paths or directories to stage, relative to the repository root.
  

**Example**:

```python
# Stage a single file
sandbox.git.add("workspace/repo", ["file.txt"])

# Stage multiple files
sandbox.git.add("workspace/repo", [
    "src/main.py",
    "tests/test_main.py",
    "README.md"
])
```

#### Git.branches

```python
@intercept_errors(message_prefix="Failed to list branches: ")
def branches(path: str) -> ListBranchResponse
```

Lists branches in the repository.

**Arguments**:

- `path` _str_ - Path to the Git repository root. Relative paths are resolved based on
  the sandbox working directory.
  

**Returns**:

- `ListBranchResponse` - List of branches in the repository.
  

**Example**:

```python
response = sandbox.git.branches("workspace/repo")
print(f"Branches: {response.branches}")
```

#### Git.clone

```python
@intercept_errors(message_prefix="Failed to clone repository: ")
def clone(url: str,
          path: str,
          branch: Optional[str] = None,
          commit_id: Optional[str] = None,
          username: Optional[str] = None,
          password: Optional[str] = None) -> None
```

Clones a Git repository into the specified path. It supports
cloning specific branches or commits, and can authenticate with the remote
repository if credentials are provided.

**Arguments**:

- `url` _str_ - Repository URL to clone from.
- `path` _str_ - Path where the repository should be cloned. Relative paths are resolved
  based on the sandbox working directory.
- `branch` _Optional[str]_ - Specific branch to clone. If not specified,
  clones the default branch.
- `commit_id` _Optional[str]_ - Specific commit to clone. If specified,
  the repository will be left in a detached HEAD state at this commit.
- `username` _Optional[str]_ - Git username for authentication.
- `password` _Optional[str]_ - Git password or token for authentication.
  

**Example**:

```python
# Clone the default branch
sandbox.git.clone(
    url="https://github.com/user/repo.git",
    path="workspace/repo"
)

# Clone a specific branch with authentication
sandbox.git.clone(
    url="https://github.com/user/private-repo.git",
    path="workspace/private",
    branch="develop",
    username="user",
    password="token"
)

# Clone a specific commit
sandbox.git.clone(
    url="https://github.com/user/repo.git",
    path="workspace/repo-old",
    commit_id="abc123"
)
```

#### Git.commit

```python
@intercept_errors(message_prefix="Failed to commit changes: ")
def commit(path: str,
           message: str,
           author: str,
           email: str,
           allow_empty: bool = False) -> GitCommitResponse
```

Creates a new commit with the staged changes. Make sure to stage
changes using the add() method before committing.

**Arguments**:

- `path` _str_ - Path to the Git repository root. Relative paths are resolved based on
  the sandbox working directory.
- `message` _str_ - Commit message describing the changes.
- `author` _str_ - Name of the commit author.
- `email` _str_ - Email address of the commit author.
- `allow_empty` _bool, optional_ - Allow creating an empty commit when no changes are staged. Defaults to False.
  

**Example**:

```python
# Stage and commit changes
sandbox.git.add("workspace/repo", ["README.md"])
sandbox.git.commit(
    path="workspace/repo",
    message="Update documentation",
    author="John Doe",
    email="john@example.com",
    allow_empty=True
)
```

#### Git.push

```python
@intercept_errors(message_prefix="Failed to push changes: ")
def push(path: str,
         username: Optional[str] = None,
         password: Optional[str] = None) -> None
```

Pushes all local commits on the current branch to the remote
repository. If the remote repository requires authentication, provide
username and password/token.

**Arguments**:

- `path` _str_ - Path to the Git repository root. Relative paths are resolved based on
  the sandbox working directory.
- `username` _Optional[str]_ - Git username for authentication.
- `password` _Optional[str]_ - Git password or token for authentication.
  

**Example**:

```python
# Push without authentication (for public repos or SSH)
sandbox.git.push("workspace/repo")

# Push with authentication
sandbox.git.push(
    path="workspace/repo",
    username="user",
    password="github_token"
)
```

#### Git.pull

```python
@intercept_errors(message_prefix="Failed to pull changes: ")
def pull(path: str,
         username: Optional[str] = None,
         password: Optional[str] = None) -> None
```

Pulls changes from the remote repository. If the remote repository requires authentication,
provide username and password/token.

**Arguments**:

- `path` _str_ - Path to the Git repository root. Relative paths are resolved based on
  the sandbox working directory.
- `username` _Optional[str]_ - Git username for authentication.
- `password` _Optional[str]_ - Git password or token for authentication.
  

**Example**:

```python
# Pull without authentication
sandbox.git.pull("workspace/repo")

# Pull with authentication
sandbox.git.pull(
    path="workspace/repo",
    username="user",
    password="github_token"
)
```

#### Git.status

```python
@intercept_errors(message_prefix="Failed to get status: ")
def status(path: str) -> GitStatus
```

Gets the current Git repository status.

**Arguments**:

- `path` _str_ - Path to the Git repository root. Relative paths are resolved based on
  the sandbox working directory.
  

**Returns**:

- `GitStatus` - Repository status information including:
  - current_branch: Current branch name
  - file_status: List of file statuses
  - ahead: Number of local commits not pushed to remote
  - behind: Number of remote commits not pulled locally
  - branch_published: Whether the branch has been published to the remote repository
  

**Example**:

```python
status = sandbox.git.status("workspace/repo")
print(f"On branch: {status.current_branch}")
print(f"Commits ahead: {status.ahead}")
print(f"Commits behind: {status.behind}")
```

#### Git.checkout\_branch

```python
@intercept_errors(message_prefix="Failed to checkout branch: ")
def checkout_branch(path: str, branch: str) -> None
```

Checkout branch in the repository.

**Arguments**:

- `path` _str_ - Path to the Git repository root. Relative paths are resolved based on
  the sandbox working directory.
- `branch` _str_ - Name of the branch to checkout
  

**Example**:

```python
# Checkout a branch
sandbox.git.checkout_branch("workspace/repo", "feature-branch")
```

#### Git.create\_branch

```python
@intercept_errors(message_prefix="Failed to create branch: ")
def create_branch(path: str, name: str) -> None
```

Create branch in the repository.

**Arguments**:

- `path` _str_ - Path to the Git repository root. Relative paths are resolved based on
  the sandbox working directory.
- `name` _str_ - Name of the new branch to create
  

**Example**:

```python
# Create a new branch
sandbox.git.create_branch("workspace/repo", "new-feature")
```

#### Git.delete\_branch

```python
@intercept_errors(message_prefix="Failed to delete branch: ")
def delete_branch(path: str, name: str) -> None
```

Delete branch in the repository.

**Arguments**:

- `path` _str_ - Path to the Git repository root. Relative paths are resolved based on
  the sandbox working directory.
- `name` _str_ - Name of the branch to delete
  

**Example**:

```python
# Delete a branch
sandbox.git.delete_branch("workspace/repo", "old-feature")
```


## GitCommitResponse

```python
class GitCommitResponse()
```

Response from the git commit.

**Attributes**:

- `sha` _str_ - The SHA of the commit

## LspServer

```python
class LspServer()
```

Provides Language Server Protocol functionality for code intelligence to provide
IDE-like features such as code completion, symbol search, and more.

#### LspServer.\_\_init\_\_

```python
def __init__(language_id: LspLanguageId, path_to_project: str,
             api_client: LspApi)
```

Initializes a new LSP server instance.

**Arguments**:

- `language_id` _LspLanguageId_ - The language server type (e.g., LspLanguageId.TYPESCRIPT).
- `path_to_project` _str_ - Absolute path to the project root directory.
- `api_client` _LspApi_ - API client for Sandbox operations.
- `instance` _SandboxInstance_ - The Sandbox instance this server belongs to.

#### LspServer.start

```python
@intercept_errors(message_prefix="Failed to start LSP server: ")
def start() -> None
```

Starts the language server.

This method must be called before using any other LSP functionality.
It initializes the language server for the specified language and project.

**Example**:

```python
lsp = sandbox.create_lsp_server("typescript", "workspace/project")
lsp.start()  # Initialize the server
# Now ready for LSP operations
```

#### LspServer.stop

```python
@intercept_errors(message_prefix="Failed to stop LSP server: ")
def stop() -> None
```

Stops the language server.

This method should be called when the LSP server is no longer needed to
free up system resources.

**Example**:

```python
# When done with LSP features
lsp.stop()  # Clean up resources
```

#### LspServer.did\_open

```python
@intercept_errors(message_prefix="Failed to open file: ")
def did_open(path: str) -> None
```

Notifies the language server that a file has been opened.

This method should be called when a file is opened in the editor to enable
language features like diagnostics and completions for that file. The server
will begin tracking the file's contents and providing language features.

**Arguments**:

- `path` _str_ - Path to the opened file. Relative paths are resolved based on the project path
  set in the LSP server constructor.
  

**Example**:

```python
# When opening a file for editing
lsp.did_open("workspace/project/src/index.ts")
# Now can get completions, symbols, etc. for this file
```

#### LspServer.did\_close

```python
@intercept_errors(message_prefix="Failed to close file: ")
def did_close(path: str) -> None
```

Notify the language server that a file has been closed.

This method should be called when a file is closed in the editor to allow
the language server to clean up any resources associated with that file.

**Arguments**:

- `path` _str_ - Path to the closed file. Relative paths are resolved based on the project path
  set in the LSP server constructor.
  

**Example**:

```python
# When done editing a file
lsp.did_close("workspace/project/src/index.ts")
```

#### LspServer.document\_symbols

```python
@intercept_errors(message_prefix="Failed to get symbols from document: ")
def document_symbols(path: str) -> List[LspSymbol]
```

Gets symbol information (functions, classes, variables, etc.) from a document.

**Arguments**:

- `path` _str_ - Path to the file to get symbols from. Relative paths are resolved based on the project path
  set in the LSP server constructor.
  

**Returns**:

- `List[LspSymbol]` - List of symbols in the document. Each symbol includes:
  - name: The symbol's name
  - kind: The symbol's kind (function, class, variable, etc.)
  - location: The location of the symbol in the file
  

**Example**:

```python
# Get all symbols in a file
symbols = lsp.document_symbols("workspace/project/src/index.ts")
for symbol in symbols:
    print(f"{symbol.kind} {symbol.name}: {symbol.location}")
```

#### LspServer.workspace\_symbols

```python
@deprecated(
    reason=
    "Method is deprecated. Use `sandbox_symbols` instead. This method will be removed in a future version."
)
def workspace_symbols(query: str) -> List[LspSymbol]
```

Searches for symbols matching the query string across all files
in the Sandbox.

**Arguments**:

- `query` _str_ - Search query to match against symbol names.
  

**Returns**:

- `List[LspSymbol]` - List of matching symbols from all files.

#### LspServer.sandbox\_symbols

```python
@intercept_errors(message_prefix="Failed to get symbols from sandbox: ")
def sandbox_symbols(query: str) -> List[LspSymbol]
```

Searches for symbols matching the query string across all files
in the Sandbox.

**Arguments**:

- `query` _str_ - Search query to match against symbol names.
  

**Returns**:

- `List[LspSymbol]` - List of matching symbols from all files. Each symbol
  includes:
  - name: The symbol's name
  - kind: The symbol's kind (function, class, variable, etc.)
  - location: The location of the symbol in the file
  

**Example**:

```python
# Search for all symbols containing "User"
symbols = lsp.sandbox_symbols("User")
for symbol in symbols:
    print(f"{symbol.name} in {symbol.location}")
```

#### LspServer.completions

```python
@intercept_errors(message_prefix="Failed to get completions: ")
def completions(path: str, position: LspCompletionPosition) -> CompletionList
```

Gets completion suggestions at a position in a file.

**Arguments**:

- `path` _str_ - Path to the file. Relative paths are resolved based on the project path
  set in the LSP server constructor.
- `position` _LspCompletionPosition_ - Cursor position to get completions for.
  

**Returns**:

- `CompletionList` - List of completion suggestions. The list includes:
  - isIncomplete: Whether more items might be available
  - items: List of completion items, each containing:
  - label: The text to insert
  - kind: The kind of completion
  - detail: Additional details about the item
  - documentation: Documentation for the item
  - sortText: Text used to sort the item in the list
  - filterText: Text used to filter the item
  - insertText: The actual text to insert (if different from label)
  

**Example**:

```python
# Get completions at a specific position
pos = LspCompletionPosition(line=10, character=15)
completions = lsp.completions("workspace/project/src/index.ts", pos)
for item in completions.items:
    print(f"{item.label} ({item.kind}): {item.detail}")
```


## LspLanguageId

```python
class LspLanguageId(Enum)
```

Language IDs for Language Server Protocol (LSP).

**Enum Members**:
    - `PYTHON` ("python")
    - `TYPESCRIPT` ("typescript")
    - `JAVASCRIPT` ("javascript")

## LspCompletionPosition

```python
class LspCompletionPosition()
```

Represents a zero-based completion position in a text document,
specified by line number and character offset.

**Attributes**:

- `line` _int_ - Zero-based line number in the document.
- `character` _int_ - Zero-based character offset on the line.

#### LspCompletionPosition.\_\_init\_\_

```python
def __init__(line: int, character: int)
```

Initialize a new LspCompletionPosition instance.

**Arguments**:

- `line` _int_ - Zero-based line number in the document.
- `character` _int_ - Zero-based character offset on the line.

## ObjectStorage

```python
class ObjectStorage()
```

ObjectStorage class for interacting with object storage services.

**Attributes**:

- `endpoint_url` _str_ - The endpoint URL for the object storage service.
- `aws_access_key_id` _str_ - The access key ID for the object storage service.
- `aws_secret_access_key` _str_ - The secret access key for the object storage service.
- `aws_session_token` _str_ - The session token for the object storage service. Used for temporary credentials.
- `bucket_name` _str_ - The name of the bucket to use. Defaults to "daytona-volume-builds".

#### ObjectStorage.upload

```python
def upload(path: str,
           organization_id: str,
           archive_base_path: str | None = None) -> str
```

Uploads a file to the object storage service.

**Arguments**:

- `path` _str_ - The path to the file to upload.
- `organization_id` _str_ - The organization ID to use.
- `archive_base_path` _str_ - The base path to use for the archive.
  

**Returns**:

- `str` - The hash of the uploaded file.

## Process

```python
class Process()
```

Handles process and code execution within a Sandbox.

#### Process.\_\_init\_\_

```python
def __init__(code_toolbox: SandboxPythonCodeToolbox, api_client: ProcessApi,
             ensure_toolbox_url: Callable[[], None])
```

Initialize a new Process instance.

**Arguments**:

- `code_toolbox` _SandboxPythonCodeToolbox_ - Language-specific code execution toolbox.
- `api_client` _ProcessApi_ - API client for process operations.
- `ensure_toolbox_url` _Callable[[], None]_ - Ensures the toolbox API URL is initialized.
  Must be called before invoking any private methods on the API client.

#### Process.exec

```python
@intercept_errors(message_prefix="Failed to execute command: ")
def exec(command: str,
         cwd: Optional[str] = None,
         env: Optional[Dict[str, str]] = None,
         timeout: Optional[int] = None) -> ExecuteResponse
```

Execute a shell command in the Sandbox.

**Arguments**:

- `command` _str_ - Shell command to execute.
- `cwd` _Optional[str]_ - Working directory for command execution. If not
  specified, uses the sandbox working directory.
- `env` _Optional[Dict[str, str]]_ - Environment variables to set for the command.
- `timeout` _Optional[int]_ - Maximum time in seconds to wait for the command
  to complete. 0 means wait indefinitely.
  

**Returns**:

- `ExecuteResponse` - Command execution results containing:
  - exit_code: The command's exit status
  - result: Standard output from the command
  - artifacts: ExecutionArtifacts object containing `stdout` (same as result)
  and `charts` (matplotlib charts metadata)
  

**Example**:

```python
# Simple command
response = sandbox.process.exec("echo 'Hello'")
print(response.artifacts.stdout)  # Prints: Hello

# Command with working directory
result = sandbox.process.exec("ls", cwd="workspace/src")

# Command with timeout
result = sandbox.process.exec("sleep 10", timeout=5)
```

#### Process.code\_run

```python
def code_run(code: str,
             params: Optional[CodeRunParams] = None,
             timeout: Optional[int] = None) -> ExecuteResponse
```

Executes code in the Sandbox using the appropriate language runtime.

**Arguments**:

- `code` _str_ - Code to execute.
- `params` _Optional[CodeRunParams]_ - Parameters for code execution.
- `timeout` _Optional[int]_ - Maximum time in seconds to wait for the code
  to complete. 0 means wait indefinitely.
  

**Returns**:

- `ExecuteResponse` - Code execution result containing:
  - exit_code: The execution's exit status
  - result: Standard output from the code
  - artifacts: ExecutionArtifacts object containing `stdout` (same as result)
  and `charts` (matplotlib charts metadata)
  

**Example**:

```python
# Run Python code
response = sandbox.process.code_run('''
    x = 10
    y = 20
    print(f"Sum: {x + y}")
''')
print(response.artifacts.stdout)  # Prints: Sum: 30
```
  
  Matplotlib charts are automatically detected and returned in the `charts` field
  of the `ExecutionArtifacts` object.
```python
code = '''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 30)
y = np.sin(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, 'b-', linewidth=2)
plt.title('Line Chart')
plt.xlabel('X-axis (seconds)')
plt.ylabel('Y-axis (amplitude)')
plt.grid(True)
plt.show()
'''

response = sandbox.process.code_run(code)
chart = response.artifacts.charts[0]

print(f"Type: {chart.type}")
print(f"Title: {chart.title}")
if chart.type == ChartType.LINE and isinstance(chart, LineChart):
    print(f"X Label: {chart.x_label}")
    print(f"Y Label: {chart.y_label}")
    print(f"X Ticks: {chart.x_ticks}")
    print(f"X Tick Labels: {chart.x_tick_labels}")
    print(f"X Scale: {chart.x_scale}")
    print(f"Y Ticks: {chart.y_ticks}")
    print(f"Y Tick Labels: {chart.y_tick_labels}")
    print(f"Y Scale: {chart.y_scale}")
    print("Elements:")
    for element in chart.elements:
        print(f"Label: {element.label}")
        print(f"Points: {element.points}")
```

#### Process.create\_session

```python
@intercept_errors(message_prefix="Failed to create session: ")
def create_session(session_id: str) -> None
```

Creates a new long-running background session in the Sandbox.

Sessions are background processes that maintain state between commands, making them ideal for
scenarios requiring multiple related commands or persistent environment setup. You can run
long-running commands and monitor process status.

**Arguments**:

- `session_id` _str_ - Unique identifier for the new session.
  

**Example**:

```python
# Create a new session
session_id = "my-session"
sandbox.process.create_session(session_id)
session = sandbox.process.get_session(session_id)
# Do work...
sandbox.process.delete_session(session_id)
```

#### Process.get\_session

```python
@intercept_errors(message_prefix="Failed to get session: ")
def get_session(session_id: str) -> Session
```

Gets a session in the Sandbox.

**Arguments**:

- `session_id` _str_ - Unique identifier of the session to retrieve.
  

**Returns**:

- `Session` - Session information including:
  - session_id: The session's unique identifier
  - commands: List of commands executed in the session
  

**Example**:

```python
session = sandbox.process.get_session("my-session")
for cmd in session.commands:
    print(f"Command: {cmd.command}")
```

#### Process.get\_session\_command

```python
@intercept_errors(message_prefix="Failed to get session command: ")
def get_session_command(session_id: str, command_id: str) -> Command
```

Gets information about a specific command executed in a session.

**Arguments**:

- `session_id` _str_ - Unique identifier of the session.
- `command_id` _str_ - Unique identifier of the command.
  

**Returns**:

- `Command` - Command information including:
  - id: The command's unique identifier
  - command: The executed command string
  - exit_code: Command's exit status (if completed)
  

**Example**:

```python
cmd = sandbox.process.get_session_command("my-session", "cmd-123")
if cmd.exit_code == 0:
    print(f"Command {cmd.command} completed successfully")
```

#### Process.execute\_session\_command

```python
@intercept_errors(message_prefix="Failed to execute session command: ")
def execute_session_command(
        session_id: str,
        req: SessionExecuteRequest,
        timeout: Optional[int] = None) -> SessionExecuteResponse
```

Executes a command in the session.

**Arguments**:

- `session_id` _str_ - Unique identifier of the session to use.
- `req` _SessionExecuteRequest_ - Command execution request containing:
  - command: The command to execute
  - run_async: Whether to execute asynchronously
  

**Returns**:

- `SessionExecuteResponse` - Command execution results containing:
  - cmd_id: Unique identifier for the executed command
  - output: Combined command output (stdout and stderr) (if synchronous execution)
  - stdout: Standard output from the command
  - stderr: Standard error from the command
  - exit_code: Command exit status (if synchronous execution)
  

**Example**:

```python
# Execute commands in sequence, maintaining state
session_id = "my-session"

# Change directory
req = SessionExecuteRequest(command="cd /workspace")
sandbox.process.execute_session_command(session_id, req)

# Create a file
req = SessionExecuteRequest(command="echo 'Hello' > test.txt")
sandbox.process.execute_session_command(session_id, req)

# Read the file
req = SessionExecuteRequest(command="cat test.txt")
result = sandbox.process.execute_session_command(session_id, req)
print(f"Command stdout: {result.stdout}")
print(f"Command stderr: {result.stderr}")
```

#### Process.get\_session\_command\_logs

```python
@intercept_errors(message_prefix="Failed to get session command logs: ")
def get_session_command_logs(session_id: str,
                             command_id: str) -> SessionCommandLogsResponse
```

Get the logs for a command executed in a session.

**Arguments**:

- `session_id` _str_ - Unique identifier of the session.
- `command_id` _str_ - Unique identifier of the command.
  

**Returns**:

- `SessionCommandLogsResponse` - Command logs including:
  - output: Combined command output (stdout and stderr)
  - stdout: Standard output from the command
  - stderr: Standard error from the command
  

**Example**:

```python
logs = sandbox.process.get_session_command_logs(
    "my-session",
    "cmd-123"
)
print(f"Command stdout: {logs.stdout}")
print(f"Command stderr: {logs.stderr}")
```

#### Process.get\_session\_command\_logs\_async

```python
@intercept_errors(message_prefix="Failed to get session command logs: ")
async def get_session_command_logs_async(
        session_id: str, command_id: str, on_stdout: Callable[[str], None],
        on_stderr: Callable[[str], None]) -> None
```

Asynchronously retrieves and processes the logs for a command executed in a session as they become available.

**Arguments**:

- `session_id` _str_ - Unique identifier of the session.
- `command_id` _str_ - Unique identifier of the command.
- `on_stdout` _Callable[[str], None]_ - Callback function to handle stdout log chunks as they arrive.
- `on_stderr` _Callable[[str], None]_ - Callback function to handle stderr log chunks as they arrive.
  

**Example**:

```python
await sandbox.process.get_session_command_logs_async(
    "my-session",
    "cmd-123",
    lambda log: print(f"[STDOUT]: {log}"),
    lambda log: print(f"[STDERR]: {log}"),
)
```

#### Process.list\_sessions

```python
@intercept_errors(message_prefix="Failed to list sessions: ")
def list_sessions() -> List[Session]
```

Lists all sessions in the Sandbox.

**Returns**:

- `List[Session]` - List of all sessions in the Sandbox.
  

**Example**:

```python
sessions = sandbox.process.list_sessions()
for session in sessions:
    print(f"Session {session.session_id}:")
    print(f"  Commands: {len(session.commands)}")
```

#### Process.delete\_session

```python
@intercept_errors(message_prefix="Failed to delete session: ")
def delete_session(session_id: str) -> None
```

Terminates and removes a session from the Sandbox, cleaning up any resources
associated with it.

**Arguments**:

- `session_id` _str_ - Unique identifier of the session to delete.
  

**Example**:

```python
# Create and use a session
sandbox.process.create_session("temp-session")
# ... use the session ...

# Clean up when done
sandbox.process.delete_session("temp-session")
```

#### Process.create\_pty\_session

```python
@intercept_errors(message_prefix="Failed to create PTY session: ")
def create_pty_session(id: str,
                       cwd: Optional[str] = None,
                       envs: Optional[Dict[str, str]] = None,
                       pty_size: Optional[PtySize] = None) -> PtyHandle
```

Creates a new PTY (pseudo-terminal) session in the Sandbox.

Creates an interactive terminal session that can execute commands and handle user input.
The PTY session behaves like a real terminal, supporting features like command history.

**Arguments**:

- `id` - Unique identifier for the PTY session. Must be unique within the Sandbox.
- `cwd` - Working directory for the PTY session. Defaults to the sandbox's working directory.
- `env` - Environment variables to set in the PTY session. These will be merged with
  the Sandbox's default environment variables.
- `pty_size` - Terminal size configuration. Defaults to 80x24 if not specified.
  

**Returns**:

- `PtyHandle` - Handle for managing the created PTY session. Use this to send input,
  receive output, resize the terminal, and manage the session lifecycle.
  

**Raises**:

- `DaytonaError` - If the PTY session creation fails or the session ID is already in use.

#### Process.connect\_pty\_session

```python
@intercept_errors(message_prefix="Failed to connect PTY session: ")
def connect_pty_session(session_id: str) -> PtyHandle
```

Connects to an existing PTY session in the Sandbox.

Establishes a WebSocket connection to an existing PTY session, allowing you to
interact with a previously created terminal session.

**Arguments**:

- `session_id` - Unique identifier of the PTY session to connect to.
  

**Returns**:

- `PtyHandle` - Handle for managing the connected PTY session.
  

**Raises**:

- `DaytonaError` - If the PTY session doesn't exist or connection fails.

#### Process.list\_pty\_sessions

```python
@intercept_errors(message_prefix="Failed to list PTY sessions: ")
def list_pty_sessions() -> List[PtySessionInfo]
```

Lists all PTY sessions in the Sandbox.

Retrieves information about all PTY sessions in this Sandbox.

**Returns**:

- `List[PtySessionInfo]` - List of PTY session information objects containing
  details about each session's state, creation time, and configuration.
  

**Example**:

```python
# List all PTY sessions
sessions = sandbox.process.list_pty_sessions()

for session in sessions:
    print(f"Session ID: {session.id}")
    print(f"Active: {session.active}")
    print(f"Created: {session.created_at}")
```

#### Process.get\_pty\_session\_info

```python
@intercept_errors(message_prefix="Failed to get PTY session info: ")
def get_pty_session_info(session_id: str) -> PtySessionInfo
```

Gets detailed information about a specific PTY session.

Retrieves comprehensive information about a PTY session including its current state,
configuration, and metadata.

**Arguments**:

- `session_id` - Unique identifier of the PTY session to retrieve information for.
  

**Returns**:

- `PtySessionInfo` - Detailed information about the PTY session including ID, state,
  creation time, working directory, environment variables, and more.
  

**Raises**:

- `DaytonaError` - If the PTY session doesn't exist.
  

**Example**:

```python
# Get details about a specific PTY session
session_info = sandbox.process.get_pty_session_info("my-session")

print(f"Session ID: {session_info.id}")
print(f"Active: {session_info.active}")
print(f"Working Directory: {session_info.cwd}")
print(f"Terminal Size: {session_info.cols}x{session_info.rows}")
```

#### Process.kill\_pty\_session

```python
@intercept_errors(message_prefix="Failed to kill PTY session: ")
def kill_pty_session(session_id: str) -> None
```

Kills a PTY session and terminates its associated process.

Forcefully terminates the PTY session and cleans up all associated resources.
This will close any active connections and kill the underlying shell process.
This operation is irreversible. Any unsaved work in the terminal session will be lost.

**Arguments**:

- `session_id` - Unique identifier of the PTY session to kill.
  

**Raises**:

- `DaytonaError` - If the PTY session doesn't exist or cannot be killed.
  

**Example**:

```python
# Kill a specific PTY session
sandbox.process.kill_pty_session("my-session")

# Verify the session no longer exists
pty_sessions = sandbox.process.list_pty_sessions()
for pty_session in pty_sessions:
    print(f"PTY session: {pty_session.id}")
```

#### Process.resize\_pty\_session

```python
@intercept_errors(message_prefix="Failed to resize PTY session: ")
def resize_pty_session(session_id: str, pty_size: PtySize) -> PtySessionInfo
```

Resizes a PTY session's terminal dimensions.

Changes the terminal size of an active PTY session. This is useful when the
client terminal is resized or when you need to adjust the display for different
output requirements.

**Arguments**:

- `session_id` - Unique identifier of the PTY session to resize.
- `pty_size` - New terminal dimensions containing the desired columns and rows.
  

**Returns**:

- `PtySessionInfo` - Updated session information reflecting the new terminal size.
  

**Raises**:

- `DaytonaError` - If the PTY session doesn't exist or resize operation fails.
  

**Example**:

```python
from daytona.common.pty import PtySize

# Resize a PTY session to a larger terminal
new_size = PtySize(rows=40, cols=150)
updated_info = sandbox.process.resize_pty_session("my-session", new_size)

print(f"Terminal resized to {updated_info.cols}x{updated_info.rows}")

# You can also use the PtyHandle's resize method
pty_handle.resize(new_size)
```


## CodeRunParams

```python
@dataclass
class CodeRunParams()
```

Parameters for code execution.

**Attributes**:

- `argv` _Optional[List[str]]_ - Command line arguments
- `env` _Optional[Dict[str, str]]_ - Environment variables

## SessionExecuteRequest

```python
class SessionExecuteRequest(ApiSessionExecuteRequest,
                            AsyncApiSessionExecuteRequest)
```

Contains the request for executing a command in a session.

**Attributes**:

- `command` _str_ - The command to execute.
- `run_async` _Optional[bool]_ - Whether to execute the command asynchronously.
- `var_async` _Optional[bool]_ - Deprecated. Use `run_async` instead.

## ExecutionArtifacts

```python
class ExecutionArtifacts()
```

Artifacts from the command execution.

**Attributes**:

- `stdout` _str_ - Standard output from the command, same as `result` in `ExecuteResponse`
- `charts` _Optional[List[Chart]]_ - List of chart metadata from matplotlib

## ExecuteResponse

```python
class ExecuteResponse(BaseModel)
```

Response from the command execution.

**Attributes**:

- `exit_code` _int_ - The exit code from the command execution
- `result` _str_ - The output from the command execution
- `artifacts` _Optional[ExecutionArtifacts]_ - Artifacts from the command execution

## SessionExecuteResponse

```python
class SessionExecuteResponse(ApiSessionExecuteResponse)
```

Response from the session command execution.

**Attributes**:

- `output` _str_ - The output from the command execution
- `exit_code` _int_ - The exit code from the command execution

## SessionCommandLogsResponse

```python
class SessionCommandLogsResponse()
```

Response from the command logs.

**Attributes**:

- `output` _str_ - The combined output from the command
- `stdout` _str_ - The stdout from the command
- `stderr` _str_ - The stderr from the command

#### parse\_session\_command\_logs

```python
def parse_session_command_logs(data: bytes) -> SessionCommandLogsResponse
```

Parse combined stdout/stderr output into separate streams.

**Arguments**:

- `data` - Combined log bytes with STDOUT_PREFIX and STDERR_PREFIX markers
  

**Returns**:

  SessionCommandLogsResponse with separated stdout and stderr

#### demux\_log

```python
def demux_log(data: bytes) -> tuple[bytes, bytes]
```

Demultiplex combined stdout/stderr log data.

**Arguments**:

- `data` - Combined log bytes with STDOUT_PREFIX and STDERR_PREFIX markers
  

**Returns**:

  Tuple of (stdout_bytes, stderr_bytes)

## Sandbox

```python
class Sandbox(SandboxDto)
```

Represents a Daytona Sandbox.

**Attributes**:

- `fs` _FileSystem_ - File system operations interface.
- `git` _Git_ - Git operations interface.
- `process` _Process_ - Process execution interface.
- `computer_use` _ComputerUse_ - Computer use operations interface for desktop automation.
- `id` _str_ - Unique identifier for the Sandbox.
- `name` _str_ - Name of the Sandbox.
- `organization_id` _str_ - Organization ID of the Sandbox.
- `snapshot` _str_ - Daytona snapshot used to create the Sandbox.
- `user` _str_ - OS user running in the Sandbox.
- `env` _Dict[str, str]_ - Environment variables set in the Sandbox.
- `labels` _Dict[str, str]_ - Custom labels attached to the Sandbox.
- `public` _bool_ - Whether the Sandbox is publicly accessible.
- `target` _str_ - Target location of the runner where the Sandbox runs.
- `cpu` _int_ - Number of CPUs allocated to the Sandbox.
- `gpu` _int_ - Number of GPUs allocated to the Sandbox.
- `memory` _int_ - Amount of memory allocated to the Sandbox in GiB.
- `disk` _int_ - Amount of disk space allocated to the Sandbox in GiB.
- `state` _SandboxState_ - Current state of the Sandbox (e.g., "started", "stopped").
- `error_reason` _str_ - Error message if Sandbox is in error state.
- `backup_state` _SandboxBackupStateEnum_ - Current state of Sandbox backup.
- `backup_created_at` _str_ - When the backup was created.
- `auto_stop_interval` _int_ - Auto-stop interval in minutes.
- `auto_archive_interval` _int_ - Auto-archive interval in minutes.
- `auto_delete_interval` _int_ - Auto-delete interval in minutes.
- `volumes` _List[str]_ - Volumes attached to the Sandbox.
- `build_info` _str_ - Build information for the Sandbox if it was created from dynamic build.
- `created_at` _str_ - When the Sandbox was created.
- `updated_at` _str_ - When the Sandbox was last updated.
- `network_block_all` _bool_ - Whether to block all network access for the Sandbox.
- `network_allow_list` _str_ - Comma-separated list of allowed CIDR network addresses for the Sandbox.

#### Sandbox.\_\_init\_\_

```python
def __init__(sandbox_dto: SandboxDto, toolbox_api: ApiClient,
             sandbox_api: SandboxApi, code_toolbox: SandboxCodeToolbox,
             get_toolbox_base_url: Callable[[], str])
```

Initialize a new Sandbox instance.

**Arguments**:

- `sandbox_dto` _SandboxDto_ - The sandbox data from the API.
- `toolbox_api` _ApiClient_ - API client for toolbox operations.
- `sandbox_api` _SandboxApi_ - API client for Sandbox operations.
- `code_toolbox` _SandboxCodeToolbox_ - Language-specific toolbox implementation.
- `get_toolbox_base_url` _Callable[[], str]_ - Function to get the toolbox base URL.

#### Sandbox.refresh\_data

```python
@intercept_errors(message_prefix="Failed to refresh sandbox data: ")
def refresh_data() -> None
```

Refreshes the Sandbox data from the API.

**Example**:

```python
sandbox.refresh_data()
print(f"Sandbox {sandbox.id}:")
print(f"State: {sandbox.state}")
print(f"Resources: {sandbox.cpu} CPU, {sandbox.memory} GiB RAM")
```

#### Sandbox.get\_user\_home\_dir

```python
@intercept_errors(message_prefix="Failed to get user home directory: ")
def get_user_home_dir() -> str
```

Gets the user's home directory path inside the Sandbox.

**Returns**:

- `str` - The absolute path to the user's home directory inside the Sandbox.
  

**Example**:

```python
user_home_dir = sandbox.get_user_home_dir()
print(f"Sandbox user home: {user_home_dir}")
```

#### Sandbox.get\_work\_dir

```python
@intercept_errors(message_prefix="Failed to get working directory path: ")
def get_work_dir() -> str
```

Gets the working directory path inside the Sandbox.

**Returns**:

- `str` - The absolute path to the Sandbox working directory. Uses the WORKDIR specified in
  the Dockerfile if present, or falling back to the user's home directory if not.
  

**Example**:

```python
work_dir = sandbox.get_work_dir()
print(f"Sandbox working directory: {work_dir}")
```

#### Sandbox.create\_lsp\_server

```python
def create_lsp_server(language_id: LspLanguageId,
                      path_to_project: str) -> LspServer
```

Creates a new Language Server Protocol (LSP) server instance.

The LSP server provides language-specific features like code completion,
diagnostics, and more.

**Arguments**:

- `language_id` _LspLanguageId_ - The language server type (e.g., LspLanguageId.PYTHON).
- `path_to_project` _str_ - Path to the project root directory. Relative paths are resolved
  based on the sandbox working directory.
  

**Returns**:

- `LspServer` - A new LSP server instance configured for the specified language.
  

**Example**:

```python
lsp = sandbox.create_lsp_server("python", "workspace/project")
```

#### Sandbox.set\_labels

```python
@intercept_errors(message_prefix="Failed to set labels: ")
def set_labels(labels: Dict[str, str]) -> Dict[str, str]
```

Sets labels for the Sandbox.

Labels are key-value pairs that can be used to organize and identify Sandboxes.

**Arguments**:

- `labels` _Dict[str, str]_ - Dictionary of key-value pairs representing Sandbox labels.
  

**Returns**:

  Dict[str, str]: Dictionary containing the updated Sandbox labels.
  

**Example**:

```python
new_labels = sandbox.set_labels({
    "project": "my-project",
    "environment": "development",
    "team": "backend"
})
print(f"Updated labels: {new_labels}")
```

#### Sandbox.start

```python
@intercept_errors(message_prefix="Failed to start sandbox: ")
@with_timeout(error_message=lambda self, timeout: (
    f"Sandbox {self.id} failed to start within the {timeout} seconds timeout period"
))
def start(timeout: Optional[float] = 60)
```

Starts the Sandbox and waits for it to be ready.

**Arguments**:

- `timeout` _Optional[float]_ - Maximum time to wait in seconds. 0 means no timeout. Default is 60 seconds.
  

**Raises**:

- `DaytonaError` - If timeout is negative. If sandbox fails to start or times out.
  

**Example**:

```python
sandbox = daytona.get_current_sandbox("my-sandbox")
sandbox.start(timeout=40)  # Wait up to 40 seconds
print("Sandbox started successfully")
```

#### Sandbox.stop

```python
@intercept_errors(message_prefix="Failed to stop sandbox: ")
@with_timeout(error_message=lambda self, timeout: (
    f"Sandbox {self.id} failed to stop within the {timeout} seconds timeout period"
))
def stop(timeout: Optional[float] = 60)
```

Stops the Sandbox and waits for it to be fully stopped.

**Arguments**:

- `timeout` _Optional[float]_ - Maximum time to wait in seconds. 0 means no timeout. Default is 60 seconds.
  

**Raises**:

- `DaytonaError` - If timeout is negative; If sandbox fails to stop or times out
  

**Example**:

```python
sandbox = daytona.get_current_sandbox("my-sandbox")
sandbox.stop()
print("Sandbox stopped successfully")
```

#### Sandbox.delete

```python
@intercept_errors(message_prefix="Failed to remove sandbox: ")
def delete(timeout: Optional[float] = 60) -> None
```

Deletes the Sandbox.

**Arguments**:

- `timeout` _Optional[float]_ - Timeout (in seconds) for sandbox deletion. 0 means no timeout.
  Default is 60 seconds.

#### Sandbox.wait\_for\_sandbox\_start

```python
@intercept_errors(
    message_prefix="Failure during waiting for sandbox to start: ")
@with_timeout(error_message=lambda self, timeout: (
    f"Sandbox {self.id} failed to become ready within the {timeout} seconds timeout period"
))
def wait_for_sandbox_start(timeout: Optional[float] = 60) -> None
```

Waits for the Sandbox to reach the 'started' state. Polls the Sandbox status until it
reaches the 'started' state, encounters an error or times out.

**Arguments**:

- `timeout` _Optional[float]_ - Maximum time to wait in seconds. 0 means no timeout. Default is 60 seconds.
  

**Raises**:

- `DaytonaError` - If timeout is negative; If Sandbox fails to start or times out

#### Sandbox.wait\_for\_sandbox\_stop

```python
@intercept_errors(
    message_prefix="Failure during waiting for sandbox to stop: ")
@with_timeout(error_message=lambda self, timeout: (
    f"Sandbox {self.id} failed to become stopped within the {timeout} seconds timeout period"
))
def wait_for_sandbox_stop(timeout: Optional[float] = 60) -> None
```

Waits for the Sandbox to reach the 'stopped' state. Polls the Sandbox status until it
reaches the 'stopped' state, encounters an error or times out. It will wait up to 60 seconds
for the Sandbox to stop.
Treats destroyed as stopped to cover ephemeral sandboxes that are automatically deleted after stopping.

**Arguments**:

- `timeout` _Optional[float]_ - Maximum time to wait in seconds. 0 means no timeout. Default is 60 seconds.
  

**Raises**:

- `DaytonaError` - If timeout is negative. If Sandbox fails to stop or times out.

#### Sandbox.set\_autostop\_interval

```python
@intercept_errors(message_prefix="Failed to set auto-stop interval: ")
def set_autostop_interval(interval: int) -> None
```

Sets the auto-stop interval for the Sandbox.

The Sandbox will automatically stop after being idle (no new events) for the specified interval.
Events include any state changes or interactions with the Sandbox through the SDK.
Interactions using Sandbox Previews are not included.

**Arguments**:

- `interval` _int_ - Number of minutes of inactivity before auto-stopping.
  Set to 0 to disable auto-stop. Defaults to 15.
  

**Raises**:

- `DaytonaError` - If interval is negative
  

**Example**:

```python
# Auto-stop after 1 hour
sandbox.set_autostop_interval(60)
# Or disable auto-stop
sandbox.set_autostop_interval(0)
```

#### Sandbox.set\_auto\_archive\_interval

```python
@intercept_errors(message_prefix="Failed to set auto-archive interval: ")
def set_auto_archive_interval(interval: int) -> None
```

Sets the auto-archive interval for the Sandbox.

The Sandbox will automatically archive after being continuously stopped for the specified interval.

**Arguments**:

- `interval` _int_ - Number of minutes after which a continuously stopped Sandbox will be auto-archived.
  Set to 0 for the maximum interval. Default is 7 days.
  

**Raises**:

- `DaytonaError` - If interval is negative
  

**Example**:

```python
# Auto-archive after 1 hour
sandbox.set_auto_archive_interval(60)
# Or use the maximum interval
sandbox.set_auto_archive_interval(0)
```

#### Sandbox.set\_auto\_delete\_interval

```python
@intercept_errors(message_prefix="Failed to set auto-delete interval: ")
def set_auto_delete_interval(interval: int) -> None
```

Sets the auto-delete interval for the Sandbox.

The Sandbox will automatically delete after being continuously stopped for the specified interval.

**Arguments**:

- `interval` _int_ - Number of minutes after which a continuously stopped Sandbox will be auto-deleted.
  Set to negative value to disable auto-delete. Set to 0 to delete immediately upon stopping.
  By default, auto-delete is disabled.
  

**Example**:

```python
# Auto-delete after 1 hour
sandbox.set_auto_delete_interval(60)
# Or delete immediately upon stopping
sandbox.set_auto_delete_interval(0)
# Or disable auto-delete
sandbox.set_auto_delete_interval(-1)
```

#### Sandbox.get\_preview\_link

```python
@intercept_errors(message_prefix="Failed to get preview link: ")
def get_preview_link(port: int) -> PortPreviewUrl
```

Retrieves the preview link for the sandbox at the specified port. If the port is closed,
it will be opened automatically. For private sandboxes, a token is included to grant access
to the URL.

**Arguments**:

- `port` _int_ - The port to open the preview link on.
  

**Returns**:

- `PortPreviewUrl` - The response object for the preview link, which includes the `url`
  and the `token` (to access private sandboxes).
  

**Example**:

```python
preview_link = sandbox.get_preview_link(3000)
print(f"Preview URL: {preview_link.url}")
print(f"Token: {preview_link.token}")
```

#### Sandbox.archive

```python
@intercept_errors(message_prefix="Failed to archive sandbox: ")
def archive() -> None
```

Archives the sandbox, making it inactive and preserving its state. When sandboxes are
archived, the entire filesystem state is moved to cost-effective object storage, making it
possible to keep sandboxes available for an extended period. The tradeoff between archived
and stopped states is that starting an archived sandbox takes more time, depending on its size.
Sandbox must be stopped before archiving.

#### Sandbox.create\_ssh\_access

```python
@intercept_errors(message_prefix="Failed to create SSH access: ")
def create_ssh_access(
        expires_in_minutes: Optional[int] = None) -> SshAccessDto
```

Creates an SSH access token for the sandbox.

**Arguments**:

- `expires_in_minutes` _Optional[int]_ - The number of minutes the SSH access token will be valid for.

#### Sandbox.revoke\_ssh\_access

```python
@intercept_errors(message_prefix="Failed to revoke SSH access: ")
def revoke_ssh_access(token: str) -> None
```

Revokes an SSH access token for the sandbox.

**Arguments**:

- `token` _str_ - The token to revoke.

#### Sandbox.validate\_ssh\_access

```python
@intercept_errors(message_prefix="Failed to validate SSH access: ")
def validate_ssh_access(token: str) -> SshAccessValidationDto
```

Validates an SSH access token for the sandbox.

**Arguments**:

- `token` _str_ - The token to validate.


## PaginatedSandboxes

```python
class PaginatedSandboxes(PaginatedSandboxesDto)
```

Represents a paginated list of Daytona Sandboxes.

**Attributes**:

- `items` _List[Sandbox]_ - List of Sandbox instances in the current page.
- `total` _int_ - Total number of Sandboxes across all pages.
- `page` _int_ - Current page number.
- `total_pages` _int_ - Total number of pages available.

## Resources

```python
@dataclass
class Resources()
```

Resources configuration for Sandbox.

**Attributes**:

- `cpu` _Optional[int]_ - Number of CPU cores to allocate.
- `memory` _Optional[int]_ - Amount of memory in GiB to allocate.
- `disk` _Optional[int]_ - Amount of disk space in GiB to allocate.
- `gpu` _Optional[int]_ - Number of GPUs to allocate.
  

**Example**:

```python
resources = Resources(
    cpu=2,
    memory=4,  # 4GiB RAM
    disk=20,   # 20GiB disk
    gpu=1
)
params = CreateSandboxFromImageParams(
    image=Image.debian_slim("3.12"),
    language="python",
    resources=resources
)
```

## Snapshot

```python
class Snapshot(SnapshotDto)
```

Represents a Daytona Snapshot which is a pre-configured sandbox.

**Attributes**:

- `id` _StrictStr_ - Unique identifier for the Snapshot.
- `organization_id` _Optional[StrictStr]_ - Organization ID of the Snapshot.
- `general` _Optional[bool]_ - Whether the Snapshot is general.
- `name` _StrictStr_ - Name of the Snapshot.
- `image_name` _StrictStr_ - Name of the Image of the Snapshot.
- `state` _StrictStr_ - State of the Snapshot.
- `size` _Optional[Union[StrictFloat, StrictInt]]_ - Size of the Snapshot.
- `entrypoint` _Optional[List[str]]_ - Entrypoint of the Snapshot.
- `cpu` _Union[StrictFloat, StrictInt]_ - CPU of the Snapshot.
- `gpu` _Union[StrictFloat, StrictInt]_ - GPU of the Snapshot.
- `mem` _Union[StrictFloat, StrictInt]_ - Memory of the Snapshot in GiB.
- `disk` _Union[StrictFloat, StrictInt]_ - Disk of the Snapshot in GiB.
- `error_reason` _Optional[StrictStr]_ - Error reason of the Snapshot.
- `created_at` _StrictStr_ - Timestamp when the Snapshot was created.
- `updated_at` _StrictStr_ - Timestamp when the Snapshot was last updated.
- `last_used_at` _StrictStr_ - Timestamp when the Snapshot was last used.


## SnapshotService

```python
class SnapshotService()
```

Service for managing Daytona Snapshots. Can be used to list, get, create and delete Snapshots.

#### SnapshotService.list

```python
@intercept_errors(message_prefix="Failed to list snapshots: ")
def list(page: Optional[int] = None,
         limit: Optional[int] = None) -> PaginatedSnapshots
```

Returns paginated list of Snapshots.

**Arguments**:

- `page` _Optional[int]_ - Page number for pagination (starting from 1).
- `limit` _Optional[int]_ - Maximum number of items per page.
  

**Returns**:

- `PaginatedSnapshots` - Paginated list of Snapshots.
  

**Example**:

```python
daytona = Daytona()
result = daytona.snapshot.list(page=2, limit=10)
for snapshot in result.items:
    print(f"{snapshot.name} ({snapshot.image_name})")
```

#### SnapshotService.delete

```python
@intercept_errors(message_prefix="Failed to delete snapshot: ")
def delete(snapshot: Snapshot) -> None
```

Delete a Snapshot.

**Arguments**:

- `snapshot` _Snapshot_ - Snapshot to delete.
  

**Example**:

```python
daytona = Daytona()
snapshot = daytona.snapshot.get("test-snapshot")
daytona.snapshot.delete(snapshot)
print("Snapshot deleted")
```

#### SnapshotService.get

```python
@intercept_errors(message_prefix="Failed to get snapshot: ")
def get(name: str) -> Snapshot
```

Get a Snapshot by name.

**Arguments**:

- `name` _str_ - Name of the Snapshot to get.
  

**Returns**:

- `Snapshot` - The Snapshot object.
  

**Example**:

```python
daytona = Daytona()
snapshot = daytona.snapshot.get("test-snapshot-name")
print(f"{snapshot.name} ({snapshot.image_name})")
```

#### SnapshotService.create

```python
@intercept_errors(message_prefix="Failed to create snapshot: ")
@with_timeout(error_message=lambda self, timeout: (
    f"Failed to create snapshot within {timeout} seconds timeout period."))
def create(params: CreateSnapshotParams,
           *,
           on_logs: Callable[[str], None] = None,
           timeout: Optional[float] = 0) -> Snapshot
```

Creates and registers a new snapshot from the given Image definition.

**Arguments**:

- `params` _CreateSnapshotParams_ - Parameters for snapshot creation.
- `on_logs` _Callable[[str], None]_ - This callback function handles snapshot creation logs.
- `timeout` _Optional[float]_ - Default is no timeout. Timeout in seconds (0 means no timeout).

**Example**:

```python
image = Image.debianSlim('3.12').pipInstall('numpy')
daytona.snapshot.create(
    CreateSnapshotParams(name='my-snapshot', image=image),
    on_logs=lambda chunk: print(chunk, end=""),
)
```

#### SnapshotService.activate

```python
def activate(snapshot: Snapshot) -> Snapshot
```

Activate a snapshot.

**Arguments**:

- `snapshot` _Snapshot_ - The Snapshot instance.

**Returns**:

- `Snapshot` - The activated Snapshot instance.

#### SnapshotService.process\_image\_context

```python
@staticmethod
def process_image_context(object_storage_api: ObjectStorageApi,
                          image: Image) -> List[str]
```

Processes the image context by uploading it to object storage.

**Arguments**:

- `image` _Image_ - The Image instance.

**Returns**:

- `List[str]` - List of context hashes stored in object storage.

## PaginatedSnapshots

```python
class PaginatedSnapshots(PaginatedSnapshotsDto)
```

Represents a paginated list of Daytona Snapshots.

**Attributes**:

- `items` _List[Snapshot]_ - List of Snapshot instances in the current page.
- `total` _int_ - Total number of Snapshots across all pages.
- `page` _int_ - Current page number.
- `total_pages` _int_ - Total number of pages available.

## CreateSnapshotParams

```python
class CreateSnapshotParams(BaseModel)
```

Parameters for creating a new snapshot.

**Attributes**:

- `name` _Optional[str]_ - Name of the snapshot.
- `image` _Union[str, Image]_ - Image of the snapshot. If a string is provided,
  it should be available on some registry. If an Image instance is provided,
  it will be used to create a new image in Daytona.
- `resources` _Optional[Resources]_ - Resources of the snapshot.
- `entrypoint` _Optional[List[str]]_ - Entrypoint of the snapshot.

## Volume

```python
class Volume(VolumeDto)
```

Represents a Daytona Volume which is a shared storage volume for Sandboxes.

**Attributes**:

- `id` _StrictStr_ - Unique identifier for the Volume.
- `name` _StrictStr_ - Name of the Volume.
- `organization_id` _StrictStr_ - Organization ID of the Volume.
- `state` _StrictStr_ - State of the Volume.
- `created_at` _StrictStr_ - Date and time when the Volume was created.
- `updated_at` _StrictStr_ - Date and time when the Volume was last updated.
- `last_used_at` _StrictStr_ - Date and time when the Volume was last used.


## VolumeService

```python
class VolumeService()
```

Service for managing Daytona Volumes. Can be used to list, get, create and delete Volumes.

#### VolumeService.list

```python
def list() -> List[Volume]
```

List all Volumes.

**Returns**:

- `List[Volume]` - List of all Volumes.
  

**Example**:

```python
daytona = Daytona()
volumes = daytona.volume.list()
for volume in volumes:
    print(f"{volume.name} ({volume.id})")
```

#### VolumeService.get

```python
def get(name: str, create: bool = False) -> Volume
```

Get a Volume by name.

**Arguments**:

- `name` _str_ - Name of the Volume to get.
- `create` _bool_ - If True, create a new Volume if it doesn't exist.
  

**Returns**:

- `Volume` - The Volume object.
  

**Example**:

```python
daytona = Daytona()
volume = daytona.volume.get("test-volume-name", create=True)
print(f"{volume.name} ({volume.id})")
```

#### VolumeService.create

```python
def create(name: str) -> Volume
```

Create a new Volume.

**Arguments**:

- `name` _str_ - Name of the Volume to create.
  

**Returns**:

- `Volume` - The Volume object.
  

**Example**:

```python
daytona = Daytona()
volume = daytona.volume.create("test-volume")
print(f"{volume.name} ({volume.id}); state: {volume.state}")
```

#### VolumeService.delete

```python
def delete(volume: Volume) -> None
```

Delete a Volume.

**Arguments**:

- `volume` _Volume_ - Volume to delete.
  

**Example**:

```python
daytona = Daytona()
volume = daytona.volume.get("test-volume")
daytona.volume.delete(volume)
print("Volume deleted")
```

The Daytona SDK can be configured to run in multiple geographic regions. The following regions are currently available:

| Region        | Target |
| ------------- | ---- |
| United States | `us` |
| Europe        | `eu` |

The region is specificed by setting the `target` parameter on initialization:

```python
from daytona import Daytona, DaytonaConfig

# Configure Daytona to use the US region
config = DaytonaConfig(
    target="us"
)

# Initialize the Daytona client with the specified configuration
daytona = Daytona(config)
```
```typescript
import { Daytona } from '@daytonaio/sdk';

// Configure Daytona to use the EU region
const daytona: Daytona = new Daytona({
    target: "eu"
});
```

For more information, see [Configuration](https://www.daytona.io/docs/configuration.md).

import Image from 'astro/components/Image.astro'

Sandboxes are isolated development environments managed by Daytona. This guide covers how to create, manage, and remove Sandboxes using the SDK.
By default, Sandboxes auto-stop after 15 minutes of inactivity and use **1 vCPU**, **1GB RAM**, and **3GiB disk**.

## Sandbox Lifecycle

Throughout its lifecycle, a Daytona Sandbox can have several different states. The diagram below shows the states and possible transitions between them.

<Fragment set:html={sandboxDiagram} />

By default, sandboxes auto-stop after `15 minutes` of inactivity and auto-archive after `7 days` of being stopped. To keep the Sandbox running indefinitely without interruption, set the auto-stop value to `0` during creation.

## Creating Sandboxes

The Daytona SDK provides an option to create Sandboxes with default or custom configurations. You can specify the language, [Snapshot](https://www.daytona.io/docs/en/snapshots.md), resources, environment variables, and volumes for the Sandbox.
Running Sandboxes utilize CPU, memory, and disk storage. Every resource is charged per second of usage.

:::tip
If you want to prolong the auto-stop interval, you can [set the auto-stop interval parameter](https://www.daytona.io/docs/en/sandbox-management.md#auto-stop-interval) when creating a Sandbox.
:::

### Basic Sandbox Creation

The Daytona SDK provides methods to create Sandboxes with default configurations, specific languages, custom names, or custom labels using Python and TypeScript.

    ```python
    from daytona import Daytona, CreateSandboxFromSnapshotParams

    daytona = Daytona()

    # Create a basic Sandbox

    sandbox = daytona.create()

    # Create a Sandbox with specific language

    params = CreateSandboxFromSnapshotParams(language="python")
    sandbox = daytona.create(params)

    # Create a Sandbox with a custom name

    params = CreateSandboxFromSnapshotParams(name="my-sandbox")
    sandbox = daytona.create(params)

    # Create a Sandbox with custom labels

    params = CreateSandboxFromSnapshotParams(labels={"SOME_LABEL": "my-label"})
    sandbox = daytona.create(params)

    ```


    ```typescript
    import { Daytona } from '@daytonaio/sdk';

    const daytona = new Daytona();

    // Create a basic Sandbox
    const sandbox = await daytona.create();

    // Create a Sandbox with specific language
    const sandbox = await daytona.create({ language: 'typescript' });

    // Create a Sandbox with a custom name
    const sandbox = await daytona.create({ name: 'my-sandbox' });

    // Create a Sandbox with custom labels
    const sandbox = await daytona.create({ labels: { SOME_LABEL: 'my-label' } });
    ```


:::note
**Sandbox Names**: You can specify a custom name for your sandbox using the `name` parameter. If not provided, the sandbox ID will be used as the name. Sandbox names are reusable - once a sandbox with a specific name is destroyed, that name becomes available for use again.
:::

See: [create (Python SDK)](https://www.daytona.io/docs/en/python-sdk/sync/daytona.md#daytonacreate), [create (TypeScript SDK)](https://www.daytona.io/docs/en/typescript-sdk/daytona.md#create)

When Sandboxes are not actively used, it is recommended that they be stopped. This can be done manually [using the stop command](https://www.daytona.io/docs/en/sandbox-management.md#stop-and-start-sandbox) or automatically by [setting the auto-stop interval](https://www.daytona.io/docs/en/sandbox-management.md#auto-stop-and-auto-archive).

:::note
Daytona keeps a pool of warm Sandboxes using default Snapshots.\
When available, your Sandbox will launch in milliseconds instead of cold-booting.
:::

### Sandbox Resources

Daytona Sandboxes come with **1 vCPU**, **1GB RAM**, and **3GiB disk** by default.

Use the `Resources` class to define exactly what you need: CPU, memory, and disk space are all customizable.

Organizations get a maximum Sandbox resource limit of 4 vCPUs, 8GB RAM, and 10GB disk. Need more power? Contact [support@daytona.io](mailto:support@daytona.io) and let us know your use case.

Check your available resources and limits in the [dashboard](https://app.daytona.io/dashboard/limits).

    ```python
    from daytona import Daytona, Resources, CreateSandboxFromImageParams, Image

    daytona = Daytona()

    # Create a Sandbox with custom resources

    resources = Resources(
        cpu=2,  # 2 CPU cores
        memory=4,  # 4GB RAM
        disk=8,  # 8GB disk space
    )

    params = CreateSandboxFromImageParams(
        image=Image.debian_slim("3.12"),
        resources=resources
    )

    sandbox = daytona.create(params)

    ```


    ```typescript
    import { Daytona, Image } from "@daytonaio/sdk";

    async function main() {
      const daytona = new Daytona();

      // Create a Sandbox with custom resources
      const sandbox = await daytona.create({
        image: Image.debianSlim("3.13"),
        resources: {
          cpu: 2, // 2 CPU cores
          memory: 4, // 4GB RAM
          disk: 8, // 8GB disk space
        },
      });
    }

    main();
    ```


:::note
All resource parameters are optional. If not specified, Daytona will use default values appropriate for the selected language and use case.
:::

### Ephemeral Sandboxes

Ephemeral Sandboxes are Sandboxes that are automatically deleted once they are stopped. They are useful for short-lived tasks or for testing purposes.

To create an ephemeral Sandbox, set `ephemeral` to `True` when creating a Sandbox:

    ```python
    from daytona import Daytona, CreateSandboxFromSnapshotParams

    daytona = Daytona()

    # Create an ephemeral Sandbox

    params = CreateSandboxFromSnapshotParams(
      ephemeral=True,
      auto_stop_interval=5 # the ephemeral sandbox will be deleted after 5 minutes of inactivity
    )
    sandbox = daytona.create(params)
    ```


    ```typescript
    import { Daytona } from '@daytonaio/sdk';

    const daytona = new Daytona();

    // Create an ephemeral Sandbox
    const sandbox = await daytona.create({
      ephemeral: true,
      autoStopInterval: 5 // the ephemeral sandbox will be deleted after 5 minutes of inactivity
    });
    ```


:::note
Setting ["autoDeleteInterval: 0"](#auto-delete-interval) has the same effect as setting "ephemeral" to `true`.
:::

### Network Settings (Firewall)

Daytona Sandboxes provide configurable network firewall controls to enhance security and manage connectivity. By default, network access follows standard security policies, but you can customize network settings when creating a Sandbox.
Learn more about network limits in the [Network Limits](https://www.daytona.io/docs/en/network-limits.md) documentation.

## Sandbox Information

The Daytona SDK provides methods to get information about a Sandbox, such as ID, root directory, and status using Python and TypeScript.

    ```python
    # Get Sandbox ID
    sandbox_id = sandbox.id

    # Get the root directory of the Sandbox user

    root_dir = sandbox.get_user_root_dir()

    # Get the Sandbox id, auto-stop interval and state

    print(sandbox.id)
    print(sandbox.auto_stop_interval)
    print(sandbox.state)

    ```


    ```typescript
    // Get Sandbox ID
    const sandboxId = sandbox.id;

    // Get the root directory of the Sandbox user
    const rootDir = await sandbox.getUserRootDir();

    // Get the Sandbox id, auto-stop interval and state
    console.log(sandbox.id)
    console.log(sandbox.autoStopInterval)
    console.log(sandbox.state)
    ```


To get the preview URL for a specific port, check out [Preview & Authentication](https://www.daytona.io/docs/en/preview-and-authentication.md).

## Stop and Start Sandbox

The Daytona SDK provides methods to stop and start Sandboxes using Python and TypeScript.

Stopped Sandboxes maintain filesystem persistence while their memory state is cleared. They incur only disk usage costs and can be started again when needed.

    ```python
    sandbox = daytona.create(CreateSandboxParams(language="python"))

    # Stop Sandbox

    sandbox.stop()

    print(sandbox.id) # 7cd11133-96c1-4cc8-9baa-c757b8f8c916

    # The sandbox ID can later be used to find the sandbox and start it

    sandbox = daytona.find_one("7cd11133-96c1-4cc8-9baa-c757b8f8c916")

    # Start Sandbox

    sandbox.start()

    ```


    ```typescript
    const sandbox = await daytona.create({ language: 'typescript' });

    // Stop Sandbox
    await sandbox.stop();

    console.log(sandbox.id) // 7cd11133-96c1-4cc8-9baa-c757b8f8c916

    // The sandbox ID can later be used to find the sandbox and start it

    const sandbox = await daytona.findOne("7cd11133-96c1-4cc8-9baa-c757b8f8c916");

    // Start Sandbox
    await sandbox.start();
    ```


See: [stop (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/sandbox.md#sandboxstop), [start (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/sandbox.md#sandboxstart), [find_one (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/daytona.md#daytonafind_one), [stop (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/sandbox.md#stop), [start (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/sandbox.md#start), [findOne (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/daytona.md#findone)

The stopped state should be used when the Sandbox is expected to be started again soon. Otherwise, it is recommended to stop and then archive the Sandbox to eliminate disk usage costs.

## Archive Sandbox

The Daytona SDK provides methods to archive Sandboxes using Python and TypeScript.

When Sandboxes are archived, the entire filesystem state is moved to very cost-effective object storage, making it possible to keep Sandboxes available for an extended period.
Starting an archived Sandbox takes more time than starting a stopped Sandbox, depending on its size.

A Sandbox must be stopped before it can be archived, and can be started again in the same way as a stopped Sandbox.

    ```python
    # Archive Sandbox
    sandbox.archive()
    ```

    ```typescript
    // Archive Sandbox
    await sandbox.archive();
    ```

See: [archive (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/sandbox.md#sandboxarchive), [archive (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/sandbox.md#archive)

## Delete Sandbox

The Daytona SDK provides methods to delete Sandboxes using Python and TypeScript.

    ```python
    # Delete Sandbox
    sandbox.delete()
    ```

    ```typescript
    // Delete Sandbox
    await sandbox.delete();
    ```

See: [delete (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/sandbox.md#sandboxdelete), [delete (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/sandbox.md#delete)

:::tip
Check out the [Daytona CLI](https://www.daytona.io/docs/en/getting-started.md#setting-up-the-daytona-cli) if you prefer managing Sandboxes through the terminal:

```bash
daytona sandbox list
```

```text
Sandbox               State           Region        Last Event
───────────────────────────────────────────────────────────────────────────
ugliest_quokka        STARTED         us            1 hour ago

associated_yak        STARTED         us            14 hours ago

developed_lemur       STARTED         us            17 hours ago
```

```bash
daytona sandbox start|stop|remove --all
```

```text
All sandboxes have been deleted
```

:::

## Automated Lifecycle Management

Daytona Sandboxes can be automatically stopped, archived, and deleted based on user-defined intervals.

### Auto-stop Interval

The auto-stop interval parameter sets the amount of time after which a running Sandbox will be automatically stopped.

Sandbox activity, such as SDK API calls or network requests through [preview URLs](https://www.daytona.io/docs/en/preview-and-authentication.md), will reset the auto-stop timer.

The parameter can either be set to:

- a time interval in minutes
- `0`, which disables the auto-stop functionality, allowing the sandbox to run indefinitely

If the parameter is not set, the default interval of `15` minutes will be used.

    ```python
    sandbox = daytona.create(CreateSandboxFromSnapshotParams(
        snapshot="my-snapshot-name",
        auto_stop_interval=0,  # Disables the auto-stop feature - default is 15 minutes
    ))
    ```

    ```typescript
    const sandbox = await daytona.create({
        snapshot: "my-snapshot-name",
        autoStopInterval: 0, // Disables the auto-stop feature - default is 15 minutes
    });
    ```

### Auto-archive Interval

The auto-archive interval parameter sets the amount of time after which a continuously stopped Sandbox will be automatically archived.

The parameter can either be set to:

- a time interval in minutes
- `0`, which means the maximum interval of `30 days` will be used

If the parameter is not set, the default interval of `7 days` days will be used.

    ```python
    sandbox = daytona.create(CreateSandboxFromSnapshotParams(
        snapshot="my-snapshot-name",
        auto_archive_interval=60 # Auto-archive after a Sandbox has been stopped for 1 hour
    ))
    ```

    ```typescript
    const sandbox = await daytona.create({
        snapshot: "my-snapshot-name",
        autoArchiveInterval: 60 // Auto-archive after a Sandbox has been stopped for 1 hour
    });
    ```

### Auto-delete Interval

The auto-delete interval parameter sets the amount of time after which a continuously stopped Sandbox will be automatically deleted. By default, Sandboxes will never be automatically deleted.

The parameter can either be set to:

- a time interval in minutes
- `-1`, which disables the auto-delete functionality
- `0`, which means the Sandbox will be deleted immediately after stopping

If the parameter is not set, the Sandbox will not be deleted automatically.

    ```python
    sandbox = daytona.create(CreateSandboxFromSnapshotParams(
        snapshot="my-snapshot-name",
        auto_delete_interval=60,  # Auto-delete after a Sandbox has been stopped for 1 hour
    ))

    # Delete the Sandbox immediately after it has been stopped

    sandbox.set_auto_delete_interval(0)

    # Disable auto-deletion

    sandbox.set_auto_delete_interval(-1)

    ```


    ```typescript
    const sandbox = await daytona.create({
        snapshot: "my-snapshot-name",
        autoDeleteInterval: 60, // Auto-delete after a Sandbox has been stopped for 1 hour
    });

    // Delete the Sandbox immediately after it has been stopped
    await sandbox.setAutoDeleteInterval(0)

    // Disable auto-deletion
    await sandbox.setAutoDeleteInterval(-1)
    ```


## Run Indefinitely

By default, Sandboxes auto-stop after 15 minutes of inactivity. To keep a Sandbox running without interruption, set the auto-stop interval to `0` when creating a new Sandbox:

    ```python
    sandbox = daytona.create(CreateSandboxFromSnapshotParams(
        snapshot="my-snapshot-name",
        auto_stop_interval=0,  # Disables the auto-stop feature - default is 15 minutes
    ))
    ```

    ```typescript
    const sandbox = await daytona.create({
        snapshot: "my-snapshot-name",
        autoStopInterval: 0, // Disables the auto-stop feature - default is 15 minutes
    });
    ```

Snapshots are Sandbox templates that can be created from [Docker](https://www.docker.com/) or [OCI](https://opencontainers.org/) compatible images. New Sandboxes can be created from a custom Snapshot pre-configured with your required dependencies, settings, and resources, or from the [default Snapshot](#default-snapshot).

## Creating Snapshots

Snapshots can be created in one of four ways: [from a public image](#using-a-public-image), [from a private image](#using-private-registries), [from a local image](#using-a-local-image), or [using the Declarative Builder](#using-the-declarative-builder).

### Using a Public Image

To create a Snapshot from a public image, follow these steps:

1. Visit the Dashboard and click on [Snapshots](https://app.daytona.io/dashboard/snapshots)
2. Click on **Create Snapshot**
3. Enter the name and tag of any publicly accessible image from Docker Hub (e.g. `alpine:3.21.3`) or from another public container registry (e.g. `my-public-registry.com/custom-alpine:3.21`)

Optionally, set the entrypoint field. If the image does not have a long-running entrypoint, Daytona will automatically run `sleep infinity` to prevent the container from exiting immediately.

:::note
Since images tagged `latest` get frequent updates, only specific tags (e.g. `0.1.0`) are supported. Same idea applies to tags such as `lts` or `stable` and we recommend avoiding those when defining an image.
:::

Once the Snapshot is pulled, validated and has an `Active` state, it is ready to be used.

### Images from Private Registries

To create a Snapshot from an image that is available in a private container registry:

1. Go to the [Registries](https://app.daytona.io/dashboard/registries) page in the Dashboard
2. Click the **Add Registry** button.
3. Fill out the form with an appropriate custom name, URL, username, password, and project (if applicable)
4. Once the Container Registry is created, you may go back to the [Snapshots](https://app.daytona.io/dashboard/snapshots) page
5. When creating the Snapshot, make sure to input the entire private image name, including the registry location and project name (e.g. `my-private-registry.com/<my-project>/custom-alpine:3.21`)

The next step is the same; simply set the `CreateSandboxFromSnapshotParams` field to use the custom Snapshot and no further authentication is needed.

#### Using a Private Docker Hub Image

To use a private Docker Hub image, you'll need to [add a Container Registry](https://www.daytona.io/docs/en/snapshots.md#images-from-private-registries) with your Docker Hub credentials:

- **Registry URL**: Set this to `docker.io`
- **Username**: Enter your Docker Hub username (the account with access to the private image)
- **Password**: Use a [Docker Hub Personal Access Token](https://docs.docker.com/docker-hub/access-tokens/) (not your account password)
- **Create the Snapshot**: Once the registry is added, you can create a Snapshot using the full image path as the image name: `docker.io/<username>/<image>:<tag>`

### Using a Local Image

In order to avoid having to manually set up a private container registry and push your image there, the [Daytona CLI](https://www.daytona.io/docs/en/getting-started.md#setting-up-the-daytona-cli) allows you to create a Snapshot from your local image or from a local Dockerfile and use it in your Sandboxes.

To create a Snapshot from a local image:

1. Run `docker images` to ensure the image and tag you want to use is available
2. Run `daytona snapshot push <your_local_docker_image>` to create a Snapshot and push it to Daytona, e.g.:

```bash
daytona snapshot push custom-alpine:3.21 --name alpine-minimal
```

:::tip
Use the flags `--cpu`, `--memory` and `--disk` to specify the resources you want the underlying Sandboxes to have

For example `daytona snapshot push custom-alpine:3.21 --name alpine-minimal --cpu 2 --memory 4 --disk 8` will create Alpine Sandboxes with 2 vCPU, 4GiB of memory and 8GiB of disk space.
:::

:::note
Daytona expects the local image to be built for AMD64 architecture. Therefore, the `--platform=linux/amd64` flag is required when building the Docker image if your machine is running on a different architecture.

For more information, see the [CLI documentation](https://www.daytona.io/docs/en/tools/cli.md#daytona-snapshot-push).
:::

Alternatively, to do it through the CLI, use the `--dockerfile` flag under `create` to pass the path to the Dockerfile you want to use and Daytona will build the Snapshot for you. The COPY/ADD commands will be automatically parsed and added to the context - to manually add files to the context you can use the `--context` flag.

```bash
daytona snapshot create data-analysis01 --dockerfile ./Dockerfile
```

```text
Building image from /Users/idagelic/docs/Dockerfile
Step 1/5 : FROM alpine:latest

...

 ⡿  Waiting for the Snapshot to be validated ...

 ...

 ✓  Use 'harbor-transient.internal.daytona.app/daytona/trying-daytona:0.0.1' to create a new sandbox using this Snapshot

```

### Using the Declarative Builder

The declarative builder allows you to define your Snapshots using a code-first approach. See [Declarative Builder](https://www.daytona.io/docs/declarative-builder.md) for more information.

### Specifying Resources

Snapshots can be customized with specific resource requirements. By default, Daytona Sandboxes come with **1 vCPU**, **1GB RAM**, and **3GiB disk**.

To customize these resources, use the `Resources` class to define exactly what you need:

```python
from daytona import (
    Daytona,
    CreateSnapshotParams,
    Image,
    Resources,
)

daytona = Daytona()

# Create a Snapshot with custom resources
daytona.snapshot.create(
    CreateSnapshotParams(
        name="my-snapshot",
        image=Image.debian_slim("3.12"),
        # All resource parameters are optional:
        resources=Resources(
          cpu=2,
          memory=4,
          disk=8,
        ),
    ),
    on_logs=print,
)
```
```typescript
import { Daytona, Image } from "@daytonaio/sdk";

const daytona = new Daytona();

// Create a Snapshot with custom resources
await daytona.snapshot.create(
  {
    name: "my-snapshot",
    image: Image.debianSlim("3.13"),
    // All resource parameters are optional:
    resources: {
      cpu: 2,
      memory: 4,
      disk: 8,
    },
  },
  { onLogs: console.log }
);
```



Check your available resources and limits in the [dashboard](https://app.daytona.io/dashboard/limits).

## Using Snapshots

To use a Snapshot in your Sandbox, specify the `snapshot` field in the `CreateSandboxFromSnapshotParams` object:

```python
sandbox = daytona.create(CreateSandboxFromSnapshotParams(
    snapshot="my-snapshot-name",
))
```
```typescript
const sandbox = await daytona.create({
  snapshot: "my-snapshot-name",
})
```

For examples of running code inside a sandbox, see the [Getting Started Guide](https://www.daytona.io/docs/en/getting-started.md#run-code-inside-a-sandbox).

## Deleting Snapshots

To delete custom Snapshots:

1. Go to the [Snapshots](https://app.daytona.io/dashboard/snapshots) page
2. Click the three dots at the end of the row for the Snapshot you want to delete
3. Click the `Delete` button that appears

:::tip

To temporarily disable a Snapshot, instead of deleting, you can click `Disable`. This will prevent the Snapshot from being used in any new Sandboxes but will not delete it.

:::

## Running Docker in a Sandbox

Daytona Sandboxes can run Docker containers inside them (**Docker-in-Docker**), enabling you to build, test, and deploy containerized applications. This is particularly useful when your projects have dependencies on external services like databases, message queues, or other microservices.

Agents can seamlessly interact with these services since they run within the same sandbox environment, providing better isolation and security compared to external service dependencies.

### Creating a DinD Snapshot

You can create a Snapshot with Docker support using pre-built Docker-in-Docker images as a base or by manually installing Docker in a custom image.

#### Using Pre-built Images

The following base images are widely used for creating Docker-in-Docker snapshots or can be used as a base for a custom Dockerfile:

- `docker:28.3.3-dind` - Official Docker-in-Docker image (Alpine-based, lightweight)
- `docker:28.3.3-dind-rootless` - Rootless Docker-in-Docker for enhanced security
- `docker:28.3.2-dind-alpine3.22` - Docker-in-Docker image with Alpine 3.22

#### Manual Docker Installation

Alternatively, you can install Docker manually in a custom Dockerfile:

```dockerfile
FROM ubuntu:22.04
# Install Docker using the official install script
RUN curl -fsSL https://get.docker.com | VERSION=28.3.3 sh -
```

### Use Cases

- Run databases (PostgreSQL, Redis, MySQL) and other services
- Build and test containerized applications
- Deploy microservices and their dependencies
- Create isolated development environments with full container orchestration

:::note
Docker-in-Docker Sandboxes require additional resources due to the Docker daemon overhead. Consider allocating at least 2 vCPU and 4GiB of memory for optimal performance.
:::

## Default Snapshot

When a Sandbox is created with no Snapshot specified, Daytona uses a default Snapshot that includes `python`, `node`, their language servers, and several common pip packages:
- `anthropic` (v0.49.0)
- `beautifulsoup4` (v4.13.3)
- `daytona_sdk` (v0.11.1)
- `django` (v5.1.7)
- `flask` (v3.1.0)
- `huggingface` (v0.0.1)
- `instructor` (v1.7.3)
- `keras` (v3.9.0)
- `langchain` (v0.3.20)
- `llama-index` (v0.12.22)
- `matplotlib` (v3.10.1)
- `numpy` (v2.2.3)
- `ollama` (v0.4.7)
- `openai` (v1.65.4)
- `opencv-python` (v4.11.0.86)
- `pandas` (v2.2.3)
- `pillow` (v11.1.0)
- `pydantic-ai` (v0.0.35)
- `requests` (v2.32.3)
- `scikit-learn` (v1.6.1)
- `scipy` (v1.15.2)
- `seaborn` (v0.13.2)
- `SQLAlchemy` (v2.0.38)
- `transformers` (v4.49.0)

You can connect to any of your sandboxes via SSH using token-based authentication.

## Creating an SSH Access Token

To connect to a sandbox, you'll need to create an SSH access token first. This token provides secure, time-limited access to your sandbox.

SSH access can be initialized from the dashboard by opening the sandbox’s options menu and selecting `Create SSH Access`.
It can also be initialized programmatically using one of the SDKs listed below.


```python
from daytona import Daytona

daytona = Daytona()
sandbox = daytona.get("sandbox-abc123")

# Create SSH access token
ssh_access = sandbox.create_ssh_access(expires_in_minutes=60)
print(f"SSH Token: {ssh_access.token}")
```


```typescript
import { Daytona } from '@daytonaio/sdk'

const daytona = new Daytona()
const sandbox = await daytona.get('sandbox-abc123')

// Create SSH access token
const sshAccess = await sandbox.createSshAccess(60)
console.log(`SSH Token: ${sshAccess.token}`)
```


## Connection Command

Once you have your token, connect using:

```bash
ssh <token>@ssh.app.daytona.io
```

## Connecting with VSCode

Connecting your local VSCode to a sandbox requires a few simple steps:

1. Make sure that the [Remote Explorer extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.remote-explorer) is installed in your VSCode.
2. Add a new SSH connection
3. When prompted for the SSH connection URL, paste your SSH command from above.

Find out more about the extension [here](https://code.visualstudio.com/docs/remote/ssh).

## Connecting with JetBrains IDEs

Connecting your local JetBrains IDEs to a sandbox requires a few simple steps:

1. Download the [JetBrains Gateway](https://www.jetbrains.com/remote-development/gateway/) app to your local machine.
2. Add a new connection.
3. When prompted for the SSH connection URL, paste your SSH command from above.
4. Choose an IDE you want installed in your sandbox.

## Managing SSH Access

### Token Expiration

SSH access tokens expire automatically for security:

- **Default**: 60 minutes

### Revoking Access

You can revoke SSH access tokens at any time:


```python
# Revoke all SSH access for the sandbox
sandbox.revoke_ssh_access()

# Revoke specific SSH access for the sandbox
sandbox.revoke_ssh_access(token="specific-token")
```


```typescript
// Revoke all SSH access for the sandbox
await sandbox.revokeSshAccess()

// Revoke specific SSH access for the sandbox
await sandbox.revokeSshAccess('specific-token')
```

The `daytona` command-line tool provides access to Daytona's core features including managing Snapshots and the lifecycle of Daytona Sandboxes. View the installation instructions by clicking [here](https://www.daytona.io/docs/en/getting-started.md#setting-up-the-daytona-cli).

This reference lists all commands supported by the `daytona` command-line tool complete with a description of their behaviour, and any supported flags.
You can access this documentation on a per-command basis by appending the `--help`/`-h` flag when invoking `daytona`.

## daytona
Daytona CLI

```shell
daytona [flags]
```

__Flags__
| Long | Short | Description |
| :--- | :---- | :---------- |
| `--help` |  | help for daytona |
| `--version` | `-v` | Display the version of Daytona |


## daytona autocomplete
Adds a completion script for your shell environment

```shell
daytona autocomplete [bash|zsh|fish|powershell] [flags]
```

__Flags__
| Long | Short | Description |
| :--- | :---- | :---------- |
| `--help` |  | help for daytona |

<Aside type="note">
If using bash shell environment, make sure you have bash-completion installed in order to get full autocompletion functionality.
Linux Installation: ```sudo apt-get install bash-completion```
macOS Installation: ```brew install bash-completion```
</Aside>

## daytona docs
Opens the Daytona documentation in your default browser.

```shell
daytona docs [flags]
```

__Flags__
| Long | Short | Description |
| :--- | :---- | :---------- |
| `--help` |  | help for daytona |


## daytona login
Log in to Daytona

```shell
daytona login [flags]
```

__Flags__
| Long | Short | Description |
| :--- | :---- | :---------- |
| `--api-key` |  | API key to use for authentication |
| `--help` |  | help for daytona |


## daytona logout
Logout from Daytona

```shell
daytona logout [flags]
```

__Flags__
| Long | Short | Description |
| :--- | :---- | :---------- |
| `--help` |  | help for daytona |


## daytona mcp
Manage Daytona MCP Server

```shell
daytona mcp [flags]
```

__Flags__
| Long | Short | Description |
| :--- | :---- | :---------- |
| `--help` |  | help for daytona |


## daytona mcp config
Outputs JSON configuration for Daytona MCP Server

```shell
daytona mcp config [AGENT_NAME] [flags]
```

__Flags__
| Long | Short | Description |
| :--- | :---- | :---------- |
| `--help` |  | help for daytona |


## daytona mcp init
Initialize Daytona MCP Server with an agent (currently supported: claude, windsurf, cursor)


```shell
daytona mcp init [AGENT_NAME] [flags]
```

__Flags__
| Long | Short | Description |
| :--- | :---- | :---------- |
| `--help` |  | help for daytona |


## daytona mcp start
Start Daytona MCP Server

```shell
daytona mcp start [flags]
```

__Flags__
| Long | Short | Description |
| :--- | :---- | :---------- |
| `--help` |  | help for daytona |


## daytona organization
Manage Daytona organizations

```shell
daytona organization [flags]
```

__Flags__
| Long | Short | Description |
| :--- | :---- | :---------- |
| `--help` |  | help for daytona |


## daytona organization create
Create a new organization and set it as active

```shell
daytona organization create [ORGANIZATION_NAME] [flags]
```

__Flags__
| Long | Short | Description |
| :--- | :---- | :---------- |
| `--help` |  | help for daytona |


## daytona organization delete
Delete an organization

```shell
daytona organization delete [ORGANIZATION] [flags]
```

__Flags__
| Long | Short | Description |
| :--- | :---- | :---------- |
| `--help` |  | help for daytona |


## daytona organization list
List all organizations

```shell
daytona organization list [flags]
```

__Flags__
| Long | Short | Description |
| :--- | :---- | :---------- |
| `--format` | `-f` | Output format. Must be one of (yaml, json) |
| `--help` |  | help for daytona |


## daytona organization use
Set active organization

```shell
daytona organization use [ORGANIZATION] [flags]
```

__Flags__
| Long | Short | Description |
| :--- | :---- | :---------- |
| `--help` |  | help for daytona |


## daytona sandbox
Manage Daytona sandboxes

```shell
daytona sandbox [flags]
```

__Flags__
| Long | Short | Description |
| :--- | :---- | :---------- |
| `--help` |  | help for daytona |


## daytona sandbox create
Create a new sandbox

```shell
daytona sandbox create [flags]
```

__Flags__
| Long | Short | Description |
| :--- | :---- | :---------- |
| `--name` |  | Name of the sandbox |
| `--auto-archive` |  | Auto-archive interval in minutes (0 means the maximum interval will be used) |
| `--auto-delete` |  | Auto-delete interval in minutes (negative value means disabled, 0 means delete immediately upon stopping) |
| `--auto-stop` |  | Auto-stop interval in minutes (0 means disabled) |
| `--class` |  | Sandbox class type (small, medium, large) |
| `--context` | `-c` | Files or directories to include in the build context (can be specified multiple times) |
| `--cpu` |  | CPU cores allocated to the sandbox |
| `--disk` |  | Disk space allocated to the sandbox in GB |
| `--dockerfile` | `-f` | Path to Dockerfile for Sandbox snapshot |
| `--env` | `-e` | Environment variables (format: KEY=VALUE) |
| `--gpu` |  | GPU units allocated to the sandbox |
| `--label` | `-l` | Labels (format: KEY=VALUE) |
| `--memory` |  | Memory allocated to the sandbox in MB |
| `--name` |  | Name of the sandbox |
| `--network-allow-list` |  | Comma-separated list of allowed CIDR network addresses for the sandbox |
| `--network-block-all` |  | Whether to block all network access for the sandbox |
| `--public` |  | Make sandbox publicly accessible |
| `--snapshot` |  | Snapshot to use for the sandbox |
| `--target` |  | Target region (eu, us) |
| `--user` |  | User associated with the sandbox |
| `--volume` | `-v` | Volumes to mount (format: VOLUME_NAME:MOUNT_PATH) |
| `--help` |  | help for daytona |


## daytona sandbox delete
Delete a sandbox

```shell
daytona sandbox delete [SANDBOX_ID] | [SANDBOX_NAME] [flags]
```

__Flags__
| Long | Short | Description |
| :--- | :---- | :---------- |
| `--all` | `-a` | Delete all sandboxes |
| `--help` |  | help for daytona |


## daytona sandbox info
Get sandbox info

```shell
daytona sandbox info [SANDBOX_ID] | [SANDBOX_NAME] [flags]
```

__Flags__
| Long | Short | Description |
| :--- | :---- | :---------- |
| `--format` | `-f` | Output format. Must be one of (yaml, json) |
| `--help` |  | help for daytona |


## daytona sandbox list
List sandboxes

```shell
daytona sandbox list [flags]
```

__Flags__
| Long | Short | Description |
| :--- | :---- | :---------- |
| `--format` | `-f` | Output format. Must be one of (yaml, json) |
| `--limit` | `-l` | Maximum number of items per page |
| `--page` | `-p` | Page number for pagination (starting from 1) |
| `--help` |  | help for daytona |


## daytona sandbox start
Start a sandbox

```shell
daytona sandbox start [SANDBOX_ID] | [SANDBOX_NAME] [flags]
```

__Flags__
| Long | Short | Description |
| :--- | :---- | :---------- |
| `--help` |  | help for daytona |


## daytona sandbox stop
Stop a sandbox

```shell
daytona sandbox stop [SANDBOX_ID] | [SANDBOX_NAME] [flags]
```

__Flags__
| Long | Short | Description |
| :--- | :---- | :---------- |
| `--help` |  | help for daytona |


## daytona snapshot
Manage Daytona snapshots

```shell
daytona snapshot [flags]
```

__Flags__
| Long | Short | Description |
| :--- | :---- | :---------- |
| `--help` |  | help for daytona |


## daytona snapshot create
Create a snapshot

```shell
daytona snapshot create [SNAPSHOT] [flags]
```

__Flags__
| Long | Short | Description |
| :--- | :---- | :---------- |
| `--context` | `-c` | Files or directories to include in the build context (can be specified multiple times). If not provided, context will be automatically determined from COPY/ADD commands in the Dockerfile |
| `--cpu` |  | CPU cores that will be allocated to the underlying sandboxes (default: 1) |
| `--disk` |  | Disk space that will be allocated to the underlying sandboxes in GB (default: 3) |
| `--dockerfile` | `-f` | Path to Dockerfile to build |
| `--entrypoint` | `-e` | The entrypoint command for the snapshot |
| `--image` | `-i` | The image name for the snapshot |
| `--memory` |  | Memory that will be allocated to the underlying sandboxes in GB (default: 1) |
| `--help` |  | help for daytona |


## daytona snapshot delete
Delete a snapshot

```shell
daytona snapshot delete [SNAPSHOT_ID] [flags]
```

__Flags__
| Long | Short | Description |
| :--- | :---- | :---------- |
| `--all` | `-a` | Delete all snapshots |
| `--help` |  | help for daytona |


## daytona snapshot list
List all snapshots

```shell
daytona snapshot list [flags]
```

__Flags__
| Long | Short | Description |
| :--- | :---- | :---------- |
| `--format` | `-f` | Output format. Must be one of (yaml, json) |
| `--limit` | `-l` | Maximum number of items per page |
| `--page` | `-p` | Page number for pagination (starting from 1) |
| `--help` |  | help for daytona |


## daytona snapshot push
Push local snapshot

```shell
daytona snapshot push [SNAPSHOT] [flags]
```

__Flags__
| Long | Short | Description |
| :--- | :---- | :---------- |
| `--cpu` |  | CPU cores that will be allocated to the underlying sandboxes (default: 1) |
| `--disk` |  | Disk space that will be allocated to the underlying sandboxes in GB (default: 3) |
| `--entrypoint` | `-e` | The entrypoint command for the image |
| `--memory` |  | Memory that will be allocated to the underlying sandboxes in GB (default: 1) |
| `--name` | `-n` | Specify the Snapshot name |
| `--help` |  | help for daytona |


## daytona version
Print the version number

```shell
daytona version [flags]
```

__Flags__
| Long | Short | Description |
| :--- | :---- | :---------- |
| `--help` |  | help for daytona |


## daytona volume
Manage Daytona volumes

```shell
daytona volume [flags]
```

__Flags__
| Long | Short | Description |
| :--- | :---- | :---------- |
| `--help` |  | help for daytona |


## daytona volume create
Create a volume

```shell
daytona volume create [NAME] [flags]
```

__Flags__
| Long | Short | Description |
| :--- | :---- | :---------- |
| `--size` | `-s` | Size of the volume in GB |
| `--help` |  | help for daytona |


## daytona volume delete
Delete a volume

```shell
daytona volume delete [VOLUME_ID] [flags]
```

__Flags__
| Long | Short | Description |
| :--- | :---- | :---------- |
| `--help` |  | help for daytona |


## daytona volume get
Get volume details

```shell
daytona volume get [VOLUME_ID] [flags]
```

__Flags__
| Long | Short | Description |
| :--- | :---- | :---------- |
| `--format` | `-f` | Output format. Must be one of (yaml, json) |
| `--help` |  | help for daytona |


## daytona volume list
List all volumes

```shell
daytona volume list [flags]
```

__Flags__
| Long | Short | Description |
| :--- | :---- | :---------- |
| `--format` | `-f` | Output format. Must be one of (yaml, json) |
| `--help` |  | help for daytona |

## ChartType

Chart types

**Enum Members**:

- `BAR` ("bar")
- `LINE` ("line")
- `PIE` ("pie")
- `SCATTER` ("scatter")
- `UNKNOWN` ("unknown")

## parseChart()

```ts
function parseChart(data: any): Chart
```

**Parameters**:

- `data` _any_


**Returns**:

- `Chart`

***


## BarChart

```ts
type BarChart = Chart2D & {
  elements: BarData[];
  type: BAR;
};
```

Represents a bar chart with metadata.

**Type declaration**:

- `elements` _BarData\[\]_ - The bars of the chart
- `type` _BAR_ - The type of chart
    


## BarData

```ts
type BarData = {
  group: string;
  label: string;
  value: string;
};
```

Represents a bar in a bar chart.

**Type declaration**:

- `group` _string_ - The group of the bar
- `label` _string_ - The label of the bar
- `value` _string_ - The value of the bar
    


## BoxAndWhiskerChart

```ts
type BoxAndWhiskerChart = Chart2D & {
  elements: BoxAndWhiskerData[];
  type: BOX_AND_WHISKER;
};
```

Represents a box and whisker chart with metadata.

**Type declaration**:

- `elements` _BoxAndWhiskerData\[\]_ - The box and whiskers of the chart
- `type` _BOX\_AND\_WHISKER_ - The type of chart
    


## BoxAndWhiskerData

```ts
type BoxAndWhiskerData = {
  first_quartile: number;
  label: string;
  max: number;
  median: number;
  min: number;
  outliers: number[];
};
```

Represents a box and whisker in a box and whisker chart.

**Type declaration**:

- `first\_quartile` _number_ - The first quartile of the box and whisker
- `label` _string_ - The label of the box and whisker
- `max` _number_ - The third quartile of the box and whisker
- `median` _number_ - The median of the box and whisker
- `min` _number_ - The minimum value of the box and whisker
- `outliers` _number\[\]_


## Chart

```ts
type Chart = {
  elements: any[];
  png: string;
  title: string;
  type: ChartType;
};
```

Represents a chart with metadata from matplotlib.

**Type declaration**:

- `elements` _any\[\]_ - The elements of the chart
- `png?` _string_ - The PNG representation of the chart encoded in base64
- `title` _string_ - The title of the chart
- `type` _ChartType_ - The type of chart
    


## Chart2D

```ts
type Chart2D = Chart & {
  x_label: string;
  y_label: string;
};
```

Represents a 2D chart with metadata.

**Type declaration**:

- `x\_label?` _string_ - The label of the x-axis
- `y\_label?` _string_ - The label of the y-axis
    


## CompositeChart

```ts
type CompositeChart = Chart & {
  elements: Chart[];
  type: COMPOSITE_CHART;
};
```

Represents a composite chart with metadata.

**Type declaration**:

- `elements` _Chart\[\]_ - The charts of the composite chart
- `type` _COMPOSITE\_CHART_ - The type of chart
    


## LineChart

```ts
type LineChart = PointChart & {
  type: LINE;
};
```

Represents a line chart with metadata.

**Type declaration**:

- `type` _LINE_ - The type of chart
    


## PieChart

```ts
type PieChart = Chart & {
  elements: PieData[];
  type: PIE;
};
```

Represents a pie chart with metadata.

**Type declaration**:

- `elements` _PieData\[\]_ - The pie slices of the chart
- `type` _PIE_ - The type of chart
    


## PieData

```ts
type PieData = {
  angle: number;
  label: string;
  radius: number;
};
```

Represents a pie slice in a pie chart.

**Type declaration**:

- `angle` _number_ - The angle of the pie slice
- `label` _string_ - The label of the pie slice
- `radius` _number_ - The radius of the pie slice
    


## PointChart

```ts
type PointChart = Chart2D & {
  elements: PointData[];
  x_scale: string;
  x_tick_labels: string[];
  x_ticks: (number | string)[];
  y_scale: string;
  y_tick_labels: string[];
  y_ticks: (number | string)[];
};
```

Represents a point chart with metadata.

**Type declaration**:

- `elements` _PointData\[\]_ - The points of the chart
- `x\_scale` _string_ - The scale of the x-axis
- `x\_tick\_labels` _string\[\]_ - The labels of the x-axis
- `x\_ticks` _\(number \| string\)\[\]_ - The ticks of the x-axis
- `y\_scale` _string_ - The scale of the y-axis
- `y\_tick\_labels` _string\[\]_ - The labels of the y-axis
- `y\_ticks` _\(number \| string\)\[\]_ - The ticks of the y-axis
    


## PointData

```ts
type PointData = {
  label: string;
  points: [number | string, number | string][];
};
```

Represents a point in a 2D chart.

**Type declaration**:

- `label` _string_ - The label of the point
- `points` _\[number \| string, number \| string\]\[\]_ - The points of the chart
    


## ScatterChart

```ts
type ScatterChart = PointChart & {
  type: SCATTER;
};
```

Represents a scatter chart with metadata.

**Type declaration**:

- `type` _SCATTER_ - The type of chart

## ComputerUse

Computer Use functionality for interacting with the desktop environment.

**Properties**:

- `display` _Display_ - Display operations interface
- `keyboard` _Keyboard_ - Keyboard operations interface
- `mouse` _Mouse_ - Mouse operations interface
- `screenshot` _Screenshot_ - Screenshot operations interface
    




Provides access to mouse, keyboard, screenshot, and display operations
for automating desktop interactions within a sandbox.

### Constructors

#### new ComputerUse()

```ts
new ComputerUse(apiClient: ComputerUseApi): ComputerUse
```

**Parameters**:

- `apiClient` _ComputerUseApi_


**Returns**:

- `ComputerUse`

### Methods

#### getProcessErrors()

```ts
getProcessErrors(processName: string): Promise<ProcessErrorsResponse>
```

Gets error logs for a specific VNC process

**Parameters**:

- `processName` _string_ - Name of the process to get error logs for


**Returns**:

- `Promise<ProcessErrorsResponse>` - Process error logs

**Example:**

```typescript
const errorsResp = await sandbox.computerUse.getProcessErrors('x11vnc');
console.log('X11VNC errors:', errorsResp.errors);
```

***

#### getProcessLogs()

```ts
getProcessLogs(processName: string): Promise<ProcessLogsResponse>
```

Gets logs for a specific VNC process

**Parameters**:

- `processName` _string_ - Name of the process to get logs for


**Returns**:

- `Promise<ProcessLogsResponse>` - Process logs

**Example:**

```typescript
const logsResp = await sandbox.computerUse.getProcessLogs('novnc');
console.log('NoVNC logs:', logsResp.logs);
```

***

#### getProcessStatus()

```ts
getProcessStatus(processName: string): Promise<ProcessStatusResponse>
```

Gets the status of a specific VNC process

**Parameters**:

- `processName` _string_ - Name of the process to check


**Returns**:

- `Promise<ProcessStatusResponse>` - Status information about the specific process

**Example:**

```typescript
const xvfbStatus = await sandbox.computerUse.getProcessStatus('xvfb');
const noVncStatus = await sandbox.computerUse.getProcessStatus('novnc');
```

***

#### getStatus()

```ts
getStatus(): Promise<ComputerUseStatusResponse>
```

Gets the status of all computer use processes

**Returns**:

- `Promise<ComputerUseStatusResponse>` - Status information about all VNC desktop processes

**Example:**

```typescript
const status = await sandbox.computerUse.getStatus();
console.log('Computer use status:', status.status);
```

***

#### restartProcess()

```ts
restartProcess(processName: string): Promise<ProcessRestartResponse>
```

Restarts a specific VNC process

**Parameters**:

- `processName` _string_ - Name of the process to restart


**Returns**:

- `Promise<ProcessRestartResponse>` - Process restart response

**Example:**

```typescript
const result = await sandbox.computerUse.restartProcess('xfce4');
console.log('XFCE4 process restarted:', result.message);
```

***

#### start()

```ts
start(): Promise<ComputerUseStartResponse>
```

Starts all computer use processes (Xvfb, xfce4, x11vnc, novnc)

**Returns**:

- `Promise<ComputerUseStartResponse>` - Computer use start response

**Example:**

```typescript
const result = await sandbox.computerUse.start();
console.log('Computer use processes started:', result.message);
```

***

#### stop()

```ts
stop(): Promise<ComputerUseStopResponse>
```

Stops all computer use processes

**Returns**:

- `Promise<ComputerUseStopResponse>` - Computer use stop response

**Example:**

```typescript
const result = await sandbox.computerUse.stop();
console.log('Computer use processes stopped:', result.message);
```
## Display

Display operations for computer use functionality

### Constructors

#### new Display()

```ts
new Display(apiClient: ComputerUseApi): Display
```

**Parameters**:

- `apiClient` _ComputerUseApi_


**Returns**:

- `Display`

### Methods

#### getInfo()

```ts
getInfo(): Promise<DisplayInfoResponse>
```

Gets information about the displays

**Returns**:

- `Promise<DisplayInfoResponse>` - Display information including primary display and all available displays

**Example:**

```typescript
const info = await sandbox.computerUse.display.getInfo();
console.log(`Primary display: ${info.primary_display.width}x${info.primary_display.height}`);
console.log(`Total displays: ${info.total_displays}`);
info.displays.forEach((display, index) => {
  console.log(`Display ${index}: ${display.width}x${display.height} at ${display.x},${display.y}`);
});
```

***

#### getWindows()

```ts
getWindows(): Promise<WindowsResponse>
```

Gets the list of open windows

**Returns**:

- `Promise<WindowsResponse>` - List of open windows with their IDs and titles

**Example:**

```typescript
const windows = await sandbox.computerUse.display.getWindows();
console.log(`Found ${windows.count} open windows:`);
windows.windows.forEach(window => {
  console.log(`- ${window.title} (ID: ${window.id})`);
});
```

***


## Keyboard

Keyboard operations for computer use functionality

### Constructors

#### new Keyboard()

```ts
new Keyboard(apiClient: ComputerUseApi): Keyboard
```

**Parameters**:

- `apiClient` _ComputerUseApi_


**Returns**:

- `Keyboard`

### Methods

#### hotkey()

```ts
hotkey(keys: string): Promise<void>
```

Presses a hotkey combination

**Parameters**:

- `keys` _string_ - The hotkey combination (e.g., 'ctrl+c', 'alt+tab', 'cmd+shift+t')


**Returns**:

- `Promise<void>`

**Throws**:

If the hotkey operation fails

**Example:**

```typescript
// Copy
try {
  await sandbox.computerUse.keyboard.hotkey('ctrl+c');
  console.log('Operation success');
} catch (e) {
  console.log('Operation failed:', e);
}

// Paste
try {
  await sandbox.computerUse.keyboard.hotkey('ctrl+v');
  console.log('Operation success');
} catch (e) {
  console.log('Operation failed:', e);
}

// Alt+Tab
try {
  await sandbox.computerUse.keyboard.hotkey('alt+tab');
  console.log('Operation success');
} catch (e) {
  console.log('Operation failed:', e);
}
```

***

#### press()

```ts
press(key: string, modifiers?: string[]): Promise<void>
```

Presses a key with optional modifiers

**Parameters**:

- `key` _string_ - The key to press (e.g., 'Enter', 'Escape', 'Tab', 'a', 'A')
- `modifiers?` _string\[\] = \[\]_ - Modifier keys ('ctrl', 'alt', 'meta', 'shift')


**Returns**:

- `Promise<void>`

**Throws**:

If the press operation fails

**Example:**

```typescript
// Press Enter
try {
  await sandbox.computerUse.keyboard.press('Return');
  console.log('Operation success');
} catch (e) {
  console.log('Operation failed:', e);
}

// Press Ctrl+C
try {
  await sandbox.computerUse.keyboard.press('c', ['ctrl']);
  console.log('Operation success');
} catch (e) {
  console.log('Operation failed:', e);
}

// Press Ctrl+Shift+T
try {
  await sandbox.computerUse.keyboard.press('t', ['ctrl', 'shift']);
  console.log('Operation success');
} catch (e) {
  console.log('Operation failed:', e);
}
```

***

#### type()

```ts
type(text: string, delay?: number): Promise<void>
```

Types the specified text

**Parameters**:

- `text` _string_ - The text to type
- `delay?` _number_ - Delay between characters in milliseconds


**Returns**:

- `Promise<void>`

**Throws**:

If the type operation fails

**Example:**

```typescript
try {
  await sandbox.computerUse.keyboard.type('Hello, World!');
  console.log('Operation success');
} catch (e) {
  console.log('Operation failed:', e);
}

// With delay between characters
try {
  await sandbox.computerUse.keyboard.type('Slow typing', 100);
  console.log('Operation success');
} catch (e) {
  console.log('Operation failed:', e);
}
```

***


## Mouse

Mouse operations for computer use functionality

### Constructors

#### new Mouse()

```ts
new Mouse(apiClient: ComputerUseApi): Mouse
```

**Parameters**:

- `apiClient` _ComputerUseApi_


**Returns**:

- `Mouse`

### Methods

#### click()

```ts
click(
   x: number, 
   y: number, 
   button?: string, 
double?: boolean): Promise<MouseClickResponse>
```

Clicks the mouse at the specified coordinates

**Parameters**:

- `x` _number_ - The x coordinate to click at
- `y` _number_ - The y coordinate to click at
- `button?` _string = 'left'_ - The mouse button to click ('left', 'right', 'middle')
- `double?` _boolean = false_ - Whether to perform a double-click


**Returns**:

- `Promise<MouseClickResponse>` - Click operation result

**Example:**

```typescript
// Single left click
const result = await sandbox.computerUse.mouse.click(100, 200);

// Double click
const doubleClick = await sandbox.computerUse.mouse.click(100, 200, 'left', true);

// Right click
const rightClick = await sandbox.computerUse.mouse.click(100, 200, 'right');
```

***

#### drag()

```ts
drag(
   startX: number, 
   startY: number, 
   endX: number, 
   endY: number, 
button?: string): Promise<MouseDragResponse>
```

Drags the mouse from start coordinates to end coordinates

**Parameters**:

- `startX` _number_ - The starting x coordinate
- `startY` _number_ - The starting y coordinate
- `endX` _number_ - The ending x coordinate
- `endY` _number_ - The ending y coordinate
- `button?` _string = 'left'_ - The mouse button to use for dragging


**Returns**:

- `Promise<MouseDragResponse>` - Drag operation result

**Example:**

```typescript
const result = await sandbox.computerUse.mouse.drag(50, 50, 150, 150);
console.log(`Dragged from ${result.from.x},${result.from.y} to ${result.to.x},${result.to.y}`);
```

***

#### getPosition()

```ts
getPosition(): Promise<MousePositionResponse>
```

Gets the current mouse cursor position

**Returns**:

- `Promise<MousePositionResponse>` - Current mouse position with x and y coordinates

**Example:**

```typescript
const position = await sandbox.computerUse.mouse.getPosition();
console.log(`Mouse is at: ${position.x}, ${position.y}`);
```

***

#### move()

```ts
move(x: number, y: number): Promise<MousePositionResponse>
```

Moves the mouse cursor to the specified coordinates

**Parameters**:

- `x` _number_ - The x coordinate to move to
- `y` _number_ - The y coordinate to move to


**Returns**:

- `Promise<MousePositionResponse>` - Position after move

**Example:**

```typescript
const result = await sandbox.computerUse.mouse.move(100, 200);
console.log(`Mouse moved to: ${result.x}, ${result.y}`);
```

***

#### scroll()

```ts
scroll(
   x: number, 
   y: number, 
   direction: "up" | "down", 
amount?: number): Promise<boolean>
```

Scrolls the mouse wheel at the specified coordinates

**Parameters**:

- `x` _number_ - The x coordinate to scroll at
- `y` _number_ - The y coordinate to scroll at
- `direction` _The direction to scroll_ - `"up"` | `"down"`
- `amount?` _number = 1_ - The amount to scroll


**Returns**:

- `Promise<boolean>` - Whether the scroll operation was successful

**Example:**

```typescript
// Scroll up
const scrollUp = await sandbox.computerUse.mouse.scroll(100, 200, 'up', 3);

// Scroll down
const scrollDown = await sandbox.computerUse.mouse.scroll(100, 200, 'down', 5);
```

***


## Screenshot

Screenshot operations for computer use functionality

### Constructors

#### new Screenshot()

```ts
new Screenshot(apiClient: ComputerUseApi): Screenshot
```

**Parameters**:

- `apiClient` _ComputerUseApi_


**Returns**:

- `Screenshot`

### Methods

#### takeCompressed()

```ts
takeCompressed(options?: ScreenshotOptions): Promise<ScreenshotResponse>
```

Takes a compressed screenshot of the entire screen

**Parameters**:

- `options?` _ScreenshotOptions = {}_ - Compression and display options


**Returns**:

- `Promise<ScreenshotResponse>` - Compressed screenshot data

**Example:**

```typescript
// Default compression
const screenshot = await sandbox.computerUse.screenshot.takeCompressed();

// High quality JPEG
const jpeg = await sandbox.computerUse.screenshot.takeCompressed({
  format: 'jpeg',
  quality: 95,
  showCursor: true
});

// Scaled down PNG
const scaled = await sandbox.computerUse.screenshot.takeCompressed({
  format: 'png',
  scale: 0.5
});
```

***

#### takeCompressedRegion()

```ts
takeCompressedRegion(region: ScreenshotRegion, options?: ScreenshotOptions): Promise<ScreenshotResponse>
```

Takes a compressed screenshot of a specific region

**Parameters**:

- `region` _ScreenshotRegion_ - The region to capture
- `options?` _ScreenshotOptions = {}_ - Compression and display options


**Returns**:

- `Promise<ScreenshotResponse>` - Compressed screenshot data

**Example:**

```typescript
const region = { x: 0, y: 0, width: 800, height: 600 };
const screenshot = await sandbox.computerUse.screenshot.takeCompressedRegion(region, {
  format: 'webp',
  quality: 80,
  showCursor: true
});
console.log(`Compressed size: ${screenshot.size_bytes} bytes`);
```

***

#### takeFullScreen()

```ts
takeFullScreen(showCursor?: boolean): Promise<ScreenshotResponse>
```

Takes a screenshot of the entire screen

**Parameters**:

- `showCursor?` _boolean = false_ - Whether to show the cursor in the screenshot


**Returns**:

- `Promise<ScreenshotResponse>` - Screenshot data with base64 encoded image

**Example:**

```typescript
const screenshot = await sandbox.computerUse.screenshot.takeFullScreen();
console.log(`Screenshot size: ${screenshot.width}x${screenshot.height}`);

// With cursor visible
const withCursor = await sandbox.computerUse.screenshot.takeFullScreen(true);
```

***

#### takeRegion()

```ts
takeRegion(region: ScreenshotRegion, showCursor?: boolean): Promise<ScreenshotResponse>
```

Takes a screenshot of a specific region

**Parameters**:

- `region` _ScreenshotRegion_ - The region to capture
- `showCursor?` _boolean = false_ - Whether to show the cursor in the screenshot


**Returns**:

- `Promise<ScreenshotResponse>` - Screenshot data with base64 encoded image

**Example:**

```typescript
const region = { x: 100, y: 100, width: 300, height: 200 };
const screenshot = await sandbox.computerUse.screenshot.takeRegion(region);
console.log(`Captured region: ${screenshot.region.width}x${screenshot.region.height}`);
```

***


## ScreenshotOptions

Interface for screenshot compression options

**Properties**:

- `format?` _string_
- `quality?` _number_
- `scale?` _number_
- `showCursor?` _boolean_
## ScreenshotRegion

Interface for region coordinates used in screenshot operations

**Properties**:

- `height` _number_
- `width` _number_
- `x` _number_
- `y` _number_

## Daytona

Main class for interacting with the Daytona API.
Provides methods for creating, managing, and interacting with Daytona Sandboxes.
Can be initialized either with explicit configuration or using environment variables.

**Properties**:

- `snapshot` _SnapshotService_ - Service for managing Daytona Snapshots
- `volume` _VolumeService_ - Service for managing Daytona Volumes
    




**Examples:**

```ts
// Using environment variables
// Uses DAYTONA_API_KEY, DAYTONA_API_URL, DAYTONA_TARGET
const daytona = new Daytona();
const sandbox = await daytona.create();
```

```ts
// Using explicit configuration
const config: DaytonaConfig = {
    apiKey: "your-api-key",
    apiUrl: "https://your-api.com",
    target: "us"
};
const daytona = new Daytona(config);

@class
```

### Constructors

#### new Daytona()

```ts
new Daytona(config?: DaytonaConfig): Daytona
```

Creates a new Daytona client instance.

**Parameters**:

- `config?` _DaytonaConfig_ - Configuration options


**Returns**:

- `Daytona`

**Throws**:

- `DaytonaError` - When API key is missing

### Methods

#### create()

##### Call Signature

```ts
create(params?: CreateSandboxFromSnapshotParams, options?: {
  timeout: number;
}): Promise<Sandbox>
```

Creates Sandboxes from specified or default snapshot. You can specify various parameters,
including language, image, environment variables, and volumes.

**Parameters**:

- `params?` _CreateSandboxFromSnapshotParams_ - Parameters for Sandbox creation from snapshot
- `options?` _Options for the create operation_
- `timeout?` _number_ - Timeout in seconds (0 means no timeout, default is 60)

**Returns**:

- `Promise<Sandbox>` - The created Sandbox instance

**Examples:**

```ts
const sandbox = await daytona.create();
```

```ts
// Create a custom sandbox
const params: CreateSandboxFromSnapshotParams = {
    language: 'typescript',
    snapshot: 'my-snapshot-id',
    envVars: {
        NODE_ENV: 'development',
        DEBUG: 'true'
    },
    autoStopInterval: 60,
    autoArchiveInterval: 60,
    autoDeleteInterval: 120
};
const sandbox = await daytona.create(params, { timeout: 100 });
```

##### Call Signature

```ts
create(params?: CreateSandboxFromImageParams, options?: {
  onSnapshotCreateLogs: (chunk: string) => void;
  timeout: number;
}): Promise<Sandbox>
```

Creates Sandboxes from specified image available on some registry or declarative Daytona Image. You can specify various parameters,
including resources, language, image, environment variables, and volumes. Daytona creates snapshot from
provided image and uses it to create Sandbox.

**Parameters**:

- `params?` _CreateSandboxFromImageParams_ - Parameters for Sandbox creation from image
- `options?` _Options for the create operation_
- `onSnapshotCreateLogs?` _\(chunk: string\) =\> void_ - Callback function to handle snapshot creation logs.
- `timeout?` _number_ - Timeout in seconds (0 means no timeout, default is 60)

**Returns**:

- `Promise<Sandbox>` - The created Sandbox instance

**Examples:**

```ts
const sandbox = await daytona.create({ image: 'debian:12.9' }, { timeout: 90, onSnapshotCreateLogs: console.log });
```

```ts
// Create a custom sandbox
const image = Image.base('alpine:3.18').pipInstall('numpy');
const params: CreateSandboxFromImageParams = {
    language: 'typescript',
    image,
    envVars: {
        NODE_ENV: 'development',
        DEBUG: 'true'
    },
    resources: {
        cpu: 2,
        memory: 4 // 4GB RAM
    },
    autoStopInterval: 60,
    autoArchiveInterval: 60,
    autoDeleteInterval: 120
};
const sandbox = await daytona.create(params, { timeout: 100, onSnapshotCreateLogs: console.log });
```

***

#### delete()

```ts
delete(sandbox: Sandbox, timeout: number): Promise<void>
```

Deletes a Sandbox.

**Parameters**:

- `sandbox` _Sandbox_ - The Sandbox to delete
- `timeout` _number = 60_ - Timeout in seconds (0 means no timeout, default is 60)


**Returns**:

- `Promise<void>`

**Example:**

```ts
const sandbox = await daytona.get('my-sandbox-id');
await daytona.delete(sandbox);
```

***

#### findOne()

```ts
findOne(filter: SandboxFilter): Promise<Sandbox>
```

Finds a Sandbox by its ID or name or labels.

**Parameters**:

- `filter` _SandboxFilter_ - Filter for Sandboxes


**Returns**:

- `Promise<Sandbox>` - First Sandbox that matches the ID or name or labels.

**Example:**

```ts
const sandbox = await daytona.findOne({ labels: { 'my-label': 'my-value' } });
console.log(`Sandbox ID: ${sandbox.id}, State: ${sandbox.state}`);
```

***

#### get()

```ts
get(sandboxIdOrName: string): Promise<Sandbox>
```

Gets a Sandbox by its ID or name.

**Parameters**:

- `sandboxIdOrName` _string_ - The ID or name of the Sandbox to retrieve


**Returns**:

- `Promise<Sandbox>` - The Sandbox

**Example:**

```ts
const sandbox = await daytona.get('my-sandbox-id-or-name');
console.log(`Sandbox state: ${sandbox.state}`);
```

***

#### getProxyToolboxUrl()

```ts
getProxyToolboxUrl(): Promise<string>
```

**Returns**:

- `Promise<string>`

***

#### list()

```ts
list(
   labels?: Record<string, string>, 
   page?: number, 
limit?: number): Promise<PaginatedSandboxes>
```

Returns paginated list of Sandboxes filtered by labels.

**Parameters**:

- `labels?` _Record\<string, string\>_ - Labels to filter Sandboxes
- `page?` _number_ - Page number for pagination (starting from 1)
- `limit?` _number_ - Maximum number of items per page


**Returns**:

- `Promise<PaginatedSandboxes>` - Paginated list of Sandboxes that match the labels.

**Example:**

```ts
const result = await daytona.list({ 'my-label': 'my-value' }, 2, 10);
for (const sandbox of result.items) {
    console.log(`${sandbox.id}: ${sandbox.state}`);
}
```

***

#### start()

```ts
start(sandbox: Sandbox, timeout?: number): Promise<void>
```

Starts a Sandbox and waits for it to be ready.

**Parameters**:

- `sandbox` _Sandbox_ - The Sandbox to start
- `timeout?` _number_ - Optional timeout in seconds (0 means no timeout)


**Returns**:

- `Promise<void>`

**Example:**

```ts
const sandbox = await daytona.get('my-sandbox-id');
// Wait up to 60 seconds for the sandbox to start
await daytona.start(sandbox, 60);
```

***

#### stop()

```ts
stop(sandbox: Sandbox): Promise<void>
```

Stops a Sandbox.

**Parameters**:

- `sandbox` _Sandbox_ - The Sandbox to stop


**Returns**:

- `Promise<void>`

**Example:**

```ts
const sandbox = await daytona.get('my-sandbox-id');
await daytona.stop(sandbox);
```
## CodeLanguage

Supported programming languages for code execution

**Enum Members**:

- `JAVASCRIPT` ("javascript")
- `PYTHON` ("python")
- `TYPESCRIPT` ("typescript")

## CreateSandboxBaseParams

Base parameters for creating a new Sandbox.

**Properties**:

- `autoArchiveInterval?` _number_ - Auto-archive interval in minutes (0 means the maximum interval will be used). Default is 7 days.
- `autoDeleteInterval?` _number_ - Auto-delete interval in minutes (negative value means disabled, 0 means delete immediately upon stopping). By default, auto-delete is disabled.
- `autoStopInterval?` _number_ - Auto-stop interval in minutes (0 means disabled). Default is 15 minutes.
- `envVars?` _Record\<string, string\>_ - Optional environment variables to set in the Sandbox
- `ephemeral?` _boolean_ - Whether the Sandbox should be ephemeral. If true, autoDeleteInterval will be set to 0.
- `labels?` _Record\<string, string\>_ - Sandbox labels
- `language?` _string_ - Programming language for direct code execution
- `name?` _string_
- `networkAllowList?` _string_ - Comma-separated list of allowed CIDR network addresses for the Sandbox
- `networkBlockAll?` _boolean_ - Whether to block all network access for the Sandbox
- `public?` _boolean_ - Is the Sandbox port preview public
- `user?` _string_ - Optional os user to use for the Sandbox
- `volumes?` _VolumeMount\[\]_ - Optional array of volumes to mount to the Sandbox
## CreateSandboxFromImageParams

Parameters for creating a new Sandbox.

**Properties**:

- `autoArchiveInterval?` _number_
- `autoDeleteInterval?` _number_
- `autoStopInterval?` _number_
- `envVars?` _Record\<string, string\>_
- `ephemeral?` _boolean_
- `image` _string \| Image_ - Custom Docker image to use for the Sandbox. If an Image object is provided,
    the image will be dynamically built.
- `labels?` _Record\<string, string\>_
- `language?` _string_
- `name?` _string_
- `networkAllowList?` _string_
- `networkBlockAll?` _boolean_
- `public?` _boolean_
- `resources?` _Resources_ - Resource allocation for the Sandbox. If not provided, sandbox will
    have default resources.
- `user?` _string_
- `volumes?` _VolumeMount\[\]_
## CreateSandboxFromSnapshotParams

Parameters for creating a new Sandbox from a snapshot.

**Properties**:

- `autoArchiveInterval?` _number_
- `autoDeleteInterval?` _number_
- `autoStopInterval?` _number_
- `envVars?` _Record\<string, string\>_
- `ephemeral?` _boolean_
- `labels?` _Record\<string, string\>_
- `language?` _string_
- `name?` _string_
- `networkAllowList?` _string_
- `networkBlockAll?` _boolean_
- `public?` _boolean_
- `snapshot?` _string_ - Name of the snapshot to use for the Sandbox.
- `user?` _string_
- `volumes?` _VolumeMount\[\]_
## DaytonaConfig

Configuration options for initializing the Daytona client.

**Properties**:

- `apiKey?` _string_ - API key for authentication with the Daytona API
- `apiUrl?` _string_ - URL of the Daytona API. Defaults to 'https://app.daytona.io/api'
    if not set here and not set in environment variable DAYTONA_API_URL.
- `jwtToken?` _string_ - JWT token for authentication with the Daytona API. If not set, it must be provided
    via the environment variable `DAYTONA_JWT_TOKEN`, or an API key must be provided instead.
- `organizationId?` _string_ - Organization ID used for JWT-based authentication. Required if a JWT token
    is provided, and must be set either here or in the environment variable `DAYTONA_ORGANIZATION_ID`.
- ~~`serverUrl?`~~ _string_ - **_Deprecated_** - Use `apiUrl` instead. This property will be removed in future versions.
- `target?` _string_ - Target location for Sandboxes
    




**Example:**

```ts
const config: DaytonaConfig = {
    apiKey: "your-api-key",
    apiUrl: "https://your-api.com",
    target: "us"
};
const daytona = new Daytona(config);
```
## Resources

Resource allocation for a Sandbox.

**Properties**:

- `cpu?` _number_ - CPU allocation for the Sandbox in cores
- `disk?` _number_ - Disk space allocation for the Sandbox in GiB
- `gpu?` _number_ - GPU allocation for the Sandbox in units
- `memory?` _number_ - Memory allocation for the Sandbox in GiB
    




**Example:**

```ts
const resources: SandboxResources = {
    cpu: 2,
    memory: 4,  // 4GiB RAM
    disk: 20    // 20GiB disk
};
```
## SandboxFilter

Filter for Sandboxes.

**Properties**:

- `idOrName?` _string_ - The ID or name of the Sandbox to retrieve
- `labels?` _Record\<string, string\>_ - Labels to filter Sandboxes
## VolumeMount

Represents a volume mount for a Sandbox.

**Properties**:

- `mountPath` _string_ - Path on the Sandbox to mount the Volume
    
- `volumeId` _string_ - ID of the Volume to mount
    



**Extends:**

- `SandboxVolume`

## DaytonaError

Base error for Daytona SDK.

**Extends:**

- `Error`

### Extended by

- `DaytonaNotFoundError`

### Constructors

#### new DaytonaError()

_Inherited from_: `Error.constructor`

```ts
new DaytonaError(message?: string): DaytonaError
```

**Parameters**:

- `message?` _string_


**Returns**:

- `DaytonaError`

#### new DaytonaError()

_Inherited from_: `Error.constructor`

```ts
new DaytonaError(message?: string, options?: ErrorOptions): DaytonaError
```

**Parameters**:

- `message?` _string_
- `options?` _ErrorOptions_


**Returns**:

- `DaytonaError`

***


## DaytonaNotFoundError

Base error for Daytona SDK.

**Extends:**

- `DaytonaError`

### Constructors

#### new DaytonaNotFoundError()

_Inherited from_: `DaytonaError.constructor`

```ts
new DaytonaNotFoundError(message?: string): DaytonaNotFoundError
```

**Parameters**:

- `message?` _string_


**Returns**:

- `DaytonaNotFoundError`

#### new DaytonaNotFoundError()

_Inherited from_: `DaytonaError.constructor`

```ts
new DaytonaNotFoundError(message?: string, options?: ErrorOptions): DaytonaNotFoundError
```

**Parameters**:

- `message?` _string_
- `options?` _ErrorOptions_


**Returns**:

- `DaytonaNotFoundError`

## ExecuteResponse

Response from the command execution.

**Properties**:

- `artifacts?` _ExecutionArtifacts_ - Artifacts from the command execution
- `exitCode` _number_ - The exit code from the command execution
- `result` _string_ - The output from the command execution
## ExecutionArtifacts

Artifacts from the command execution.

**Properties**:

- `charts?` _Chart\[\]_ - List of chart metadata from matplotlib
- `stdout` _string_ - Standard output from the command, same as `result` in `ExecuteResponse`

## FileSystem

Provides file system operations within a Sandbox.

### Constructors

#### new FileSystem()

```ts
new FileSystem(
   clientConfig: Configuration, 
   apiClient: FileSystemApi, 
   ensureToolboxUrl: () => Promise<void>): FileSystem
```

**Parameters**:

- `clientConfig` _Configuration_
- `apiClient` _FileSystemApi_
- `ensureToolboxUrl` _\(\) =\> Promise\<void\>_


**Returns**:

- `FileSystem`

### Methods

#### createFolder()

```ts
createFolder(path: string, mode: string): Promise<void>
```

Create a new directory in the Sandbox with specified permissions.

**Parameters**:

- `path` _string_ - Path where the directory should be created. Relative paths are resolved based on the sandbox working directory.
- `mode` _string_ - Directory permissions in octal format (e.g. "755")


**Returns**:

- `Promise<void>`

**Example:**

```ts
// Create a directory with standard permissions
await fs.createFolder('app/data', '755');
```

***

#### deleteFile()

```ts
deleteFile(path: string, recursive?: boolean): Promise<void>
```

Deletes a file or directory from the Sandbox.

**Parameters**:

- `path` _string_ - Path to the file or directory to delete. Relative paths are resolved based on the sandbox working directory.
- `recursive?` _boolean_ - If the file is a directory, this must be true to delete it.


**Returns**:

- `Promise<void>`

**Example:**

```ts
// Delete a file
await fs.deleteFile('app/temp.log');
```

***

#### downloadFile()

##### Call Signature

```ts
downloadFile(remotePath: string, timeout?: number): Promise<Buffer<ArrayBufferLike>>
```

Downloads a file from the Sandbox. This method loads the entire file into memory, so it is not recommended
for downloading large files.

**Parameters**:

- `remotePath` _string_ - Path to the file to download. Relative paths are resolved based on the sandbox working directory.
- `timeout?` _number_ - Timeout for the download operation in seconds. 0 means no timeout.
    Default is 30 minutes.

**Returns**:

- `Promise<Buffer<ArrayBufferLike>>` - The file contents as a Buffer.

**Example:**

```ts
// Download and process a file
const fileBuffer = await fs.downloadFile('tmp/data.json');
console.log('File content:', fileBuffer.toString());
```

##### Call Signature

```ts
downloadFile(
   remotePath: string, 
   localPath: string, 
timeout?: number): Promise<void>
```

Downloads a file from the Sandbox and saves it to a local file. This method uses streaming to download the file,
so it is recommended for downloading larger files.

**Parameters**:

- `remotePath` _string_ - Path to the file to download in the Sandbox. Relative paths are resolved based on the sandbox working directory.
- `localPath` _string_ - Path to save the downloaded file.
- `timeout?` _number_ - Timeout for the download operation in seconds. 0 means no timeout.
    Default is 30 minutes.

**Returns**:

- `Promise<void>`

**Example:**

```ts
// Download and save a file
await fs.downloadFile('tmp/data.json', 'local_file.json');
```

***

#### downloadFiles()

```ts
downloadFiles(files: FileDownloadRequest[], timeoutSec?: number): Promise<FileDownloadResponse[]>
```

Downloads multiple files from the Sandbox. If the files already exist locally, they will be overwritten.

**Parameters**:

- `files` _FileDownloadRequest\[\]_ - Array of file download requests.
- `timeoutSec?` _number = ..._ - Timeout for the download operation in seconds. 0 means no timeout.
    Default is 30 minutes.


**Returns**:

- `Promise<FileDownloadResponse[]>` - Array of download results.

**Throws**:

If the request itself fails (network issues, invalid request/response, etc.). Individual
file download errors are returned in the `FileDownloadResponse.error` field.

**Example:**

```ts
// Download multiple files
const results = await fs.downloadFiles([
  { source: 'tmp/data.json' },
  { source: 'tmp/config.json', destination: 'local_config.json' }
]);
results.forEach(result => {
  if (result.error) {
    console.error(`Error downloading ${result.source}: ${result.error}`);
  } else if (result.result) {
    console.log(`Downloaded ${result.source} to ${result.result}`);
  }
});
```

***

#### findFiles()

```ts
findFiles(path: string, pattern: string): Promise<Match[]>
```

Searches for text patterns within files in the Sandbox.

**Parameters**:

- `path` _string_ - Directory to search in. Relative paths are resolved based on the sandbox working directory.
- `pattern` _string_ - Search pattern


**Returns**:

- `Promise<Match[]>` - Array of matches with file and line information

**Example:**

```ts
// Find all TODO comments in TypeScript files
const matches = await fs.findFiles('app/src', 'TODO:');
matches.forEach(match => {
  console.log(`${match.file}:${match.line}: ${match.content}`);
});
```

***

#### getFileDetails()

```ts
getFileDetails(path: string): Promise<FileInfo>
```

Retrieves detailed information about a file or directory.

**Parameters**:

- `path` _string_ - Path to the file or directory. Relative paths are resolved based on the sandbox working directory.


**Returns**:

- `Promise<FileInfo>` - Detailed file information including size, permissions, modification time

**Example:**

```ts
// Get file details
const info = await fs.getFileDetails('app/config.json');
console.log(`Size: ${info.size}, Modified: ${info.modTime}`);
```

***

#### listFiles()

```ts
listFiles(path: string): Promise<FileInfo[]>
```

Lists contents of a directory in the Sandbox.

**Parameters**:

- `path` _string_ - Directory path to list. Relative paths are resolved based on the sandbox working directory.


**Returns**:

- `Promise<FileInfo[]>` - Array of file and directory information

**Example:**

```ts
// List directory contents
const files = await fs.listFiles('app/src');
files.forEach(file => {
  console.log(`${file.name} (${file.size} bytes)`);
});
```

***

#### moveFiles()

```ts
moveFiles(source: string, destination: string): Promise<void>
```

Moves or renames a file or directory.

**Parameters**:

- `source` _string_ - Source path. Relative paths are resolved based on the sandbox working directory.
- `destination` _string_ - Destination path. Relative paths are resolved based on the sandbox working directory.


**Returns**:

- `Promise<void>`

**Example:**

```ts
// Move a file to a new location
await fs.moveFiles('app/temp/data.json', 'app/data/data.json');
```

***

#### replaceInFiles()

```ts
replaceInFiles(
   files: string[], 
   pattern: string, 
newValue: string): Promise<ReplaceResult[]>
```

Replaces text content in multiple files.

**Parameters**:

- `files` _string\[\]_ - Array of file paths to process. Relative paths are resolved based on the sandbox working directory.
- `pattern` _string_ - Pattern to replace
- `newValue` _string_ - Replacement text


**Returns**:

- `Promise<ReplaceResult[]>` - Results of the replace operation for each file

**Example:**

```ts
// Update version number across multiple files
const results = await fs.replaceInFiles(
  ['app/package.json', 'app/version.ts'],
  '"version": "1.0.0"',
  '"version": "1.1.0"'
);
```

***

#### searchFiles()

```ts
searchFiles(path: string, pattern: string): Promise<SearchFilesResponse>
```

Searches for files and directories by name pattern in the Sandbox.

**Parameters**:

- `path` _string_ - Directory to search in. Relative paths are resolved based on the sandbox working directory.
- `pattern` _string_ - File name pattern (supports globs)


**Returns**:

- `Promise<SearchFilesResponse>` - Search results with matching files

**Example:**

```ts
// Find all TypeScript files
const result = await fs.searchFiles('app', '*.ts');
result.files.forEach(file => console.log(file));
```

***

#### setFilePermissions()

```ts
setFilePermissions(path: string, permissions: FilePermissionsParams): Promise<void>
```

Sets permissions and ownership for a file or directory.

**Parameters**:

- `path` _string_ - Path to the file or directory. Relative paths are resolved based on the sandbox working directory.
- `permissions` _FilePermissionsParams_ - Permission settings


**Returns**:

- `Promise<void>`

**Example:**

```ts
// Set file permissions and ownership
await fs.setFilePermissions('app/script.sh', {
  owner: 'daytona',
  group: 'users',
  mode: '755'  // Execute permission for shell script
});
```

***

#### uploadFile()

##### Call Signature

```ts
uploadFile(
   file: Buffer, 
   remotePath: string, 
timeout?: number): Promise<void>
```

Uploads a file to the Sandbox. This method loads the entire file into memory, so it is not recommended
for uploading large files.

**Parameters**:

- `file` _Buffer_ - Buffer of the file to upload.
- `remotePath` _string_ - Destination path in the Sandbox. Relative paths are resolved based on the sandbox working directory.
- `timeout?` _number_ - Timeout for the upload operation in seconds. 0 means no timeout.
    Default is 30 minutes.

**Returns**:

- `Promise<void>`

**Example:**

```ts
// Upload a configuration file
await fs.uploadFile(Buffer.from('{"setting": "value"}'), 'tmp/config.json');
```

##### Call Signature

```ts
uploadFile(
   localPath: string, 
   remotePath: string, 
timeout?: number): Promise<void>
```

Uploads a file from the local file system to the Sandbox. This method uses streaming to upload the file,
so it is recommended for uploading larger files.

**Parameters**:

- `localPath` _string_ - Path to the local file to upload.
- `remotePath` _string_ - Destination path in the Sandbox. Relative paths are resolved based on the sandbox working directory.
- `timeout?` _number_ - Timeout for the upload operation in seconds. 0 means no timeout.
    Default is 30 minutes.

**Returns**:

- `Promise<void>`

**Example:**

```ts
// Upload a local file
await fs.uploadFile('local_file.txt', 'tmp/file.txt');
```

***

#### uploadFiles()

```ts
uploadFiles(files: FileUpload[], timeout?: number): Promise<void>
```

Uploads multiple files to the Sandbox. If files already exist at the destination paths,
they will be overwritten.

**Parameters**:

- `files` _FileUpload\[\]_ - Array of files to upload.
- `timeout?` _number = ..._ - Timeout for the upload operation in seconds. 0 means no timeout.
    Default is 30 minutes.


**Returns**:

- `Promise<void>`

**Example:**

```ts
// Upload multiple text files
const files = [
  {
    source: Buffer.from('Content of file 1'),
    destination: '/tmp/file1.txt'
  },
  {
    source: 'app/data/file2.txt',
    destination: '/tmp/file2.txt'
  },
  {
    source: Buffer.from('{"key": "value"}'),
    destination: '/tmp/config.json'
  }
];
await fs.uploadFiles(files);
```

***


## DownloadMetadata

Represents metadata for a file download operation.

**Properties**:

- `destination?` _string_ - Destination path in the local filesystem where the file content will be streamed to.
- `error?` _string_ - Error message if the download failed, undefined if successful.
- `result?` _string \| Uint8Array\<ArrayBufferLike\> \| Buffer\<ArrayBufferLike\>_ - The download result - file path (if destination provided in the request)
    or bytes content (if no destination in the request), undefined if failed or no data received.
## FileDownloadRequest

Represents a request to download a single file from the Sandbox.

**Properties**:

- `destination?` _string_ - Destination path in the local filesystem where the file content will be
    streamed to. If not provided, the file will be downloaded in the bytes buffer (might cause memory issues if the file is large).
- `source` _string_ - Source path in the Sandbox. Relative paths are resolved based on the user's
    root directory.
## FileDownloadResponse

Represents the response to a single file download request.

**Properties**:

- `error?` _string_ - Error message if the download failed, undefined if successful.
- `result?` _string \| Buffer\<ArrayBufferLike\>_ - The download result - file path (if destination provided in the request)
    or bytes content (if no destination in the request), undefined if failed or no data received.
- `source` _string_ - The original source path requested for download.
## FilePermissionsParams

Parameters for setting file permissions in the Sandbox.

**Properties**:

- `group?` _string_ - Group owner of the file
- `mode?` _string_ - File mode/permissions in octal format (e.g. "644")
- `owner?` _string_ - User owner of the file
    




**Example:**

```ts
const permissions: FilePermissionsParams = {
  mode: '644',
  owner: 'daytona',
  group: 'users'
};
```
## FileUpload

Represents a file to be uploaded to the Sandbox.

**Properties**:

- `destination` _string_ - Absolute destination path in the Sandbox. Relative paths are resolved based on the sandbox working directory.
- `source` _string \| Buffer\<ArrayBufferLike\>_ - File to upload. If a Buffer, it is interpreted as the file content which is loaded into memory.
    Make sure it fits into memory, otherwise use the local file path which content will be streamed to the Sandbox.

## Git

Provides Git operations within a Sandbox.

### Constructors

#### new Git()

```ts
new Git(apiClient: GitApi): Git
```

**Parameters**:

- `apiClient` _GitApi_


**Returns**:

- `Git`

### Methods

#### add()

```ts
add(path: string, files: string[]): Promise<void>
```

Stages the specified files for the next commit, similar to
running 'git add' on the command line.

**Parameters**:

- `path` _string_ - Path to the Git repository root. Relative paths are resolved based on the sandbox working directory.
- `files` _string\[\]_ - List of file paths or directories to stage, relative to the repository root


**Returns**:

- `Promise<void>`

**Examples:**

```ts
// Stage a single file
await git.add('workspace/repo', ['file.txt']);
```

```ts
// Stage whole repository
await git.add('workspace/repo', ['.']);
```

***

#### branches()

```ts
branches(path: string): Promise<ListBranchResponse>
```

List branches in the repository.

**Parameters**:

- `path` _string_ - Path to the Git repository root. Relative paths are resolved based on the sandbox working directory.


**Returns**:

- `Promise<ListBranchResponse>` - List of branches in the repository

**Example:**

```ts
const response = await git.branches('workspace/repo');
console.log(`Branches: ${response.branches}`);
```

***

#### checkoutBranch()

```ts
checkoutBranch(path: string, branch: string): Promise<void>
```

Checkout branche in the repository.

**Parameters**:

- `path` _string_ - Path to the Git repository root. Relative paths are resolved based on the sandbox working directory.
- `branch` _string_ - Name of the branch to checkout


**Returns**:

- `Promise<void>`

**Example:**

```ts
await git.checkoutBranch('workspace/repo', 'new-feature');
```

***

#### clone()

```ts
clone(
   url: string, 
   path: string, 
   branch?: string, 
   commitId?: string, 
   username?: string, 
password?: string): Promise<void>
```

Clones a Git repository into the specified path. It supports
cloning specific branches or commits, and can authenticate with the remote
repository if credentials are provided.

**Parameters**:

- `url` _string_ - Repository URL to clone from
- `path` _string_ - Path where the repository should be cloned. Relative paths are resolved based on the sandbox working directory.
- `branch?` _string_ - Specific branch to clone. If not specified, clones the default branch
- `commitId?` _string_ - Specific commit to clone. If specified, the repository will be left in a detached HEAD state at this commit
- `username?` _string_ - Git username for authentication
- `password?` _string_ - Git password or token for authentication


**Returns**:

- `Promise<void>`

**Examples:**

```ts
// Clone the default branch
await git.clone(
  'https://github.com/user/repo.git',
  'workspace/repo'
);
```

```ts
// Clone a specific branch with authentication
await git.clone(
  'https://github.com/user/private-repo.git',
  'workspace/private',
  branch='develop',
  username='user',
  password='token'
);
```

```ts
// Clone a specific commit
await git.clone(
  'https://github.com/user/repo.git',
  'workspace/repo-old',
  commitId='abc123'
);
```

***

#### commit()

```ts
commit(
   path: string, 
   message: string, 
   author: string, 
   email: string, 
allowEmpty?: boolean): Promise<GitCommitResponse>
```

Commits staged changes.

**Parameters**:

- `path` _string_ - Path to the Git repository root. Relative paths are resolved based on the sandbox working directory.
- `message` _string_ - Commit message describing the changes
- `author` _string_ - Name of the commit author
- `email` _string_ - Email address of the commit author
- `allowEmpty?` _boolean_ - Allow creating an empty commit when no changes are staged


**Returns**:

- `Promise<GitCommitResponse>`

**Example:**

```ts
// Stage and commit changes
await git.add('workspace/repo', ['README.md']);
await git.commit(
  'workspace/repo',
  'Update documentation',
  'John Doe',
  'john@example.com',
  true
);
```

***

#### createBranch()

```ts
createBranch(path: string, name: string): Promise<void>
```

Create branch in the repository.

**Parameters**:

- `path` _string_ - Path to the Git repository root. Relative paths are resolved based on the sandbox working directory.
- `name` _string_ - Name of the new branch to create


**Returns**:

- `Promise<void>`

**Example:**

```ts
await git.createBranch('workspace/repo', 'new-feature');
```

***

#### deleteBranch()

```ts
deleteBranch(path: string, name: string): Promise<void>
```

Delete branche in the repository.

**Parameters**:

- `path` _string_ - Path to the Git repository root. Relative paths are resolved based on the sandbox working directory.
- `name` _string_ - Name of the branch to delete


**Returns**:

- `Promise<void>`

**Example:**

```ts
await git.deleteBranch('workspace/repo', 'new-feature');
```

***

#### pull()

```ts
pull(
   path: string, 
   username?: string, 
password?: string): Promise<void>
```

Pulls changes from the remote repository.

**Parameters**:

- `path` _string_ - Path to the Git repository root. Relative paths are resolved based on the sandbox working directory.
- `username?` _string_ - Git username for authentication
- `password?` _string_ - Git password or token for authentication


**Returns**:

- `Promise<void>`

**Examples:**

```ts
// Pull from a public repository
await git.pull('workspace/repo');
```

```ts
// Pull from a private repository
await git.pull(
  'workspace/repo',
  'user',
  'token'
);
```

***

#### push()

```ts
push(
   path: string, 
   username?: string, 
password?: string): Promise<void>
```

Push local changes to the remote repository.

**Parameters**:

- `path` _string_ - Path to the Git repository root. Relative paths are resolved based on the sandbox working directory.
- `username?` _string_ - Git username for authentication
- `password?` _string_ - Git password or token for authentication


**Returns**:

- `Promise<void>`

**Examples:**

```ts
// Push to a public repository
await git.push('workspace/repo');
```

```ts
// Push to a private repository
await git.push(
  'workspace/repo',
  'user',
  'token'
);
```

***

#### status()

```ts
status(path: string): Promise<GitStatus>
```

Gets the current status of the Git repository.

**Parameters**:

- `path` _string_ - Path to the Git repository root. Relative paths are resolved based on the sandbox working directory.


**Returns**:

- `Promise<GitStatus>` - Current repository status including:
    - currentBranch: Name of the current branch
    - ahead: Number of commits ahead of the remote branch
    - behind: Number of commits behind the remote branch
    - branchPublished: Whether the branch has been published to the remote repository
    - fileStatus: List of file statuses

**Example:**

```ts
const status = await sandbox.git.status('workspace/repo');
console.log(`Current branch: ${status.currentBranch}`);
console.log(`Commits ahead: ${status.ahead}`);
console.log(`Commits behind: ${status.behind}`);
```

***


## GitCommitResponse

Response from the git commit.

**Properties**:

- `sha` _string_ - The SHA of the commit

## Image

Represents an image definition for a Daytona sandbox.
Do not construct this class directly. Instead use one of its static factory methods,
such as `Image.base()`, `Image.debianSlim()` or `Image.fromDockerfile()`.

### Accessors

#### contextList

##### Get Signature

```ts
get contextList(): Context[]
```

###### Returns

`Context`[]

The list of context files to be added to the image.

***

#### dockerfile

##### Get Signature

```ts
get dockerfile(): string
```

**Returns**:

- `string` - The Dockerfile content.

### Methods

#### base()

```ts
static base(image: string): Image
```

Creates an Image from an existing base image.

**Parameters**:

- `image` _string_ - The base image to use.


**Returns**:

- `Image` - The Image instance.

**Example:**

```ts
const image = Image.base('python:3.12-slim-bookworm')
```

***

#### debianSlim()

```ts
static debianSlim(pythonVersion?: "3.9" | "3.10" | "3.11" | "3.12" | "3.13"): Image
```

Creates a Debian slim image based on the official Python Docker image.

**Parameters**:

- `pythonVersion?` _The Python version to use._ - `"3.9"` | `"3.10"` | `"3.11"` | `"3.12"` | `"3.13"`


**Returns**:

- `Image` - The Image instance.

**Example:**

```ts
const image = Image.debianSlim('3.12')
```

***

#### fromDockerfile()

```ts
static fromDockerfile(path: string): Image
```

Creates an Image from an existing Dockerfile.

**Parameters**:

- `path` _string_ - The path to the Dockerfile.


**Returns**:

- `Image` - The Image instance.

**Example:**

```ts
const image = Image.fromDockerfile('Dockerfile')
```

***

#### addLocalDir()

```ts
addLocalDir(localPath: string, remotePath: string): Image
```

Adds a local directory to the image.

**Parameters**:

- `localPath` _string_ - The path to the local directory.
- `remotePath` _string_ - The path of the directory in the image.


**Returns**:

- `Image` - The Image instance.

**Example:**

```ts
const image = Image
 .debianSlim('3.12')
 .addLocalDir('src', '/home/daytona/src')
```

***

#### addLocalFile()

```ts
addLocalFile(localPath: string, remotePath: string): Image
```

Adds a local file to the image.

**Parameters**:

- `localPath` _string_ - The path to the local file.
- `remotePath` _string_ - The path of the file in the image.


**Returns**:

- `Image` - The Image instance.

**Example:**

```ts
const image = Image
 .debianSlim('3.12')
 .addLocalFile('requirements.txt', '/home/daytona/requirements.txt')
```

***

#### cmd()

```ts
cmd(cmd: string[]): Image
```

Sets the default command for the image.

**Parameters**:

- `cmd` _string\[\]_ - The command to set as the default command.


**Returns**:

- `Image` - The Image instance.

**Example:**

```ts
const image = Image
 .debianSlim('3.12')
 .cmd(['/bin/bash'])
```

***

#### dockerfileCommands()

```ts
dockerfileCommands(dockerfileCommands: string[], contextDir?: string): Image
```

Extends an image with arbitrary Dockerfile-like commands.

**Parameters**:

- `dockerfileCommands` _string\[\]_ - The commands to add to the Dockerfile.
- `contextDir?` _string_ - The path to the context directory.


**Returns**:

- `Image` - The Image instance.

**Example:**

```ts
const image = Image
 .debianSlim('3.12')
 .dockerfileCommands(['RUN echo "Hello, world!"'])
```

***

#### entrypoint()

```ts
entrypoint(entrypointCommands: string[]): Image
```

Sets the entrypoint for the image.

**Parameters**:

- `entrypointCommands` _string\[\]_ - The commands to set as the entrypoint.


**Returns**:

- `Image` - The Image instance.

**Example:**

```ts
const image = Image
 .debianSlim('3.12')
 .entrypoint(['/bin/bash'])
```

***

#### env()

```ts
env(envVars: Record<string, string>): Image
```

Sets environment variables in the image.

**Parameters**:

- `envVars` _Record\<string, string\>_ - The environment variables to set.


**Returns**:

- `Image` - The Image instance.

**Example:**

```ts
const image = Image
 .debianSlim('3.12')
 .env({ FOO: 'bar' })
```

***

#### pipInstall()

```ts
pipInstall(packages: string | string[], options?: PipInstallOptions): Image
```

Adds commands to install packages using pip.

**Parameters**:

- `packages` _The packages to install._ - `string` | `string`[]
- `options?` _PipInstallOptions_ - The options for the pip install command.


**Returns**:

- `Image` - The Image instance.

**Example:**

```ts
const image = Image.debianSlim('3.12').pipInstall('numpy', { findLinks: ['https://pypi.org/simple'] })
```

***

#### pipInstallFromPyproject()

```ts
pipInstallFromPyproject(pyprojectToml: string, options?: PyprojectOptions): Image
```

Installs dependencies from a pyproject.toml file.

**Parameters**:

- `pyprojectToml` _string_ - The path to the pyproject.toml file.
- `options?` _PyprojectOptions_ - The options for the pip install command.


**Returns**:

- `Image` - The Image instance.

**Example:**

```ts
const image = Image.debianSlim('3.12')
image.pipInstallFromPyproject('pyproject.toml', { optionalDependencies: ['dev'] })
```

***

#### pipInstallFromRequirements()

```ts
pipInstallFromRequirements(requirementsTxt: string, options?: PipInstallOptions): Image
```

Installs dependencies from a requirements.txt file.

**Parameters**:

- `requirementsTxt` _string_ - The path to the requirements.txt file.
- `options?` _PipInstallOptions_ - The options for the pip install command.


**Returns**:

- `Image` - The Image instance.

**Example:**

```ts
const image = Image.debianSlim('3.12')
image.pipInstallFromRequirements('requirements.txt', { findLinks: ['https://pypi.org/simple'] })
```

***

#### runCommands()

```ts
runCommands(...commands: (string | string[])[]): Image
```

Runs commands in the image.

**Parameters**:

- `commands` _...\(string \| string\[\]\)\[\]_ - The commands to run.


**Returns**:

- `Image` - The Image instance.

**Example:**

```ts
const image = Image
 .debianSlim('3.12')
 .runCommands(
   'echo "Hello, world!"',
   ['bash', '-c', 'echo Hello, world, again!']
 )
```

***

#### workdir()

```ts
workdir(dirPath: string): Image
```

Sets the working directory in the image.

**Parameters**:

- `dirPath` _string_ - The path to the working directory.


**Returns**:

- `Image` - The Image instance.

**Example:**

```ts
const image = Image
 .debianSlim('3.12')
 .workdir('/home/daytona')
```

***


## Context

Represents a context file to be added to the image.

**Properties**:

- `archivePath` _string_ - The path inside the archive file in object storage.
- `sourcePath` _string_ - The path to the source file or directory.
## PipInstallOptions

Options for the pip install command.

**Properties**:

- `extraIndexUrls?` _string\[\]_ - The extra index URLs to use for the pip install command.
- `extraOptions?` _string_ - The extra options to use for the pip install command. Given string is passed directly to the pip install command.
- `findLinks?` _string\[\]_ - The find-links to use for the pip install command.
- `indexUrl?` _string_ - The index URL to use for the pip install command.
- `pre?` _boolean_ - Whether to install pre-release versions.
    




### Extended by

- `PyprojectOptions`
## PyprojectOptions

Options for the pip install command from a pyproject.toml file.

**Properties**:

- `extraIndexUrls?` _string\[\]_ - The extra index URLs to use for the pip install command.
    - _Inherited from_: `PipInstallOptions.extraIndexUrls`
- `extraOptions?` _string_ - The extra options to use for the pip install command. Given string is passed directly to the pip install command.
    - _Inherited from_: `PipInstallOptions.extraOptions`
- `findLinks?` _string\[\]_ - The find-links to use for the pip install command.
    - _Inherited from_: `PipInstallOptions.findLinks`
- `indexUrl?` _string_ - The index URL to use for the pip install command.
    - _Inherited from_: `PipInstallOptions.indexUrl`
- `optionalDependencies?` _string\[\]_ - The optional dependencies to install.
- `pre?` _boolean_ - Whether to install pre-release versions.
    - _Inherited from_: `PipInstallOptions.pre`



**Extends:**

- `PipInstallOptions`

The Daytona TypeScript SDK provides a powerful interface for programmatically interacting with Daytona Sandboxes.

## Installation

Install the Daytona TypeScript SDK using npm:

```bash
npm install @daytonaio/sdk
```

Or using yarn:

```bash
yarn add @daytonaio/sdk
```

## Getting Started

Here's a simple example to help you get started with the Daytona TypeScript SDK:

```typescript
import { Daytona } from '@daytonaio/sdk'

async function main() {
  // Initialize the SDK (uses environment variables by default)
  const daytona = new Daytona()

  // Create a new sandbox
  const sandbox = await daytona.create({
    language: 'typescript',
    envVars: { NODE_ENV: 'development' },
  })

  // Execute a command
  const response = await sandbox.process.executeCommand('echo "Hello, World!"')
  console.log(response.result)
}

main().catch(console.error)
```

## Configuration

The SDK can be configured using environment variables or by passing options to the constructor:

```typescript
import { Daytona } from '@daytonaio/sdk';

// Using environment variables (DAYTONA_API_KEY, DAYTONA_API_URL, DAYTONA_TARGET)
const daytona = new Daytona();

// Using explicit configuration
const daytona = new Daytona({
  apiKey: 'your-api-key',
  apiUrl: 'https://app.daytona.io/api',
  target: 'us'
});
```

## Multiple Runtime Support

The Daytona TypeScript SDK works across multiple JavaScript runtimes including Node.js, Deno, Bun, browsers, and serverless platforms (Cloudflare Workers, AWS Lambda, Azure Functions, etc.).

:::note[Browser and Framework Configuration]
When using the SDK in browser-based environments or frameworks like Vite and Next.js, you'll need to configure node polyfills. See the sections below for setup instructions.
:::

### Daytona in Vite Projects

When using Daytona SDK in a Vite-based project, you need to configure node polyfills to ensure compatibility. Add the following configuration to your `vite.config.ts` file in the plugins array:

```typescript
import { nodePolyfills } from 'vite-plugin-node-polyfills'

  plugins: [
    // ... other plugins
    nodePolyfills({
      globals: { global: true, process: true, Buffer: true },
      overrides: {
        path: 'path-browserify-win32',
      },
    }),
  ],
  // ... rest of your config
})
```

### Daytona in Next.js Projects

When using Daytona SDK in a Next.js project, you need to configure node polyfills to ensure compatibility with Webpack and Turbopack bundlers (depending on what you're using). Add the following configuration to your `next.config.ts` file:

```typescript
import type { NextConfig } from 'next'
import NodePolyfillPlugin from 'node-polyfill-webpack-plugin'
import { env, nodeless } from 'unenv'

const { alias: turbopackAlias } = env(nodeless, {})

const nextConfig: NextConfig = {
  // Turbopack
  experimental: {
    turbo: {
      resolveAlias: {
        ...turbopackAlias,
      },
    },
  },
  // Webpack
  webpack: (config, { isServer }) => {
    if (!isServer) {
      config.plugins.push(new NodePolyfillPlugin())
    }
    return config
  },
}

```

## LspServer

Provides Language Server Protocol functionality for code intelligence to provide
IDE-like features such as code completion, symbol search, and more.

### Constructors

#### new LspServer()

```ts
new LspServer(
   languageId: LspLanguageId, 
   pathToProject: string, 
   apiClient: LspApi): LspServer
```

**Parameters**:

- `languageId` _LspLanguageId_
- `pathToProject` _string_
- `apiClient` _LspApi_


**Returns**:

- `LspServer`

### Methods

#### completions()

```ts
completions(path: string, position: Position): Promise<CompletionList>
```

Gets completion suggestions at a position in a file.

**Parameters**:

- `path` _string_ - Path to the file. Relative paths are resolved based on the project path
    set in the LSP server constructor.
- `position` _Position_ - The position in the file where completion was requested


**Returns**:

- `Promise<CompletionList>` - List of completion suggestions. The list includes:
    - isIncomplete: Whether more items might be available
    - items: List of completion items, each containing:
    - label: The text to insert
    - kind: The kind of completion
    - detail: Additional details about the item
    - documentation: Documentation for the item
    - sortText: Text used to sort the item in the list
    - filterText: Text used to filter the item
    - insertText: The actual text to insert (if different from label)

**Example:**

```ts
// Get completions at a specific position
const completions = await lsp.completions('workspace/project/src/index.ts', {
  line: 10,
  character: 15
});
completions.items.forEach(item => {
  console.log(`${item.label} (${item.kind}): ${item.detail}`);
});
```

***

#### didClose()

```ts
didClose(path: string): Promise<void>
```

Notifies the language server that a file has been closed, should be called when a file is closed
in the editor to allow the language server to clean up any resources associated with that file.

**Parameters**:

- `path` _string_ - Path to the closed file. Relative paths are resolved based on the project path
    set in the LSP server constructor.


**Returns**:

- `Promise<void>`

**Example:**

```ts
// When done editing a file
await lsp.didClose('workspace/project/src/index.ts');
```

***

#### didOpen()

```ts
didOpen(path: string): Promise<void>
```

Notifies the language server that a file has been opened, enabling
language features like diagnostics and completions for that file. The server
will begin tracking the file's contents and providing language features.

**Parameters**:

- `path` _string_ - Path to the opened file. Relative paths are resolved based on the sandbox working directory.


**Returns**:

- `Promise<void>`

**Example:**

```ts
// When opening a file for editing
await lsp.didOpen('workspace/project/src/index.ts');
// Now can get completions, symbols, etc. for this file
```

***

#### documentSymbols()

```ts
documentSymbols(path: string): Promise<LspSymbol[]>
```

Get symbol information (functions, classes, variables, etc.) from a document.

**Parameters**:

- `path` _string_ - Path to the file to get symbols from. Relative paths are resolved based on the project path
    set in the LSP server constructor.


**Returns**:

- `Promise<LspSymbol[]>` - List of symbols in the document. Each symbol includes:
    - name: The symbol's name
    - kind: The symbol's kind (function, class, variable, etc.)
    - location: The location of the symbol in the file

**Example:**

```ts
// Get all symbols in a file
const symbols = await lsp.documentSymbols('workspace/project/src/index.ts');
symbols.forEach(symbol => {
  console.log(`${symbol.kind} ${symbol.name}: ${symbol.location}`);
});
```

***

#### sandboxSymbols()

```ts
sandboxSymbols(query: string): Promise<LspSymbol[]>
```

Searches for symbols matching the query string across the entire Sandbox.

**Parameters**:

- `query` _string_ - Search query to match against symbol names


**Returns**:

- `Promise<LspSymbol[]>` - List of matching symbols from all files. Each symbol includes:
    - name: The symbol's name
    - kind: The symbol's kind (function, class, variable, etc.)
    - location: The location of the symbol in the file

**Example:**

```ts
// Search for all symbols containing "User"
const symbols = await lsp.sandboxSymbols('User');
symbols.forEach(symbol => {
  console.log(`${symbol.name} (${symbol.kind}) in ${symbol.location}`);
});
```

***

#### start()

```ts
start(): Promise<void>
```

Starts the language server, must be called before using any other LSP functionality.
It initializes the language server for the specified language and project.

**Returns**:

- `Promise<void>`

**Example:**

```ts
const lsp = await sandbox.createLspServer('typescript', 'workspace/project');
await lsp.start();  // Initialize the server
// Now ready for LSP operations
```

***

#### stop()

```ts
stop(): Promise<void>
```

Stops the language server, should be called when the LSP server is no longer needed to
free up system resources.

**Returns**:

- `Promise<void>`

**Example:**

```ts
// When done with LSP features
await lsp.stop();  // Clean up resources
```

***

#### ~~workspaceSymbols()~~

```ts
workspaceSymbols(query: string): Promise<LspSymbol[]>
```

Searches for symbols matching the query string across the entire Sandbox.

**Parameters**:

- `query` _string_ - Search query to match against symbol names


**Returns**:

- `Promise<LspSymbol[]>` - List of matching symbols from all files. Each symbol includes:
    - name: The symbol's name
    - kind: The symbol's kind (function, class, variable, etc.)
    - location: The location of the symbol in the file

##### Deprecated

Use `sandboxSymbols` instead. This method will be removed in a future version.

***


## LspLanguageId

Supported language server types.

**Enum Members**:

- `JAVASCRIPT` ("javascript")
- `PYTHON` ("python")
- `TYPESCRIPT` ("typescript")

## Position

Represents a zero-based position within a text document,
specified by line number and character offset.

**Properties**:

- `character` _number_ - Zero-based character offset on the line
- `line` _number_ - Zero-based line number in the document



**Example:**

```ts
const position: Position = {
  line: 10,     // Line 11 (zero-based)
  character: 15  // Character 16 on the line (zero-based)
};
```

## ObjectStorage

ObjectStorage class for interacting with object storage services.

### Param

The configuration for the object storage service.

### Constructors

#### new ObjectStorage()

```ts
new ObjectStorage(config: ObjectStorageConfig): ObjectStorage
```

**Parameters**:

- `config` _ObjectStorageConfig_


**Returns**:

- `ObjectStorage`

### Methods

#### upload()

```ts
upload(
   path: string, 
   organizationId: string, 
archiveBasePath: string): Promise<string>
```

Upload a file or directory to object storage.

**Parameters**:

- `path` _string_ - The path to the file or directory to upload.
- `organizationId` _string_ - The organization ID to use for the upload.
- `archiveBasePath` _string_ - The base path to use for the archive.


**Returns**:

- `Promise<string>` - The hash of the uploaded file or directory.

***


## ObjectStorageConfig

Configuration for the ObjectStorage class.

**Properties**:

- `accessKeyId` _string_ - The access key ID for the object storage service.
- `bucketName?` _string_ - The name of the bucket to use.
- `endpointUrl` _string_ - The endpoint URL for the object storage service.
- `secretAccessKey` _string_ - The secret access key for the object storage service.
- `sessionToken?` _string_ - The session token for the object storage service. Used for temporary credentials.

## CodeRunParams

Parameters for code execution.

**Properties**:

- `argv?` _string\[\]_ - Command line arguments
- `env?` _Record\<string, string\>_ - Environment variables
    




### Constructors

#### new CodeRunParams()

```ts
new CodeRunParams(): CodeRunParams
```

**Returns**:

- `CodeRunParams`
## Process

Handles process and code execution within a Sandbox.

### Constructors

#### new Process()

```ts
new Process(
   clientConfig: Configuration, 
   codeToolbox: SandboxCodeToolbox, 
   apiClient: ProcessApi, 
   getPreviewToken: () => Promise<string>, 
   ensureToolboxUrl: () => Promise<void>): Process
```

**Parameters**:

- `clientConfig` _Configuration_
- `codeToolbox` _SandboxCodeToolbox_
- `apiClient` _ProcessApi_
- `getPreviewToken` _\(\) =\> Promise\<string\>_
- `ensureToolboxUrl` _\(\) =\> Promise\<void\>_


**Returns**:

- `Process`

### Methods

#### codeRun()

```ts
codeRun(
   code: string, 
   params?: CodeRunParams, 
timeout?: number): Promise<ExecuteResponse>
```

Executes code in the Sandbox using the appropriate language runtime.

**Parameters**:

- `code` _string_ - Code to execute
- `params?` _CodeRunParams_ - Parameters for code execution
- `timeout?` _number_ - Maximum time in seconds to wait for execution to complete


**Returns**:

- `Promise<ExecuteResponse>` - Code execution results containing:
    - exitCode: The execution's exit status
    - result: Standard output from the code
    - artifacts: ExecutionArtifacts object containing `stdout` (same as result) and `charts` (matplotlib charts metadata)

**Examples:**

```ts
// Run TypeScript code
const response = await process.codeRun(`
  const x = 10;
  const y = 20;
  console.log(\`Sum: \${x + y}\`);
`);
console.log(response.artifacts.stdout);  // Prints: Sum: 30
```

```ts
// Run Python code with matplotlib
const response = await process.codeRun(`
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 30)
y = np.sin(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, 'b-', linewidth=2)
plt.title('Line Chart')
plt.xlabel('X-axis (seconds)')
plt.ylabel('Y-axis (amplitude)')
plt.grid(True)
plt.show()
`);

if (response.artifacts?.charts) {
  const chart = response.artifacts.charts[0];

  console.log(`Type: ${chart.type}`);
  console.log(`Title: ${chart.title}`);
  if (chart.type === ChartType.LINE) {
    const lineChart = chart as LineChart
    console.log('X Label:', lineChart.x_label)
    console.log('Y Label:', lineChart.y_label)
    console.log('X Ticks:', lineChart.x_ticks)
    console.log('Y Ticks:', lineChart.y_ticks)
    console.log('X Tick Labels:', lineChart.x_tick_labels)
    console.log('Y Tick Labels:', lineChart.y_tick_labels)
    console.log('X Scale:', lineChart.x_scale)
    console.log('Y Scale:', lineChart.y_scale)
    console.log('Elements:')
    console.dir(lineChart.elements, { depth: null })
  }
}
```

***

#### connectPty()

```ts
connectPty(sessionId: string, options?: PtyConnectOptions): Promise<PtyHandle>
```

Connect to an existing PTY session in the sandbox.

Establishes a WebSocket connection to an existing PTY session, allowing you to
interact with a previously created terminal session.

**Parameters**:

- `sessionId` _string_ - ID of the PTY session to connect to
- `options?` _PtyConnectOptions_ - Options for the connection including data handler


**Returns**:

- `Promise<PtyHandle>` - PTY handle for managing the session

**Example:**

```ts
// Connect to an existing PTY session
const handle = await process.connectPty('my-session', {
  onData: (data) => {
    // Handle terminal output
    const text = new TextDecoder().decode(data);
    process.stdout.write(text);
  },
});

// Wait for connection to be established
await handle.waitForConnection();

// Send commands to the existing session
await handle.sendInput('pwd\n');
await handle.sendInput('ls -la\n');
await handle.sendInput('exit\n');

// Wait for completion
const result = await handle.wait();
console.log(`Session exited with code: ${result.exitCode}`);

// Clean up
await handle.disconnect();
```

***

#### createPty()

```ts
createPty(options?: PtyCreateOptions & PtyConnectOptions): Promise<PtyHandle>
```

Create a new PTY (pseudo-terminal) session in the sandbox.

Creates an interactive terminal session that can execute commands and handle user input.
The PTY session behaves like a real terminal, supporting features like command history.

**Parameters**:

- `options?` _PtyCreateOptions & PtyConnectOptions_ - PTY session configuration including creation and connection options


**Returns**:

- `Promise<PtyHandle>` - PTY handle for managing the session

**Example:**

```ts
// Create a PTY session with custom configuration
const ptyHandle = await process.createPty({
  id: 'my-interactive-session',
  cwd: '/workspace',
  envs: { TERM: 'xterm-256color', LANG: 'en_US.UTF-8' },
  cols: 120,
  rows: 30,
  onData: (data) => {
    // Handle terminal output
    const text = new TextDecoder().decode(data);
    process.stdout.write(text);
  },
});

// Wait for connection to be established
await ptyHandle.waitForConnection();

// Send commands to the terminal
await ptyHandle.sendInput('ls -la\n');
await ptyHandle.sendInput('echo "Hello, PTY!"\n');
await ptyHandle.sendInput('exit\n');

// Wait for completion and get result
const result = await ptyHandle.wait();
console.log(`PTY session completed with exit code: ${result.exitCode}`);

// Clean up
await ptyHandle.disconnect();
```

***

#### createSession()

```ts
createSession(sessionId: string): Promise<void>
```

Creates a new long-running background session in the Sandbox.

Sessions are background processes that maintain state between commands, making them ideal for
scenarios requiring multiple related commands or persistent environment setup. You can run
long-running commands and monitor process status.

**Parameters**:

- `sessionId` _string_ - Unique identifier for the new session


**Returns**:

- `Promise<void>`

**Example:**

```ts
// Create a new session
const sessionId = 'my-session';
await process.createSession(sessionId);
const session = await process.getSession(sessionId);
// Do work...
await process.deleteSession(sessionId);
```

***

#### deleteSession()

```ts
deleteSession(sessionId: string): Promise<void>
```

Delete a session from the Sandbox.

**Parameters**:

- `sessionId` _string_ - Unique identifier of the session to delete


**Returns**:

- `Promise<void>`

**Example:**

```ts
// Clean up a completed session
await process.deleteSession('my-session');
```

***

#### executeCommand()

```ts
executeCommand(
   command: string, 
   cwd?: string, 
   env?: Record<string, string>, 
timeout?: number): Promise<ExecuteResponse>
```

Executes a shell command in the Sandbox.

**Parameters**:

- `command` _string_ - Shell command to execute
- `cwd?` _string_ - Working directory for command execution. If not specified, uses the sandbox working directory.
- `env?` _Record\<string, string\>_ - Environment variables to set for the command
- `timeout?` _number_ - Maximum time in seconds to wait for the command to complete. 0 means wait indefinitely.


**Returns**:

- `Promise<ExecuteResponse>` - Command execution results containing:
    - exitCode: The command's exit status
    - result: Standard output from the command
    - artifacts: ExecutionArtifacts object containing `stdout` (same as result) and `charts` (matplotlib charts metadata)

**Examples:**

```ts
// Simple command
const response = await process.executeCommand('echo "Hello"');
console.log(response.artifacts.stdout);  // Prints: Hello
```

```ts
// Command with working directory
const result = await process.executeCommand('ls', 'workspace/src');
```

```ts
// Command with timeout
const result = await process.executeCommand('sleep 10', undefined, 5);
```

***

#### executeSessionCommand()

```ts
executeSessionCommand(
   sessionId: string, 
   req: SessionExecuteRequest, 
timeout?: number): Promise<SessionExecuteResponse>
```

Executes a command in an existing session.

**Parameters**:

- `sessionId` _string_ - Unique identifier of the session to use
- `req` _SessionExecuteRequest_ - Command execution request containing:
    - command: The command to execute
    - runAsync: Whether to execute asynchronously
- `timeout?` _number_ - Timeout in seconds


**Returns**:

- `Promise<SessionExecuteResponse>` - Command execution results containing:
    - cmdId: Unique identifier for the executed command
    - output: Combined command output (stdout and stderr) (if synchronous execution)
    - stdout: Standard output from the command
    - stderr: Standard error from the command
    - exitCode: Command exit status (if synchronous execution)

**Example:**

```ts
// Execute commands in sequence, maintaining state
const sessionId = 'my-session';

// Change directory
await process.executeSessionCommand(sessionId, {
  command: 'cd /home/daytona'
});

// Run command in new directory
const result = await process.executeSessionCommand(sessionId, {
  command: 'pwd'
});
console.log('[STDOUT]:', result.stdout);
console.log('[STDERR]:', result.stderr);
```

***

#### getPtySessionInfo()

```ts
getPtySessionInfo(sessionId: string): Promise<PtySessionInfo>
```

Get detailed information about a specific PTY session.

Retrieves comprehensive information about a PTY session including its current state,
configuration, and metadata.

**Parameters**:

- `sessionId` _string_ - ID of the PTY session to retrieve information for


**Returns**:

- `Promise<PtySessionInfo>` - PTY session information

**Throws**:

If the PTY session doesn't exist

**Example:**

```ts
// Get details about a specific PTY session
const session = await process.getPtySessionInfo('my-session');

console.log(`Session ID: ${session.id}`);
console.log(`Active: ${session.active}`);
console.log(`Working Directory: ${session.cwd}`);
console.log(`Terminal Size: ${session.cols}x${session.rows}`);

if (session.processId) {
  console.log(`Process ID: ${session.processId}`);
}
```

***

#### getSession()

```ts
getSession(sessionId: string): Promise<Session>
```

Get a session in the sandbox.

**Parameters**:

- `sessionId` _string_ - Unique identifier of the session to retrieve


**Returns**:

- `Promise<Session>` - Session information including:
    - sessionId: The session's unique identifier
    - commands: List of commands executed in the session

**Example:**

```ts
const session = await process.getSession('my-session');
session.commands.forEach(cmd => {
  console.log(`Command: ${cmd.command}`);
});
```

***

#### getSessionCommand()

```ts
getSessionCommand(sessionId: string, commandId: string): Promise<Command>
```

Gets information about a specific command executed in a session.

**Parameters**:

- `sessionId` _string_ - Unique identifier of the session
- `commandId` _string_ - Unique identifier of the command


**Returns**:

- `Promise<Command>` - Command information including:
    - id: The command's unique identifier
    - command: The executed command string
    - exitCode: Command's exit status (if completed)

**Example:**

```ts
const cmd = await process.getSessionCommand('my-session', 'cmd-123');
if (cmd.exitCode === 0) {
  console.log(`Command ${cmd.command} completed successfully`);
}
```

***

#### getSessionCommandLogs()

##### Call Signature

```ts
getSessionCommandLogs(sessionId: string, commandId: string): Promise<SessionCommandLogsResponse>
```

Get the logs for a command executed in a session.

**Parameters**:

- `sessionId` _string_ - Unique identifier of the session
- `commandId` _string_ - Unique identifier of the command

**Returns**:

- `Promise<SessionCommandLogsResponse>` - Command logs containing: output (combined stdout and stderr), stdout and stderr

**Example:**

```ts
const logs = await process.getSessionCommandLogs('my-session', 'cmd-123');
console.log('[STDOUT]:', logs.stdout);
console.log('[STDERR]:', logs.stderr);
```

##### Call Signature

```ts
getSessionCommandLogs(
   sessionId: string, 
   commandId: string, 
   onStdout: (chunk: string) => void, 
onStderr: (chunk: string) => void): Promise<void>
```

Asynchronously retrieve and process the logs for a command executed in a session as they become available.

**Parameters**:

- `sessionId` _string_ - Unique identifier of the session
- `commandId` _string_ - Unique identifier of the command
- `onStdout` _\(chunk: string\) =\> void_ - Callback function to handle stdout log chunks
- `onStderr` _\(chunk: string\) =\> void_ - Callback function to handle stderr log chunks

**Returns**:

- `Promise<void>`

**Example:**

```ts
const logs = await process.getSessionCommandLogs('my-session', 'cmd-123', (chunk) => {
  console.log('[STDOUT]:', chunk);
}, (chunk) => {
  console.log('[STDERR]:', chunk);
});
```

***

#### killPtySession()

```ts
killPtySession(sessionId: string): Promise<void>
```

Kill a PTY session and terminate its associated process.

Forcefully terminates the PTY session and cleans up all associated resources.
This will close any active connections and kill the underlying shell process.

**Parameters**:

- `sessionId` _string_ - ID of the PTY session to kill


**Returns**:

- `Promise<void>`

**Throws**:

If the PTY session doesn't exist or cannot be killed

##### Note

This operation is irreversible. Any unsaved work in the terminal session will be lost.

**Example:**

```ts
// Kill a specific PTY session
await process.killPtySession('my-session');

// Verify the session is no longer active
try {
  const info = await process.getPtySessionInfo('my-session');
  console.log(`Session still exists but active: ${info.active}`);
} catch (error) {
  console.log('Session has been completely removed');
}
```

***

#### listPtySessions()

```ts
listPtySessions(): Promise<PtySessionInfo[]>
```

List all PTY sessions in the sandbox.

Retrieves information about all PTY sessions, both active and inactive,
that have been created in this sandbox.

**Returns**:

- `Promise<PtySessionInfo[]>` - Array of PTY session information

**Example:**

```ts
// List all PTY sessions
const sessions = await process.listPtySessions();

for (const session of sessions) {
  console.log(`Session ID: ${session.id}`);
  console.log(`Active: ${session.active}`);
  console.log(`Created: ${session.createdAt}`);
  }
  console.log('---');
}
```

***

#### listSessions()

```ts
listSessions(): Promise<Session[]>
```

Lists all active sessions in the Sandbox.

**Returns**:

- `Promise<Session[]>` - Array of active sessions

**Example:**

```ts
const sessions = await process.listSessions();
sessions.forEach(session => {
  console.log(`Session ${session.sessionId}:`);
  session.commands.forEach(cmd => {
    console.log(`- ${cmd.command} (${cmd.exitCode})`);
  });
});
```

***

#### resizePtySession()

```ts
resizePtySession(
   sessionId: string, 
   cols: number, 
rows: number): Promise<PtySessionInfo>
```

Resize a PTY session's terminal dimensions.

Changes the terminal size of an active PTY session. This is useful when the
client terminal is resized or when you need to adjust the display for different
output requirements.

**Parameters**:

- `sessionId` _string_ - ID of the PTY session to resize
- `cols` _number_ - New number of terminal columns
- `rows` _number_ - New number of terminal rows


**Returns**:

- `Promise<PtySessionInfo>` - Updated session information reflecting the new terminal size

**Throws**:

If the PTY session doesn't exist or resize operation fails

##### Note

The resize operation will send a SIGWINCH signal to the shell process,
allowing terminal applications to adapt to the new size.

**Example:**

```ts
// Resize a PTY session to a larger terminal
const updatedInfo = await process.resizePtySession('my-session', 150, 40);
console.log(`Terminal resized to ${updatedInfo.cols}x${updatedInfo.rows}`);

// You can also use the PtyHandle's resize method
await ptyHandle.resize(150, 40); // cols, rows
```

***


## SessionCommandLogsResponse

**Properties**:

- `output?` _string_
- `stderr?` _string_
- `stdout?` _string_
## SessionExecuteResponse

**Extends:**

**Properties**:

- `cmdId?` _string_
    - _Inherited from_: `SessionExecuteResponse.cmdId`
- `exitCode?` _number_
    - _Inherited from_: `SessionExecuteResponse.exitCode`
- `output?` _string_
    - _Inherited from_: `SessionExecuteResponse.output`
- `stderr?` _string_
- `stdout?` _string_




- `SessionExecuteResponse`
## MAX\_PREFIX\_LEN

```ts
const MAX_PREFIX_LEN: number;
```

***


## STDERR\_PREFIX\_BYTES

```ts
const STDERR_PREFIX_BYTES: Uint8Array<ArrayBuffer>;
```

***


## STDOUT\_PREFIX\_BYTES

```ts
const STDOUT_PREFIX_BYTES: Uint8Array<ArrayBuffer>;
```

## PtyHandle

PTY session handle for managing a single PTY session.

**Properties**:

- `sessionId` _string_



Provides methods for sending input, resizing the terminal, waiting for completion,
and managing the WebSocket connection to a PTY session.

**Example:**

```typescript
// Create a PTY session
const ptyHandle = await process.createPty({
  id: 'my-session',
  cols: 120,
  rows: 30,
  onData: (data) => {
    const text = new TextDecoder().decode(data);
    process.stdout.write(text);
  },
});

// Send commands
await ptyHandle.sendInput('ls -la\n');
await ptyHandle.sendInput('exit\n');

// Wait for completion
const result = await ptyHandle.wait();
console.log(`PTY exited with code: ${result.exitCode}`);

// Clean up
await ptyHandle.disconnect();
```

### Accessors

#### error

##### Get Signature

```ts
get error(): string
```

Error message if the PTY failed

**Returns**:

- `string`

***

#### exitCode

##### Get Signature

```ts
get exitCode(): number
```

Exit code of the PTY process (if terminated)

**Returns**:

- `number`

### Constructors

#### new PtyHandle()

```ts
new PtyHandle(
   ws: WebSocket, 
   handleResize: (cols: number, rows: number) => Promise<PtySessionInfo>, 
   handleKill: () => Promise<void>, 
   onPty: (data: Uint8Array) => void | Promise<void>, 
   sessionId: string): PtyHandle
```

**Parameters**:

- `ws` _WebSocket_
- `handleResize` _\(cols: number, rows: number\) =\> Promise\<PtySessionInfo\>_
- `handleKill` _\(\) =\> Promise\<void\>_
- `onPty` _\(data: Uint8Array\) =\> void \| Promise\<void\>_
- `sessionId` _string_


**Returns**:

- `PtyHandle`

### Methods

#### disconnect()

```ts
disconnect(): Promise<void>
```

Disconnect from the PTY session and clean up resources.

Closes the WebSocket connection and releases any associated resources.
Should be called when done with the PTY session.

**Returns**:

- `Promise<void>`

**Example:**

```ts
// Always clean up when done
try {
  // ... use PTY session
} finally {
  await ptyHandle.disconnect();
}
```

***

#### isConnected()

```ts
isConnected(): boolean
```

Check if connected to the PTY session

**Returns**:

- `boolean`

***

#### kill()

```ts
kill(): Promise<void>
```

Kill the PTY process and terminate the session.

Forcefully terminates the PTY session and its associated process.
This operation is irreversible and will cause the PTY to exit immediately.

**Returns**:

- `Promise<void>`

**Throws**:

If the kill operation fails

**Example:**

```ts
// Kill a long-running process
await ptyHandle.kill();

// Wait to confirm termination
const result = await ptyHandle.wait();
console.log(`Process terminated with exit code: ${result.exitCode}`);
```

***

#### resize()

```ts
resize(cols: number, rows: number): Promise<PtySessionInfo>
```

Resize the PTY terminal dimensions.

Changes the terminal size which will notify terminal applications
about the new dimensions via SIGWINCH signal.

**Parameters**:

- `cols` _number_ - New number of terminal columns
- `rows` _number_ - New number of terminal rows


**Returns**:

- `Promise<PtySessionInfo>`

**Example:**

```ts
// Resize to 120x30
await ptyHandle.resize(120, 30);
```

***

#### sendInput()

```ts
sendInput(data: string | Uint8Array<ArrayBufferLike>): Promise<void>
```

Send input data to the PTY session.

Sends keyboard input or commands to the terminal session. The data will be
processed as if it was typed in the terminal.

**Parameters**:

- `data` _Input data to send \(commands, keystrokes, etc.\)_ - `string` | `Uint8Array`\<`ArrayBufferLike`\>


**Returns**:

- `Promise<void>`

**Throws**:

If PTY is not connected or sending fails

**Example:**

```ts
// Send a command
await ptyHandle.sendInput('ls -la\n');

// Send raw bytes
await ptyHandle.sendInput(new Uint8Array([3])); // Ctrl+C
```

***

#### wait()

```ts
wait(): Promise<PtyResult>
```

Wait for the PTY process to exit and return the result.

This method blocks until the PTY process terminates and returns
information about how it exited.

**Returns**:

- `Promise<PtyResult>` - Result containing exit code and error information

**Example:**

```ts
// Wait for process to complete
const result = await ptyHandle.wait();

if (result.exitCode === 0) {
  console.log('Process completed successfully');
} else {
  console.log(`Process failed with code: ${result.exitCode}`);
  if (result.error) {
    console.log(`Error: ${result.error}`);
  }
}
```

***

#### waitForConnection()

```ts
waitForConnection(): Promise<void>
```

Wait for the WebSocket connection to be established.

This method ensures the PTY session is ready to receive input and send output.
It waits for the server to confirm the connection is established.

**Returns**:

- `Promise<void>`

**Throws**:

If connection times out (10 seconds) or connection fails

## PtyConnectOptions

Options for connecting to a PTY session

**Properties**:

- `onData()` _\(data: Uint8Array\) =\> void \| Promise\<void\>_ - Callback to handle PTY output data
    
    **Parameters**:
    
    - `data` _Uint8Array_
    
    
    ##### Returns
    
    `void` \| `Promise<void>`
## PtyCreateOptions

Options for creating a PTY session

**Properties**:

- `cols?` _number_ - Number of terminal columns
- `cwd?` _string_ - Starting directory for the PTY session, defaults to the sandbox's working directory
- `envs?` _Record\<string, string\>_ - Environment variables for the PTY session
- `id` _string_ - The unique identifier for the PTY session
- `rows?` _number_ - Number of terminal rows
## PtyResult

PTY session result on exit

**Properties**:

- `error?` _string_ - Error message if the PTY failed
- `exitCode?` _number_ - Exit code when the PTY process ends

## Sandbox

Represents a Daytona Sandbox.

**Properties**:

- `autoArchiveInterval?` _number_ - Auto-archive interval in minutes
    
    ##### Implementation of
    
    ```ts
    SandboxDto.autoArchiveInterval
    ```
- `autoDeleteInterval?` _number_ - Auto-delete interval in minutes
    
    ##### Implementation of
    
    ```ts
    SandboxDto.autoDeleteInterval
    ```
- `autoStopInterval?` _number_ - Auto-stop interval in minutes
    
    ##### Implementation of
    
    ```ts
    SandboxDto.autoStopInterval
    ```
- `backupCreatedAt?` _string_ - When the backup was created
    
    ##### Implementation of
    
    ```ts
    SandboxDto.backupCreatedAt
    ```
- `backupState?` _SandboxBackupStateEnum_ - Current state of Sandbox backup
    
    ##### Implementation of
    
    ```ts
    SandboxDto.backupState
    ```
- `buildInfo?` _BuildInfo_ - Build information for the Sandbox if it was created from dynamic build
    
    ##### Implementation of
    
    ```ts
    SandboxDto.buildInfo
    ```
- `computerUse` _ComputerUse_ - Computer use operations interface for desktop automation
- `cpu` _number_ - Number of CPUs allocated to the Sandbox
    
    ##### Implementation of
    
    ```ts
    SandboxDto.cpu
    ```
- `createdAt?` _string_ - When the Sandbox was created
    
    ##### Implementation of
    
    ```ts
    SandboxDto.createdAt
    ```
- `disk` _number_ - Amount of disk space allocated to the Sandbox in GiB
    
    ##### Implementation of
    
    ```ts
    SandboxDto.disk
    ```
- `env` _Record\<string, string\>_ - Environment variables set in the Sandbox
    
    ##### Implementation of
    
    ```ts
    SandboxDto.env
    ```
- `errorReason?` _string_ - Error message if Sandbox is in error state
    
    ##### Implementation of
    
    ```ts
    SandboxDto.errorReason
    ```
- `fs` _FileSystem_ - File system operations interface
- `git` _Git_ - Git operations interface
- `gpu` _number_ - Number of GPUs allocated to the Sandbox
    
    ##### Implementation of
    
    ```ts
    SandboxDto.gpu
    ```
- `id` _string_ - Unique identifier for the Sandbox
    
    ##### Implementation of
    
    ```ts
    SandboxDto.id
    ```
- `labels` _Record\<string, string\>_ - Custom labels attached to the Sandbox
    
    ##### Implementation of
    
    ```ts
    SandboxDto.labels
    ```
- `memory` _number_ - Amount of memory allocated to the Sandbox in GiB
    
    ##### Implementation of
    
    ```ts
    SandboxDto.memory
    ```
- `name` _string_ - The name of the sandbox
    
    ##### Implementation of
    
    ```ts
    SandboxDto.name
    ```
- `networkAllowList?` _string_ - Comma-separated list of allowed CIDR network addresses for the Sandbox
    
    ##### Implementation of
    
    ```ts
    SandboxDto.networkAllowList
    ```
- `networkBlockAll` _boolean_ - Whether to block all network access for the Sandbox
    
    ##### Implementation of
    
    ```ts
    SandboxDto.networkBlockAll
    ```
- `organizationId` _string_ - Organization ID of the Sandbox
    
    ##### Implementation of
    
    ```ts
    SandboxDto.organizationId
    ```
- `process` _Process_ - Process execution interface
- `public` _boolean_ - Whether the Sandbox is publicly accessible
    
    ##### Implementation of
    
    ```ts
    SandboxDto.public
    ```
- `snapshot?` _string_ - Daytona snapshot used to create the Sandbox
    
    ##### Implementation of
    
    ```ts
    SandboxDto.snapshot
    ```
- `state?` _SandboxState_ - Current state of the Sandbox (e.g., "started", "stopped")
    
    ##### Implementation of
    
    ```ts
    SandboxDto.state
    ```
- `target` _string_ - Target location of the runner where the Sandbox runs
    
    ##### Implementation of
    
    ```ts
    SandboxDto.target
    ```
- `updatedAt?` _string_ - When the Sandbox was last updated
    
    ##### Implementation of
    
    ```ts
    SandboxDto.updatedAt
    ```
- `user` _string_ - OS user running in the Sandbox
    
    ##### Implementation of
    
    ```ts
    SandboxDto.user
    ```
- `volumes?` _SandboxVolume\[\]_ - Volumes attached to the Sandbox
    
    ##### Implementation of
    
    ```ts
    SandboxDto.volumes
    ```
    




### Implements

- `Sandbox`

### Constructors

#### new Sandbox()

```ts
new Sandbox(
   sandboxDto: Sandbox, 
   clientConfig: Configuration, 
   axiosInstance: AxiosInstance, 
   sandboxApi: SandboxApi, 
   codeToolbox: SandboxCodeToolbox, 
   getToolboxBaseUrl: () => Promise<string>): Sandbox
```

Creates a new Sandbox instance

**Parameters**:

- `sandboxDto` _Sandbox_ - The API Sandbox instance
- `clientConfig` _Configuration_
- `axiosInstance` _AxiosInstance_
- `sandboxApi` _SandboxApi_ - API client for Sandbox operations
- `codeToolbox` _SandboxCodeToolbox_ - Language-specific toolbox implementation
- `getToolboxBaseUrl` _\(\) =\> Promise\<string\>_


**Returns**:

- `Sandbox`

### Methods

#### archive()

```ts
archive(): Promise<void>
```

Archives the sandbox, making it inactive and preserving its state. When sandboxes are archived, the entire filesystem
state is moved to cost-effective object storage, making it possible to keep sandboxes available for an extended period.
The tradeoff between archived and stopped states is that starting an archived sandbox takes more time, depending on its size.
Sandbox must be stopped before archiving.

**Returns**:

- `Promise<void>`

***

#### createLspServer()

```ts
createLspServer(languageId: string, pathToProject: string): Promise<LspServer>
```

Creates a new Language Server Protocol (LSP) server instance.

The LSP server provides language-specific features like code completion,
diagnostics, and more.

**Parameters**:

- `languageId` _string_ - The language server type (e.g., "typescript")
- `pathToProject` _string_ - Path to the project root directory. Relative paths are resolved based on the sandbox working directory.


**Returns**:

- `Promise<LspServer>` - A new LSP server instance configured for the specified language

**Example:**

```ts
const lsp = await sandbox.createLspServer('typescript', 'workspace/project');
```

***

#### createSshAccess()

```ts
createSshAccess(expiresInMinutes?: number): Promise<SshAccessDto>
```

Creates an SSH access token for the sandbox.

**Parameters**:

- `expiresInMinutes?` _number_ - The number of minutes the SSH access token will be valid for.


**Returns**:

- `Promise<SshAccessDto>` - The SSH access token.

***

#### delete()

```ts
delete(timeout: number): Promise<void>
```

Deletes the Sandbox.

**Parameters**:

- `timeout` _number = 60_


**Returns**:

- `Promise<void>`

***

#### getPreviewLink()

```ts
getPreviewLink(port: number): Promise<PortPreviewUrl>
```

Retrieves the preview link for the sandbox at the specified port. If the port is closed,
it will be opened automatically. For private sandboxes, a token is included to grant access
to the URL.

**Parameters**:

- `port` _number_ - The port to open the preview link on.


**Returns**:

- `Promise<PortPreviewUrl>` - The response object for the preview link, which includes the `url`
    and the `token` (to access private sandboxes).

**Example:**

```ts
const previewLink = await sandbox.getPreviewLink(3000);
console.log(`Preview URL: ${previewLink.url}`);
console.log(`Token: ${previewLink.token}`);
```

***

#### getUserHomeDir()

```ts
getUserHomeDir(): Promise<string>
```

Gets the user's home directory path for the logged in user inside the Sandbox.

**Returns**:

- `Promise<string>` - The absolute path to the Sandbox user's home directory for the logged in user

**Example:**

```ts
const userHomeDir = await sandbox.getUserHomeDir();
console.log(`Sandbox user home: ${userHomeDir}`);
```

***

#### ~~getUserRootDir()~~

```ts
getUserRootDir(): Promise<string>
```

**Returns**:

- `Promise<string>`

##### Deprecated

Use `getUserHomeDir` instead. This method will be removed in a future version.

***

#### getWorkDir()

```ts
getWorkDir(): Promise<string>
```

Gets the working directory path inside the Sandbox.

**Returns**:

- `Promise<string>` - The absolute path to the Sandbox working directory. Uses the WORKDIR specified
    in the Dockerfile if present, or falling back to the user's home directory if not.

**Example:**

```ts
const workDir = await sandbox.getWorkDir();
console.log(`Sandbox working directory: ${workDir}`);
```

***

#### refreshData()

```ts
refreshData(): Promise<void>
```

Refreshes the Sandbox data from the API.

**Returns**:

- `Promise<void>`

**Example:**

```ts
await sandbox.refreshData();
console.log(`Sandbox ${sandbox.id}:`);
console.log(`State: ${sandbox.state}`);
console.log(`Resources: ${sandbox.cpu} CPU, ${sandbox.memory} GiB RAM`);
```

***

#### revokeSshAccess()

```ts
revokeSshAccess(token: string): Promise<void>
```

Revokes an SSH access token for the sandbox.

**Parameters**:

- `token` _string_ - The token to revoke.


**Returns**:

- `Promise<void>`

***

#### setAutoArchiveInterval()

```ts
setAutoArchiveInterval(interval: number): Promise<void>
```

Set the auto-archive interval for the Sandbox.

The Sandbox will automatically archive after being continuously stopped for the specified interval.

**Parameters**:

- `interval` _number_ - Number of minutes after which a continuously stopped Sandbox will be auto-archived.
    Set to 0 for the maximum interval. Default is 7 days.


**Returns**:

- `Promise<void>`

**Throws**:

- `DaytonaError` - If interval is not a non-negative integer

**Example:**

```ts
// Auto-archive after 1 hour
await sandbox.setAutoArchiveInterval(60);
// Or use the maximum interval
await sandbox.setAutoArchiveInterval(0);
```

***

#### setAutoDeleteInterval()

```ts
setAutoDeleteInterval(interval: number): Promise<void>
```

Set the auto-delete interval for the Sandbox.

The Sandbox will automatically delete after being continuously stopped for the specified interval.

**Parameters**:

- `interval` _number_ - Number of minutes after which a continuously stopped Sandbox will be auto-deleted.
    Set to negative value to disable auto-delete. Set to 0 to delete immediately upon stopping.
    By default, auto-delete is disabled.


**Returns**:

- `Promise<void>`

**Example:**

```ts
// Auto-delete after 1 hour
await sandbox.setAutoDeleteInterval(60);
// Or delete immediately upon stopping
await sandbox.setAutoDeleteInterval(0);
// Or disable auto-delete
await sandbox.setAutoDeleteInterval(-1);
```

***

#### setAutostopInterval()

```ts
setAutostopInterval(interval: number): Promise<void>
```

Set the auto-stop interval for the Sandbox.

The Sandbox will automatically stop after being idle (no new events) for the specified interval.
Events include any state changes or interactions with the Sandbox through the sdk.
Interactions using Sandbox Previews are not included.

**Parameters**:

- `interval` _number_ - Number of minutes of inactivity before auto-stopping.
    Set to 0 to disable auto-stop. Default is 15 minutes.


**Returns**:

- `Promise<void>`

**Throws**:

- `DaytonaError` - If interval is not a non-negative integer

**Example:**

```ts
// Auto-stop after 1 hour
await sandbox.setAutostopInterval(60);
// Or disable auto-stop
await sandbox.setAutostopInterval(0);
```

***

#### setLabels()

```ts
setLabels(labels: Record<string, string>): Promise<Record<string, string>>
```

Sets labels for the Sandbox.

Labels are key-value pairs that can be used to organize and identify Sandboxes.

**Parameters**:

- `labels` _Record\<string, string\>_ - Dictionary of key-value pairs representing Sandbox labels


**Returns**:

- `Promise<Record<string, string>>`

**Example:**

```ts
// Set sandbox labels
await sandbox.setLabels({
  project: 'my-project',
  environment: 'development',
  team: 'backend'
});
```

***

#### start()

```ts
start(timeout?: number): Promise<void>
```

Start the Sandbox.

This method starts the Sandbox and waits for it to be ready.

**Parameters**:

- `timeout?` _number = 60_ - Maximum time to wait in seconds. 0 means no timeout.
    Defaults to 60-second timeout.


**Returns**:

- `Promise<void>`

**Throws**:

- `DaytonaError` - If Sandbox fails to start or times out

**Example:**

```ts
const sandbox = await daytona.getCurrentSandbox('my-sandbox');
await sandbox.start(40);  // Wait up to 40 seconds
console.log('Sandbox started successfully');
```

***

#### stop()

```ts
stop(timeout?: number): Promise<void>
```

Stops the Sandbox.

This method stops the Sandbox and waits for it to be fully stopped.

**Parameters**:

- `timeout?` _number = 60_ - Maximum time to wait in seconds. 0 means no timeout.
    Defaults to 60-second timeout.


**Returns**:

- `Promise<void>`

**Example:**

```ts
const sandbox = await daytona.getCurrentSandbox('my-sandbox');
await sandbox.stop();
console.log('Sandbox stopped successfully');
```

***

#### validateSshAccess()

```ts
validateSshAccess(token: string): Promise<SshAccessValidationDto>
```

Validates an SSH access token for the sandbox.

**Parameters**:

- `token` _string_ - The token to validate.


**Returns**:

- `Promise<SshAccessValidationDto>` - The SSH access validation result.

***

#### waitUntilStarted()

```ts
waitUntilStarted(timeout?: number): Promise<void>
```

Waits for the Sandbox to reach the 'started' state.

This method polls the Sandbox status until it reaches the 'started' state
or encounters an error.

**Parameters**:

- `timeout?` _number = 60_ - Maximum time to wait in seconds. 0 means no timeout.
    Defaults to 60 seconds.


**Returns**:

- `Promise<void>`

**Throws**:

- `DaytonaError` - If the sandbox ends up in an error state or fails to start within the timeout period.

***

#### waitUntilStopped()

```ts
waitUntilStopped(timeout?: number): Promise<void>
```

Wait for Sandbox to reach 'stopped' state.

This method polls the Sandbox status until it reaches the 'stopped' state
or encounters an error.

**Parameters**:

- `timeout?` _number = 60_ - Maximum time to wait in seconds. 0 means no timeout.
    Defaults to 60 seconds.


**Returns**:

- `Promise<void>`

**Throws**:

- `DaytonaError` - If the sandbox fails to stop within the timeout period.
## PaginatedSandboxes

**Extends:**

**Properties**:

- `items` _Sandbox\[\]_
- `page` _number_
    - _Inherited from_: `PaginatedSandboxes.page`
- `total` _number_
    - _Inherited from_: `PaginatedSandboxes.total`
- `totalPages` _number_
    - _Inherited from_: `PaginatedSandboxes.totalPages`




- `Omit`\<`PaginatedSandboxesDto`, `"items"`\>
## SandboxCodeToolbox

Interface defining methods that a code toolbox must implement

### Methods

#### getRunCommand()

```ts
getRunCommand(code: string, params?: CodeRunParams): string
```

Generates a command to run the provided code

**Parameters**:

- `code` _string_
- `params?` _CodeRunParams_


**Returns**:

- `string`

## SnapshotService

Service for managing Daytona Snapshots. Can be used to list, get, create and delete Snapshots.

### Constructors

#### new SnapshotService()

```ts
new SnapshotService(
   clientConfig: Configuration, 
   snapshotsApi: SnapshotsApi, 
   objectStorageApi: ObjectStorageApi): SnapshotService
```

**Parameters**:

- `clientConfig` _Configuration_
- `snapshotsApi` _SnapshotsApi_
- `objectStorageApi` _ObjectStorageApi_


**Returns**:

- `SnapshotService`

### Methods

#### activate()

```ts
activate(snapshot: Snapshot): Promise<Snapshot>
```

Activates a snapshot.

**Parameters**:

- `snapshot` _Snapshot_ - Snapshot to activate


**Returns**:

- `Promise<Snapshot>` - The activated Snapshot instance

***

#### create()

```ts
create(params: CreateSnapshotParams, options: {
  onLogs: (chunk: string) => void;
  timeout: number;
}): Promise<Snapshot>
```

Creates and registers a new snapshot from the given Image definition.

**Parameters**:

- `params` _CreateSnapshotParams_ - Parameters for snapshot creation.
- `options` _Options for the create operation._
- `onLogs?` _\(chunk: string\) =\> void_ - This callback function handles snapshot creation logs.
- `timeout?` _number_ - Default is no timeout. Timeout in seconds (0 means no timeout).


**Returns**:

- `Promise<Snapshot>`

**Example:**

```ts
const image = Image.debianSlim('3.12').pipInstall('numpy');
await daytona.snapshot.create({ name: 'my-snapshot', image: image }, { onLogs: console.log });
```

***

#### delete()

```ts
delete(snapshot: Snapshot): Promise<void>
```

Deletes a Snapshot.

**Parameters**:

- `snapshot` _Snapshot_ - Snapshot to delete


**Returns**:

- `Promise<void>`

**Throws**:

If the Snapshot does not exist or cannot be deleted

**Example:**

```ts
const daytona = new Daytona();
const snapshot = await daytona.snapshot.get("snapshot-name");
await daytona.snapshot.delete(snapshot);
console.log("Snapshot deleted successfully");
```

***

#### get()

```ts
get(name: string): Promise<Snapshot>
```

Gets a Snapshot by its name.

**Parameters**:

- `name` _string_ - Name of the Snapshot to retrieve


**Returns**:

- `Promise<Snapshot>` - The requested Snapshot

**Throws**:

If the Snapshot does not exist or cannot be accessed

**Example:**

```ts
const daytona = new Daytona();
const snapshot = await daytona.snapshot.get("snapshot-name");
console.log(`Snapshot ${snapshot.name} is in state ${snapshot.state}`);
```

***

#### list()

```ts
list(page?: number, limit?: number): Promise<PaginatedSnapshots>
```

List paginated list of Snapshots.

**Parameters**:

- `page?` _number_ - Page number for pagination (starting from 1)
- `limit?` _number_ - Maximum number of items per page


**Returns**:

- `Promise<PaginatedSnapshots>` - Paginated list of Snapshots

**Example:**

```ts
const daytona = new Daytona();
const result = await daytona.snapshot.list(2, 10);
console.log(`Found ${result.total} snapshots`);
result.items.forEach(snapshot => console.log(`${snapshot.name} (${snapshot.imageName})`));
```

***


## PaginatedSnapshots

Represents a paginated list of Daytona Snapshots.

**Properties**:

- `items` _Snapshot\[\]_ - List of Snapshot instances in the current page.
- `page` _number_ - Current page number.
    - _Inherited from_: `Omit.page`
- `total` _number_ - Total number of Snapshots across all pages.
    - _Inherited from_: `Omit.total`
- `totalPages` _number_ - Total number of pages available.
    
    - _Inherited from_: `Omit.totalPages`




**Extends:**

- `Omit`\<`PaginatedSnapshotsDto`, `"items"`\>
## CreateSnapshotParams

```ts
type CreateSnapshotParams = {
  entrypoint: string[];
  image: string | Image;
  name: string;
  resources: Resources;
};
```

Parameters for creating a new snapshot.

**Type declaration**:

- `entrypoint?` _string\[\]_
- `image` _string \| Image_
- `name` _string_
- `resources?` _Resources_


## Snapshot

```ts
type Snapshot = SnapshotDto & {
  __brand: "Snapshot";
};
```

Represents a Daytona Snapshot which is a pre-configured sandbox.

**Type declaration**:

- `\_\_brand` _"Snapshot"_

## VolumeService

Service for managing Daytona Volumes.

This service provides methods to list, get, create, and delete Volumes.

### Constructors

#### new VolumeService()

```ts
new VolumeService(volumesApi: VolumesApi): VolumeService
```

**Parameters**:

- `volumesApi` _VolumesApi_


**Returns**:

- `VolumeService`

### Methods

#### create()

```ts
create(name: string): Promise<Volume>
```

Creates a new Volume with the specified name.

**Parameters**:

- `name` _string_ - Name for the new Volume


**Returns**:

- `Promise<Volume>` - The newly created Volume

**Throws**:

If the Volume cannot be created

**Example:**

```ts
const daytona = new Daytona();
const volume = await daytona.volume.create("my-data-volume");
console.log(`Created volume ${volume.name} with ID ${volume.id}`);
```

***

#### delete()

```ts
delete(volume: Volume): Promise<void>
```

Deletes a Volume.

**Parameters**:

- `volume` _Volume_ - Volume to delete


**Returns**:

- `Promise<void>`

**Throws**:

If the Volume does not exist or cannot be deleted

**Example:**

```ts
const daytona = new Daytona();
const volume = await daytona.volume.get("volume-name");
await daytona.volume.delete(volume);
console.log("Volume deleted successfully");
```

***

#### get()

```ts
get(name: string, create: boolean): Promise<Volume>
```

Gets a Volume by its name.

**Parameters**:

- `name` _string_ - Name of the Volume to retrieve
- `create` _boolean = false_ - Whether to create the Volume if it does not exist


**Returns**:

- `Promise<Volume>` - The requested Volume

**Throws**:

If the Volume does not exist or cannot be accessed

**Example:**

```ts
const daytona = new Daytona();
const volume = await daytona.volume.get("volume-name", true);
console.log(`Volume ${volume.name} is in state ${volume.state}`);
```

***

#### list()

```ts
list(): Promise<Volume[]>
```

Lists all available Volumes.

**Returns**:

- `Promise<Volume[]>` - List of all Volumes accessible to the user

**Example:**

```ts
const daytona = new Daytona();
const volumes = await daytona.volume.list();
console.log(`Found ${volumes.length} volumes`);
volumes.forEach(vol => console.log(`${vol.name} (${vol.id})`));
```

***


## Volume

```ts
type Volume = VolumeDto & {
  __brand: "Volume";
};
```

Represents a Daytona Volume which is a shared storage volume for Sandboxes.

**Type declaration**:

- `\_\_brand` _"Volume"_

Volumes are FUSE-based mounts that provide shared file access across Sandboxes. They allow Sandboxes to read from large files instantly - no need to upload files manually to each Sandbox. Volume data is stored on an S3-compatible object store.

- Multiple volumes can be mounted to a single Sandbox  
- A single volume can be mounted to multiple Sandboxes

## Creating Volumes

Before mounting a volume to a Sandbox, it must be created.

```bash
volume = daytona.volume.get("my-volume", create=True)
```
```bash
const volume = await daytona.volume.get('my-volume', true)
```

See: [volume.get (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/volume.md#volumeserviceget), [volume.get (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/volume.md#get)

## Mounting Volumes

Once a volume is created, it can be mounted to a Sandbox by specifying it in the `CreateSandboxFromSnapshotParams` object. Volume mount paths must meet the following requirements:

- **Must be absolute paths**: Mount paths must start with `/` (e.g., `/home/daytona/volume`)
- **Cannot be root directory**: Cannot mount to `/` or `//`
- **No relative path components**: Cannot contain `/../`, `/./`, or end with `/..` or `/.`
- **No consecutive slashes**: Cannot contain multiple consecutive slashes like `//` (except at the beginning)
- **Cannot mount to system directories**: The following system directories are prohibited:
  - `/proc`, `/sys`, `/dev`, `/boot`, `/etc`, `/bin`, `/sbin`, `/lib`, `/lib64`

```python
import os
from daytona import CreateSandboxFromSnapshotParams, Daytona, VolumeMount

daytona = Daytona()

# Create a new volume or get an existing one
volume = daytona.volume.get("my-volume", create=True)

# Mount the volume to the sandbox
mount_dir_1 = "/home/daytona/volume"

params = CreateSandboxFromSnapshotParams(
    language="python",
    volumes=[VolumeMount(volumeId=volume.id, mountPath=mount_dir_1)],
)
sandbox = daytona.create(params)
```

```typescript
import { Daytona } from '@daytonaio/sdk'
import path from 'path'

const daytona = new Daytona()

//  Create a new volume or get an existing one
const volume = await daytona.volume.get('my-volume', true)

// Mount the volume to the sandbox
const mountDir1 = '/home/daytona/volume'

const sandbox1 = await daytona.create({
  language: 'typescript',
  volumes: [{ volumeId: volume.id, mountPath: mountDir1 }],
})
```


See: [CreateSandboxFromSnapshotParams (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/daytona.md#createSandboxBaseParams), [CreateSandboxFromSnapshotParams (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/daytona.md#createSandboxBaseParams)

## Working with Volumes

Once mounted, you can read from and write to the volume just like any other directory in the Sandbox file system. Files written to the volume persist beyond the lifecycle of any individual Sandbox.

    ```python
    # Write to a file in the mounted volume
    with open("/home/daytona/volume/example.txt", "w") as f:
        f.write("Hello from Daytona volume!")

    # When you're done with the sandbox, you can remove it
    # The volume will persist even after the sandbox is removed
    sandbox.delete()
    ```
    ```typescript
    import fs from 'fs/promises'

    // Write to a file in the mounted volume
    await fs.writeFile('/home/daytona/volume/example.txt', 'Hello from Daytona volume!')

    // When you're done with the sandbox, you can remove it
    // The volume will persist even after the sandbox is removed
    await daytona.delete(sandbox1)
    ```

## Deleting Volumes

When a volume is no longer needed, it can be deleted.

```python
volume = daytona.volume.get("my-volume", create=True)
daytona.volume.delete(volume)
```
```typescript
const volume = await daytona.volume.get('my-volume', true)
await daytona.volume.delete(volume)
```

## Limitations

Since volumes are FUSE-based mounts, they can not be used for applications that require block storage access (like database tables).
Volumes are generally slower for both read and write operations compared to the local Sandbox file system.

Daytona provides a Web Terminal for interacting with your Sandboxes, allowing for a convenient way to view files, run commands, and debug.

You can open it by clicking on the Terminal icon `>_` in the [Sandbox list](https://app.daytona.io/dashboard/sandboxes) under Access for any running Sandbox. It is available by default and is accessible on port `22222`.

```text

ID                    State         Region     Created             Access
──────────────────────────────────────────────────────────────────────────────
sandbox-963e3f71      STARTED       us         12 minutes ago      >_

```

:::note
Since Terminal access is a very sensitive procedure, it is accessible only to users in your Organization, even when setting the `public` parameter to `True` in `CreateSandboxFromSnapshotParams` or `CreateSandboxFromImageParams`.
:::

Webhooks are HTTP callbacks that Daytona sends to your specified endpoints when specific events occur.
Think of them as "reverse API calls" - instead of your application asking Daytona for updates, Daytona
proactively notifies your application when something important happens.

## Use Cases

Webhooks enable powerful automation and integration scenarios:

- **Real-time Notifications**: Get instant alerts when sandboxes are created, started, or stopped
- **Automated Workflows**: Trigger deployment pipelines when snapshots are created
- **Monitoring & Analytics**: Track usage patterns and resource utilization across your organization
- **Integration**: Connect Daytona with your existing tools like Slack, Discord, or custom applications
- **Audit & Compliance**: Maintain detailed logs of all important changes

---

## Getting Started

### Accessing Webhooks

If you don't see **Webhooks** in your dashboard sidebar, contact [support@daytona.io](mailto:support@daytona.io) to enable webhooks for your organization. Provide your organization ID (found in your organization settings) when requesting access.

Once webhooks are enabled for your organization:

1. Navigate to your [Daytona Dashboard](https://app.daytona.io/dashboard)
2. Click **Webhooks** in the left sidebar
3. You'll be able to access the webhook management interface

:::note
Webhooks are available to organization admins and members with appropriate permissions.
:::

---

## Managing Webhook Endpoints

### Creating Endpoints

To start receiving webhook events:

1. Go to the **Endpoints** tab in your webhook dashboard
2. Click **Add Endpoint**
3. Configure your endpoint:
   - **Endpoint URL**: The HTTPS endpoint where you want to receive events
   - **Description**: A helpful description for this endpoint
   - **Subscribe to events**: Select which events you want to receive

### Testing Endpoints

Before going live, test your webhook endpoints:

1. Select webhook from **Endpoints** list
2. Go to the **Testing** tab
3. Configure test event and send it
4. Verify your endpoint receives the test payload correctly
5. Check that your application handles the webhook format properly

---

## Available Events

Daytona sends webhooks for lifecycle events across your infrastructure resources. You can subscribe to specific event types or receive all events and filter them in your application.

##### Event Categories

- Sandbox Lifecycle Events
- Snapshot Lifecycle Events
- Volume Lifecycle Events

---

## Webhook Payload Format

All webhook events follow a consistent structure:

```json
{
  "event": "event.type",
  "timestamp": "2024-01-15T10:30:00Z",
  "data": {
    // Event-specific data
  }
}
```

**Common Fields:**

- `event`: The type of event (e.g., "sandbox.created")
- `timestamp`: ISO 8601 timestamp when the event occurred
- `data`: Event-specific payload containing relevant information

---

## Monitoring and Activity

### Activity

The **Activity** tab provides a visual overview of your webhook activity, including delivery statistics, event volume trends, and performance metrics to help you monitor the health of your webhook integrations.

### Event Logs

The **Logs** tab shows detailed information about webhook deliveries, including event history, delivery status, and retry information for troubleshooting and monitoring purposes.