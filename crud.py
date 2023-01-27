from sqlalchemy.orm import Session

from . import models, schemas


def get_admin_accounts(db: Session):
    return db.query(models.AdminAccount).all()


def get_account(db: Session, admin_account_id: int, external_user_id: str):
    account = db.query(models.Account).filter(
        models.Account.admin_account_id == admin_account_id,
        models.Account.external_user_id == external_user_id
    ).first()
    return account


def create_account(db: Session, account: schemas.AccountCreate):
    new_account = models.Account()
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return new_account

