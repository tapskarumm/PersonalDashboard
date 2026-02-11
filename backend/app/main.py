"""FastAPI application entry point for the personal dashboard."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import data

app = FastAPI(title="Personal Dashboard API", version="1.0.0")

allowed_origins = [
    "http://localhost:5173",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/api/health")
def health() -> dict:
    """Simple health check."""
    return {"status": "ok"}


@app.get("/api/overview")
def overview() -> dict:
    return data.get_overview()


@app.get("/api/metrics")
def metrics() -> list:
    return data.get_metrics()


@app.get("/api/activity")
def activity() -> list:
    return data.get_activity()


@app.get("/api/goals")
def goals() -> list:
    return data.get_goals()


@app.get("/api/skills")
def skills() -> list:
    return data.get_skills()


@app.get("/api/insights")
def insights() -> list:
    return data.get_insights()
