#!/usr/bin/python3
"""
    A script that adds the State object 'Louisiana'
    to the data base hbtn_0e_6_usa
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

    new_state = State()
    new_state.name = 'Louisiana'
    session.add(new_state)
    session.commit()

    print(new_state.id)
