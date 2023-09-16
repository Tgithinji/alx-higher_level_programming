#!/usr/bin/python3
"""
This module contains a script that lists all states
from a database
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
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print('Error:', e)
