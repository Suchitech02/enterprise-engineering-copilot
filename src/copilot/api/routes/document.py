from fastapi import APIRouter, Depends

from copilot.document.models import (
    DocumentRequest,
    DocumentResponse,
)
from copilot.document.service import DocumentService
from copilot.llm.factory import get_llm

router = APIRouter(prefix="/document", tags=["AI Code Documentations"])


def get_document_service() -> DocumentService:
    """Create a Document Service Instance"""
    llm = get_llm()
    return DocumentService(llm)


@router.post("", response_model=DocumentResponse)
def document(
    request: DocumentRequest,
    service: DocumentService = Depends(get_document_service),
) -> DocumentResponse:
    "Generate AI-powered documentation for the supplied code."
    return service.document(request)
