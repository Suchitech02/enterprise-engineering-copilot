from abc import ABC, abstractmethod


class BaseVectorStore(ABC):
    """Abstract vector store."""

    @abstractmethod
    def add(
        self,
        text: str,
        embedding: list[float],
    ) -> None:
        ...

    @abstractmethod
    def search(
        self,
        embedding: list[float],
        limit: int = 5,
    ) -> list[str]:
        ...