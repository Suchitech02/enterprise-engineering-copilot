from pydantic_settings import BaseSettings, SettingsConfigDict


class LLMSettings(BaseSettings):
    """Configuration for LLM providers."""

    llm_provider: str = "ollama"

    ollama_host: str = "http://localhost:11434"
    ollama_model: str = "qwen3:8b"

    openai_api_key: str = ""
    openai_model: str = "gpt-4o"

    anthropic_api_key: str = ""
    anthropic_model: str = "claude-4-sonnet"

    model_config = SettingsConfigDict(env_file=".env", env_prefix="", extra="ignore")


settings = LLMSettings()
