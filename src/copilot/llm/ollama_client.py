from ollama import Client
from copilot.llm.base import BaseLLMClient

class OllamaClient(BaseLLMClient):
    """Ollama implementation."""

    def __init__(self) -> None:
        self.client = Client(host="http://localhost:11434")

    def generate(self, prompt: str) -> str:
        response = self.client.generate(
            model="qwen3:8b",
            prompt=prompt,
        )

        return response["response"]