from src.config import get_config
from src.gitlab_client import GitLabClient

def main():
    project_id = 7757
    mr_id = 7

    config = get_config()
    client = GitLabClient(config.gitlab_url, config.gitlab_token)
    
    metadata = client.get_mr_metadata(project_id, mr_id)
    print(f"MR Metadaten: {metadata}\n")
    
    diffs = client.get_mr_diffs(project_id, mr_id)
    for diff in diffs:
        print(f"Datei: {diff.get('new_path')}")
        print(diff.get('diff'))
        print("-" * 40)

if __name__ == '__main__':
    main()