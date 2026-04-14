# AI-based-Merge-Request-Review-Assistant
This is the Individual Practical Work of my Apprenticeship at SIX, that implements an internal AI-powered assistant that automatically analyzes incoming GitLab merge requests and generates review comments using Large Language Models.


python -m venv.venv

source .venv/bin/activate

pip install -r requirements.txt

python -m src.main review --project-id [PROJECT_ID] --mr-id [MR_ID] --dry-run
