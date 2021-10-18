import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

try:
    DATABASE_URL = os.environ['DATABASE_URL']
    engine = create_engine(
        DATABASE_URL,
    )
    SessionLocal = sessionmaker(
        bind=engine,
        autocommit=False,
        autoflush=False,
    )

except KeyError as e:
    pass


Base = declarative_base()


def create_tables():
    Base.metadata.create_all(bind=engine)
