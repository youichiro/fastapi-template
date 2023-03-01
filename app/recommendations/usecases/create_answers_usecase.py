from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app import models
from app.recommendations.schemas import answer_schema


def exec(db: Session, account_id: int, body: answer_schema.AnswerCreateInput):
    if db.query(models.Account).filter(models.Account.id == account_id).first() is None:
        raise HTTPException(status_code=404, detail=f"Not found account id: {account_id}.")

    new_answers = []
    for answer in body.answers:
        new_answer = models.Answer(
            account_id=account_id,
            section_code=answer.section_code,
            is_correct=answer.is_correct,
            answered_at=answer.answered_at,
        )
        new_answers.append(new_answer)

    try:
        db.add_all(new_answers)
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise e
