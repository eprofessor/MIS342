# insert.py, test to clear records from MySQL database
# PgP 9/7/2022 works ok

import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.1.15",
  user="user",
  password="user",
  database="sensor"
)

mycursor = mydb.cursor()


sql = "DELETE FROM dht;"
mycursor.execute(sql)
mydb.commit()
