#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.id, cities.name, states.name FROM states\
        JOIN cities ON cities.state_id = states.id ORDER BY cities.id"
    )
    counter = 0
    find = sys.argv[4]
    for row in cursor.fetchall():
        if row[2] == find:
            if (counter > 0):
                print(", ", end="")
            print("{:s}".format(row[1]), end="")
            counter += 1
    print()
    db.close()
    cursor.close()
