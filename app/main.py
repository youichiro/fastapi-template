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


@app.post("/v1/accounts", status_code=201, responses={
    404: {"description": "Not found admin_account"},
    400: {"description": "Account already exists."},
})
def create_accounts(body: schemas.AccountCreateInput, db: Session = Depends(get_db)) -> str:
    """アカウント一括登録API"""
    crud.create_accounts(db=db, body=body)
    return "created"
