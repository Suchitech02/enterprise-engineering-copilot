import json

from copilot.document.models import (
    DocumentRequest,
    DocumentResponse,
)
from copilot.document.prompts import (
    SYSTEM_PROMPT,
    build_document_prompt,
)
from copilot.llm.base import BaseLLMClient


class DocumentService:
    """Service for generating AI-powered code documentation."""

    def __init__(self, llm: BaseLLMClient):
        self.llm = llm

    def document(
        self,
        request: DocumentRequest,
    ) -> DocumentResponse:
        """Generate documentation for the supplied source code."""

        prompt = build_document_prompt(
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

        return DocumentResponse.model_validate(parsed)
