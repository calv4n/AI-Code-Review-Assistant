# KI-basierter Merge Request Review Assistant

Dieses Projekt ist im Rahmen meiner individuellen Praktischen Arbeit (IPA) für das eidgenössische Fähigkeitszeugnis (EFZ) zum Informatiker mit Fachrichtung Applikationsentwicklung entstanden.

Es handelt sich um einen KI-Assistenten, der eingehende Merge Requests in GitLab automatisch analysiert und zeilenbasierte Code-Reviews als Kommentare erstellt.
Unterstützt werden sowohl lokale LLMs (z. B. Ollama) als auch OpenAI-kompatible API-Anbieter.

## Features
* **Automatisierte Code-Reviews:** Analysiert geänderte Dateien (Diffs) eines Merge Requests.
* **6 Review-Kategorien:** Prüft auf Bugs, Edge Cases, Performance, Security, Code Style und Lesbarkeit.
* **Zeilenbezogenes Feedback:** Generiert präzise Hinweise mit Dateinamen und Zeilennummern.
* **Lokale KI:** Standardmässig für Ollama konfiguriert. Alternativ OpenAI-kompaktible API-Anbieter

## Voraussetzungen
* Python >= 3.11
* Ein laufender Ollama-Server ODER ein API-Key für OpenRouter, OpenAI. Falls nicht vorhanden [Ollama Setup Guide](https://docs.ollama.com/quickstart)
* Ein GitLab Access Token mit den Scopes `read_api` und `api`.

## Installation

1. **Richtiges Ollama Model pullen (bei OpenAI überspringen)**
   ```bash
   ollama pull codellama 
   ```

2. **Repository klonen:**
   ```bash
   git clone https://github.com/calv4n/AI-Code-Review-Assistant
   ```
3. **in das Projektverzeichnis wechseln**
   ```bash
   cd AI-Code-Review-Assistant
   ```
4. **Virtual Environment (venv) erstellen und aktivieren**
   ```bash
   python -m venv .venv
   source .venv/bin/activate # Linux/Mac
   # oder: .venv\Scripts\activate # Windows
   ```
5. **Abhängigkeiten installieren**
   ```bash
   pip install -r requirements.txt
   ```

## Konfiguration

Das Tool wird ausschliesslich über Umgebungsvariablen gesteuert.

1. **Beispiel-Konfigurationsdatei kopieren**

```bash
cp .env.example .env
```

2. **Werte in der .env anpassen**

```bash
#### GitLab Konfiguration
GITLAB_URL=https://gitlab.com
GITLAB_TOKEN=dein_access_token_hier

#### LLM Konfiguration
LLM_PROVIDER=ollama  # Optionen: 'ollama' oder 'openrouter'
LLM_MODEL=codellama  # oder 'mistral', 'llama3', etc.
LLM_TEMPERATURE=0.3

#### Optional (falls LLM_PROVIDER=openrouter)
OPENROUTER_API_KEY=dein_openrouter_key
```

## Verwendung (CLI)

Das Tool verfügt über ein Kommandozeilen-Interface (CLI).

- **Einen Merge Request reviewen und posten**
```bash
python -m src.main review --project-id <PROJEKT_ID> --mr-id <MR_ID>
```

- **Dry-Run Modus (Ergebnis nur auf Konsole printen)**
```bash
python -m src.main review --project-id <PROJEKT_ID> --mr-id <MR_ID> --dry-run
```

## Lizenz

Dieses Projekt besteht ausschliesslich aus Free Open Source Software (FOSS) und ist unter der MIT-Lizenz veröffentlicht.