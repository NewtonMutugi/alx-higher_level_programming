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
    """
    changes the name of a State object from the database hbtn_0e_6_usa
    """

    username = argv[1]
    password = argv[2]
    database = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter_by(id=2).first()
    state.name = 'New Mexico'
    session.commit()
    session.close()


if __name__ == '__main__':
    change_state()
