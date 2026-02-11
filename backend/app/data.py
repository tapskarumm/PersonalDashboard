"""Static data and helpers for the personal dashboard."""

from datetime import datetime


def calculate_focus_score(hours_deep_work: float, hours_meetings: float) -> int:
    """Return a 0-100 focus score where more deep work and fewer meetings is better."""
    if hours_deep_work < 0 or hours_meetings < 0:
        return 0
    raw = (hours_deep_work * 12) - (hours_meetings * 5)
    return max(0, min(100, int(raw)))


def get_overview() -> dict:
    return {
        "name": "Tapiwa Karumekayi",
        "role": "Full-Stack Developer",
        "location": "Tallahassee, FL",
        "focus": "Building fast, reliable web apps",
        "status": "In a focused build sprint",
        "lastUpdated": datetime.utcnow().isoformat(),
    }


def get_metrics() -> list:
    return [
        {"label": "Focus Score", "value": 88, "delta": "+6", "trend": "up"},
        {"label": "Projects Shipped", "value": 14, "delta": "+2", "trend": "up"},
        {"label": "Avg. Response Time", "value": "210ms", "delta": "-35ms", "trend": "down"},
        {"label": "Weekly Deep Work", "value": "18.5h", "delta": "+3.5h", "trend": "up"},
    ]


def get_activity() -> list:
    return [
        {"time": "Today 9:10 AM", "detail": "Refactored analytics pipeline for 22% faster processing."},
        {"time": "Yesterday 4:45 PM", "detail": "Launched personal dashboard MVP with real-time metrics."},
        {"time": "Yesterday 10:30 AM", "detail": "Added typed API schemas and data validation layer."},
        {"time": "Mon 6:20 PM", "detail": "Polished UI with new typography and motion system."},
    ]


def get_goals() -> list:
    return [
        {"title": "Ship portfolio refresh", "progress": 72},
        {"title": "Automate weekly reporting", "progress": 48},
        {"title": "Publish API performance writeup", "progress": 35},
    ]


def get_skills() -> list:
    return [
        "FastAPI",
        "React",
        "PostgreSQL",
        "TypeScript",
        "CI/CD",
        "Design Systems",
        "Data Visualization",
        "Testing",
    ]


def get_insights() -> list:
    return [
        {"day": "Mon", "hours": 2.5},
        {"day": "Tue", "hours": 3.0},
        {"day": "Wed", "hours": 4.2},
        {"day": "Thu", "hours": 3.7},
        {"day": "Fri", "hours": 5.1},
        {"day": "Sat", "hours": 1.8},
        {"day": "Sun", "hours": 2.2},
    ]
