import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app import main, models
from app.dependencies import get_db


class MockTestingSession(Session):
    # refer to: https://www.rhoboro.com/2021/02/27/fastapi-sqlalchemy-dbtest.html
    def commit(self):
        self.flush()

    def rollback(self):
        self.expire_all()


@pytest.fixture
def db():
    db_user = "root"
    db_password = os.environ["MYSQL_ROOT_PASSWORD"]
    db_host = os.environ["MYSQL_HOST"]
    db_port = os.environ["MYSQL_PORT"]
    db_name = os.environ["MYSQL_TEST_DATABASE"]
    sqlalchemy_database_url = f"mysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

    engine = create_engine(sqlalchemy_database_url)
    TestingSessionLocal = sessionmaker(class_=MockTestingSession, autocommit=False, autoflush=False, bind=engine)
    models.Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()

    def override_get_db():
        try:
            yield db
        except Exception as e:
            db.rollback()
            raise e

    main.app.dependency_overrides[get_db] = override_get_db

    yield db

    db.rollback()
    db.close()
