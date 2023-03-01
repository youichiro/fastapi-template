from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_hello():
    response = client.get("/")
    assert response.status_code == 200
