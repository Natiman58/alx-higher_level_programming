#!/usr/bin/python3
"""
    A script that deletes all State objects with a name letter 'a'
    from the db hbtn_0e_6_usa
"""

if __name__ == '__main__':
    from model_state import Base, State
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy.schema import Table

    user = sys.argv[1]
    pw = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, pw, db_name, pool_pre_ping=True))
    Base.metadata.create_all(engine)

    session = Session(engine)

    for obj in session.query(State).filter(State.name.like('%a%')):
        session.delete(obj)

    session.commit()
    session.close()
