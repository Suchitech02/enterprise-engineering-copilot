import math

from copilot.models.document import Document
from copilot.vectorstore.base import BaseVectorStore


class InMemoryVectorStore(BaseVectorStore):
    """Simple in-memory vector store."""

    def __init__(self) -> None:
        self._vectors: list[tuple[list[float], Document]] = []

    def add(
        self,
        document: Document,
        embedding: list[float],
    ) -> None:
        self._vectors.append(
            (
                embedding,
                document,
            )
        )

    @staticmethod
    def _cosine_similarity(
        vector1: list[float],
        vector2: list[float],
    ) -> float:
        """Compute cosine similarity."""

        dot_product = sum(
            a * b
            for a, b in zip(
                vector1,
                vector2,
            )
        )

        magnitude1 = math.sqrt(sum(a * a for a in vector1))

        magnitude2 = math.sqrt(sum(b * b for b in vector2))

        if magnitude1 == 0 or magnitude2 == 0:
            return 0.0

        return dot_product / (magnitude1 * magnitude2)

    def search(
        self,
        embedding: list[float],
        limit: int = 5,
    ) -> list[Document]:
        """Return the most similar documents by cosine similarity."""

        scored_documents: list[tuple[float, Document]] = []

        for stored_embedding, document in self._vectors:
            score = self._cosine_similarity(
                embedding,
                stored_embedding,
            )

            scored_documents.append(
                (
                    score,
                    document,
                )
            )

        scored_documents.sort(
            key=lambda item: item[0],
            reverse=True,
        )

        return [document for _, document in scored_documents[:limit]]
