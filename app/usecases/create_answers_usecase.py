from sqlalchemy.orm import Session

from app.schemas import answer_schema


def exec(db: Session, account_id: int, body: answer_schema.AnswerCreateInput):
    return
