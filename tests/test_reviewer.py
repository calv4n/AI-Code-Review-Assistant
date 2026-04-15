import pytest
from unittest.mock import MagicMock
from src.reviewer import run_review
from src.config_loader import Config
from langchain_core.messages import AIMessage
from langchain_core.runnables import RunnableLambda

# Erstelle ein Mock Runnable, das sich exakt wie ein Chat-Modell verhält
# und ein Objekt mit einem .content Attribut zurückgibt
mock_chat_model = RunnableLambda(lambda x: AIMessage(content="Hier ist dein KI Review!"))
error_chat_model = RunnableLambda(lambda x: (_ for _ in ()).throw(Exception("Ollama ist nicht erreichbar")))

@pytest.fixture
def mock_dependencies(monkeypatch, mock_mr_metadata, mock_raw_diff):
    monkeypatch.setattr("src.reviewer.get_config", lambda: Config("u", "t", "ollama", "m", 0.1, ""))
    
    mock_client = MagicMock()
    mock_client.get_mr_metadata.return_value = mock_mr_metadata
    mock_client.get_mr_diffs.return_value = mock_raw_diff
    monkeypatch.setattr("src.reviewer.GitLabClient", lambda u, t: mock_client)
    
    # Nutze das RunnableLambda, das ein AIMessage-Objekt zurückgibt
    monkeypatch.setattr("src.reviewer.get_llm", lambda x: mock_chat_model)
    
    return mock_client

def test_t11_dry_run_mode(mock_dependencies):
    mock_client = mock_dependencies
    run_review(7757, 7, dry_run=True)
    assert not mock_client.post_comment.called

def test_t12_end_to_end_workflow(mock_dependencies):
    mock_client = mock_dependencies
    run_review(7757, 7, dry_run=False)
    # Jetzt sollte es fehlerfrei durchlaufen!
    mock_client.post_comment.assert_called_once_with(7757, 7, "Hier ist dein KI Review!")

def test_t09_fail_error(mock_dependencies, monkeypatch):
    mock_client = mock_dependencies
    # Überschreibe das LLM mit dem Fehler-Modell
    monkeypatch.setattr("src.reviewer.get_llm", lambda x: error_chat_model)
    
    try:
        run_review(7757, 7, dry_run=False)
    except Exception:
        pytest.fail("Reviewer ist abgestürzt!")
        
    assert not mock_client.post_comment.called