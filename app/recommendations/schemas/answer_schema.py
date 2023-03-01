from datetime import datetime

from pydantic import BaseModel


class AnswerBase(BaseModel):
    section_code: str
    is_correct: bool
    answered_at: datetime | None = None


class AnswerCreateInput(BaseModel):
    answers: list[AnswerBase]

    class Config:
        schema_extra = {
            "example": {
                "answers": [
                    {
                        "section_code": "section_code_111",
                        "is_correct": False,
                    },
                    {
                        "section_code": "section_code_222",
                        "is_correct": False,
                    },
                    {
                        "section_code": "section_code_333",
                        "is_correct": True,
                    },
                ],
            }
        }
