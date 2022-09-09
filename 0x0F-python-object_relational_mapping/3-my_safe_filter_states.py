#!/usr/bin/python3
"""
    A script that is safe from sql injection
    using parameterized statements; place holders.
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    user_name = sys.argv[1]
    pass_word = sys.argv[2]
    db_name = sys.argv[3]
    arg = sys.argv[4]

    cnx = MySQLdb.connect(
            user=user_name,
            passwd=pass_word,
            db=db_name,
            host='localhost',
            port=3306)

    work_space = cnx.cursor()
    work_space.execute(""" SELECT * FROM states WHERE name LIKE BINARY %s\
            ORDER BY states.id ASC;""", (arg, ))

    rows = work_space.fetchall()
    for row in rows:
        print(row)

    work_space.close()
    cnx.close()
