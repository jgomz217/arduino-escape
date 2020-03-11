import paho.mqtt.publish as publish
import os

numOfActions = 4

def userInput():
    print("\nEnter corresponding number or Enter help to print menu again")
    command = input(">").strip()
    if(command.lower() != "help"):
        if(not command.isdigit()):
            return "Invalid"
        if(int(command) > numOfActions or int(command) == 0):
            return "Invalid"
    return command

def printMainMenu():
    print("\n-----List of available actions-----")
    menu = "1. {a}\n2. {b}\n3. {c}\n4. {d}\n5. {e}\n6. {f}".format(a="Open laser cabinet",e="Print sofa image",c="Open TV drawer",f="Reboot PI's",d="CLose TV drawer",b="Close laser cabinet")
    print(menu)

def runCommand(num):
    path = "~/Desktop/testPrint.txt"
    if(num == 1):
        print("Opening cabinet")
        publish.single("wendigo/laser", "cabinet ok", hostname="172.16.100.11")
    if(num == 5):
        print("Printing sofa image")
        os.system("lp -d Canon_MG3600_series -o sides=one-sided ~/Desktop/testPrint.txt")
    if(num == 3):
        print("Opening TV drawer")
        publish.single("wendigo/tv", "tv ok", hostname="172.16.100.11")
    if(num == 6):
        print("Rebooting PI's")
        publish.single("wendigo/laser", "force reboot", hostname="172.16.100.11")
        publish.single("wendigo/tv", "force reboot", hostname="172.16.100.11")
        publish.single("wendigo/cabinet", "force reboot", hostname="172.16.100.11")
    if(num == 2):
        print("Closing cabinet")
        publish.single("wendigo/cabinet", "cabinet close", hostname="172.16.100.11")
    if(num == 4):
        print("Closing TV")
        publish.single("wendigo/tv", "tv close", hostname="172.16.100.11")

printMainMenu()
while(1):
    com = userInput()
    if(com == "Invalid"):
        print("Invalid command. Enter corresponding number.")
        printMainMenu()
    else:
        runCommand(int(com))
