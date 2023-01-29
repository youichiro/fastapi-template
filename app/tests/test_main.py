from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_accounts(db):
    response = client.post(
        "/v1/accounts",
        json={
            "admin_secret": "demo_secret",
             "accounts": [
                {
                    "external_user_id": "example_external_user_1",
                    "school_id": 1,
                },
                {
                    "external_user_id": "example_external_user_2",
                    "school_id": 2,
                },
            ]
        }
    )
    assert response.status_code == 201
