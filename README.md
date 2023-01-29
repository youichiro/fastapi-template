# New CALE
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
make setup_development_db
make setup_test_db
```

## Setup FastAPI
### on local
```sh
# install poetry
curl -sSL https://install.python-poetry.org | python3 - --version 1.3.2

# install dependencies
poetry install --no-root

# run fastapi server
poetry run uvicorn app.main:app --reload
```

### on docker-compose
wip

## Test
```sh
poetry run pytest # or make pytest
```

## Dependency management
```sh
# add to main group
porty add xxx

# add to test group
porty add --group test xxx
```

## Migration
```sh
# go to alembic.ini directory
cd db

# generate a new version refer to model definitions
poetry run alembic revision --autogenerate -m "version comment"

# migrate
poetry run alembic upgrade head

# show history
poetry run alembic history
```

## TODOs
- fastapiのdocker-compose
- CI


## Memo
- アカウントトークン
  - いらない
- admin_accountsの認証dependencies
  - いらない
- admin accountは手動で作る
