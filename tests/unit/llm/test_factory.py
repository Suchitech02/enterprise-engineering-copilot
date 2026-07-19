from unittest.mock import patch

import pytest

from copilot.llm.factory import get_llm


def test_get_llm_returns_ollama(monkeypatch):
    monkeypatch.setattr(
        "copilot.llm.factory.settings.llm_provider",
        "ollama",
    )

    with patch("copilot.llm.factory.OllamaClient") as mock_client:
        get_llm()
        mock_client.assert_called_once()


def test_get_llm_returns_openai(monkeypatch):
    monkeypatch.setattr(
        "copilot.llm.factory.settings.llm_provider",
        "openai",
    )

    with patch("copilot.llm.factory.OpenAIClient") as mock_client:
        get_llm()
        mock_client.assert_called_once()


def test_get_llm_invalid_provider(monkeypatch):
    monkeypatch.setattr(
        "copilot.llm.factory.settings.llm_provider",
        "invalid",
    )

    with pytest.raises(ValueError):
        get_llm()
