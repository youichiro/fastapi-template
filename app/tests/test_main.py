from fastapi.testclient import TestClient

from app.main import app
from app.schemas import account_schema, answer_schema

client = TestClient(app)


def test_hello():
    response = client.get("/")
    assert response.status_code == 200


def test_create_accounts(db, mocker):
    mock = mocker.patch("app.usecases.create_accounts_usecase.exec", return_value=None)
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


def test_create_answers(db, mocker):
    mock = mocker.patch("app.usecases.create_answers_usecase.exec", return_value=None)
    json_dict = {
        "answers": [
            {
                "section_code": "section_code_111",
                "is_correct": False,
            },
            {
                "section_code": "section_code_222",
                "is_correct": False,
            },
            {
                "section_code": "section_code_333",
                "is_correct": True,
            },
        ]
    }
    response = client.post(f"/v1/accounts/1/answers", json=json_dict)

    body = answer_schema.AnswerCreateInput.parse_obj(json_dict)
    mock.assert_called_once_with(db, 1, body)
    assert response.status_code == 201
