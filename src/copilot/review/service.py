import json

from copilot.llm.base import BaseLLMClient

from .models import ReviewRequest, ReviewResponse
from .prompts import SYSTEM_PROMPT, build_review_prompt


class ReviewService:
    """Coordinates AI-powered code reviews."""

    def __init__(self, llm: BaseLLMClient):
        self.llm = llm
  
    def review(
            self,
            request: ReviewRequest,
    ) -> ReviewResponse:
        """Review a source code snippet using the configured LLM."""
        
        prompt = build_review_prompt(
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

        return ReviewResponse.model_validate(parsed)
        