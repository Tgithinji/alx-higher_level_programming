#!/usr/bin/python3
"""
This script lists all cities from a database with their
respective states
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    execute only as main program
    """
    try:
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )

        cursor = db.cursor()
        cursor.execute("SELECT cities.id, cities.name, states.name "
                       "FROM cities LEFT JOIN states "
                       "ON states.id = cities.state_id")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error:", e)
