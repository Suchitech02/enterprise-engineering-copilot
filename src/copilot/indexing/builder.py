from copilot.embeddings.base import BaseEmbeddingModel
from copilot.indexing.base import BaseIndexBuilder
from copilot.vectorstore.base import BaseVectorStore


class IndexBuilder(BaseIndexBuilder):
    """Builds a vector index from documents."""

    def __init__(
        self,
        embedding_model: BaseEmbeddingModel,
    ):
        self.embedding_model = embedding_model

    def build(
        self,
        documents: list[str],
        vector_store: BaseVectorStore,
    ) -> None:
        
        for document in documents:
            embedding = self.embedding_model.embed(
                document
            )

            vector_store.add(
                text=document,
                embedding=embedding,
            )