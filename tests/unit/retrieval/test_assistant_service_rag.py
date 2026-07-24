from unittest.mock import MagicMock

from copilot.models.document import Document
from copilot.services.assistant_service import AssistantService


def test_retrieve_and_generate() -> None:
    retriever = MagicMock()
    retriever.retrieve.return_value = [
        Document(
            text="Databricks supports Delta Live Tables.",
            metadata={
                "source": "databricks.md",
            },
        ),
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

    assert len(response.sources) == 1
    assert response.sources[0].source == "databricks.md"
