from copilot.llm.base import BaseLLMClient
from copilot.llm.factory import get_llm
from copilot.models.bronze import BronzeGenerationRequest, BronzeGenerationResponse
from copilot.prompts.prompt_builder import PromptBuilder
from copilot.parsers.bronze_parser import BronzeParser


class BronzeService:
    """Service responsible for Bronze AI orchestration."""

    def __init__(self, llm: BaseLLMClient | None = None) -> None:
        if llm is None:
            llm = get_llm()

        self.llm = llm

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

        return BronzeParser.parse(answer)