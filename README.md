## Versions
- python: 3.11.1
- fastapi: 0.89.1
- mysql: 8.0.32

## Setup DB
```sh
docker compose up -d db
```

## Setup FastAPI
### on local
```sh
pip install -r requirements.txt
export SQLALCHEMY_DATABASE_URL="mysql://cale:password@0.0.0.0:3306/cale_development"
uvicorn app.main:app --reload
```

### on docker-compose
wip

## TODOs
- fastapiのdocker-compose
- テスト
- admin_accountsの認証dependencies

## Non-TODOs
- アカウントトークン
