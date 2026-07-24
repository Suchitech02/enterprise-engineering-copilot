from abc import ABC, abstractmethod

from copilot.models.document import Document
from copilot.vectorstore.base import BaseVectorStore


class BaseIndexBuilder(ABC):
    """Abstract base class for index builders."""

    @abstractmethod
    def build(
        self,
        documents: list[Document],
        vector_store: BaseVectorStore,
    ) -> None:
        """Build an index from documents."""
        ...
