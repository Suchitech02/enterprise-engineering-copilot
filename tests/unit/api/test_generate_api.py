from unittest.mock import patch

from fastapi.testclient import TestClient

from copilot.main import app
from copilot.models.generate import GenerateResponse

client = TestClient(app)


@patch("copilot.api.routes.generate.assistant")
def test_generate_endpoint(mock_assistant):
    """Test the generate endpoint."""

    mock_assistant.generate.return_value = GenerateResponse(
        response="Hello from AI",
    )

    response = client.post(
        "/generate",
        json={
            "prompt": "Say hello",
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "response": "Hello from AI",
    }


@patch("copilot.api.routes.generate.assistant")
def test_generate_stream_endpoint(mock_assistant):
    """Test the streaming generate endpoint."""

    mock_assistant.stream_generate.return_value = iter(
        [
            "Hello ",
            "World",
        ]
    )

    response = client.post(
        "/generate/stream",
        json={
            "prompt": "Say hello",
        },
    )

    assert response.status_code == 200
    assert response.text == "Hello World"