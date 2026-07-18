from fastapi import APIRouter, Depends

from copilot.llm.factory import get_llm
from copilot.refactor.models import (
    RefactorRequest,
    RefactorResponse,
)
from copilot.refactor.service import RefactorService

router = APIRouter(
    prefix="/refactor",
    tags=["AI Code Refactoring"],
)


def get_refactor_service() -> RefactorService:
    """Create a RefactorService instance."""
    llm = get_llm()
    return RefactorService(llm)


@router.post("", response_model=RefactorResponse)
def refactor(
    request: RefactorRequest,
    service: RefactorService = Depends(get_refactor_service),
) -> RefactorResponse:
    """Generate an AI-powered code refactoring."""
    return service.refactor(request)
