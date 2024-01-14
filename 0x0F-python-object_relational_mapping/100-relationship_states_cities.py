#!/usr/bin/python3

""" A script that prints the first State object from the database hbtn_0e_6_usa """
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    newState = State(name="California")
    newCity = City(name="San Francisco")
    newState.cities.append(newCity)

    session.add(newState)
    session.add(newCity)
    session.commit()
