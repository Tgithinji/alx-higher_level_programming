#!/usr/bin/python3
"""
This module contains a script that lists all states
that match the given name from a database
and its safe from MySQL injections
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """
    execute if the script is only run as main program
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
        cursor.execute("SELECT * FROM states WHERE name = %s"
                       "ORDER BY states.id ASC", (sys.argv[4],))
        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print('Error:', e)

    finally:
        cursor.close()
        db.close()
