from pydantic import BaseModel


class RefactorRequest(BaseModel):
    language: str
    code: str


class RefactorResponse(BaseModel):
    summary: str
    refactored_code: str
    changes: list[str]
