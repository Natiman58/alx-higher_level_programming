#!/usr/bin/python3
"""
    A script that prints the first 'State' obj
    from db hbtn_0e_6_usa
"""

if __name__ == '__main__':
    from model_state import Base, State
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    user = sys.argv[1]
    pw = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, pw, db_name, pool_pre_ping=True))
    Base.metadata.create_all(engine)

    session = Session(engine)

    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    session.close()
