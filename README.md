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
sh db/test/import_schema.sh # dump development db tables and restore into test db
```

## Setup FastAPI
### on local
```sh
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### on docker-compose
wip

## TODOs
- テスト用DB
  - session scopeでget_dbをoverrideする
  - テスト用DB作る
  - commitをmockしてinsertしないようにする
  - refs
    - https://fastapi.tiangolo.com/advanced/testing-database/
    - https://www.rhoboro.com/2021/02/27/fastapi-sqlalchemy-dbtest.html
- fastapiのdocker-compose
- テスト
- CI

## Memo
- アカウントトークン
  - いらない
- admin_accountsの認証dependencies
  - いらない
- admin accountは手動で作る
