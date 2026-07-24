from dataclasses import dataclass, field


@dataclass(slots=True)
class Document:
    """Represents an indexed document."""

    text: str

    metadata: dict[str, str] = field(
        default_factory=dict,
    )
