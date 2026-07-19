from unittest.mock import patch

from fastapi.testclient import TestClient

from copilot.main import app
from copilot.models.chat import ChatResponse

client = TestClient(app)


@patch("copilot.api.routes.chat.assistant")
def test_chat_endpoint(mock_assistant):
    """Test the chat endpoint."""

    mock_assistant.chat.return_value = ChatResponse(
        conversation_id="conversation-1",
        response="Hello!",
    )

    response = client.post(
        "/chat",
        json={
            "conversation_id": "conversation-1",
            "message": "Hi",
        },
    )

    assert response.status_code == 200

    assert response.json() == {
        "conversation_id": "conversation-1",
        "response": "Hello!",
    }

    mock_assistant.chat.assert_called_once_with(
        conversation_id="conversation-1",
        message="Hi",
    )