from dataclasses import dataclass, field

from pydantic import BaseModel


@dataclass(slots=True)
class Source:
    source: str


class RagRequest(BaseModel):
    """Request model for retrieval-augmented generation."""

    question: str


@dataclass(slots=True)
class RagResponse:
    response: str
    sources: list[Source] = field(default_factory=list)
