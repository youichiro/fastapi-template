import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from ..models import Base
from app.main import app, get_db


@pytest.fixture
def test_db():
    engine = create_engine(os.environ["SQLALCHEMY_DATABASE_URL"])
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

