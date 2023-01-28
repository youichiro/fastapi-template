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
