from fastapi import APIRouter, Depends

from copilot.explain.models import ExplainRequest, ExplainResponse
from copilot.explain.service import ExplainService
from copilot.llm.factory import get_llm

router = APIRouter(prefix="/explain", tags=["AI Code Explanation"])


def get_explain_service() -> ExplainService:
    """Create ExplainService Instance."""
    llm = get_llm()
    return ExplainService(llm)


@router.post("", response_model=ExplainResponse)
def explain(
    request: ExplainRequest,
    service: ExplainService = Depends(get_explain_service),
) -> ExplainResponse:
    """Generate an AI Explanation for the supplied code."""
    return service.explain(request)
