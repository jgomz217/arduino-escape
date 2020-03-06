import os

numOfActions = 4

def userInput():
    print("\nEnter corresponding number or Enter help to print menu again")
    command = input(">").strip()
    if(command.lower() != "help"):
        if(not command.isdigit()):
            return "Invalid"
        if(int(command) > 4 or int(command) == 0):
            return "Invalid"
    return command

def printMainMenu():
    print("\n-----List of available actions-----")
    menu = "1. {a}\n2. {b}\n3. {c}\n4. {d}".format(a="Open cabinet for lasers",b="Print sofa image",c="Open TV drawer",d="Reboot PI's")
    print(menu)

def runCommand(num):
    path = "~/Desktop/testPrint.txt"
    if(num == 1):
        print("Turning off 2nd set")
        print("Opening cabinet")
        #os.system("mosquitto_pub -h 172.16.100.26 -t \"wendigo/laser\" -m \"cabinet ok\"")
    if(num == 2):
        print("Printing sofa image")
        print("os.system(\"lp -d Canon_MG3600_series -o sides=one-sided {}\".format(path))")
    if(num == 3):
        print("Opening TV drawer")
        #os.system("mosquitto_pub -h 172.16.100.26 -t \"wendigo/tv\" -m \"tv ok\"")
    if(num == 4):
        print("Rebooting PI's")
        #os.system("mosquitto_pub -h 172.16.100.26 -t \"wendigo/lazer\" -m \"force reboot\"")
        #os.system("mosquitto_pub -h 172.16.100.26 -t \"wendigo/tv\" -m \"force reboot\"")
        #os.system("mosquitto_pub -h 172.16.100.26 -t \"wendigo/cabinet\" -m \"force reboot\"")

printMainMenu()
while(1):
    com = userInput()
    if(com == "Invalid"):
        print("Invalid command. Enter corresponding number.")
        printMainMenu()
    else:
        runCommand(int(com))
