#!/usr/bin/python3
"""
    script that changes the name of a State object
    from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def change_state():
    """ changes the name of a State object from the database hbtn_0e_6_usa
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
        argv[4]: state id to update
        argv[5]: name to update
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2],
                                   argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.id == argv[4]).first()
    state.name = argv[5]
    session.commit()
    session.close()


if __name__ == "__main__":
    change_state()
