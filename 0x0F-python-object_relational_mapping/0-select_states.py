#!/usr/bin/python3
"""
    A python script that  lists all states from the database hbtn_0e_0_usa
"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    user_name = sys.argv[1]
    pass_word = sys.argv[2]
    data_base = sys.argv[3]

    cnx = MySQLdb.connect(
            user=user_name,
            passwd=pass_word, db=data_base, host='localhost', port=3306)

    work_space = cnx.cursor()
    work_space.execute("SELECT * FROM states ORDER BY states.id ASC;")
    rows = work_space.fetchall()

    for row in rows:
        print(row)
