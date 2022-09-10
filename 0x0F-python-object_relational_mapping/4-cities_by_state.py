#!/usr/bin/python3
"""
     A script that lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    user_name = sys.argv[1]
    pass_word = sys.argv[2]
    db_name = sys.argv[3]

    cnx = MySQLdb.connect(
            user=user_name,
            passwd=pass_word,
            db=db_name,
            host='localhost',
            port=3306)

    work_space = cnx.cursor()
    work_space.execute("SELECT cities.id, cities.name, states.name\
            FROM cities INNER JOIN states ON cities.state_id=states.id;")

    rows = work_space.fetchall()
    for row in rows:
        print(row)

    work_space.close()
    cnx.close()
