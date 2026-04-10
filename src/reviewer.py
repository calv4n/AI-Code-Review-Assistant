from src.config_loader import get_config
from src.gitlab_client import GitLabClient
from src.diff_processor import process_diffs
from src.prompt_builder import build_review_prompt
from src.llm_adapter import get_llm
import time
from src.logger import logger

def run_review(project_id: int, mr_id: int, dry_run: bool = False):
    start_time = time.time()
    config = get_config()

    log_context = {
        "mr_id": mr_id,
        "project_id": project_id,
        "llm": f"{config.llm_provider}/{config.llm_model}"
    }

    logger.info("Starte MR-Review", **log_context)

    try:
        # ---- 1 Daten holen
        client = GitLabClient(config.gitlab_url, config.gitlab_token)
        metadata = client.get_mr_metadata(project_id, mr_id)
        raw_diffs = client.get_mr_diffs(project_id, mr_id)

        # ---- 2 Diffs verarbeiten
        diff_text = process_diffs(raw_diffs)
        if not diff_text.strip():
            logger.info("Keine änderungen im MR gefunden. Abbruch.", **log_context)
            return
    
        # ---- 3 Prompt bauen
        prompt = build_review_prompt()
        llm = get_llm(config)
        chain = prompt | llm

        logger.info("Sende Daten an LLM...", **log_context)

        response = chain.invoke({
            "title": metadata.get('title', 'Unbekannt'),
            "author": metadata.get('author', 'Unbekannt'),
            "diff_text": diff_text
        })

        review_result = response.content
    
        # ---- 4 Kommentar posten oder in die Konsole ausgeben

        if dry_run:
            print("\n" + "="*50)
            print("DRY-RUN ERGEBNIS (Wird nicht gepostet):")
            print("="*50)
            print(review_result)
        else:
            client.post_comment(project_id, mr_id, review_result)
            logger.info("Review-Kommentar erfolgreich gepostet.", **log_context)

        # Erfolgs Logging

        duration = round(time.time() - start_time, 2)
        logger.info("Review abgeschlossen", status="erfolgreich", dauer_sekunden=duration, **log_context)

    except Exception as e:
        # expeption, Prozess nicht blockieren, aber loggen.
        duration = round(time.time() - start_time, 2)
        logger.error("Fehler während des Reviews", error=str(e), status="fehler", dauer_sekunden=duration, **log_context)
        if dry_run:
            print(f"Ein Fehler ist aufgetreten: {e}")
