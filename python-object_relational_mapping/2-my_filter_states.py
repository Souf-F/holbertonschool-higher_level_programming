#!/usr/bin/python3
"""Module getting all states and filter by user input"""

import sys
import MySQLdb

if __name__ == "__main__":
    
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )
    
    cursor = db.cursor()  # je créer le stylo
    cursor.execute(
        """SELECT *
        FROM states
        WHERE BINARY name = '{}'
        ORDER BY id ASC""".format(state_name_searched)
    )
    
    states_list = cursor.fetchall()
    for state in states_list:
        print(state)
        
    cursor.close()
    db.close()