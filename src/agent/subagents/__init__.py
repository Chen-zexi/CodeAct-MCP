"""Sub-agent definitions for deepagent delegation."""

from typing import Any, Dict, List, Optional

from .general import create_general_subagent, get_general_subagent_config
from .research import create_research_subagent, get_research_subagent_config

# Registry mapping subagent names to their creation functions
SUBAGENT_REGISTRY = {
    "research": create_research_subagent,
    "general": create_general_subagent,
}

# Subagents that require sandbox and mcp_registry
STATEFUL_SUBAGENTS = {"general"}

# Parameter mapping for each subagent type
# Maps generic parameter names to subagent-specific parameter names
SUBAGENT_PARAMS = {
    "research": {
        "accepted": ["max_researcher_iterations", "mcp_tools"],
    },
    "general": {
        "accepted": ["max_iterations", "additional_tools", "include_mcp_docs", "tool_exposure_mode"],
    },
}


def create_subagent_by_name(
    name: str,
    sandbox: Optional[Any] = None,
    mcp_registry: Optional[Any] = None,
    **kwargs,
) -> Dict[str, Any]:
    """Create a subagent by name using the registry.

    Args:
        name: Name of the subagent (e.g., "research", "general")
        sandbox: CodeActSandbox instance (required for stateful subagents)
        mcp_registry: MCPRegistry instance (required for stateful subagents)
        **kwargs: Additional arguments passed to the subagent creation function

    Returns:
        Configured subagent dictionary

    Raises:
        ValueError: If subagent name is not found in registry
        ValueError: If stateful subagent is missing required dependencies
    """
    if name not in SUBAGENT_REGISTRY:
        available = ", ".join(SUBAGENT_REGISTRY.keys())
        raise ValueError(f"Unknown subagent: '{name}'. Available: {available}")

    create_fn = SUBAGENT_REGISTRY[name]

    # Filter kwargs to only include parameters accepted by this subagent
    accepted_params = SUBAGENT_PARAMS.get(name, {}).get("accepted", [])
    filtered_kwargs = {k: v for k, v in kwargs.items() if k in accepted_params}

    # Check if this is a stateful subagent requiring sandbox/mcp_registry
    if name in STATEFUL_SUBAGENTS:
        if sandbox is None or mcp_registry is None:
            raise ValueError(
                f"Subagent '{name}' requires sandbox and mcp_registry"
            )
        return create_fn(sandbox=sandbox, mcp_registry=mcp_registry, **filtered_kwargs)

    # Stateless subagent (e.g., research)
    return create_fn(**filtered_kwargs)


def create_subagents_from_names(
    names: List[str],
    sandbox: Optional[Any] = None,
    mcp_registry: Optional[Any] = None,
    **kwargs,
) -> List[Dict[str, Any]]:
    """Create multiple subagents from a list of names.

    Args:
        names: List of subagent names to create
        sandbox: CodeActSandbox instance (required for stateful subagents)
        mcp_registry: MCPRegistry instance (required for stateful subagents)
        **kwargs: Additional arguments passed to all subagent creation functions

    Returns:
        List of configured subagent dictionaries
    """
    return [
        create_subagent_by_name(name, sandbox, mcp_registry, **kwargs)
        for name in names
    ]


__all__ = [
    "create_general_subagent",
    "get_general_subagent_config",
    "create_research_subagent",
    "get_research_subagent_config",
    "create_subagent_by_name",
    "create_subagents_from_names",
    "SUBAGENT_REGISTRY",
]
