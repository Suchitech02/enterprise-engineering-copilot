from copilot.vectorstore.in_memory import (
    InMemoryVectorStore,
)


def test_add_vector():
    """Test adding vectors."""

    store = InMemoryVectorStore()

    store.add(
        text="Databrciks",
        embedding=[1.0,2.0],
    )

    assert len(store._vectors) == 1

def test_search_returns_text():
    """Test searching vectors."""

    store = InMemoryVectorStore()

    store.add(
        text="Databricks",
        embedding=[1.0],
    )

    results = store.search(
        embedding=[1.0],
    )

    assert results == [
        "Databricks",
    ]

def test_search_limit():
    """Test search limit."""

    store = InMemoryVectorStore()

    for i in range(10):
        store.add(
            text=f"Doc {i}",
            embedding=[float(i)],
        )

    results = store.search(
        embedding=[1.0],
        limit=3,
    )

    assert len(results) == 3