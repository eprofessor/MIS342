# PgP 10/31/2023
# sensorReading.py
# read GrovePi+ sensors to check status
# light, potentiometer, sound, ultrasonic, DHT
# Test of WSU COB Somsen 301 GrovePi+ system
# Press button to start test of all sensors and actuators
# send readings to mariaDB


#!/usr/bin/env python

import time
import grovepi
import sys
import datetime

from grovepi import *

# Assign ports for all sensors and actuators

light_sensor = 0           # Analog  Port for Light sensor
potentiometer = 1          # Analog  Port for Rotary Angle sensor
sound_sensor = 2           # Analog  Port for Sound sensor

ultrasonic_ranger = 2      # Digital Port for Ultrasonic Ranger sensor
buzzer_pin=3               # Digital Port for Buzzer actuator
#button=4                   # Digital Port for Button actuator
dht_sensor_port = 5        # Digital Port for DHT sensor
dht_sensor_type = 0        # use 0 for the blue-colored sensor and 1 for the white-colored sensor
#ledbar = 6                 # Digital Port for LED Bar actuator
#relay = 8                  # Digital Port for Relay
#pinMode(button, "INPUT")   # Assign Button as input
#pinMode(buzzer_pin,"OUTPUT")  #Assign Buzzer as output
#pinMode(relay,"OUTPUT")    # Assign Relay as output
pinMode(potentiometer,"INPUT")  #Assign Potentiometer as input
pinMode(sound_sensor,"INPUT")  # Assign Microphone as input


        
# Test 2-ultrasonic ranger
distance = (ultrasonicRead(ultrasonic_ranger))
inches =str(int(distance / 2.54))
print("Ultrasonic sensor indicates distance to object is ", inches, " inches")


# Test 3- Tenperature and Humidity sensor
[ temp,hum ] = dht(dht_sensor_port,dht_sensor_type)
temperature = str(int(temp * 9 / 5 + 32))
humidity = str(int(hum))
print("Temperature is ", temperature, "degrees Fahrenheit, Humidity is ", humidity, " percent")


# Test 7, light sensor        
light=str(grovepi.analogRead(light_sensor))
print("Light level is ", light, " out of a 1023 maximum")                
 
        
# Test 8, potentiometer     
adc_ref = 5  #analog to digital converter reference voltage
grove_vcc = 5  # grove interface voltage
full_angle = 300   # potentiometer rotates through 300 degrees
# Read sensor value from potentiometer
sensor_value = grovepi.analogRead(potentiometer)
# Calculate voltage
voltage = round((float)(sensor_value) * adc_ref / 1023, 2)
# Calculate rotation in degrees (0 to 300)
degrees = round((voltage * full_angle) / grove_vcc, 2)

print("Potentiometer setting = %d   voltage = %.2f   degrees = %.1f " %(sensor_value, voltage, degrees))             
        
# Test 9, microphone
sound_value = grovepi.analogRead(sound_sensor)
soundValue = str(int(sound_value))
print ("Background sound level is ", soundValue, " out of a 1023 maximum")        