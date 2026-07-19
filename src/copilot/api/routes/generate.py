from fastapi import APIRouter
from fastapi.responses import StreamingResponse

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


@router.post("/generate/stream")
def generate_stream(
    request: GenerateRequest,
) -> StreamingResponse:
    """Generate streaming AI response."""

    return StreamingResponse(
        assistant.stream_generate(request.prompt),
        media_type="text/plain",
    )
