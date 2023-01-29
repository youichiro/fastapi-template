## Versions
- python: 3.11.1
- fastapi: 0.89.1
- mysql: 8.0.32

## Load environment variables
```sh
brew install direnv
direnv allow . # load .envrc, then load .env
```

Inspired by https://blog.p1ass.com/posts/direnv-dotenv/

## Setup DB
```sh
docker compose up -d db
make setup_test_db
```

## Setup FastAPI
### on local
```sh
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### on docker-compose
wip

## Test
```sh
pytest # or make pytest
```

## TODOs
- fastapiのdocker-compose
- poetry
- CI


## Memo
- アカウントトークン
  - いらない
- admin_accountsの認証dependencies
  - いらない
- admin accountは手動で作る
