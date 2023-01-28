from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas, usecases
from .database import SessionLocal, engine
from .usecases import create_account_usecase

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/v1/accounts", status_code=201, responses={
    404: {"description": "Not found admin_account"},
    429: {"description": "Too many account length"},
    400: {"description": "Account already exists."},
})
def create_accounts(body: schemas.AccountCreateInput, db: Session = Depends(get_db)) -> str:
    """アカウント一括登録API"""
    create_account_usecase.exec(db=db, body=body)
    return "created"
