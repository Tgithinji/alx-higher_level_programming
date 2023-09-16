#!/usr/bin/python3
"""
This script lists all states with a name starting with N
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    Script not executed when imported
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
        sq = 'SELECT * FROM states WHERE name LIKE "N%" ORDER BY states.id ASC'
        cursor.execute(sq)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print('Error:', e)
