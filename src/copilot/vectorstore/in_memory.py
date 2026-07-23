from copilot.vectorstore.base import BaseVectorStore


class InMemoryVectorStore(BaseVectorStore):
    """Simple in-memory vector store."""

    def __init__(self) -> None:
        self._vectors: list[
            tuple[list[float], str]
        ] = []

    def add(
        self,
        text: str,
        embedding: list[float],
    ) -> None:
        self._vectors.append(
            (
                embedding,
                text,
            )
        )

    def search(
        self,
        embedding: list[float],
        limit: int = 5,
    ) -> list[str]:
        return [
            text
            for _, text in self._vectors[:limit]
        ]