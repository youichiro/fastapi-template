from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/v1/admin_accounts", response_model=list[schemas.AdminAccount]):
def get_admin_accounts(db: Session = Depends(get_db)):
    admin_accounts = crud.get_admin_accounts(db)
    return admin_accounts


@app.post("/v1/accounts", response_model=schemas.Account)
def create_account(account: schemas.AccountCreate, db: Session = Depends(get_db)):
    account = crud.get_account(db, account.admin_account_id, account.external_user_id)
    if account:
        HTTPException(s
            tatus_code=400,
            detail=f"Account admin_account_id: {account.admin_account_id}, external_user_id: {account.external_user_id} already exists."
        )
    return crud.create_account(db=db, account=account)

