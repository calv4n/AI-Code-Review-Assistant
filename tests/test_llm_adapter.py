import pytest
from src.llm_adapter import get_llm
from src.config_loader import Config

def test_t08_create_correct_llm_provider():
    # Teste Ollama Erstellung
    config_ollama = Config("url", "token", "ollama", "codellama", 0.1, "")
    llm_ollama = get_llm(config_ollama)
    assert "ChatOllama" in str(type(llm_ollama))
    
    # Teste OpenRouter Erstellung
    config_openrouter = Config("url", "token", "openrouter", "openai/gpt-4o", 0.1, "key")
    llm_openrouter = get_llm(config_openrouter)
    assert "ChatOpenAI" in str(type(llm_openrouter))
    
    # Teste ungültigen Provider
    config_invalid = Config("url", "token", "invalid", "model", 0.1, "")
    with pytest.raises(ValueError, match="Nicht unterstützter LLM-Provider"):
        get_llm(config_invalid)