import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker

from app import main, models


class MockTestingSession(Session):
    # refer to: https://www.rhoboro.com/2021/02/27/fastapi-sqlalchemy-dbtest.html
    def commit(self):
        self.flush()
        self.expire_all()


class MockErrorTestingSession(Session):
    def commit(self):
        raise SQLAlchemyError("mock testing session error")


def _create_testing_session_local(do_raise_error=False):
    db_user = "root"
    db_password = os.environ["MYSQL_ROOT_PASSWORD"]
    db_host = os.environ["MYSQL_HOST"]
    db_port = os.environ["MYSQL_PORT"]
    db_name = os.environ["MYSQL_TEST_DATABASE"]
    sqlalchemy_database_url = f"mysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

    engine = create_engine(sqlalchemy_database_url)
    sessionmaker_class = MockTestingSession if not do_raise_error else MockErrorTestingSession
    TestingSessionLocal = sessionmaker(class_=sessionmaker_class, autocommit=False, autoflush=False, bind=engine)
    return engine, TestingSessionLocal


@pytest.fixture
def db():
    engine, TestingSessionLocal = _create_testing_session_local()
    models.Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()

    def override_get_db():
        yield db
        db.commit()

    main.app.dependency_overrides[main.get_db] = override_get_db

    yield db

    db.rollback()
    db.close()


@pytest.fixture
def error_db():
    engine, TestingSessionLocal = _create_testing_session_local(do_raise_error=True)
    models.Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()

    def override_get_db():
        yield db
        db.commit()

    main.app.dependency_overrides[main.get_db] = override_get_db

    yield db

    db.rollback()
    db.close()
