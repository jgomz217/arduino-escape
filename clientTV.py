import paho.mqtt.client as mqtt
#import RPi.GPIO as GPIO
import os

relay = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay,GPIO.OUT)
GPIO.output(relay,GPIO.HIGH)

client_name = "TV"
ip_address = "172.16.100.26"

def on_connect(client,userdata,flags,rc):
    print("Connected with result code " + str(rc))
    client.subscribe("wendigo/tv")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    message = str(msg.payload)
    if(message[2:12] == "tv ok"):
        print("Unlocking cabinet...")
        GPIO.output(relay,GPIO.LOW)
        time.sleep(600)
        GPIO.output(relay,GPIO.HIGH)
    if(message[2:14] == "force reboot"):
        print("Rebooting " + client_name)
        #os.system("sudo reboot")

client = mqtt.Client(client_name)
client.on_connect = on_connect
client.on_message = on_message
client.connect(ip_address, 1883, 60)
client.loop_forever()
