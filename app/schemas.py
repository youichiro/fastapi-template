from datetime import datetime

from pydantic import BaseModel


class AdminAccount(BaseModel):
    id: int
    admin_name: str
    admin_secret: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class AccountBase(BaseModel):
    admin_account_id: int
    external_user_id: str
    school_id: int


class AccountCreate(AccountBase):
    pass

    class Config:
        schema_extra = {
            "example": {
                "admin_account_id": 1,
                "external_user_id": "example_external_user_id",
                "school_id": 1,
            }
        }


class Account(AccountBase):
    id: int
    admin_account: AdminAccount
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
