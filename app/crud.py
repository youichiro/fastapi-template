from fastapi import HTTPException
from sqlalchemy.orm import Session

from . import models, schemas


def get_admin_account(db: Session, admin_account_id: int):
    return db.query(models.AdminAccount).filter(models.AdminAccount.id == admin_account_id).first()

def get_admin_accounts(db: Session):
    return db.query(models.AdminAccount).all()


def get_account(db: Session, admin_account_id: int, external_user_id: str):
    return db.query(models.Account).filter(
        models.Account.admin_account_id == admin_account_id,
        models.Account.external_user_id == external_user_id
    ).first()


def create_account(db: Session, account: schemas.AccountCreate):
    db_admin_account = get_admin_account(db, account.admin_account_id)
    if not db_admin_account:
        raise HTTPException(
            status_code=404,
            detail=f"Not found admin_account id: {account.admin_account_id}."
        )

    db_account = get_account(db, account.admin_account_id, account.external_user_id)
    if db_account:
        raise HTTPException(
            status_code=400,
            detail=f"Account admin_account_id: {account.admin_account_id}, external_user_id: {account.external_user_id} already exists."
        )

    new_account = models.Account(
        admin_account_id=account.admin_account_id,
        external_user_id=account.external_user_id,
        school_id=account.school_id,
    )
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return new_account

