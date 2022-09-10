#!/usr/bin/python3
"""
    A script that prints the State object
    with the name passed as an argumentt
"""

if __name__ == '__main__':
    from model_state import Base, State
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    user = sys.argv[1]
    pw = sys.argv[2]
    db_name = sys.argv[3]
    st_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, pw, db_name, pool_pre_ping=True))
    Base.metadata.create_all(engine)

    session = Session(engine)

    state_rq = session.query(State).order_by(State.id).filter(
                        State.name == st_name).first()

    if state_rq:
        print('{}'.format(state_rq.id))
    else:
        print("Not found")

    session.close()
