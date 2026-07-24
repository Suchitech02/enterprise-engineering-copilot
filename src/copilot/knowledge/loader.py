from pathlib import Path

from copilot.models.document import Document


class DocumentLoader:
    """Loads knowledge base documents."""

    SUPPORTED_EXTENSIONS = {
        ".md",
        ".txt",
    }

    def load_documents(
        self,
        directory: Path,
    ) -> list[Document]:
        """
        Load all supported documents from a directory.

        Args:
            directory: Directory containing knowledge base documents.

        Returns:
            A list of loaded documents with metadata.
        """
        documents: list[Document] = []

        if not directory.exists():
            return documents

        for file_path in sorted(directory.iterdir()):
            if file_path.is_file() and file_path.suffix.lower() in self.SUPPORTED_EXTENSIONS:
                documents.append(
                    Document(
                        text=file_path.read_text(
                            encoding="utf-8",
                        ),
                        metadata={
                            "source": file_path.name,
                        },
                    )
                )

        return documents
