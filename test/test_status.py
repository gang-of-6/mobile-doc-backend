from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_index():
    """Checking if the status returns success"""
    response = client.get("/")
    response_json = response.json()
    assert response.status_code == 200
    assert response_json["success"] is True
