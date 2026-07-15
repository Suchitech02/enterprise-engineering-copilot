from copilot.llm.factory import get_llm
from copilot.models.bronze import BronzeGenerationRequest, BronzeGenerationResponse
from copilot.prompts.prompt_builder import PromptBuilder

class BronzeService:
    """Service responsible for Bronze AI orchestration."""

    def __init__(self):
        self.llm = get_llm()

    def generate(
        self,
        request: BronzeGenerationRequest,
    ) -> BronzeGenerationResponse:
        """Generate Bronze Ingestion Pipelines."""

        print("========== Bronze Generator ==========")

        print("Step 1 - Building prompt")

        prompt = PromptBuilder.build_bronze_prompt(
            api_name=request.api_name,
            endpoint=request.endpoint,
            authentication=request.authentication,
            description=request.description,
            sample_response=request.sample_response
        )

        print("✅ Step 2 - Prompt built")
        print(f"Prompt length: {len(prompt)} characters")

        print("Step 3 - Calling Ollama...")

        answer = self.llm.generate(prompt)

        print("✅ Step 4 - Ollama returned")
        print(f"Response length: {len(answer)}")

        return BronzeGenerationResponse(
            explanation=answer
        )