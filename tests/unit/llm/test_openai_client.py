from unittest.mock import MagicMock, patch

from copilot.llm.openai_client import OpenAIClient


@patch("copilot.llm.openai_client.OpenAI")
def test_generate_returns_response(mock_openai):
    """Test that OpenAIClient returns the generated response."""

    message = MagicMock()
    message.content = "Hello from OpenAI"

    choice = MagicMock()
    choice.message = message

    response = MagicMock()
    response.choices = [choice]

    client = MagicMock()
    client.chat.completions.create.return_value = response

    mock_openai.return_value = client

    llm = OpenAIClient()

    result = llm.generate(
        system_prompt="You are a helpful assistant.",
        user_prompt="Say hello.",
    )

    assert result == "Hello from OpenAI"

    client.chat.completions.create.assert_called_once_with(
        model=llm.model,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": "Say hello.",
            },
        ],
    )
