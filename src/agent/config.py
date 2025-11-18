"""Agent configuration management.

This module contains agent-specific configuration that builds on top of
the core codeact_mcp configuration (sandbox, MCP).

LLM definitions are loaded from llms.json catalog.
Credentials are loaded from .env file.
"""

import asyncio
import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

import aiofiles
import yaml
from dotenv import load_dotenv
from pydantic import BaseModel, Field

from src.codeact_mcp.config import (
    CoreConfig,
    DaytonaConfig,
    FilesystemConfig,
    LoggingConfig,
    MCPConfig,
    MCPServerConfig,
    SecurityConfig,
)


class LLMDefinition(BaseModel):
    """Definition of an LLM from llms.json catalog."""

    model_id: str
    provider: str
    sdk: str  # e.g., "langchain_anthropic.ChatAnthropic"
    api_key_env: str  # Name of environment variable containing API key
    base_url: Optional[str] = None
    output_version: Optional[str] = None
    use_previous_response_id: Optional[bool] = False
    parameters: Dict[str, Any] = Field(default_factory=dict)


class LLMConfig(BaseModel):
    """LLM configuration - references an LLM from llms.json."""

    name: str  # Name/alias from llms.json


class AgentConfig(BaseModel):
    """Agent-specific configuration.

    This config contains agent-related settings (LLM, security, logging)
    while using the core config for sandbox and MCP settings.
    """

    # Agent-specific configurations
    llm: LLMConfig
    security: SecurityConfig
    logging: LoggingConfig

    # Reference to core config (sandbox, MCP, filesystem)
    daytona: DaytonaConfig
    mcp: MCPConfig
    filesystem: FilesystemConfig

    # Runtime data (not from config files)
    llm_definition: LLMDefinition = Field(default=None, exclude=True)

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def load(
        cls,
        config_file: Optional[Path] = None,
        llms_file: Optional[Path] = None,
        env_file: Optional[Path] = None,
    ) -> "AgentConfig":
        """Load agent configuration from config.yaml, llms.json, and credentials from .env.

        Args:
            config_file: Optional path to config.yaml file (default: ./config.yaml)
            llms_file: Optional path to llms.json file (default: ./llms.json)
            env_file: Optional path to .env file (default: ./.env)

        Returns:
            Configured AgentConfig instance

        Raises:
            FileNotFoundError: If config.yaml or llms.json is not found
            ValueError: If required configuration is missing or invalid
            KeyError: If required fields are missing from config files
        """
        # Determine file paths
        if config_file is None:
            config_file = Path.cwd() / "config.yaml"
        if llms_file is None:
            llms_file = Path.cwd() / "llms.json"

        # Load environment variables for credentials
        if env_file:
            load_dotenv(env_file)
        else:
            load_dotenv()

        # Load llms.json first
        if not llms_file.exists():
            raise FileNotFoundError(
                f"LLM catalog not found: {llms_file}\n"
                f"Please create llms.json with LLM definitions."
            )

        try:
            with open(llms_file, "r") as f:
                llms_data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse llms.json: {e}")

        if "llms" not in llms_data:
            raise ValueError(
                "llms.json must have 'llms' key containing LLM definitions."
            )

        llm_catalog = {
            name: LLMDefinition(**definition)
            for name, definition in llms_data["llms"].items()
        }

        # Load config.yaml
        if not config_file.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {config_file}\n"
                f"Please create config.yaml with all required settings."
            )

        try:
            with open(config_file, "r") as f:
                config_data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise ValueError(f"Failed to parse config.yaml: {e}")

        if not config_data:
            raise ValueError(
                "config.yaml is empty. Please add required configuration sections."
            )

        # Validate that all required sections exist in config.yaml
        required_sections = ["llm", "daytona", "security", "mcp", "logging", "filesystem"]
        missing_sections = [s for s in required_sections if s not in config_data]
        if missing_sections:
            raise ValueError(
                f"Missing required sections in config.yaml: {', '.join(missing_sections)}\n"
                f"Please add these sections to your config.yaml file."
            )

        # Load LLM configuration from config.yaml
        llm_data = config_data["llm"]

        # Handle both formats: simple string or dict with name
        if isinstance(llm_data, str):
            llm_name = llm_data
        elif isinstance(llm_data, dict) and "name" in llm_data:
            llm_name = llm_data["name"]
        else:
            raise ValueError(
                "llm section must be either a string (LLM name) or dict with 'name' field"
            )

        # Look up LLM definition from catalog
        if llm_name not in llm_catalog:
            available = ", ".join(llm_catalog.keys())
            raise ValueError(
                f"LLM '{llm_name}' not found in llms.json.\n"
                f"Available LLMs: {available}"
            )

        llm_definition = llm_catalog[llm_name]

        # Create LLM config
        llm_config = LLMConfig(name=llm_name)

        # Load Daytona configuration
        daytona_data = config_data["daytona"]
        required_daytona_fields = [
            "base_url",
            "auto_stop_interval",
            "auto_archive_interval",
            "auto_delete_interval",
            "python_version",
        ]
        missing_daytona = [f for f in required_daytona_fields if f not in daytona_data]
        if missing_daytona:
            raise ValueError(
                f"Missing required fields in daytona section: {', '.join(missing_daytona)}"
            )

        # Load snapshot configuration
        daytona_config = DaytonaConfig(
            api_key=os.getenv("DAYTONA_API_KEY", ""),
            base_url=daytona_data["base_url"],
            auto_stop_interval=daytona_data["auto_stop_interval"],
            auto_archive_interval=daytona_data["auto_archive_interval"],
            auto_delete_interval=daytona_data["auto_delete_interval"],
            python_version=daytona_data["python_version"],
            snapshot_enabled=daytona_data.get("snapshot_enabled", True),
            snapshot_name=daytona_data.get("snapshot_name"),
            snapshot_auto_create=daytona_data.get("snapshot_auto_create", True),
        )

        # Load Security configuration
        security_data = config_data["security"]
        required_security_fields = [
            "max_execution_time",
            "max_code_length",
            "max_file_size",
            "enable_code_validation",
            "allowed_imports",
            "blocked_patterns",
        ]
        missing_security = [
            f for f in required_security_fields if f not in security_data
        ]
        if missing_security:
            raise ValueError(
                f"Missing required fields in security section: {', '.join(missing_security)}"
            )

        security_config = SecurityConfig(
            max_execution_time=security_data["max_execution_time"],
            max_code_length=security_data["max_code_length"],
            max_file_size=security_data["max_file_size"],
            enable_code_validation=security_data["enable_code_validation"],
            allowed_imports=security_data["allowed_imports"],
            blocked_patterns=security_data["blocked_patterns"],
        )

        # Load MCP configuration
        mcp_data = config_data["mcp"]
        if "servers" not in mcp_data:
            raise ValueError("Missing required field in mcp section: servers")
        if "tool_discovery_enabled" not in mcp_data:
            raise ValueError(
                "Missing required field in mcp section: tool_discovery_enabled"
            )

        mcp_servers = [MCPServerConfig(**server) for server in mcp_data["servers"]]
        mcp_config = MCPConfig(
            servers=mcp_servers,
            tool_discovery_enabled=mcp_data["tool_discovery_enabled"],
            lazy_load=mcp_data.get("lazy_load", True),
            cache_duration=mcp_data.get("cache_duration"),
            tool_exposure_mode=mcp_data.get("tool_exposure_mode", "summary"),
        )

        # Load Logging configuration
        logging_data = config_data["logging"]
        required_logging_fields = ["level", "format", "file"]
        missing_logging = [f for f in required_logging_fields if f not in logging_data]
        if missing_logging:
            raise ValueError(
                f"Missing required fields in logging section: {', '.join(missing_logging)}"
            )

        logging_config = LoggingConfig(
            level=logging_data["level"],
            format=logging_data["format"],
            file=logging_data["file"],
        )

        # Load Filesystem configuration
        filesystem_data = config_data["filesystem"]
        required_filesystem_fields = ["allowed_directories"]
        missing_filesystem = [
            f for f in required_filesystem_fields if f not in filesystem_data
        ]
        if missing_filesystem:
            raise ValueError(
                f"Missing required fields in filesystem section: {', '.join(missing_filesystem)}"
            )

        filesystem_config = FilesystemConfig(
            allowed_directories=filesystem_data["allowed_directories"],
            enable_path_validation=filesystem_data.get("enable_path_validation", True),
        )

        # Create config object
        config = cls(
            llm=llm_config,
            security=security_config,
            logging=logging_config,
            daytona=daytona_config,
            mcp=mcp_config,
            filesystem=filesystem_config,
        )

        # Store runtime data
        config.llm_definition = llm_definition

        return config

    @classmethod
    async def load_async(
        cls,
        config_file: Optional[Path] = None,
        llms_file: Optional[Path] = None,
        env_file: Optional[Path] = None,
    ) -> "AgentConfig":
        """Load agent configuration asynchronously from config.yaml, llms.json, and credentials from .env.

        This is the async version of load() that uses aiofiles to avoid blocking I/O.
        Use this method in async contexts like LangGraph deployment.

        Args:
            config_file: Optional path to config.yaml file (default: ./config.yaml)
            llms_file: Optional path to llms.json file (default: ./llms.json)
            env_file: Optional path to .env file (default: ./.env)

        Returns:
            Configured AgentConfig instance

        Raises:
            FileNotFoundError: If config.yaml or llms.json is not found
            ValueError: If required configuration is missing or invalid
            KeyError: If required fields are missing from config files
        """
        # Determine file paths
        if config_file is None or llms_file is None:
            cwd = await asyncio.to_thread(Path.cwd)
            if config_file is None:
                config_file = cwd / "config.yaml"
            if llms_file is None:
                llms_file = cwd / "llms.json"

        # Load environment variables for credentials (sync operation - dotenv doesn't have async)
        # This is fast as it reads a small file and is usually cached by the OS
        if env_file:
            await asyncio.to_thread(load_dotenv, env_file)
        else:
            await asyncio.to_thread(load_dotenv)

        # Load llms.json asynchronously
        if not llms_file.exists():
            raise FileNotFoundError(
                f"LLM catalog not found: {llms_file}\n"
                f"Please create llms.json with LLM definitions."
            )

        try:
            async with aiofiles.open(llms_file, "r") as f:
                llms_content = await f.read()
            llms_data = json.loads(llms_content)
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse llms.json: {e}")

        if "llms" not in llms_data:
            raise ValueError(
                "llms.json must have 'llms' key containing LLM definitions."
            )

        llm_catalog = {
            name: LLMDefinition(**definition)
            for name, definition in llms_data["llms"].items()
        }

        # Load config.yaml asynchronously
        if not config_file.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {config_file}\n"
                f"Please create config.yaml with all required settings."
            )

        try:
            async with aiofiles.open(config_file, "r") as f:
                config_content = await f.read()
            config_data = yaml.safe_load(config_content)
        except yaml.YAMLError as e:
            raise ValueError(f"Failed to parse config.yaml: {e}")

        if not config_data:
            raise ValueError(
                "config.yaml is empty. Please add required configuration sections."
            )

        # Validate that all required sections exist in config.yaml
        required_sections = ["llm", "daytona", "security", "mcp", "logging", "filesystem"]
        missing_sections = [s for s in required_sections if s not in config_data]
        if missing_sections:
            raise ValueError(
                f"Missing required sections in config.yaml: {', '.join(missing_sections)}\n"
                f"Please add these sections to your config.yaml file."
            )

        # Load LLM configuration from config.yaml
        llm_data = config_data["llm"]

        # Handle both formats: simple string or dict with name
        if isinstance(llm_data, str):
            llm_name = llm_data
        elif isinstance(llm_data, dict) and "name" in llm_data:
            llm_name = llm_data["name"]
        else:
            raise ValueError(
                "llm section must be either a string (LLM name) or dict with 'name' field"
            )

        # Look up LLM definition from catalog
        if llm_name not in llm_catalog:
            available = ", ".join(llm_catalog.keys())
            raise ValueError(
                f"LLM '{llm_name}' not found in llms.json.\n"
                f"Available LLMs: {available}"
            )

        llm_definition = llm_catalog[llm_name]

        # Create LLM config
        llm_config = LLMConfig(name=llm_name)

        # Load Daytona configuration
        daytona_data = config_data["daytona"]
        required_daytona_fields = [
            "base_url",
            "auto_stop_interval",
            "auto_archive_interval",
            "auto_delete_interval",
            "python_version",
        ]
        missing_daytona = [f for f in required_daytona_fields if f not in daytona_data]
        if missing_daytona:
            raise ValueError(
                f"Missing required fields in daytona section: {', '.join(missing_daytona)}"
            )

        # Load snapshot configuration
        daytona_config = DaytonaConfig(
            api_key=os.getenv("DAYTONA_API_KEY", ""),
            base_url=daytona_data["base_url"],
            auto_stop_interval=daytona_data["auto_stop_interval"],
            auto_archive_interval=daytona_data["auto_archive_interval"],
            auto_delete_interval=daytona_data["auto_delete_interval"],
            python_version=daytona_data["python_version"],
            snapshot_enabled=daytona_data.get("snapshot_enabled", True),
            snapshot_name=daytona_data.get("snapshot_name"),
            snapshot_auto_create=daytona_data.get("snapshot_auto_create", True),
        )

        # Load Security configuration
        security_data = config_data["security"]
        required_security_fields = [
            "max_execution_time",
            "max_code_length",
            "max_file_size",
            "enable_code_validation",
            "allowed_imports",
            "blocked_patterns",
        ]
        missing_security = [
            f for f in required_security_fields if f not in security_data
        ]
        if missing_security:
            raise ValueError(
                f"Missing required fields in security section: {', '.join(missing_security)}"
            )

        security_config = SecurityConfig(
            max_execution_time=security_data["max_execution_time"],
            max_code_length=security_data["max_code_length"],
            max_file_size=security_data["max_file_size"],
            enable_code_validation=security_data["enable_code_validation"],
            allowed_imports=security_data["allowed_imports"],
            blocked_patterns=security_data["blocked_patterns"],
        )

        # Load MCP configuration
        mcp_data = config_data["mcp"]
        if "servers" not in mcp_data:
            raise ValueError("Missing required field in mcp section: servers")
        if "tool_discovery_enabled" not in mcp_data:
            raise ValueError(
                "Missing required field in mcp section: tool_discovery_enabled"
            )

        mcp_servers = [MCPServerConfig(**server) for server in mcp_data["servers"]]
        mcp_config = MCPConfig(
            servers=mcp_servers,
            tool_discovery_enabled=mcp_data["tool_discovery_enabled"],
            lazy_load=mcp_data.get("lazy_load", True),
            cache_duration=mcp_data.get("cache_duration"),
            tool_exposure_mode=mcp_data.get("tool_exposure_mode", "summary"),
        )

        # Load Logging configuration
        logging_data = config_data["logging"]
        required_logging_fields = ["level", "format", "file"]
        missing_logging = [f for f in required_logging_fields if f not in logging_data]
        if missing_logging:
            raise ValueError(
                f"Missing required fields in logging section: {', '.join(missing_logging)}"
            )

        logging_config = LoggingConfig(
            level=logging_data["level"],
            format=logging_data["format"],
            file=logging_data["file"],
        )

        # Load Filesystem configuration
        filesystem_data = config_data["filesystem"]
        required_filesystem_fields = ["allowed_directories"]
        missing_filesystem = [
            f for f in required_filesystem_fields if f not in filesystem_data
        ]
        if missing_filesystem:
            raise ValueError(
                f"Missing required fields in filesystem section: {', '.join(missing_filesystem)}"
            )

        filesystem_config = FilesystemConfig(
            allowed_directories=filesystem_data["allowed_directories"],
            enable_path_validation=filesystem_data.get("enable_path_validation", True),
        )

        # Create config object
        config = cls(
            llm=llm_config,
            security=security_config,
            logging=logging_config,
            daytona=daytona_config,
            mcp=mcp_config,
            filesystem=filesystem_config,
        )

        # Store runtime data
        config.llm_definition = llm_definition

        return config

    def validate_api_keys(self) -> None:
        """Validate that required API keys are present.

        Raises:
            ValueError: If required API keys are missing
        """
        missing_keys = []

        if not self.daytona.api_key:
            missing_keys.append("DAYTONA_API_KEY")

        # Check LLM API key
        api_key = os.getenv(self.llm_definition.api_key_env, "")
        if not api_key:
            missing_keys.append(self.llm_definition.api_key_env)

        if missing_keys:
            raise ValueError(
                f"Missing required credentials in .env file:\n"
                f"  - {chr(10).join(missing_keys)}\n"
                f"Please add these credentials to your .env file."
            )

    def get_llm_client(self):
        """Create and return appropriate LLM client based on llm_definition.

        Returns:
            LangChain LLM client instance

        Raises:
            ImportError: If SDK module cannot be imported
            AttributeError: If SDK class cannot be found
        """
        # Parse SDK string (e.g., "langchain_anthropic.ChatAnthropic")
        sdk_parts = self.llm_definition.sdk.rsplit(".", 1)
        if len(sdk_parts) != 2:
            raise ValueError(
                f"Invalid SDK format: {self.llm_definition.sdk}. "
                f"Expected 'module.ClassName'"
            )

        module_name, class_name = sdk_parts

        # Dynamically import the SDK module
        try:
            module = __import__(module_name, fromlist=[class_name])
        except ImportError as e:
            raise ImportError(
                f"Failed to import SDK module '{module_name}': {e}\n"
                f"Make sure the required package is installed."
            )

        # Get the class
        try:
            llm_class = getattr(module, class_name)
        except AttributeError:
            raise AttributeError(
                f"Class '{class_name}' not found in module '{module_name}'"
            )

        # Get API key from environment
        api_key = os.getenv(self.llm_definition.api_key_env, "")

        # Build kwargs for LLM client
        kwargs = {
            "model": self.llm_definition.model_id,
            **self.llm_definition.parameters,  # Pass through all parameters
        }

        # Add API key with provider-specific parameter name
        if self.llm_definition.provider == "anthropic":
            kwargs["anthropic_api_key"] = api_key
        elif self.llm_definition.provider == "openai":
            kwargs["openai_api_key"] = api_key
        else:
            # Generic fallback (most use 'api_key')
            kwargs["api_key"] = api_key

        # Add base_url if specified
        if self.llm_definition.base_url:
            kwargs["base_url"] = self.llm_definition.base_url

        # Add output_version if specified
        if self.llm_definition.output_version:
            kwargs["output_version"] = self.llm_definition.output_version

        # Add use_previous_response_id if specified
        if self.llm_definition.use_previous_response_id:
            kwargs["use_previous_response_id"] = self.llm_definition.use_previous_response_id

        # Instantiate and return client
        return llm_class(**kwargs)

    def to_core_config(self) -> CoreConfig:
        """Convert to CoreConfig for use with SessionManager.

        Returns:
            CoreConfig instance with sandbox/MCP settings
        """
        return CoreConfig(
            daytona=self.daytona,
            security=self.security,
            mcp=self.mcp,
            logging=self.logging,
            filesystem=self.filesystem,
        )
