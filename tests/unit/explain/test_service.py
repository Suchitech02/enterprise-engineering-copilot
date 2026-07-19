import json
from collections.abc import Iterator

import pytest

from copilot.explain.models import ExplainRequest
from copilot.explain.service import ExplainService
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
                "summary": "Adds two numbers",
                "explanation": ("This function accepts two parameters and returns their sum."),
            }
        )
    
    def stream_generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> Iterator[str]:
        yield self.generate(system_prompt, user_prompt)


def test_explain_service_returns_explanation():
    llm = MockLLMClient()
    service = ExplainService(llm)

    request = ExplainRequest(
        language="python",
        code="def add(a, b): return a + b",
    )

    response = service.explain(request)

    assert response.summary == "Adds two numbers"
    assert response.explanation == "This function accepts two parameters and returns their sum."


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


def test_explain_service_raises_for_invalid_json():
    service = ExplainService(InvalidJsonLLM())

    request = ExplainRequest(
        language="python",
        code="print('hello')",
    )

    with pytest.raises(ValueError):
        service.explain(request)
