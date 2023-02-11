from pydantic import BaseModel


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
