from copilot.embeddings.mock_embedding import MockEmbeddingModel


def test_embedding_dimension():
    """Test embedding size."""

    model = MockEmbeddingModel()

    embedding = model.embed("Databricks")

    assert len(embedding) == 10


def test_embedding_is_deterministic():
    """Same input should produce the same embedding."""

    model = MockEmbeddingModel()

    embedding1 = model.embed("Unity Catalog")
    embedding2 = model.embed("Unity Catalog")

    assert embedding1 == embedding2


def test_different_inputs():
    """Different inputs should produce different embeddings."""

    model = MockEmbeddingModel()

    embedding1 = model.embed("A")
    embedding2 = model.embed("AAAA")

    assert embedding1 != embedding2


def test_empty_string():
    """Empty string embedding."""

    model = MockEmbeddingModel()

    embedding = model.embed("")

    assert embedding == [0.0] * 10