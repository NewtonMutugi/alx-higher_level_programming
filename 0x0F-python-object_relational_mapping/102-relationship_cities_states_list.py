#!/usr/bin/python3
"""
    script that lists all City objects from the database hbtn_0e_101_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def list_cities():
    """Prints all City objects from the database hbtn_0e_101_usa.
    """
    username = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(username, password, database),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()

    for city in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()


if __name__ == "__main__":
    list_cities()
