#!/usr/bin/python3
"""
    A script that prints all City objects
    in the db hbtn_0e_14_usa
"""

if __name__ == '__main__':
    import sys
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine
    from sqlalchemy.schema import Table
    from model_state import Base, State
    from model_city import City

    user = sys.argv[1]
    pw = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, pw, db_name, pool_pre_ping=True))
    Base.metadata.create_all(engine)

    session = Session(engine)

    for state, city in session.query(State, City)\
            .filter(City.state_id == State.id)\
            .order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
