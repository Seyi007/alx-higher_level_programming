#!/usr/bin/env python3
"""lists all states with a name starting
   with N in the database hbtn_0e_0_usa"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%'ORDER BY states.id ASC;""")
    row = cur.fetchall()

    for items in row:
        print(items)
