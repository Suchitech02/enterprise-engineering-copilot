from copilot.models.generate import GenerateResponse


class AssistantService:
    """Service responsible for AI orchestration."""

    def generate(self, prompt: str) -> GenerateResponse:
        """Generate a mock AI response."""

        return GenerateResponse(
            response=f"Mock response for prompt: {prompt}"
        )