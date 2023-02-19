# fastapi-template
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


## Install dependencies
```sh
# install poetry
curl -sSL https://install.python-poetry.org | python3 - --version 1.3.2

# install dependencies
poetry install --no-root
```

## Setup databases
```sh
docker compose up -d db
make setup_development_db
make setup_test_db
```

## Run on local
```sh
# run fastapi server
poetry run uvicorn app.main:app --reload

# run tests
poetry run pytest # or make pytest
```

## Run on docker compose
```sh
# run fastapi server
docker compose up -d app

# run tests
docker compose exec app poetry run pytest
```

## Dependency management
```sh
# add to main group
poerty add xxx

# add to test group
poerty add --group test xxx

# add to dev group
poetry add --group dev xxx
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


## GitHub Actions
- [actionlint](https://github.com/rhysd/actionlint)
  - check for GitHub Actions workflow files
- [isort](https://pycqa.github.io/isort/)
  - check python imports order
- [black](https://github.com/psf/black)
  - check python code format
- [flake8](https://flake8.pycqa.org/en/latest/)
  - check python code style
- [mypy](https://mypy.readthedocs.io/en/stable/index.html)
  - check python static types
- [pytest](https://docs.pytest.org/en/7.2.x/)
  - check python tests


## TODO
- ASGI configuration
- Nginx service
- read-only database
- database connection pooling
- [Locust](https://docs.locust.io/en/stable/) for performance testing
- logging
- views
- authentication
- admin service
