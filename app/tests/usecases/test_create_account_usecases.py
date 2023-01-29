from app import schemas, models
from app.usecases import create_account_usecases


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
        ]
    }
    body = schemas.AccountCreateInput.parse_obj(json_dict)
    create_account_usecases.exec(db, body)

    db_accounts = db.query(
        models.Account.admin_account_id, models.Account.external_user_id, models.Account.school_id
    ).filter(
        models.Account.external_user_id.in_(['example_external_user_1', 'example_external_user_2'])
    ).all()

    assert len(db_accounts) == 2
    assert db_accounts[0].admin_account_id == 1
    assert db_accounts[0].external_user_id == 'example_external_user_1'
    assert db_accounts[0].school_id == 1
    assert db_accounts[1].admin_account_id == 1
    assert db_accounts[1].external_user_id == 'example_external_user_2'
    assert db_accounts[1].school_id == 2
