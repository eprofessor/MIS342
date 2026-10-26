# Import library and create instance of REST client.
from Adafruit_IO import Client
from grovepi import *

# Adafruit IO info at:  https://io.adafruit.com/
aio = Client('username', 'key')  #signup for Adafruit.io account, get username and key

dht_sensor_port = 5

while True:
    try:
        [temp,hum ] = dht(dht_sensor_port,0)       #Get the temperature and Humidity from the DHT sensor
        print("temp =", temp, "C\thumidity =", hum,"%")     
        t = str(temp)
        h = str(hum)
        # Send the values 100 to a feed called 'Foo'.
        aio.send('temperature', t)
        aio.send('humidity', h)
        time.sleep(10)
        
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