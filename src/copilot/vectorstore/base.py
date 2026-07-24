from abc import ABC, abstractmethod

from copilot.models.document import Document


class BaseVectorStore(ABC):
    """Abstract vector store."""

    @abstractmethod
    def add(
        self,
        document: Document,
        embedding: list[float],
    ) -> None: ...

    @abstractmethod
    def search(
        self,
        embedding: list[float],
        limit: int = 5,
    ) -> list[Document]: ...
