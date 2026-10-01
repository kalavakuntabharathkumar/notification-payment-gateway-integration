# Notification and Payment Gateway Integration Service

FastAPI integration service for payment, SMS, and email providers with JSON webhooks,
HTTP retries, Redis support, Docker packaging, and Jenkins CI/CD.

## Run locally
```bash
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API docs: `http://127.0.0.1:8000/docs`

## Docker
```bash
docker compose up --build
```

## AWS/Jenkins
The repository contains a Dockerfile, EC2 bootstrap script, and Jenkinsfile. Provider
credentials and production endpoints are intentionally supplied through environment
variables rather than committed to Git.

## Portfolio metrics
The resume claims (99.2% delivery, 11,500 monthly transactions, 55→9 minute releases)
should be presented as measured project outcomes only if you have the corresponding
monitoring/test/release records to substantiate them.
