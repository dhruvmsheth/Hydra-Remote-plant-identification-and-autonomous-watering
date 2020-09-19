import sys
import Adafruit_DHT
import time

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
    time.sleep(1)
if temperature < 8:
    success = 0
if (temperature > 8 and temperature < 15):
    success = 1
if (temperature > 15 and temperature < 21):
    warning = 0
if temperature > 21:
    error = 0
if humidity < 70:
    success1 = 0
if (humidity > 70 and humidity < 75):
    success1 = 1
if (temperature > 75 and temperature < 85):
    warning1 = 0
if temperature > 85:
    error1 = 0    
