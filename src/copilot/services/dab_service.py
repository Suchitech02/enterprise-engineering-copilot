from copilot.llm.base import BaseLLMClient
from copilot.llm.factory import get_llm
from copilot.models.dab import (
    DABGenerationRequest,
    DABGenerationResponse,
)
from copilot.parsers.dab_parser import DABParser
from copilot.prompts.dab_prompt_builder import (
    DABPromptBuilder,
)


class DABService:
    """Service responsible for Databricks Asset Bundle generation."""

    SYSTEM_PROMPT = (
        "You are an expert Databricks Architect specializing in Databricks Asset Bundles."
    )

    def __init__(
        self,
        llm: BaseLLMClient | None = None,
    ) -> None:
        self.llm = llm or get_llm()

    def generate(
        self,
        request: DABGenerationRequest,
    ) -> DABGenerationResponse:
        """Generate a Databricks Asset Bundle."""

        prompt = DABPromptBuilder.build_prompt(
            project_name=request.project_name,
            catalog=request.catalog,
            schema_name=request.schema_name,
            bronze_pipeline=request.bronze_pipeline,
            silver_pipeline=request.silver_pipeline,
            gold_pipeline=request.gold_pipeline,
            environment=request.environment,
        )

        answer = self.llm.generate(
            system_prompt=self.SYSTEM_PROMPT,
            user_prompt=prompt,
        )

        return DABParser.parse(answer)
