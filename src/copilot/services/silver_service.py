from copilot.llm.base import BaseLLMClient
from copilot.llm.factory import get_llm
from copilot.models.silver import SilverGenerationRequest, SilverGenerationResponse
from copilot.parsers.silver_parser import SilverParser
from copilot.prompts.silver_prompt_builder import SilverPromptBuilder


class SilverService:
    """Service responsible for Silver pipeline generation."""

    SYSTEM_PROMPT = (
        "You are an expert Databricks Data Engineer specializing in "
        "production-ready Silver layer pipelines."
    )

    def __init__(
        self,
        llm: BaseLLMClient | None = None,
    ) -> None:
        self.llm = llm or get_llm()

    def generate(
        self,
        request: SilverGenerationRequest,
    ) -> SilverGenerationResponse:
        """Generate a silver pipeline."""

        prompt = SilverPromptBuilder.build_prompt(
            bronze_code=request.bronze_code,
            business_rules=request.business_rule,
            target_table=request.target_table,
        )

        answer = self.llm.generate(
            system_prompt=self.SYSTEM_PROMPT,
            user_prompt=prompt,
        )

        return SilverParser.parse(answer)
