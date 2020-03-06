import paho.mqtt.client as mqtt
#import RPi.GPIO as GPIO
import time

client_name = "Laser"
ip_address = "172.16.100.26"

def checkInput():
    print("When done enter 1")
    mess = input(">").strip()
    if(mess == "1"):
        return True
    else:
        print("Invalid command")
        return False

def on_connect(client, userdata, flags, rc):
    print("Connected to broker")
    client.subscribe("wendigo/laser")

def on_message(client, userdata, msg):
    done = False
    print(msg.topic + " " + str(msg.payload))
    message = str(msg.payload)
    if(message[2:10] == "clock ok"):
        #implement laser part 1 here
        while not done:
            done = checkInput()
        #turn off laser part 1 here
        #turn on  laser part 2 here
        done = False
        while not done:
            done = checkInput()
        client.publish("wendigo/cabinet", "cabinet ok")
        print("Done processing message")
    if(message[2:14] == "force reboot"):
        print("Rebooting " + client_name)
        #os.system("sudo reboot")

client = mqtt.Client(client_name)
client.on_connect = on_connect
client.on_message = on_message
client.connect(ip_address, 1883, 60)
client.loop_forever()
