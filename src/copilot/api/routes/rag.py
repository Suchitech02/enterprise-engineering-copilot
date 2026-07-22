from fastapi import APIRouter

from copilot.models.generate import GenerateResponse
from copilot.models.rag import RagRequest
from copilot.services.assistant_service import AssistantService

router = APIRouter()

assistant = AssistantService()


@router.post(
    "/rag",
    response_model = GenerateResponse,
)
def rag(
    request: RagRequest,
) -> GenerateResponse:
    """Generate a response using retrieval-augmented generation."""

    return assistant.retrieve_and_generate(
        question=request.question,
    )