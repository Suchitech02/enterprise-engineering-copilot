from ollama import Client

from copilot.llm.base import BaseLLMClient
from copilot.llm.config import settings


class OllamaClient(BaseLLMClient):
    """Ollama implementation."""

    def __init__(
        self,
        model: str = "qwen3:8b",
        host: str = "http://localhost:11434",
    ) -> None:
        self.client = Client(host=settings.ollama_host)
        self.model = settings.ollama_model

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> str:
        response = self.client.chat(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )

        return response["message"]["content"]
