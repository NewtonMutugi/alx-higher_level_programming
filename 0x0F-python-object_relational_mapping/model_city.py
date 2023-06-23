#!/usr/bin/python3
"""defines a class City that inherits from declarative_base"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


class City(Base):
    """
    This class defines a city by various attributes
    Attributes:
      __tablename__(str): The name of the table in the database
      id(int) will be the id of the table and it will be the primary key
      name(str) will be the name of the state and it can't be null
      state_id(int) will be the id of the state and it can't be null
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)

    def __str__(self):
        """returns a string representation of the instance"""
        return "{}: {}".format(self.id, self.name)
