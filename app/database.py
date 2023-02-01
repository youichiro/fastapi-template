import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

db_user = os.environ["MYSQL_USER"]
db_password = os.environ["MYSQL_PASSWORD"]
db_host = os.environ["MYSQL_HOST"]
db_port = os.environ["MYSQL_PORT"]
db_name = os.environ["MYSQL_DATABASE"]
sqlalchemy_database_url = f"mysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(sqlalchemy_database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
