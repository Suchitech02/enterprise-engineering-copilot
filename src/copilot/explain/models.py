from pydantic import BaseModel


class ExplainRequest(BaseModel):
    language: str
    code: str


class ExplainResponse(BaseModel):
    summary: str
    explanation: str
