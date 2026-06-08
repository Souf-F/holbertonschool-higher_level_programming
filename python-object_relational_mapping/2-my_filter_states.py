#!/usr/bin/python3
"""
Module that lists all states with a name matching user input from database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cur = conn.cursor()

    sql = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cur.execute(sql)

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
