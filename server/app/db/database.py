from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# TODO: create a Settings class to handle this
SQLALCHEMY_DATABASE_URL = "postgresql://admin:admin@db:5432/tech-hub-db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()