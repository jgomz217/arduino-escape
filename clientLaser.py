import paho.mqtt.publish as publish
import RPi.GPIO as GPIO


def clockLogic():
    #implement clock puzzle here
    return 0

def laserLogic():
    #implement laser part 1 here
    while not done:
        done = checkInput()
        #turn off laser part 1 here
        #turn on  laser part 2 here
        done = False
    while not done:
        done = checkInput()
        publish.single("wendigo/cabinet", "cabinet ok")
        #turn off lasers part 2 here

def checkInput():
    print("When done enter 1")
    mess = input(">").strip()
    if(mess == "1"):
        return True
    else:
        print("Invalid command")
        return False
