from unittest.mock import MagicMock

from copilot.memory.in_memory import InMemoryConversationStore
from copilot.services.assistant_service import AssistantService


def test_chat_generates_response_and_stores_history():
    """Test chat generates a response and stores conversation history."""

    memory = InMemoryConversationStore()

    service = AssistantService(
        memory=memory,
    )

    service.llm = MagicMock()
    service.llm.generate.return_value = "Hello! How can I help you?"

    response = service.chat(
        conversation_id="conversation-1",
        message="Hi",
    )

    assert response.conversation_id == "conversation-1"
    assert response.response == "Hello! How can I help you?"

    history = memory.get_messages(
        conversation_id="conversation-1",
    )

    assert history == [
        {
            "role": "user",
            "content": "Hi",
        },
        {
            "role": "assistant",
            "content": "Hello! How can I help you?",
        },
    ]


def test_chat_uses_conversation_history():
    """Test chat sends the complete conversation history to the LLM."""

    memory = InMemoryConversationStore()

    memory.add_message(
        conversation_id="conversation-1",
        role="user",
        content="Hello",
    )

    memory.add_message(
        conversation_id="conversation-1",
        role="assistant",
        content="Hi!",
    )

    service = AssistantService(
        memory=memory,
    )

    service.llm = MagicMock()
    service.llm.generate.return_value = "How are you?"

    service.chat(
        conversation_id="conversation-1",
        message="How are you?",
    )

    service.llm.generate.assert_called_once()

    _, kwargs = service.llm.generate.call_args

    assert "Hello" in kwargs["user_prompt"]
    assert "Hi!" in kwargs["user_prompt"]
    assert "How are you?" in kwargs["user_prompt"]