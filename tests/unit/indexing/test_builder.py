from copilot.indexing.builder import IndexBuilder
from copilot.embeddings.mock_embedding import MockEmbeddingModel
from copilot.vectorstore.in_memory import InMemoryVectorStore


def test_build_single_document():
    """Test building an index with one document."""

    builder = IndexBuilder(
        embedding_model=MockEmbeddingModel(),
    )

    store = InMemoryVectorStore()

    builder.build(
        documents=["Databricks"],
        vector_store=store,
    )

    assert store.search(
        embedding=MockEmbeddingModel().embed("Databricks"),
    ) == [
        "Databricks",
    ]


def test_build_multiple_documents():
    """Test building an index with multiple documents."""

    builder = IndexBuilder(
        embedding_model=MockEmbeddingModel(),
    )

    store = InMemoryVectorStore()

    builder.build(
        documents=[
            "Databricks",
            "Apache Spark",
        ],
        vector_store=store,
    )

    results = store.search(
        embedding=MockEmbeddingModel().embed("Databricks"),
        limit=2,
    )

    assert len(results) == 2


def test_build_empty_documents():
    """Test building an empty index."""

    builder = IndexBuilder(
        embedding_model=MockEmbeddingModel(),
    )

    store = InMemoryVectorStore()

    builder.build(
        documents=[],
        vector_store=store,
    )

    assert store.search(
        embedding=[1.0] * 10,
    ) == []


def test_build_preserves_existing_documents():
    """Test that building adds to an existing vector store."""

    builder = IndexBuilder(
        embedding_model=MockEmbeddingModel(),
    )

    store = InMemoryVectorStore()

    builder.build(
        documents=["Document 1"],
        vector_store=store,
    )

    builder.build(
        documents=["Document 2"],
        vector_store=store,
    )

    results = store.search(
        embedding=MockEmbeddingModel().embed("Document 1"),
        limit=2,
    )

    assert len(results) == 2