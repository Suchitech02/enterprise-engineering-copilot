from fastapi import APIRouter

from copilot.models.generate import GenerateRequest, GenerateResponse
from copilot.services.assistant_service import AssistantService

router = APIRouter()

assistant = AssistantService()


@router.post(
    "/generate",
    response_model=GenerateResponse,
)
def generate(
    request: GenerateRequest,
) -> GenerateResponse:
    """Generate AI response."""

    return assistant.generate(request.prompt)
