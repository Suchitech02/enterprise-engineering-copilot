from abc import ABC, abstractmethod


class BaseChunker(ABC):
    """Abstract base class for document chunking"""

    @abstractmethod
    def chunk(
        self,
        document: str,
        chunk_size: int = 500,
        overlap: int = 50,
    ) -> list[str]:
        """Split a document into chunks.
        Args:
            document: The document to split.
            chunk_size: Maximum size of each chunk.
            overlap: Number of overlapping characters between chunks.

        Returns:
            A list of document chunks.
        """
       

