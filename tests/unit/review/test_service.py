import json

import pytest

from collections.abc import Iterator

from copilot.llm.base import BaseLLMClient
from copilot.review.models import ReviewRequest
from copilot.review.service import ReviewService


class MockLLMClient(BaseLLMClient):
    """Mock LLM used for unit testing."""

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:
        return json.dumps(
            {
                "summary": "Mock review summary",
                "findings": [
                    {
                        "severity": "low",
                        "category": "Readability",
                        "title": "Spacing",
                        "explanation": "Function parameters should be spaced.",
                        "recommendation": "Follow PEP 8 formatting.",
                    }
                ],
            }
        )
    
    def stream_generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> Iterator[str]:
        yield self.generate(system_prompt, user_prompt)


def test_review_service_returns_review_response():
    llm = MockLLMClient()
    service = ReviewService(llm)

    request = ReviewRequest(
        language="python",
        code="def add(a,b): return a+b",
    )

    response = service.review(request)

    assert response.summary == "Mock review summary"
    assert len(response.findings) == 1

    finding = response.findings[0]

    assert finding.severity.value == "low"
    assert finding.category == "Readability"
    assert finding.title == "Spacing"


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


def test_review_service_raises_for_invalid_json():
    service = ReviewService(InvalidJsonLLM())

    request = ReviewRequest(
        language="python",
        code="print('hello')",
    )

    with pytest.raises(ValueError):
        service.review(request)
