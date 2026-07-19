from fastapi import APIRouter

from copilot.models.chat import ChatRequest, ChatResponse
from copilot.services.assistant_service import AssistantService

router = APIRouter()

assistant = AssistantService()


@router.post(
    "/chat",
    response_model=ChatResponse,
)
def chat(
    request: ChatRequest,
) -> ChatResponse:
    """Generate a conversational AI response."""

    return assistant.chat(
        conversation_id=request.conversation_id,
        message=request.message,
    )