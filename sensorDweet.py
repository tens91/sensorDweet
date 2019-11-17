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
    sensor_data = {}
    sensor_data["Description"] = "IOT CA Project"
    sensor_data["Time"] = getTime()
    sensor_data["Distance"] = getDistance()
    sensor_data["Luminosity"] = getLuminosity()
    sensor_data["Buton"] = getButtonState()
    print("----make dict output----")
    print(sensor_data)
    print("returning sensor_data")
    return sensor_data
    print("------------------------")

    
def post(sensor_data):
    dweet_thing = "x15011887_2019-test"
    # remove test for prod version
    print(dweepy.dweet_for(dweet_thing, sensor_data))

while True:
    try:
        sensor_data = makeDict();
        post(sensor_data)
        print(sensor_data)
        time.sleep(2)

    except IOError:
        print(IOError)

    except KeyboardInterrupt:
        exit()

    except e:
        print(e)
