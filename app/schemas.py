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
    external_user_id: str
    school_id: int


class AccountCreateInput(BaseModel):
    admin_secret: str
    accounts: list[AccountBase]

    class Config:
        schema_extra = {
            "example": {
                "admin_secret": "demo_secret",
                "accounts": [
                    {
                        "external_user_id": "example_external_user_1",
                        "school_id": 1,
                    },
                    {
                        "external_user_id": "example_external_user_2",
                        "school_id": 2,
                    },
                ],
            }
        }


class Account(AccountBase):
    id: int
    admin_account_id: int
    admin_account: AdminAccount
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
