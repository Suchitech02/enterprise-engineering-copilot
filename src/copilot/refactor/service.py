import json

from copilot.llm.base import BaseLLMClient
from copilot.refactor.models import (
    RefactorRequest,
    RefactorResponse,
)
from copilot.refactor.prompts import (
    SYSTEM_PROMPT,
    build_refactor_prompt,
)


class RefactorService:
    """Service for generating AI-powered code refactoring."""

    def __init__(self, llm: BaseLLMClient):
        self.llm = llm

    def refactor(
        self,
        request: RefactorRequest,
    ) -> RefactorResponse:
        """Refactor the supplied source code."""

        prompt = build_refactor_prompt(
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

        return RefactorResponse.model_validate(parsed)
