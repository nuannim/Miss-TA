import mysql.connector

import mysql.connector

cnx = mysql.connector.connect(user='scott', password='password',
                              host='sql12.freesqldatabase.com',
                              database='employees')
cnx.close()