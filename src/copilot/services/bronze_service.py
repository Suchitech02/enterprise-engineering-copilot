from copilot.models.bronze import BronzeGenerationRequest, BronzeGenerationResponse

class BronzeService:
    """Service responsible for Bronze AI orchestration."""

    def generate(self) -> BronzeGenerationResponse:
        """Generate Bronze Ingestion Pipelines."""
        return BronzeGenerationResponse(
            explanation="Bronze generator is working."
        )