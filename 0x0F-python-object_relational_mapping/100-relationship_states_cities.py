#!/usr/bin/python3
"""
    script that creates the State “California” with the City
    “San Francisco” from the database hbtn_0e_100_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State


def add_state_city():
    """
        script that creates the State “California” with the
        City “San Francisco” from the database hbtn_0e_100_usa
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()


if __name__ == '__main__':
    add_state_city()
