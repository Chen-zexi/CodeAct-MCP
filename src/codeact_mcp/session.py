"""Session Management - Handle conversation lifecycle and sandbox persistence."""

import asyncio
from typing import Dict, Optional

import structlog

from .config import CoreConfig
from .mcp_registry import MCPRegistry
from .sandbox import CodeActSandbox

logger = structlog.get_logger(__name__)


class Session:
    """Represents a conversation session with a persistent sandbox."""

    def __init__(self, conversation_id: str, config: CoreConfig):
        """Initialize session.

        Args:
            conversation_id: Unique conversation identifier
            config: Application configuration
        """
        self.conversation_id = conversation_id
        self.config = config
        self.sandbox: Optional[CodeActSandbox] = None
        self.mcp_registry: Optional[MCPRegistry] = None
        self._initialized = False

        logger.info("Created session", conversation_id=conversation_id)

    async def initialize(self) -> None:
        """Initialize the session (connect MCP servers and setup sandbox)."""
        if self._initialized:
            logger.warning("Session already initialized", conversation_id=self.conversation_id)
            return

        logger.info("Initializing session", conversation_id=self.conversation_id)

        # Initialize MCP registry
        self.mcp_registry = MCPRegistry(self.config)
        await self.mcp_registry.connect_all()

        # Create and setup sandbox
        # Wrap constructor in thread to avoid blocking from Daytona SDK initialization
        self.sandbox = await asyncio.to_thread(
            CodeActSandbox, self.config, self.mcp_registry
        )
        await self.sandbox.setup()

        self._initialized = True

        logger.info("Session initialized", conversation_id=self.conversation_id)

    async def get_sandbox(self) -> CodeActSandbox:
        """Get the sandbox for this session (initializes if needed).

        Returns:
            CodeActSandbox instance
        """
        if not self._initialized:
            await self.initialize()

        return self.sandbox

    async def cleanup(self) -> None:
        """Clean up session resources."""
        logger.info("Cleaning up session", conversation_id=self.conversation_id)

        if self.sandbox:
            await self.sandbox.cleanup()
            self.sandbox = None

        if self.mcp_registry:
            await self.mcp_registry.disconnect_all()
            self.mcp_registry = None

        self._initialized = False

        logger.info("Session cleaned up", conversation_id=self.conversation_id)

    async def __aenter__(self):
        """Async context manager entry."""
        await self.initialize()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.cleanup()


class SessionManager:
    """Manages multiple conversation sessions."""

    _sessions: Dict[str, Session] = {}

    @classmethod
    def get_session(cls, conversation_id: str, config: CoreConfig) -> Session:
        """Get or create a session for a conversation.

        Args:
            conversation_id: Unique conversation identifier
            config: Application configuration

        Returns:
            Session instance
        """
        if conversation_id not in cls._sessions:
            logger.info("Creating new session", conversation_id=conversation_id)
            cls._sessions[conversation_id] = Session(conversation_id, config)
        else:
            logger.debug("Returning existing session", conversation_id=conversation_id)

        return cls._sessions[conversation_id]

    @classmethod
    async def cleanup_session(cls, conversation_id: str) -> None:
        """Clean up a specific session.

        Args:
            conversation_id: Conversation identifier
        """
        if conversation_id in cls._sessions:
            session = cls._sessions[conversation_id]
            await session.cleanup()
            del cls._sessions[conversation_id]

            logger.info("Session removed", conversation_id=conversation_id)

    @classmethod
    async def cleanup_all(cls) -> None:
        """Clean up all active sessions."""
        logger.info("Cleaning up all sessions", count=len(cls._sessions))

        for conversation_id in list(cls._sessions.keys()):
            await cls.cleanup_session(conversation_id)

        logger.info("All sessions cleaned up")

    @classmethod
    def get_active_sessions(cls) -> list[str]:
        """Get list of active session IDs.

        Returns:
            List of conversation IDs
        """
        return list(cls._sessions.keys())

    @classmethod
    def get_session_count(cls) -> int:
        """Get count of active sessions.

        Returns:
            Number of active sessions
        """
        return len(cls._sessions)
