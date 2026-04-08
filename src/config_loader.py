import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Config:
    """
    Konfigurationsklasse für GitLab-Zugriff.
    """
    gitlab_url: str
    gitlab_token: str

def get_config() -> Config:
    """
    Liest die benötigten Umgebungsvariablen aus
    und gibt eine Config-Instanz zurück.
    """
    gitlab_url = os.getenv("GITLAB_URL")
    gitlab_token = os.getenv("GITLAB_TOKEN")

    # Prüft ob beide Variablen vorhanden sind
    if not gitlab_url or not gitlab_token:
        raise ValueError("GITLAB_URL und GITLAB_TOKEN fehlen")
    return Config(
        gitlab_url=gitlab_url,
        gitlab_token=gitlab_token
    )