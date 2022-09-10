#!/usr/bin/python3
"""
     a script that takes in the name of a state as an argument\
             and lists all cities of that state,¸
             using the database hbtn_0e_4_usa
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    user_name = sys.argv[1]
    pass_word = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    cnx = MySQLdb.connect(
            user=user_name,
            passwd=pass_word,
            db=db_name,
            host='localhost',
            port=3306)

    work_space = cnx.cursor()
    work_space.execute("SELECT cities.name FROM cities\
            LEFT JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s ORDER BY cities.id ASC;", (state_name, ))

    rows = work_space.fetchall()
    for row in rows:
        print(row)

    work_space.close()
    cnx.close()
