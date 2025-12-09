"""Real API tests for session persistence.

These tests require DAYTONA_API_KEY environment variable to be set.
They test actual sandbox creation and session persistence.
"""

import os

import pytest

# Skip all tests if DAYTONA_API_KEY is not set
pytestmark = pytest.mark.skipif(
    not os.environ.get("DAYTONA_API_KEY"),
    reason="DAYTONA_API_KEY not set - skipping real sandbox tests",
)


class TestSessionPersistenceReal:
    """Test session persistence with real sandbox."""

    @pytest.mark.asyncio
    async def test_session_persisted_on_create(self, tmp_path, monkeypatch):
        """Test that session.json is created after agent creation."""
        from ptc_cli.agent.lifecycle import create_agent_with_session
        from ptc_cli.agent.persistence import load_persisted_session

        fake_home = tmp_path / "home"
        fake_home.mkdir()
        monkeypatch.setattr("pathlib.Path.home", lambda: fake_home)

        agent_name = "test-persist-create"

        agent, session, reusing = await create_agent_with_session(
            agent_name=agent_name,
            persist_session=True,
        )

        try:
            # Should not be reusing on first create
            assert reusing is False

            # Check persisted session exists
            persisted = load_persisted_session(agent_name)
            assert persisted is not None
            assert persisted["sandbox_id"] == session.sandbox.sandbox_id
        finally:
            if session:
                await session.stop()

    @pytest.mark.asyncio
    async def test_session_reuse_when_config_unchanged(self, tmp_path, monkeypatch):
        """Test that second create reuses sandbox if config unchanged."""
        from ptc_cli.agent.lifecycle import create_agent_with_session
        from ptc_cli.agent.persistence import delete_persisted_session

        fake_home = tmp_path / "home"
        fake_home.mkdir()
        monkeypatch.setattr("pathlib.Path.home", lambda: fake_home)

        agent_name = "test-persist-reuse"

        # First creation
        agent1, session1, reusing1 = await create_agent_with_session(
            agent_name=agent_name,
            persist_session=True,
        )
        first_sandbox_id = session1.sandbox.sandbox_id

        # Don't stop session1 - we want to reuse it

        # Second creation - should reuse
        agent2, session2, reusing2 = await create_agent_with_session(
            agent_name=agent_name,
            persist_session=True,
        )

        try:
            assert reusing2 is True
            assert session2.sandbox.sandbox_id == first_sandbox_id
        finally:
            if session2:
                await session2.stop()
            delete_persisted_session(agent_name)
