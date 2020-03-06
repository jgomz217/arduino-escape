#import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BOARD)
numSensors = 5
listOfSensorVals = [0] * numSensors
outList = [6,7,8,9,10]
inList = [1,2,3,4,5]
GPIO.setup(outList, GPIO.OUT)
GPIO.setup(inList, GPIO.IN)

def rodsPlaced(l):
    for i in l:
        if(i==0):
            return False
    return True

while(1):
    if(rodsPlaced(listOfSensorVals)):
        os.system("mosquitto_pub -h 172.16.100.26 -t \"wendigo/lazer\" -m \"clock ok\"")
        time.sleep(600)
