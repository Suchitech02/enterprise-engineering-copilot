import json

import pytest

from copilot.document.models import DocumentRequest
from copilot.document.service import DocumentService
from copilot.llm.base import BaseLLMClient


class MockLLMClient(BaseLLMClient):
    """Mock LLM used for unit testing."""

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:
        return json.dumps(
            {
                "summary": "Added documentation",
                "documented_code": (
                    "def add(a: int, b: int) -> int:\n"
                    '    """Return the sum of two integers."""\n'
                    "    return a + b"
                ),
                "changes": [
                    "Added function docstring",
                    "Added type hints",
                ],
            }
        )


def test_document_service_returns_documented_code():
    llm = MockLLMClient()
    service = DocumentService(llm)

    request = DocumentRequest(
        language="python",
        code="def add(a,b): return a+b",
    )

    response = service.document(request)

    assert response.summary == "Added documentation"

    assert '"""Return the sum of two integers."""' in response.documented_code

    assert response.changes == [
        "Added function docstring",
        "Added type hints",
    ]


class InvalidJsonLLM(BaseLLMClient):
    """Mock LLM that returns invalid JSON."""

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:
        return "invalid json"


def test_document_service_raises_for_invalid_json():
    service = DocumentService(InvalidJsonLLM())

    request = DocumentRequest(
        language="python",
        code="print('hello')",
    )

    with pytest.raises(ValueError):
        service.document(request)
