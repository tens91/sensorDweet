import time
import datetime
import grovepi
import dweepy

"""
Three sensors to be used for collecting data which
will be emitted to Dweet.io using HTTP Posti
 * Ultrasonic Ranger
 * Button
 * Light Sensor
"""

# mapping light sensor to analog port 0 (A0)
light_sensor = 0
grovepi.pinMode(light_sensor,"INPUT")


# mapping button to digital port 2 (D2)
button = 2
grovepi.pinMode(button,"INPUT")

# mapping ultrasonic ranger to ditital port 3 (D3)
ultrasonic_ranger = 3

def getTime():
    return time.time()
    
def getLuminosity():
    return grovepi.analogRead(light_sensor)

def getDistance():
    return grovepi.ultrasonicRead(ultrasonic_ranger)

def getButtonState():
    return grovepi.digitalRead(button)

def makeDict():
    dict = {}
    dict["Description"] = "IOT CA Project"
    dict["Time"] = getTime()
    dict["Distance"] = getDistance()
    dict["Luminosity"] = getLuminosity()
    dict["Buton"] = getButton()
    return dict

print(dict)

"""
def post(sensors_data)
    dweet_thing = "x15011887_2019-test"
    # remove test for prod version
    print(dweepy.dweet_for(dweet_thing, sensors_data))
"""
