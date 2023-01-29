import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from ..models import Base
from app.main import app, get_db


@pytest.fixture
def test_db():
    db_user = "root"
    db_password = os.environ["MYSQL_ROOT_PASSWORD"]
    db_host = os.environ["MYSQL_HOST"]
    db_port = os.environ["MYSQL_PORT"]
    db_name = os.environ["MYSQL_TEST_DATABASE"]
    sqlalchemy_database_url = f"mysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

    engine = create_engine(sqlalchemy_database_url)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)

    def override_get_db():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    # table_names = [table.name for table in Base.metadata.sorted_tables]

