from collections.abc import Iterator

from copilot.llm.factory import get_llm
from copilot.memory.base import BaseConversationStore
from copilot.memory.in_memory import InMemoryConversationStore
from copilot.models.chat import ChatResponse
from copilot.models.generate import GenerateResponse
from copilot.prompts.prompt_builder import PromptBuilder
from copilot.retrieval.base import BaseRetriever
from copilot.retrieval.in_memory import InMemoryRetriever


class AssistantService:
    """Service responsible for AI orchestration."""

    SYSTEM_PROMPT = "You are a helpful AI assistant."

    def __init__(
        self,
        memory: BaseConversationStore | None = None,
        retriever: BaseRetriever | None = None,
    ) -> None:
        self.llm = get_llm()
        self.memory: BaseConversationStore = (
            memory or InMemoryConversationStore()
        )
        self.retriever: BaseRetriever = (
            retriever
            or InMemoryRetriever(
                documents=[],
            )
        )

    def generate(
        self,
        prompt: str,
    ) -> GenerateResponse:
        """Generate an AI response."""

        full_prompt = PromptBuilder.build_general_prompt(prompt)

        answer = self.llm.generate(
            system_prompt=self.SYSTEM_PROMPT,
            user_prompt=full_prompt,
        )

        return GenerateResponse(response=answer)

    def stream_generate(
        self,
        prompt: str,
    ) -> Iterator[str]:
        """Generate a streamed AI response."""

        full_prompt = PromptBuilder.build_general_prompt(prompt)

        yield from self.llm.stream_generate(
            system_prompt=self.SYSTEM_PROMPT,
            user_prompt=full_prompt,
        )

    def retrieve_and_generate(
        self,
        question: str,
    ) -> GenerateResponse:
        """Generate a response using a retrieved context."""

        documents = self.retriever.retrieve(
            query=question,
        )

        prompt = PromptBuilder.build_rag_prompt(
            question=question,
            documents=documents,
        )

        response = self.llm.generate(
            system_prompt = self.SYSTEM_PROMPT,
            user_prompt = prompt,
        )

        return GenerateResponse(
            response=response
        )


    def chat(
        self,
        conversation_id: str,
        message: str,
    ) -> ChatResponse:
        """Generate a response using conversation history."""

        self.memory.add_message(
            conversation_id=conversation_id,
            role="user",
            content=message,
        )

        history = self.memory.get_messages(
            conversation_id=conversation_id,
        )

        prompt = PromptBuilder.build_chat_prompt(history)

        response = self.llm.generate(
            system_prompt=self.SYSTEM_PROMPT,
            user_prompt=prompt,
        )

        self.memory.add_message(
            conversation_id=conversation_id,
            role="assistant",
            content=response,
        )

        return ChatResponse(
            conversation_id=conversation_id,
            response=response,
        )