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


@app.post("/v1/accounts", status_code=201)
def create_accounts(accounts: list[schemas.AccountCreate], db: Session = Depends(get_db)) -> str:
    crud.create_accounts(db=db, accounts=accounts)
    return "created"
