import json
from collections.abc import Iterator

import pytest

from copilot.llm.base import BaseLLMClient
from copilot.refactor.models import RefactorRequest
from copilot.refactor.service import RefactorService


class MockLLMClient(BaseLLMClient):
    """Mock LLM used for unit testing."""

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:
        return json.dumps(
            {
                "summary": "Improved readability",
                "refactored_code": ("def add(a: int, b: int) -> int:\n    return a + b"),
                "changes": [
                    "Added type hints",
                    "Applied PEP 8 formatting",
                ],
            }
        )
    
    def stream_generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> Iterator[str]:
        yield self.generate(system_prompt, user_prompt)


def test_refactor_service_returns_refactored_code():
    llm = MockLLMClient()
    service = RefactorService(llm)

    request = RefactorRequest(
        language="python",
        code="def add(a,b):return a+b",
    )

    response = service.refactor(request)

    assert response.summary == "Improved readability"

    assert response.refactored_code == "def add(a: int, b: int) -> int:\n    return a + b"

    assert response.changes == [
        "Added type hints",
        "Applied PEP 8 formatting",
    ]


class InvalidJsonLLM(BaseLLMClient):
    """Mock LLM that returns invalid JSON."""

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:
        return "this is not valid json"
    
    def stream_generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> Iterator[str]:
        yield self.generate(system_prompt, user_prompt)


def test_refactor_service_raises_for_invalid_json():
    service = RefactorService(InvalidJsonLLM())

    request = RefactorRequest(
        language="python",
        code="print('hello')",
    )

    with pytest.raises(ValueError):
        service.refactor(request)
