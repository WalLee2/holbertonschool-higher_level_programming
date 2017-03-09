#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if __name__ == '__main__':
    u_input = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(u_input)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    switch = 0
    for objects in session.query(State):
        if (objects.name == sys.argv[4]):
            print("{}".format(objects.id))
            switch = 1
    if (switch == 0):
        print("Not found")
