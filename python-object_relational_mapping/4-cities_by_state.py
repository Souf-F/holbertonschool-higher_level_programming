#!/usr/bin/python3
"""
Module that lists all cities from hbtn_0e_4_usa database with state names
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cur = conn.cursor()

    sql = ("SELECT cities.id, cities.name, states.name FROM cities "
           "JOIN states ON cities.state_id = states.id "
           "ORDER BY cities.id ASC")

    cur.execute(sql)

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
