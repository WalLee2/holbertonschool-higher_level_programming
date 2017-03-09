#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    check = "SELECT * FROM states WHERE name = '{:s}'\
    ORDER BY id ASC".format(sys.argv[4])
    cursor.execute(check)
    for row in cursor.fetchall():
        if (row[1] == sys.argv[4]):
            print (row)
    db.close()
    cursor.close()
