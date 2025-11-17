# insert.py, inserts record into MySQL database
# PgP 9/5/2022

import datetime
import mysql.connector     # RPi uses version 8.0.29 or earlier, otherwise 'UTF-8 unsupported' error
from grovepi import *

dht_sensor_port = 5        # Digital Port for DHT sensor
dht_sensor_type = 0        # use 0 for the blue-colored sensor-DHT11 and 1 for the white-colored sensor-DHT22

mydb = mysql.connector.connect(       # establish database connection
  host="192.168.1.15",
  user="user",
  password="user",
  database="sensor"
)

mycursor = mydb.cursor()

while True:
    try:
        [temp,hum] = dht(dht_sensor_port,dht_sensor_type)    # ready DHT11 sensor data
        
        temperature = str(int(temp * 9 / 5 + 32))
        humidity = str(int(hum))         
        timestamp = datetime.datetime.now()
        
        sql = "INSERT INTO dht(temperature, humidity, timestamp) VALUES (%s, %s, %s)"
        val = (temperature, humidity, timestamp)
        
        mycursor.execute(sql, val)      # insert sensor readings and time into database
        mydb.commit()
        
        print("Temp:  ", temperature, "Humidity: ",humidity, "Time: ",timestamp)
        time.sleep(60)    # pause a minute      

    except (IOError,TypeError) as e:
        print("Error")