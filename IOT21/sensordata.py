import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.1.200",
  user="pi",
  password="W1n0nA",
  database="sensor"
)

mycursor = mydb.cursor()

sql = "INSERT INTO dht(temp, humidity VALUES (%s, %s)"
val = ("John", "Highway 21")  # change this array to values from DHT

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
