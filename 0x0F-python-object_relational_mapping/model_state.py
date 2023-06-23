#!/usr/bin/python3
"""This module defines a class State that inherits from declarative_base"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """This class defines a state by various attributes"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    def __init__(self, name):
        """This method initializes a state with a name"""
        self.name = name
