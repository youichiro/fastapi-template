from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.recommendations.schemas import answer_schema
from app.recommendations.usecases import create_answers_usecase

router = APIRouter()


@router.post("/v1/accounts/{account_id}/answers", status_code=201)
def create_answers(account_id: int, body: answer_schema.AnswerCreateInput, db: Session = Depends(get_db)) -> str:
    """解答履歴登録API"""
    create_answers_usecase.exec(db, account_id, body)
    return "created"
