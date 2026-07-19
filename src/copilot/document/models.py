from pydantic import BaseModel


class DocumentRequest(BaseModel):
    language: str
    code: str


class DocumentResponse(BaseModel):
    summary: str
    documented_code: str
    changes: list[str]
