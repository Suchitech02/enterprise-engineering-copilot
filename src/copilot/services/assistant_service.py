from collections.abc import Iterator

from copilot.llm.factory import get_llm
from copilot.models.generate import GenerateResponse
from copilot.prompts.prompt_builder import PromptBuilder


class AssistantService:
    """Service responsible for AI orchestration."""

    SYSTEM_PROMPT = "You are a helpful AI assistant."

    def __init__(self) -> None:
        self.llm = get_llm()

    def generate(
        self,
        prompt: str,
    ) -> GenerateResponse:
        """Generate an AI response."""

        full_prompt = PromptBuilder.build_general_prompt(prompt)

        answer = self.llm.generate(
            system_prompt=self.SYSTEM_PROMPT,
            user_prompt=full_prompt,
        )

        return GenerateResponse(response=answer)

    def stream_generate(
        self,
        prompt: str,
    ) -> Iterator[str]:
        """Generate a streamed AI response."""

        full_prompt = PromptBuilder.build_general_prompt(prompt)

        yield from self.llm.stream_generate(
            system_prompt=self.SYSTEM_PROMPT,
            user_prompt=full_prompt,
        )