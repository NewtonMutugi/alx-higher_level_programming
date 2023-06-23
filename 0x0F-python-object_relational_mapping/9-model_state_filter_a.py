#!/usr/bin/python3
"""
  script that lists all State objects that contain the letter a from the
  database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states():
    """
      lists all State objects that contain the letter a from the
      database hbtn_0e_6_usa
    """
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).filter(State.name.like('%a%'))\
            .order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()


if __name__ == "__main__":
    list_states()
