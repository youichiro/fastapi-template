from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app import models
from app.database import SessionLocal, engine
from app.schemas import account_schema, answer_schema
from app.usecases import create_accounts_usecase, create_answers_usecase

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", status_code=200)
def hello() -> str:
    return "Hello World!"


@app.post(
    "/v1/accounts",
    status_code=201,
    responses={
        404: {"description": "Not found admin_account"},
        429: {"description": "Too many account length"},
        400: {"description": "Account already exists."},
    },
)
def create_accounts(body: account_schema.AccountCreateInput, db: Session = Depends(get_db)) -> str:
    """アカウント一括登録API"""
    create_accounts_usecase.exec(db, body)
    return "created"


@app.post("/v1/accounts/{account_id}/answers", status_code=201)
def create_answers(account_id: int, body: answer_schema.AnswerCreateInput, db: Session = Depends(get_db)) -> str:
    """解答履歴登録API"""
    create_answers_usecase.exec(db, account_id, body)
    return "created"
