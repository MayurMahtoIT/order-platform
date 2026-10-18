from fastapi import FastAPI
from sqlalchemy import text

from app.config import settings
from app.database import SessionLocal
from app.routers import orders

app = FastAPI(title=settings.service_name)
app.include_router(orders.router)


@app.get("/health/live")
def liveness() -> dict:
    """Is the process up? Kubernetes uses this to decide whether to restart us."""
    return {"status": "ok"}


@app.get("/health/ready")
def readiness() -> dict:
    """Can we serve traffic (DB reachable)? Kubernetes uses this to route traffic."""
    with SessionLocal() as db:
        db.execute(text("SELECT 1"))
    return {"status": "ready"}
