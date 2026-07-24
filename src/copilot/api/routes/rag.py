from fastapi import APIRouter

from copilot.models.generate import GenerateResponse
from copilot.models.rag import RagRequest, RagResponse
from copilot.services.assistant_service import AssistantService

router = APIRouter()

assistant = AssistantService()


@router.post(
    "/rag",
    response_model=RagResponse,
)
def rag(
    request: RagRequest,
) -> RagResponse:
    """Generate a response using retrieval-augmented generation."""

    return assistant.retrieve_and_generate(
        question=request.question,
    )
