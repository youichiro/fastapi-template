from fastapi.testclient import TestClient

from app.main import app
from app import schemas, usecases

client = TestClient(app)


def test_create_accounts(db, mocker):
    mocker.patch("app.usecases.create_account_usecases.exec", return_value=None)
    json_dict = {
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
    response = client.post("/v1/accounts", json=json_dict)

    body = schemas.AccountCreateInput.parse_obj(json_dict)
    usecases.create_account_usecases.exec.assert_called_once_with(db, body)
    assert response.status_code == 201
