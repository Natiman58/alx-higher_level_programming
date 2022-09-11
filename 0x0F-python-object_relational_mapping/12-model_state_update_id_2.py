#!/usr/bin/python3
"""
    A script that changes the name of a State object
    where id = 2 to 'New Mexico'
    from the database hbtn_0e_6_usa
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

    rename_obj = session.query(State).filter(State.id == 2).first()
    rename_obj.name = 'New Mexico'
    session.commit()
    session.close()
