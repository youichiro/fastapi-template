import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app import main, models


class MockTestingSession(Session):
    def commit(self):
        self.flush()
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
        yield db
        db.commit()

    main.app.dependency_overrides[main.get_db] = override_get_db

    yield db

    db.rollback()
    db.close()
