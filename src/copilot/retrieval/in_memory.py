from copilot.retrieval.base import BaseRetriever


class InMemoryRetriever(BaseRetriever):


    def __init__(
        self,
        documents: list[str],
    ):
        self.documents: list[str] = documents

    def retrieve(
        self,
        query: str,
        limit: int = 5,
    ) -> list[str]:
        return self.documents[:limit]