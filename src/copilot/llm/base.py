from abc import ABC, abstractmethod
from collections.abc import Iterator


class BaseLLMClient(ABC):
    """Abstract base class for all LLMs."""

    @abstractmethod
    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:
        """Generate text based on the given prompt."""
        raise NotImplementedError
    
    @abstractmethod
    def stream_generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> Iterator[str]:
        """Generate streamed text chunks."""
        raise NotImplementedError
