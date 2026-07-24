from copilot.models.document import Document
from copilot.prompts.prompt_builder import PromptBuilder


def test_build_general_prompt():
    """Test general prompt generation."""

    prompt = PromptBuilder.build_general_prompt(
        "Explain Delta Lake",
    )

    assert "Explain Delta Lake" in prompt
    assert "Enterprise Engineering Copilot" in prompt


def test_build_chat_prompt():
    """Test chat prompt generation."""

    prompt = PromptBuilder.build_chat_prompt(
        [
            {
                "role": "user",
                "content": "Hello",
            },
            {
                "role": "assistant",
                "content": "Hi!",
            },
        ]
    )

    assert "user: Hello" in prompt
    assert "assistant: Hi!" in prompt


def test_build_rag_prompt():
    """Test RAG prompt generation."""

    prompt = PromptBuilder.build_rag_prompt(
        question="What is Databricks?",
        documents=[
            Document(
                text="Databricks is a unified analytics platform.",
            ),
            Document(
                text="Apache Spark is a distributed processing engine.",
            ),
        ],
    )

    assert "What is Databricks?" in prompt
    assert "Databricks is a unified analytics platform." in prompt
    assert "Apache Spark is a distributed processing engine." in prompt


def test_build_bronze_prompt():
    """Test bronze prompt generation."""

    prompt = PromptBuilder.build_bronze_prompt(
        api_name="ABC API",
        endpoint="/waste",
        authentication="Bearer Token",
        description="Waste API",
        sample_response={"id": 1},
    )

    assert "ABC API" in prompt
    assert "/waste" in prompt
    assert "Bearer Token" in prompt
    assert "Waste API" in prompt