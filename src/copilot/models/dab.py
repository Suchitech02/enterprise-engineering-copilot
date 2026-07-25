from pydantic import BaseModel


class DABGenerationRequest(BaseModel):
    """Request model for Databricks Asset Bundle generation."""

    project_name: str
    catalog: str
    schema_name: str
    bronze_pipeline: str
    silver_pipeline: str
    gold_pipeline: str
    environment: str


class DABGenerationResponse(BaseModel):
    """Response model for Databricks Asset Bundle generation."""

    summary: str
    databricks_yml: str
    jobs_yml: str
    pipelines_yml: str
    variables_yml: str
    targets_yml: str
    folder_structure: str
    assumptions: list[str]
