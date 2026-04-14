import pytest
from src.config_loader import get_config

def test_t01_load_config_success(monkeypatch):
    # Simuliere gesetzte Umgebungsvariablen
    monkeypatch.setenv("GITLAB_URL", "https://gitlab.com")
    monkeypatch.setenv("GITLAB_TOKEN", "super_secret_token")
    monkeypatch.setenv("LLM_PROVIDER", "ollama")
    
    config = get_config()
    assert config.gitlab_url == "https://gitlab.com"
    assert config.gitlab_token == "super_secret_token"
    assert config.llm_provider == "ollama"

def test_t02_missing_parameter(monkeypatch):
    # Lösche den Token aus den Umgebungsvariablen (falls vorhanden)
    monkeypatch.delenv("GITLAB_TOKEN", raising=False)
    monkeypatch.setenv("GITLAB_URL", "https://gitlab.com")
    
    with pytest.raises(ValueError, match="GITLAB_URL und GITLAB_TOKEN"):
        get_config()