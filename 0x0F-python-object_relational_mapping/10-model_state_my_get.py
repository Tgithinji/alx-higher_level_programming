#!/usr/bin/python3
"""
This module lists the first State objects from a database
"""
from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    url = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}'
    engine = create_engine(url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    found = False
    for instance in session.query(State).filter(State.name==argv[4]).order_by(State.id):
        if instance.name == argv[4]:
            print(f"{instance.id}")
            found = True
    if found is False:
        print('Not found')

    session.close()
