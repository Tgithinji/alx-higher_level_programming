#!/usr/bin/python3
"""
This module changes the name of a state object from a
database
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    url = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}'
    engine = create_engine(url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).filter(State.id == 2).first()
    instance.name = 'New Mexico'
    session.commit()
    session.close()
