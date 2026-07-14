from pydantic import BaseModel

class GenerateRequest(BaseModel):
    """Request model for AI generation."""

    prompt: str

class GenerateResponse(BaseModel):
    """Response model for AI generation."""

    response: str