from fastapi.testclient import TestClient

from app.accounts.schemas import account_schema
from app.main import app

client = TestClient(app)


def test_create_accounts(db, mocker):
    mock = mocker.patch("app.accounts.usecases.create_accounts_usecase.exec", return_value=None)
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
        ],
    }
    response = client.post("/v1/accounts", json=json_dict)

    body = account_schema.AccountCreateInput.parse_obj(json_dict)
    mock.assert_called_once_with(db, body)
    assert response.status_code == 201
