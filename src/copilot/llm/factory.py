from copilot.llm.base import BaseLLMClient
from copilot.llm.config import settings
from copilot.llm.ollama_client import OllamaClient
from copilot.llm.openai_client import OpenAIClient


def get_llm() -> BaseLLMClient:
    """Return the configured LLM implementation."""

    if settings.llm_provider == "ollama":
        return OllamaClient()

    if settings.llm_provider == "openai":
        return OpenAIClient()

    raise ValueError(f"unsupported LLM providers: {settings.llm_provider}")
