from abc import ABC, abstractmethod


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
