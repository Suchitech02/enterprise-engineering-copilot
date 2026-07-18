from enum import Enum

from pydantic import BaseModel

class Severity(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class ReviewFinding(BaseModel):
    severity: Severity
    category: str
    title: str
    explanation: str
    recommendation: str


class ReviewRequest(BaseModel):
    language: str
    code: str


class ReviewResponse(BaseModel):
    summary: str
    findings: list[ReviewFinding]
