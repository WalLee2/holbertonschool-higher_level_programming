#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import State, Base
import MySQLdb

if __name__ == '__main__':
    u_input = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(u_input)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    objects = session.query(State).first()
    if objects:
        print("{}: {}".format(objects.id, objects.name))
    else:
        print("Nothing")
