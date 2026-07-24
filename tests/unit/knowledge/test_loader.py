from pathlib import Path

from copilot.knowledge.loader import DocumentLoader


def test_load_markdown_document(tmp_path: Path):
    """Test loading a markdown document."""

    file = tmp_path / "doc.md"
    file.write_text("# Databricks", encoding="utf-8")

    loader = DocumentLoader()

    documents = loader.load_documents(tmp_path)

    assert len(documents) == 1

    assert documents[0].text == "# Databricks"

    assert documents[0].metadata == {
        "source": "doc.md",
    }


def test_load_text_document(tmp_path: Path):
    """Test loading a text document."""

    file = tmp_path / "notes.txt"
    file.write_text("Unity Catalog", encoding="utf-8")

    loader = DocumentLoader()

    documents = loader.load_documents(tmp_path)

    assert len(documents) == 1

    assert documents[0].text == "Unity Catalog"

    assert documents[0].metadata == {
        "source": "notes.txt",
    }


def test_ignore_unsupported_files(tmp_path: Path):
    """Test unsupported file types are ignored."""

    file = tmp_path / "image.png"
    file.write_text("not an image", encoding="utf-8")

    loader = DocumentLoader()

    documents = loader.load_documents(tmp_path)

    assert documents == []


def test_missing_directory_returns_empty_list():
    """Test missing directory returns an empty list."""

    loader = DocumentLoader()

    documents = loader.load_documents(
        Path("directory-that-does-not-exist"),
    )

    assert documents == []
