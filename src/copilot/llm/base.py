from abc import ABC, abstractmethod


class BaseLLMClient(ABC):
    """Abstract base class for all LLMs."""

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Generate text based on the given prompt."""
        raise NotImplementedError
