from fastapi import FastAPI

from app import models
from app.accounts.router import router as account_router
from app.database import engine
from app.recommendations.router import router as recommendation_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/", status_code=200)
def hello() -> str:
    return "Hello World!"


app.include_router(account_router)
app.include_router(recommendation_router)
