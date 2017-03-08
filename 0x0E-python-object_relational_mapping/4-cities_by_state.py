#!/usr/bin/python3
import sys
import MySQLdb

db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cursor = db.cursor()
cursor.execute(
"SELECT cities.id, cities.name, states.name FROM states JOIN cities ON cities.state_id = states.id ORDER BY cities.id"
)
for row in cursor.fetchall():
    print(row)
db.close()
