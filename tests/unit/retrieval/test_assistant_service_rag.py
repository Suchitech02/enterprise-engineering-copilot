from unittest.mock import MagicMock

from copilot.services.assistant_service import AssistantService


def test_retrieve_and_generate() -> None:
    retriever = MagicMock()
    retriever.retrieve.return_value = [
        "Databricks supports Delta Live Tables.",
    ]

    service = AssistantService(
        retriever=retriever,
    )

    service.llm = MagicMock()
    service.llm.generate.return_value = "Generated response"

    response = service.retrieve_and_generate(
        question="What is Delta Live Tables?",
    )

    retriever.retrieve.assert_called_once_with(
        query="What is Delta Live Tables?",
    )

    service.llm.generate.assert_called_once()

    assert response.response == "Generated response"