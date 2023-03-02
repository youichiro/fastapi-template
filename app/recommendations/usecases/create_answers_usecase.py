from fastapi import HTTPException
from sqlalchemy.orm import Session

from app import models
from app.recommendations.schemas import answer_schema


def exec(db: Session, account_id: int, body: answer_schema.AnswerCreateInput):
    db_account = db.query(models.Account).filter_by(id=account_id).one_or_none()
    if db_account is None:
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

    db.add_all(new_answers)
    db.commit()
