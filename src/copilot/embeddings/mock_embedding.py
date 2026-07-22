from copilot.embeddings.base import BaseEmbeddingModel


class MockEmbeddingModel(BaseEmbeddingModel):
    """Mock embedding model for testing."""

    VECTOR_SIZE = 10

    def embed(
        self,
        text: str,
    ) -> list[float]:
        """
        Generate a deterministic embedding.

        Args:
            text: Input text.

        Returns:
            A deterministic embedding vector.
        """
        value = float(len(text))

        return [
            value
            for _ in range(self.VECTOR_SIZE)
        ]