from copilot.llm.factory import get_llm
from copilot.models.generate import GenerateResponse
from copilot.prompts.prompt_builder import PromptBuilder

llm = get_llm()


class AssistantService:
    """Service responsible for AI orchestration."""

    def generate(self, prompt: str) -> GenerateResponse:
        """Generate a mock AI response."""

        full_prompt = PromptBuilder.build_general_prompt(prompt)

        answer = llm.generate(full_prompt)

        return GenerateResponse(response=answer)
