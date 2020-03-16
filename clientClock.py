import paho.mqtt.publish as publish
import RPi.GPIO as GPIO

clientName = "Clock"
ipAddress = "192.168.1.15"
mess = "clock ok"

def on_connect(client,userdata,flags,rc):
    print("Connecting with broker...")
    client.subscribe("wendigo/clock")

def on_message(client,userdata,msg):
    message = str(msg.payload)
    if(message[2:14] == "force reboot"):
        print("Rebooting " + clientName + "...")
        os.system("sudo reboot")

client = mqtt.Client(clientName)
client.on_connect = on_connect
client.on_message = on_message
client.connect(ip_address, 1883, 60)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup()
GPIO.output()

def clockLogic():
    client.publish("wendigo/lasers", mess)
    return True

client.loop_forever()
