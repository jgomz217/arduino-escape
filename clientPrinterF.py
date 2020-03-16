import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

bool done = False
client_name = "Printer"
ip_address = "172.16.100.11"

GPIO.setup(11,GPIO.IN)
GPIO.setup(13,GPIO.IN)
GPIO.setup(15,GPIO.IN)
GPIO.setup(17,GPIO.IN)
GPIO.setup(19,GPIO.IN)

while(!done):
    
def on_connect(client,userdata,flags,rc):
    print("Connecting with Broker")
    client.subscribe("wendigo/printer")

def on_message(client, userdata, msg):
    message = str(msg.payload)
    if(message[2:12] == "printer ok"):
        print("Printing picture...")
        os.system("lp -d Canon_MG3600_series -o sides=one-sided /home/pi/Desktop/test.txt")
    if(message[2:14] == "force reboot"):
        print("Rebooting " + client_name)
        os.system("sudo reboot")

client = mqtt.Client(client_name)
client.on_connect = on_connect
client.on_message = on_message
client.connect(ip_address, 1883, 60)
client.loop_forever()
