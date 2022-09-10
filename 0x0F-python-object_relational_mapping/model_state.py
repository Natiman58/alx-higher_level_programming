#!/usr/bin/python3
"""
    A module containing the class definition of a State
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
        Inherites from Base and stores
        into the states table in db.
    """
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True,
                unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
