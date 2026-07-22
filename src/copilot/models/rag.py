from pydantic import BaseModel


class RagRequest(BaseModel):
    """Request model for retrieval-augmented generation."""

    question: str