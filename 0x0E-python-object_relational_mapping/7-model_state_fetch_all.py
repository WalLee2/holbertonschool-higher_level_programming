#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if __name__ == '__main__':
    u_input = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(u_input)
    Base.metadata.create_all(engine)
    # create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # create a Session
    session = Session()
    for objects in session.query(State).order_by(State.id):
        print("{}: {}".format(objects.id, objects.name))
