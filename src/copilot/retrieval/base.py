from abc import ABC, abstractmethod

from copilot.models.document import Document


class BaseRetriever(ABC):
    """Abstract base class for document retrieval."""

    @abstractmethod
    def retrieve(
        self,
        query: str,
        limit: int = 5,
    ) -> list[Document]:
        """Retrieve relevant documents."""
        raise NotImplementedError
