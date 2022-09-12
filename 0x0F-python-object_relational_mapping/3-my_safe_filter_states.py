#!/usr/bin/env python3
"""displays all values in the states table of
   hbtn_0e_0_usa where name matches the argument
   and is free from sql injection."""

if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s\
                ORDER BY states.id ASC;".format(sys.argv[4]))
    row = cur.fetchall()

    for items in row:
        print(items)
