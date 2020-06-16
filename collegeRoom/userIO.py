import getch
#c = getch.getch() not displayed on screen
#c = getch.getche() displayed on screen

def handleInput():
    s = getch.getch()
    if(s.lower() == 'w'):
        return (0,-1)
    if(s.lower() == 'a'):
        return (-1,0)
    if(s.lower() == 's'):
        return (0,1)
    if(s.lower() == 'd'):
        return (1,0)
    else:
        return (0,0)
