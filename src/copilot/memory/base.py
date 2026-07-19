from abc import ABC, abstractmethod


class BaseConversationStore(ABC):
    """Abstract base class for conversation memory."""

    @abstractmethod
    def get_messages(
        self,
        conversation_id: str,
    ) -> list[dict[str, str]]:
        """Return the message history for a conversation."""
        raise NotImplementedError

    @abstractmethod
    def add_message(
        self,
        conversation_id: str,
        role: str,
        content: str,
    ) -> None:
        """Append a message to a conversation."""
        raise NotImplementedError

    @abstractmethod
    def clear(
        self,
        conversation_id: str,
    ) -> None:
        """Clear all messages for a conversation."""
        raise NotImplementedError