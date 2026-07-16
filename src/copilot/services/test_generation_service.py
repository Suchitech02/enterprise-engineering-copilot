from copilot.llm.base import BaseLLMClient
from copilot.llm.factory import get_llm
from copilot.prompts.test_prompt_builder import TestPromptBuilder


class UnitTestGenerationService:
    """Service responsible for AI-generated pytest tests."""

    def __init__(
        self,
        llm: BaseLLMClient | None = None,
    ) -> None:
        self.llm = llm or get_llm()

    def generate(
        self,
        python_code: str,
    ) -> str:
        """Generate pytest tests for the supplied Python pipeline."""

        prompt = TestPromptBuilder.build_test_prompt(
            python_code,
        )

        return self.llm.generate(prompt)