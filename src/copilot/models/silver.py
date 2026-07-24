from pydantic import BaseModel


class SilverGenerationRequest(BaseModel):
    """Request model for silver pipeline generation."""

    bronze_code: str
    business_rule: str
    target_table: str


class SilverGenerationResponse(BaseModel):
    """Response model for silver pipeline generation."""

    summary: str
    python_code: str
    sql_code: str
    transformations: list[str]
    quality_rules: list[str]
    assumptions: list[str]
