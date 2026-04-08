from src.config_loader import get_config
from src.gitlab_client import GitLabClient
from src.diff_processor import process_diffs

def run_review(project_id: int, mr_id: int):
    config = get_config()
    # ---- 1 Daten holen
    client = GitLabClient(config.gitlab_url, config.gitlab_token)
    
    # Metadaten eines MRs ausgeben
    print(f"Lese Daten für Projekt {project_id}, MR {mr_id}...\n")
    metadata = client.get_mr_metadata(project_id, mr_id)
    print(f"Metadaten: {metadata}\n")
    
    # ---- 2 Diffs verarbeiten
    raw_diffs = client.get_mr_diffs(project_id, mr_id)
    diff_text = process_diffs(raw_diffs)
    
    if not diff_text.strip():
        print("Keine Diffs gefunden.")
        return
        
    print("Aufbereiteter Diff-Text für das LLM:")
    print(diff_text)