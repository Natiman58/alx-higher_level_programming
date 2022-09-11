#!/usr/bin/python3
"""
    A module tha contains the class definition of City
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
        inherites from Base class
        in the mode_state.py
    """
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, unique=True, primary_key=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
