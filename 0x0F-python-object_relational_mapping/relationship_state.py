#!/usr/bin/python3
"""
    script that improves the State model
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    This class defines a state by various attributes
    Attributes:
      __tablename__(str): The name of the table in the database
      id(int) will be the id of the table and it will be the primary key
      name(str) will be the name of the state and it can't be null
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    def __str__(self):
        """returns a string representation of the instance"""
        return "{}: {}".format(self.id, self.name)
