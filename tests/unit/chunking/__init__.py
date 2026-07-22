import pytest

from copilot.chunking.simple_chunker import SimpleChunker


def test_empty_document():
    """Test chunking an empty document."""

    chunker = SimpleChunker()

    chunks = chunker.chunk("")

    assert chunks == []


def test_single_chunk():
    """Test a document smaller than the chunk size."""

    chunker = SimpleChunker()

    chunks = chunker.chunk(
        document="Hello World",
        chunk_size=100,
        overlap=10,
    )

    assert chunks == ["Hello World"]


def test_multiple_chunks():
    """Test a document split into multiple overlapping chunks."""

    chunker = SimpleChunker()

    document = "A" * 1000

    chunks = chunker.chunk(
        document=document,
        chunk_size=500,
        overlap=50,
    )

    assert len(chunks) == 3
    assert chunks[0] == "A" * 500
    assert chunks[1] == "A" * 500
    assert chunks[2] == "A" * 100


def test_invalid_overlap():
    """Test invalid chunk size and overlap."""

    chunker = SimpleChunker()

    with pytest.raises(ValueError):
        chunker.chunk(
            document="Hello",
            chunk_size=100,
            overlap=100,
        )


def test_chunk_size_smaller_than_overlap():
    """Test overlap larger than chunk size."""

    chunker = SimpleChunker()

    with pytest.raises(ValueError):
        chunker.chunk(
            document="Hello",
            chunk_size=50,
            overlap=60,
        )