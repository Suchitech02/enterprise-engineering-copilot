from copilot.llm.factory import get_llm
from copilot.models.bronze import BronzeGenerationRequest, BronzeGenerationResponse
from copilot.prompts.prompt_builder import PromptBuilder

class BronzeService:
    """Service responsible for Bronze AI orchestration."""

    def __init__(self) -> None:
        self.llm = get_llm()

    def generate(
        self,
        request: BronzeGenerationRequest,
    ) -> BronzeGenerationResponse:
        """Generate Bronze Ingestion Pipelines."""

        prompt = PromptBuilder.build_bronze_prompt(
            api_name=request.api_name,
            endpoint=request.endpoint,
            authentication=request.authentication,
            description=request.description,
            sample_response=request.sample_response
        )

        answer = self.llm.generate(prompt)

        return BronzeGenerationResponse(
            summary=f"Bronze pipeline generated for {request.api_name}",
            python_code=answer,
            sql_code="",
            folder_structure="",
            quality_rules="",
            assumptions=""
        )