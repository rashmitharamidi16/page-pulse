from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_invalid_url():
    response = client.post(
        "/api/analyze",
        json={
            "url": "https://example.com/abcd123"
        }
    )

    assert response.status_code == 404