# insertDistance.py, inserts record into MySQL database from ultrasonic sensor
# PgP 10/29/2023

import datetime
import mariadb     # RPi uses version 8.0.29 or earlier, otherwise 'UTF-8 unsupported' error
from grovepi import *

ultrasonic_ranger = 2        # Digital Port for Ultrasonic Ranger sensor

mydb = mariadb.connect(       # establish database connection
  host="10.19.0.39",
  user="user",
  password="user",
  database="sensor"
)

mycursor = mydb.cursor()

while True:
    try:      
        distance = (ultrasonicRead(ultrasonic_ranger)) # read ultrasonic
        inches = str(int(distance / 2.54))    # convert centimeter reading to inches
             
        timestamp = datetime.datetime.now()
        
        sql = "INSERT INTO distance(inches, timestamp) VALUES (%s, %s)"
        val = (inches, timestamp)
        
        mycursor.execute(sql, val)      # insert sensor readings and time into database
        mydb.commit()
        
        print("Distance:  ", inches, "    Time: ",timestamp)
        time.sleep(5)    # pause a minute      

    except (IOError,TypeError) as e:
        print("Error")