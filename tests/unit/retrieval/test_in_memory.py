from copilot.retrieval.in_memory import InMemoryRetriever


def test_retrieve_returns_documents():
    """Test retrieving documents."""

    retriever = InMemoryRetriever(
        documents=[
            "Document 1",
            "Document 2",
            "Document 3",
        ]
    )

    results = retriever.retrieve(
        query="Databricks",
    )

    assert results == [
        "Document 1",
        "Document 2",
        "Document 3",
    ]


def test_retrieve_respects_limit():
    """Test retrieval limit."""

    retriever = InMemoryRetriever(
        documents=[
            "Document 1",
            "Document 2",
            "Document 3",
            "Document 4",
        ]
    )

    results = retriever.retrieve(
        query="Spark",
        limit=2,
    )

    assert results == [
        "Document 1",
        "Document 2",
    ]


def test_retrieve_empty_documents():
    """Test retrieving from an empty document collection."""

    retriever = InMemoryRetriever(
        documents=[],
    )

    results = retriever.retrieve(
        query="Anything",
    )

    assert results == []


def test_retrieve_limit_greater_than_documents():
    """Test retrieval when limit exceeds available documents."""

    retriever = InMemoryRetriever(
        documents=[
            "Document 1",
            "Document 2",
        ]
    )

    results = retriever.retrieve(
        query="Anything",
        limit=10,
    )

    assert results == [
        "Document 1",
        "Document 2",
    ]