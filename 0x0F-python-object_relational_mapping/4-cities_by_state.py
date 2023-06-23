#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa """

import MySQLdb
import sys


def list_cities():
    """ Function lists all cities"""

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        db=database,
        passwd=password
    )
    cur = db.cursor()
    cur.execute(
        'SELECT cities.id, cities.name, states.name \
        FROM cities JOIN states ON cities.state_id = states.id \
        ORDER BY cities.id ASC'
    )
    result = cur.fetchall()

    for rows in result:
        print(rows)

    cur.close()
    db.close()


if __name__ == "__main__":
    list_cities()
