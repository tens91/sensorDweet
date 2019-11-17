import time
import datetime
import dweepy
import json
import grovepi
from grovepi import *
"""
Three sensors to be used for collecting data which
will be emitted to Dweet.io via Post request with DweePy
 * Ultrasonic Ranger
 * Button
 * Light Sensor
"""

# mapping sensors to their port
light_sensor = 0      # Analog port 0  (A0)
button = 2            # Digital port 2 (D2)
ultrasonic_ranger = 3 # Digital port 3 (D3)
led = 4               # Digital port 4 (D4)

# specifies if the sensor behaves as input 
# or output:    pinMode(pin, mode)
grovepi.pinMode(led,"OUTPUT")            
grovepi.pinMode(button,"INPUT")
grovepi.pinMode(light_sensor,"INPUT")

def getTime():
    return int(time.time())
    
# each sensor has its own method for collecting data
def getLuminosity():
    return grovepi.analogRead(light_sensor)

def getDistance():
    return grovepi.ultrasonicRead(ultrasonic_ranger)

def getButtonState():
    return grovepi.digitalRead(button)

def makeDict():
    sensor_data = {}
    sensor_data["Description"] = "IOT CA Project"
    sensor_data["Time"] = getTime()
    sensor_data["Distance"] = getDistance()
    sensor_data["Luminosity"] = getLuminosity()
    sensor_data["Button"] = getButtonState()
    return sensor_data

#print(makeDict())


# Here dweepy is used to post the data as a JSON payload


def post(sensor_data):
    digitalWrite(led,1)
    dweet_thing = "x15011887_2019"
    dweepy.dweet_for(dweet_thing, sensor_data)


while True:
    try:
        sensor_data = makeDict();
        post(sensor_data)
        print("(led on) posting data")
        print(sensor_data)
        digitalWrite(led,0)
        print("(led off) post complete")
        print("")
        time.sleep(5)

    except IOError:
        print(IOError)

    except KeyboardInterrupt:
        print("exiting application")
        exit()

    except:
        print("something is wonky")
        time.sleep(2)


