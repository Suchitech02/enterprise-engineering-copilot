from abc import ABC, abstractmethod


class BaseEmbeddingModel(ABC):
    """Abstract base class for embedding models."""

    @abstractmethod
    def embed(
        self,
        text: str,
    ) -> list[float]:
        """
        Generate an embedding for a text.

        Args:
            text: Input text.

        Returns:
            Vector representation of the text.
        """