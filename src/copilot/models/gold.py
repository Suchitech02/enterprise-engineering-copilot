from pydantic import BaseModel


class GoldGenerationRequest(BaseModel):
    """Request model for Gold pipeline generation."""

    silver_code: str
    business_requirements: str
    target_table: str


class GoldGenerationResponse(BaseModel):
    """Response model for Gold pipeline generation."""

    summary: str
    python_code: str
    sql_code: str
    kpis: list[str]
    aggregations: list[str]
    assumptions: list[str]
