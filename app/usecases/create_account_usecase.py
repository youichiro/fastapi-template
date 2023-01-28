from fastapi import HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas


MAX_ACCOUNT_NUM = 500

def exec(db: Session, body: schemas.AccountCreateInput) -> None:
    db_admin_account = db.query(models.AdminAccount).filter(
        models.AdminAccount.admin_secret == body.admin_secret
    ).first()

    if not db_admin_account:
        raise HTTPException(
            status_code=404,
            detail=f"Not found admin_account secret: {body.admin_secret}."
        )

    if len(body.accounts) > MAX_ACCOUNT_NUM:
        raise HTTPException(
            status_code=429,
            detail=f"Too many account length: {len(body.accounts)}"
        )

    for account in body.accounts:
        db_account = db.query(models.Account).filter(
            models.Account.admin_account_id == db_admin_account.id,
            models.Account.external_user_id == account.external_user_id
        ).first()

        if db_account:
            raise HTTPException(
                status_code=400,
                detail=f"Account admin_account_id: {db_admin_account.id}, external_user_id: {account.external_user_id} already exists."
            )

        new_account = models.Account(
            admin_account_id=db_admin_account.id,
            external_user_id=account.external_user_id,
            school_id=account.school_id,
        )
        db.add(new_account)
    db.commit()
