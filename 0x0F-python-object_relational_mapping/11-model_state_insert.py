#!/usr/bin/python3
"""
  script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def add_state():
    """
        adds the State object “Louisiana” to the database hbtn_0e_6_usa
    """
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    new_state = "Louisiana"
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(name=new_state)
    session.add(state)
    session.commit()
    print("{}".format(state.id))
    session.close()


if __name__ == "__main__":
    add_state()
