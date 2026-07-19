from abc import ABC, abstractmethod


class BaseRetriever(ABC):
    """Abstract base class for document retrieval."""

    @abstractmethod
    def retrieve(
        self,
        query: str,
        limit: int = 5,
    ) -> list[str]:
        """Retrieve relevant documents."""
        raise NotImplementedError