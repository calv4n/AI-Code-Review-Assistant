import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Config:
    gitlab_url: str
    gitlab_token: str

def get_config() -> Config:
    url = os.getenv("GITLAB_URL")
    token = os.getenv("GITLAB_TOKEN")
    if not url or not token:
        raise ValueError("GITLAB_URL und GITLAB_TOKEN fehlen")
    return Config(gitlab_url=url, gitlab_token=token)