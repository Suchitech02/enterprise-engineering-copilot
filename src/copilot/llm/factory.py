from copilot.llm.ollama_client import OllamaClient

def get_llm():
    """Return the configured LLM implementation."""
    return OllamaClient()