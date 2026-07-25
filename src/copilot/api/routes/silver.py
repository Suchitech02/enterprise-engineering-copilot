from fastapi import APIRouter

from copilot.models.silver import (
    SilverGenerationRequest,
    SilverGenerationResponse,
)
from copilot.services.silver_service import SilverService

router = APIRouter()

service = SilverService()


@router.post(
    "/silver",
    response_model=SilverGenerationResponse,
)
def generate_silver(request: SilverGenerationRequest) -> SilverGenerationResponse:
    """Generate a silver pipeline."""

    return service.generate(request)
