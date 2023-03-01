from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.accounts.schemas import account_schema
from app.accounts.usecases import create_accounts_usecase
from app.dependencies import get_db

router = APIRouter()


@router.post(
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
