import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient
from sqlalchemy.exc import SQLAlchemyError

from app.main import app
from app.recommendations.schemas import answer_schema

client = TestClient(app)


def test_create_answers(db, mocker):
    mock = mocker.patch("app.recommendations.usecases.create_answers_usecase.exec", return_value=None)
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
    response = client.post("/v1/accounts/1/answers", json=json_dict)

    body = answer_schema.AnswerCreateInput.parse_obj(json_dict)
    mock.assert_called_once_with(db, 1, body)
    assert response.status_code == 201


def test_create_answers_with_404(db, mocker):
    mock = mocker.patch("app.recommendations.usecases.create_answers_usecase.exec", side_effect=HTTPException(status_code=404, detail=f"error_detail"))
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
    response = client.post("/v1/accounts/1/answers", json=json_dict)

    body = answer_schema.AnswerCreateInput.parse_obj(json_dict)
    mock.assert_called_once_with(db, 1, body)
    assert response.status_code == 404
