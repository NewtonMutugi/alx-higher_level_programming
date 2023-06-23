#!/usr/bin/python3
"""
    script that prints the State object with the name passed as argument
    from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def fetch_state():
    """
        prints the State object with the name passed as argument from
        the database hbtn_0e_6_usa
    """
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == state_name).first()
    if state is None:
        print("Not found")
    else:
        print("{}".format(state.id))
    session.close()


if __name__ == "__main__":
    fetch_state()
