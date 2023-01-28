from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas, dependencies
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/v1/admin_accounts", response_model=list[schemas.AdminAccount])
def get_admin_accounts(db: Session = Depends(dependencies.get_db)):
    return crud.get_admin_accounts(db)


@app.post("/v1/accounts", response_model=schemas.Account)
def create_account(account: schemas.AccountCreate, db: Session = Depends(dependencies.get_db)):
    return crud.create_account(db=db, account=account)
