## versions
- python: 3.11.1
- fastapi: 0.89.1
- mysql: 8.0.32

## setup db
```sh
docker compose up -d db
```

## setup fastapi
### on local
```sh
pip install -r requirements.txt
export SQLALCHEMY_DATABASE_URL="mysql://cale:password@0.0.0.0:3306/cale_development"
uvicorn app.main:app --reload
```

### on docker-compose
wip

## todos
- fastapiのdocker-compose
- テスト
