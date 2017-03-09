#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    find = sys.argv[4]
    for row in cursor.fetchall():
        if (row[1] == find):
            print(row)
    db.close()
    cursor.close()
