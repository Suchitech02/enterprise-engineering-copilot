from typing import Any

from pydantic import BaseModel

class BronzeGenerationRequest(BaseModel):
    """Request model for Bronze AI generation."""
    api_name: str
    endpoint: str
    authentication: str
    description: str
    sample_response: dict[str, Any]


class BronzeGenerationResponse(BaseModel):
    """Response model for Bronze AI generation."""
    summary: str
    python_code: str
    sql_code: str
    folder_structure: str
    quality_rules: str
    assumptions: str
