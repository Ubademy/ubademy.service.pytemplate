import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.environ['DATABASE_URL']
#SQLALCHEMY_DATABASE_URL = "postgresql://danpxnytdjrlid:7ea37df76603ce3b520d6097304e8325169d9633ab66885a8e191e1cc346de0d@ec2-34-233-64-238.compute-1.amazonaws.com:5432/d1qd37afqppvqr"

engine = create_engine(
    DATABASE_URL,
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)


Base = declarative_base()


def create_tables():
    Base.metadata.create_all(bind=engine)
