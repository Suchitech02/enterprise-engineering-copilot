from copilot.chunking.base import BaseChunker


class SimpleChunker(BaseChunker):
    """Simple character based chunker."""

    def chunk(
        self,
        document: str,
        chunk_size: int = 500,
        overlap: int = 50,
    ) -> list[str]:
        """
        Split a document into overlapping chunks.

        Args:
            document: The document to split.
            chunk_size: Maximum size of each chunk.
            overlap: Number of overlapping characters between chunks.

        Returns:
            A list of document chunks.
        """
        if not document:
            return []
        
        if chunk_size <= overlap:
            raise ValueError(
                "Chunk Size must be greater than overlap."
            )
        
        chunks: list[str] = []

        step = chunk_size - overlap

        for start in range(0, len(document), step):
            chunk = document[start: start + chunk_size]

            if chunk:
                chunks.append(chunk)

        return chunks