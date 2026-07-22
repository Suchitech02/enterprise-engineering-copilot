from pathlib import Path


class DocumentLoader:
    """Loads knowledge base documents."""

    SUPPORTED_EXTENSIONS = {
        ".md",
        ".txt",
    }

    def load_documents(
        self,
        directory: Path,
    ) -> list[str]:
        """
        Load all supported documents from a directory.
        
        Args:
            directory: Directory containing knowledge base documents.

        Returns:
            A list containing the contents of each document.
        """
        documents: list[str] = []

        if not directory.exists():
            return documents

        for file_path in sorted(directory.iterdir()):
            if (
                file_path.is_file()
                and file_path.suffix.lower()
                in self.SUPPORTED_EXTENSIONS
            ):
                documents.append(
                    file_path.read_text(
                        encoding="utf-8",
                    )
                )

        return documents
