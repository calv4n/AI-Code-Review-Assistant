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