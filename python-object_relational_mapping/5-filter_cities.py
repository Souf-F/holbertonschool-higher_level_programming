#!/usr/bin/python3
"""
Module that lists all cities of a state from hbtn_0e_4_usa database
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

    sql = ("SELECT cities.name FROM cities "
           "JOIN states ON cities.state_id = states.id "
           "WHERE states.name = %s "
           "ORDER BY cities.id ASC")

    cur.execute(sql, (state_name,))

    query_rows = cur.fetchall()

    cities_list = [city[0] for city in query_rows]
    print(", ".join(cities_list))

    cur.close()
    conn.close()
