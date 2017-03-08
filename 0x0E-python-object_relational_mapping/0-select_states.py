#!/usr/bin/python3
import MySQLdb
import sys
db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cursor = db.cursor()
cursor.execute("SELECT * FROM states")
for row in cursor.fetchall():
    print (row)
db.close()
