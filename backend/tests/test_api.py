"""API tests for the personal dashboard backend."""

from fastapi.testclient import TestClient

from app.main import app
from app.data import calculate_focus_score

client = TestClient(app)


def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_overview_shape():
    response = client.get("/api/overview")
    assert response.status_code == 200
    body = response.json()
    assert "name" in body
    assert "role" in body


def test_metrics_returns_list():
    response = client.get("/api/metrics")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_focus_score_bounds():
    assert calculate_focus_score(0, 0) == 0
    assert calculate_focus_score(10, 0) <= 100
    assert calculate_focus_score(-1, 2) == 0
