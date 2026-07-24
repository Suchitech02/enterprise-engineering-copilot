from copilot.models.document import Document
from copilot.vectorstore.in_memory import (
    InMemoryVectorStore,
)


def test_add_vector():
    """Test adding vectors."""

    store = InMemoryVectorStore()

    store.add(
        document=Document(
            text="Databricks",
        ),
        embedding=[1.0, 2.0],
    )

    assert len(store._vectors) == 1
    assert store._vectors[0][1].text == "Databricks"


def test_search_returns_documents():
    """Test searching vectors."""

    store = InMemoryVectorStore()

    store.add(
        document=Document(
            text="Databricks",
        ),
        embedding=[1.0, 2.0],
    )

    results = store.search(
        embedding=[1.0, 2.0],
    )

    assert len(results) == 1
    assert results[0].text == "Databricks"


def test_search_limit():
    """Test search limit."""

    store = InMemoryVectorStore()

    for i in range(10):
        store.add(
            document=Document(
                text=f"Doc {i}",
            ),
            embedding=[float(i)],
        )

    results = store.search(
        embedding=[1.0],
        limit=3,
    )

    assert len(results) == 3
