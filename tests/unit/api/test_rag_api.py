from unittest.mock import patch

from fastapi.testclient import TestClient

from copilot.main import app
from copilot.models.rag import RagResponse, Source

client = TestClient(app)


@patch("copilot.api.routes.rag.assistant")
def test_rag_endpoint(mock_assistant):
    """Test the RAG endpoint."""

    mock_assistant.retrieve_and_generate.return_value = RagResponse(
        response="Generated response",
        sources=[
            Source(source="databricks.md"),
        ],
    )

    response = client.post(
        "/rag",
        json={
            "question": "What is Delta Lake?",
        },
    )

    assert response.status_code == 200

    assert response.json() == {
        "response": "Generated response",
        "sources": [
            {
                "source": "databricks.md",
            }
        ],
    }
