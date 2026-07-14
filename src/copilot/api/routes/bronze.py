from fastapi import APIRouter

from copilot.models.bronze import (
    BronzeGenerationRequest,
    BronzeGenerationResponse
)
from copilot.services.bronze_service import BronzeService

router = APIRouter(tags=["Bronze"])

service = BronzeService()

@router.post(
    "/bronze/generate",
    response_model=BronzeGenerationResponse,
)
def generate_bronze(
    request: BronzeGenerationRequest,
) -> BronzeGenerationResponse:
    """Generate Bronze Ingestion Pipelines."""
    return service.generate()