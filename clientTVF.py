import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import os

relay = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(relay,GPIO.OUT)
GPIO.output(relay,GPIO.HIGH)

client_name = "TV"
ip_address = "172.16.100.11"

def on_connect(client,userdata,flags,rc):
    print("Connecting with broker ")
    client.subscribe("wendigo/tv")

def on_message(client, userdata, msg):
    message = str(msg.payload)
    if(message[2:7] == "tv ok"):
        print("Unlocking TV...")
        GPIO.output(relay,GPIO.LOW)
    if(message[2:10] == "tv close"):
        print("Locking TV...")
        GPIO.output(relay,GPIO.HIGH)
    if(message[2:14] == "force reboot"):
        print("Rebooting " + client_name)
        os.system("sudo reboot")

client = mqtt.Client(client_name)
client.on_connect = on_connect
client.on_message = on_message
client.connect(ip_address, 1883, 60)
client.loop_forever()
