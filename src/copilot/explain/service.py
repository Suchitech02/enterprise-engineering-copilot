import json

from copilot.explain.models import ExplainRequest, ExplainResponse
from copilot.explain.prompts import (
    SYSTEM_PROMPT,
    build_explain_prompt,
)
from copilot.llm.base import BaseLLMClient


class ExplainService:
    """Service for generating AI-powered code explanations."""

    def __init__(self, llm: BaseLLMClient):
        self.llm = llm

    def explain(
        self,
        request: ExplainRequest,
    ) -> ExplainResponse:
        prompt = build_explain_prompt(
            request.language,
            request.code,
        )

        response = self.llm.generate(
            system_prompt=SYSTEM_PROMPT,
            user_prompt=prompt,
        )

        try:
            parsed = json.loads(response)
        except json.JSONDecodeError as exc:
            raise ValueError("LLM returned invalid JSON") from exc

        return ExplainResponse.model_validate(parsed)
