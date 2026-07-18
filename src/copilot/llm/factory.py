from copilot.llm.base import BaseLLMClient
from copilot.llm.ollama_client import OllamaClient


def get_llm() -> BaseLLMClient:
    """Return the configured LLM implementation."""
    return OllamaClient()
