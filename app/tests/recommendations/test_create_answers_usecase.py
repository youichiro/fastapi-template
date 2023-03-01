import pytest
from fastapi import HTTPException

from app import models
from app.recommendations.schemas import answer_schema
from app.recommendations.usecases import create_answers_usecase


def _create_account(db):
    db_admin_account = db.query(models.AdminAccount).first()
    new_account = models.Account(
        admin_account_id=db_admin_account.id,
        external_user_id="dummy_account",
        school_id=1,
    )
    db.add(new_account)
    db.commit()
    return new_account


def test_exec(db):
    """
    正常に解答データが作られること
    """
    account = _create_account(db)
    json_dict = {
        "answers": [
            {
                "section_code": "section_code_111",
                "is_correct": False,
            },
            {
                "section_code": "section_code_222",
                "is_correct": True,
            },
        ],
    }
    body = answer_schema.AnswerCreateInput.parse_obj(json_dict)
    create_answers_usecase.exec(db, account.id, body)

    db_answers = db.query(models.Answer).all()

    assert len(db_answers) == 2
    assert db_answers[0].section_code == "section_code_111"
    assert db_answers[0].is_correct is False
    assert db_answers[1].section_code == "section_code_222"
    assert db_answers[1].is_correct is True


def test_exec_no_account(db):
    """
    accountが存在しない場合、404を返すこと
    """
    json_dict = {
        "answers": [
            {
                "section_code": "section_code_111",
                "is_correct": False,
            },
            {
                "section_code": "section_code_222",
                "is_correct": True,
            },
        ],
    }
    body = answer_schema.AnswerCreateInput.parse_obj(json_dict)

    with pytest.raises(HTTPException) as e:
        create_answers_usecase.exec(db, 100, body)
    assert e.value.status_code == 404
