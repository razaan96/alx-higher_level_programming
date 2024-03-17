#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    curs = conn.cursor()
    curs.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = curs.fetchall()
    for row in query_rows:
        if row[1].startswith("N"):
            print(row)
    curs.close()
    conn.close()
