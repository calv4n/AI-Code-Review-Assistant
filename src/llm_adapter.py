from src.config_loader import Config
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_litellm import ChatLiteLLM

from pydantic import SecretStr

def get_llm(config: Config):
    """
    Methode zur Erstellung der LLM-Instanz mit LangChain: Ollama oder OpenRouter (OpenAI)
    """
    if config.use_litellm == True:
        return ChatLiteLLM(
            api_key=config.openrouter_api_key,
            # api_base=config.litellm_api_base,
            model=f"{config.llm_provider}/{config.llm_model}",
            temperature=config.llm_temperature
        )
    elif config.llm_provider == "ollama":
        return ChatOllama(
            model=config.llm_model,
            temperature=config.llm_temperature
        )
    elif config.llm_provider == "openrouter":
        return ChatOpenAI(
            api_key=SecretStr(config.openrouter_api_key),
            base_url="https://openrouter.ai/api/v1",
            model=config.llm_model,
            temperature=config.llm_temperature
        )
    else:
        raise ValueError(f"Nicht unterstützter LLM-Provider: {config.llm_provider}")