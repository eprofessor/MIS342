# adafruit.py, sending RPi sensor data to cloud
# Import library and create instance of REST client

# 
# USB flash drive must be named "MYDATA"
# make sure config.txt file is on USB flashdrive plugged into RPi
# config.txt must contain Adafruit Username on line 1, feedkey on line 2, and NOTHING else
#

f = open('/media/pi/MYDATA/config.txt', 'r')
line1=f.readline() # read the username
line2=f.readline() # read the key

line1=line1.strip()
line2=line2.strip()
print('username: ', line1, '\nfeedkey: ',line2)

from Adafruit_IO import Client
from grovepi import *

#aio = Client(config.username, config.key)  #signup for Adafruit.io account, get username and key
aio = Client(line1,line2)
dht_sensor_port = 5

#print(config.username, config.key)

while True:
    try:
        [temp,hum ] = dht(dht_sensor_port,0)       #Get the temperature and Humidity from the DHT sensor
        print("temp =", temp, "C\thumidity =", hum,"%")     
        t = str(temp)
        h = str(hum)
        # Send the value 100 to a feed called 'Foo'.
        aio.send('temperature', t)
        aio.send('humidity', h)
        time.sleep(120)
        
        # Retrieve the most recent value from the feeds.
        # Access the value by reading the `value` property on the returned Data object.
        # Note that all values retrieved from IO are strings so you might need to convert
        # them to an int or numeric type if you expect a number.
        
        # Troubleshooting-uncomment to try and retrieve recent data
        #data = aio.receive('temperature')
        #print('Received value: {0}'.format(data.value))
        #data = aio.receive('humidity')
        #print('Received value: {0}'.format(data.value))
        
    except (IOError,TypeError) as e:
        print("Error")
