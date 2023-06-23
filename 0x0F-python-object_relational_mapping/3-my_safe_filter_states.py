#!/usr/bin/python3
"""
    Script that safely filters states protecting against sql injections
"""


import MySQLdb
import sys


def display_info():
    """
      Function that lists all the states
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database
    )
    cur = db.cursor()
    cur.execute(
        'SELECT * FROM states WHERE name LIKE BINARY %(name)s \
            ORDER BY states.id ASC', {
                'name': sys.argv[4]
            }
    )
    result = cur.fetchall()

    for rows in result:
        print(rows)

    cur.close()
    db.close()


if __name__ == "__main__":
    display_info()
