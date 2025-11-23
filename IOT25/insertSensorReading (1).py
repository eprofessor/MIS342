# PgP 10/31/2023
# insertSensorReading.py
# read GrovePi+ sensors-light, potentiometer, sound, ultrasonic, DHT
# Test of WSU COB Somsen 301 GrovePi+ system
# send readings to mariaDB
# separate program sensorswebpage.py writes sensor values to web page

#!/usr/bin/env python

# insert.py, inserts record into maria database 'sensor'
# table-GroveSensors
# fields- temperature(F), humidity(%), distance(inches), light(0 to 1023), sound(0 to 1023), potentiometer(0 to 1023) and timestamp
# PgP 11/5/2023

import mariadb     # avoid mysql connectors which can generate 'UTF-8 unsupported' error
from grovepi import *
import grovepi
import datetime

# Assign ports for all sensors and actuators

light_sensor = 0           # Analog  Port for Light sensor
potentiometer = 1          # Analog  Port for Rotary Angle sensor
sound_sensor = 2           # Analog  Port for Sound sensor

ultrasonic_ranger = 2      # Digital Port for Ultrasonic Ranger sensor
buzzer_pin=3               # Digital Port for Buzzer actuator
dht_sensor_port = 5        # Digital Port for DHT sensor
dht_sensor_type = 0        # use 0 for the blue-colored sensor and 1 for the white-colored sensor


# setup Mariadb Connection
mydb = mariadb.connect(       # establish database connection
  host="192.168.1.208",       # replace with RPi IP address
  user="user",
  password="user",
  database="sensor"
)

mycursor = mydb.cursor()

try:
        
    # Ultrasonic ranger
    distance = (ultrasonicRead(ultrasonic_ranger))
    inches =str(int(distance / 2.54))
    print("Ultrasonic sensor indicates distance to object is ", inches, " inches")


    # Tenperature and Humidity sensor
    [temp,hum] = dht(dht_sensor_port,dht_sensor_type)
    temperature = str(int(temp * 9 / 5 + 32))
    humidity = str(int(hum))
    print("Temperature is ", temperature, "degrees Fahrenheit, Humidity is ", humidity, " percent")


    # Light Sensor        
    light=str(grovepi.analogRead(light_sensor))
    print("Light level is ", light, " out of a 1023 maximum")                
     
            
    # Potentiometer, dial     
    adc_ref = 5  #analog to digital converter reference voltage
    grove_vcc = 5  # grove interface voltage
    full_angle = 300   # potentiometer rotates through 300 degrees
    # Read sensor value from potentiometer
    sensor_value = grovepi.analogRead(potentiometer)
    # Calculate voltage
    voltage = round((float)(sensor_value) * adc_ref / 1023, 2)
    # Calculate rotation in degrees (0 to 300)
    degrees = round((voltage * full_angle) / grove_vcc, 2)
    
    timestamp = datetime.datetime.now()

    print("Potentiometer setting = %d   voltage = %.2f   degrees = %.1f " %(sensor_value, voltage, degrees))             
            
    # Microphone
    sound_value = grovepi.analogRead(sound_sensor)
    soundValue = str(int(sound_value))
    print ("Background sound level is ", soundValue, " out of a 1023 maximum")
    
    # write readings to database
    sql = "INSERT INTO GroveSensors(Humidity, Temperature_F, Distance_Inch, Light, Sound, Potentiometer, Timestamp) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (temperature, humidity, inches, light, soundValue, degrees, timestamp)
    
    mycursor.execute(sql, val)      # insert sensor readings and time into database
    mydb.commit()    


except (IOError,TypeError) as e:
    print("Error")