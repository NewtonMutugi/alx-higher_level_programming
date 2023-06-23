#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa """

import MySQLdb
import sys


def list_cities():
    """ Function lists all cities of that state """

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        db=database,
        passwd=password
    )
    cur = db.cursor()
    cur.execute(
        'SELECT cities.name FROM cities \
            JOIN states ON cities.state_id = states.id \
            WHERE states.name = %(name)s \
            ORDER BY cities.id ASC', {
                'name': state_name
            }
    )
    result = cur.fetchall()

    for rows in result:
        print(rows[0], end=", " if rows != result[-1] else "\n")

    cur.close()
    db.close()


if __name__ == "__main__":
    list_cities()
