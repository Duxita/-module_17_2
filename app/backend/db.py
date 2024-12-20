from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import sessionmaker, DeclarativeBase


engine = create_engine('sqlite:///taskmanager.db', echo=True)

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass