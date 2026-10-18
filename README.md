# Order Processing Platform

Microservices practice project (FastAPI, Postgres, Kafka, Redis, Docker, Kubernetes, AWS).

## Run everything
    docker compose up --build

Order service docs: http://localhost:8001/docs

## Run tests (no Docker needed)
    cd services/order-service
    python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
    pip install -r requirements-dev.txt
    pytest
