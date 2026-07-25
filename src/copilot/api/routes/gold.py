from fastapi import APIRouter

from copilot.models.gold import (
    GoldGenerationRequest,
    GoldGenerationResponse,
)
from copilot.services.gold_service import GoldService

router = APIRouter()

service = GoldService()


@router.post(
    "/gold",
    response_model=GoldGenerationResponse,
)
def generate_gold(
    request: GoldGenerationRequest,
) -> GoldGenerationResponse:
    """Generate a Gold pipeline."""

    return service.generate(request)
