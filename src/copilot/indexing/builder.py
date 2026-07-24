from copilot.embeddings.base import BaseEmbeddingModel
from copilot.indexing.base import BaseIndexBuilder
from copilot.models.document import Document
from copilot.vectorstore.base import BaseVectorStore


class IndexBuilder(BaseIndexBuilder):
    """Builds a vector index from documents."""

    def __init__(
        self,
        embedding_model: BaseEmbeddingModel,
    ) -> None:
        self.embedding_model = embedding_model

    def build(
        self,
        documents: list[Document],
        vector_store: BaseVectorStore,
    ) -> None:

        for document in documents:
            embedding = self.embedding_model.embed(
                document.text,
            )

            vector_store.add(
                document=document,
                embedding=embedding,
            )
