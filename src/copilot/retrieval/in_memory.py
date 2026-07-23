from copilot.embeddings.base import BaseEmbeddingModel
from copilot.embeddings.mock_embedding import MockEmbeddingModel
from copilot.retrieval.base import BaseRetriever
from copilot.vectorstore.base import BaseVectorStore
from copilot.vectorstore.in_memory import InMemoryVectorStore


class InMemoryRetriever(BaseRetriever):


    def __init__(
        self,
        documents: list[str],
        embedding_model: BaseEmbeddingModel | None = None,
        vector_store: BaseVectorStore | None = None,
    ):
        self.embedding_model = (
            embedding_model
            or MockEmbeddingModel()
        )

        self.vector_store = (
            vector_store
            or InMemoryVectorStore()
        )

        for document in documents:
            embedding = self.embedding_model.embed(
                document
            )

            self.vector_store.add(
                text=document,
                embedding=embedding,
            )

    def retrieve(
        self,
        query: str,
        limit: int = 5,
    ) -> list[str]:

        query_embedding = self.embedding_model.embed(
            query
        )

        return self.vector_store.search(
            embedding=query_embedding,
            limit=limit,
        )