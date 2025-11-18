"""Prompt templates for agent operations."""

from .base import (
    CODE_GENERATION_PROMPT,
    MULTI_TURN_PROMPT,
    TOOL_DISCOVERY_PROMPT,
    TOOL_ITEM_TEMPLATE,
    TOOL_SUMMARY_TEMPLATE,
    build_code_generation_prompt,
    build_multi_turn_prompt,
    build_tool_discovery_prompt,
    format_tool_summary,
)
from .general import GENERAL_AGENT_INSTRUCTIONS
from .task_workflow import (
    TASK_WORKFLOW_INSTRUCTIONS,
    SUBAGENT_DELEGATION_INSTRUCTIONS,
    TASK_DESCRIPTION_PREFIX,
)

__all__ = [
    # Base prompts
    "CODE_GENERATION_PROMPT",
    "MULTI_TURN_PROMPT",
    "TOOL_DISCOVERY_PROMPT",
    "TOOL_SUMMARY_TEMPLATE",
    "TOOL_ITEM_TEMPLATE",
    "build_code_generation_prompt",
    "build_multi_turn_prompt",
    "build_tool_discovery_prompt",
    "format_tool_summary",
    # General prompts
    "GENERAL_AGENT_INSTRUCTIONS",
    # Task/Research prompts
    "TASK_WORKFLOW_INSTRUCTIONS",
    "SUBAGENT_DELEGATION_INSTRUCTIONS",
    "TASK_DESCRIPTION_PREFIX",
]
