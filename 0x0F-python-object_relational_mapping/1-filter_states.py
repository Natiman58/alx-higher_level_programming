#!/usr/bin/python3
"""
    lists all the states that start with the letter 'N'
    in the data base hbtn_0e_0_usa.
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
    work_space.execute(""" SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id ASC; """)
    rows = work_space.fetchall()
    for row in rows:
        print(row)
