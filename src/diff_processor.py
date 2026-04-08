import os

def get_language_from_extension(file_path: str) -> str:
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()
    
    if ext == '.py': return 'Python'
    if ext in ['.js', '.jsx']: return 'JavaScript'
    if ext in ['.ts', '.tsx']: return 'TypeScript'
    if ext == '.java': return 'Java'
    if ext in ['.html', '.htm']: return 'HTML'
    if ext == '.css': return 'CSS'
    
    return 'Unbekannt'

def process_diffs(raw_diffs: list) -> str:
    """
    Formatiert die rohen GitLab-Diffs in einen lesbaren Text für das LLM.
    """
    processed_text = []

    for diff in raw_diffs:
        file_path = diff.get('new_path')
        diff_content = diff.get('diff', '')
            
        processed_text.append(f"--- Datei: {file_path} ---")
        processed_text.append(diff_content)
        processed_text.append("-" * 40)
        
    return "\n".join(processed_text)