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
    

@patch("copilot.llm.openai_client.OpenAI")
def test_stream_generate(mock_openai):
    """Test that OpenAIClient streams the generated response."""

    def mock_stream():
        chunk1 = MagicMock()
        chunk1.choices = [
            MagicMock(
                delta=MagicMock(content="Hello ")
            )
        ]

        chunk2 = MagicMock()
        chunk2.choices = [
            MagicMock(
                delta=MagicMock(content=None)
            )
        ]

        chunk3 = MagicMock()
        chunk3.choices = [
            MagicMock(
                delta=MagicMock(content="World")
            )
        ]

        yield chunk1
        yield chunk2
        yield chunk3

    client = MagicMock()
    client.chat.completions.create.return_value = mock_stream()

    mock_openai.return_value = client

    llm = OpenAIClient()

    result = list(
        llm.stream_generate(
            system_prompt="system",
            user_prompt="user",
        )
    )

    assert result == [
        "Hello ",
        "World",
    ]

    client.chat.completions.create.assert_called_once_with(
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
