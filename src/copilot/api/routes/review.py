from fastapi import APIRouter, Depends

from copilot.llm.factory import get_llm
from copilot.review.models import ReviewRequest, ReviewResponse
from copilot.review.service import ReviewService

router = APIRouter(prefix="/review", tags=["AI Code Review"])


def get_review_service() -> ReviewService:

    llm = get_llm()
    return ReviewService(llm)

@router.post("", response_model=ReviewResponse)
def review(
    request: ReviewRequest,
    service: ReviewService = Depends(get_review_service),
):
    return service.review(request)