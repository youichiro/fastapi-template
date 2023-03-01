import pytest
from fastapi import HTTPException

from app import models
from app.accounts.schemas import account_schema
from app.accounts.usecases import create_accounts_usecase


def test_exec(db):
    """
    正常にアカウントデータが作られること
    """
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
    body = account_schema.AccountCreateInput.parse_obj(json_dict)
    create_accounts_usecase.exec(db, body)

    db_accounts = db.query(models.Account).all()

    assert len(db_accounts) == 2
    assert db_accounts[0].admin_account_id == 1
    assert db_accounts[0].external_user_id == "example_external_user_1"
    assert db_accounts[0].school_id == 1
    assert db_accounts[1].admin_account_id == 1
    assert db_accounts[1].external_user_id == "example_external_user_2"
    assert db_accounts[1].school_id == 2


def test_exec_no_admin_account(db):
    """
    admin_accountが存在しない場合、404を返すこと
    """
    json_dict = {
        "admin_secret": "not_exist_secret",
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
    body = account_schema.AccountCreateInput.parse_obj(json_dict)

    with pytest.raises(HTTPException) as e:
        create_accounts_usecase.exec(db, body)
    assert e.value.status_code == 404


def test_exec_exceed_max_account_num(db, mocker):
    """
    最大アカウント数を超過する場合、429を返すこと
    """
    mocker.patch("app.accounts.usecases.create_accounts_usecase.MAX_ACCOUNT_NUM", 3)
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
            {
                "external_user_id": "example_external_user_3",
                "school_id": 3,
            },
            {
                "external_user_id": "example_external_user_4",
                "school_id": 4,
            },
        ],
    }
    body = account_schema.AccountCreateInput.parse_obj(json_dict)

    with pytest.raises(HTTPException) as e:
        create_accounts_usecase.exec(db, body)
    assert e.value.status_code == 429


def test_exec_exist_account(db):
    """
    既にアカウントが存在する場合、400を返すこと
    """
    new_account = models.Account(
        admin_account_id=1,
        external_user_id="example_external_user_1",
        school_id=1,
    )
    db.add(new_account)
    db.commit()

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
    body = account_schema.AccountCreateInput.parse_obj(json_dict)

    with pytest.raises(HTTPException) as e:
        create_accounts_usecase.exec(db, body)
    assert e.value.status_code == 400
