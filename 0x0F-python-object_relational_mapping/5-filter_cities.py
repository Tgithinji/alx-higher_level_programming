#!/usr/bin/python3
"""
This script takes a name of states and lists all cities
of that state from a database with their
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
        cursor.execute("SELECT cities.name "
                       "FROM cities INNER JOIN states "
                       "ON states.id = cities.state_id "
                       "WHERE states.name = %s", (sys.argv[4],))
        rows = cursor.fetchall()
        cities = [row[0] for row in rows]
        print(', '.join(cities))

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error:", e)
