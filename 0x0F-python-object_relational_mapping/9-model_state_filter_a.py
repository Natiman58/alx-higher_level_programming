#!/usr/bin/python3
"""
    script that lists all State objects that contain
    the letter 'a' from the database hbtn_0e_6_usa
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

    state_a = session.query(State).order_by(State.id).filter(
            State.name.contains('a'))

    if state_a:
        for state in state_a:
            print("{}:{}".format(state.id, state.name))
    else:
        print("Nothing")

    session.close()
