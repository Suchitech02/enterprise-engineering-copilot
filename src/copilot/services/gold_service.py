from copilot.llm.base import BaseLLMClient
from copilot.llm.factory import get_llm
from copilot.models.gold import (
    GoldGenerationRequest,
    GoldGenerationResponse,
)
from copilot.parsers.gold_parser import GoldParser
from copilot.prompts.gold_prompt_builder import (
    GoldPromptBuilder,
)


class GoldService:
    """Service responsible for Gold AI orchestration."""

    SYSTEM_PROMPT = (
        "You are an expert Enterprise Data Engineer specializing in Databricks Gold pipelines."
    )

    def __init__(
        self,
        llm: BaseLLMClient | None = None,
    ) -> None:
        self.llm = llm or get_llm()

    def generate(
        self,
        request: GoldGenerationRequest,
    ) -> GoldGenerationResponse:
        """Generate a gold pipeline."""

        prompt = GoldPromptBuilder.build_prompt(
            silver_code=request.silver_code,
            business_requirements=request.business_requirements,
            target_table=request.target_table,
        )

        answer = self.llm.generate(
            system_prompt=self.SYSTEM_PROMPT,
            user_prompt=prompt,
        )

        return GoldParser.parse(answer)
