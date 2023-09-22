#!/usr/bin/python3
"""
This module lists all City objects from a given database
"""
from sys import argv
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    url = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}'
    engine = create_engine(url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(City).join(State).\
            order_by(City.id).all():
        print(f'{instance.state.name}: ({instance.id}) {instance.name}')
    session.close()
