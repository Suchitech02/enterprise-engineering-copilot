from collections import defaultdict

from copilot.memory.base import BaseConversationStore


class InMemoryConversationStore(BaseConversationStore):
    """Simple in-memory conversation storage."""


    def __init__(self) -> None:
        self._memory = defaultdict(list)

    def get_messages(
            self,
            conversation_id: str,
    ) -> list[dict]:
        return self._memory[conversation_id]
    
    def add_message(
        self,
        conversation_id: str,
        role: str,
        content: str,
    ) -> None:
        self._memory[conversation_id].append(
            {
                "role": role,
                "content": content,
            }
        )
    
    def clear(
        self,
        conversation_id: str,
    ) -> None:
        self._memory.pop(conversation_id, None)