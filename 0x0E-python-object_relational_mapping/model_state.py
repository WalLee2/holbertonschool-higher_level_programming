#!/usr/bin/python3
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column("states", Integer, primary_key=True, autoincrement=True)
    name = Column("states", String(128), nullable=False)
