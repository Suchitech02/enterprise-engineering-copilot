from unittest.mock import MagicMock, patch

from copilot.llm.ollama_client import OllamaClient


@patch("copilot.llm.ollama_client.Client")
def test_generate_returns_response(mock_client):
    """Test that OllamaClient returns the generated response."""

    client = MagicMock()

    client.chat.return_value = {
        "message": {
            "content": "Hello from Ollama",
        }
    }

    mock_client.return_value = client

    llm = OllamaClient()

    result = llm.generate(
        system_prompt="You are helpful.",
        user_prompt="Say hello.",
    )

    assert result == "Hello from Ollama"

    client.chat.assert_called_once_with(
        model=llm.model,
        messages=[
            {
                "role": "system",
                "content": "You are helpful.",
            },
            {
                "role": "user",
                "content": "Say hello.",
            },
        ],
    )


@patch("copilot.llm.ollama_client.Client")
def test_stream_generate(mock_client):
    """Test that OllamaClient streams the generated response."""
    client = MagicMock()

    client.chat.return_value = [
        {"message": {"content": "Hello "}},
        {"message": {"content": ""}},
        {"message": {"content": "World"}},
    ]

    mock_client.return_value = client

    llm = OllamaClient()

    result = list(
        llm.stream_generate(
            "system",
            "user",
        )
    )

    assert result == [
        "Hello ",
        "World",
    ]

    client.chat.assert_called_once_with(
        model=llm.model,
        messages=[
            {
                "role": "system",
                "content": "system",
            },
            {
                "role": "user",
                "content": "user",
            },
        ],
        stream=True,
    )