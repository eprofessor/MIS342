# insert.py, test to select record from MySQL database
# PgP 9/5/2022 got to work, had to set 

import mysql.connector    # must be version 8.0.29; 8.0.30 errors out with 'utf8 unsupported'

mydb = mysql.connector.connect(
  host="192.168.1.15",
  user="user",
  password="user",
  database="sensor"
)

mycursor = mydb.cursor()

# Enforce UTF-8 for the connection.
#mycursor.execute('SET NAMES latin1')
#mycursor.execute("SET CHARACTER SET latin1")
#mycursor.execute("SET character_set_connection=latin1")

mycursor.execute("SELECT * FROM dht;")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
    

print(mycursor.rowcount, "records selected")
