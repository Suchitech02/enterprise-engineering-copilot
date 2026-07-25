from fastapi import APIRouter

from copilot.models.dab import (
    DABGenerationRequest,
    DABGenerationResponse,
)
from copilot.services.dab_service import DABService

router = APIRouter()

service = DABService()


@router.post(
    "/dab",
    response_model=DABGenerationResponse,
)
def generate_dab(
    request: DABGenerationRequest,
) -> DABGenerationResponse:
    """Generate a Databricks Asset Bundle."""

    return service.generate(request)
