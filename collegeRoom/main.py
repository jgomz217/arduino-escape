##TODO
## getch queue causing bugs on movement
## wont be a problem when we switch to physical buttons

import movement as m
import userIO as io
import audio as a


def main():
    player = { "location" : (0,0) }
    goal = (7,7)
    ping = a.AudioSegment.from_wav("Movement.wav")
    error = a.AudioSegment.from_wav("wallHit.wav")
    goalS = a.AudioSegment.from_wav("endGoal.wav")
    while(not m.checkGoal(player,goal)):
        dir = io.handleInput()
        #print("My current location " + str(player["location"]))
        #print("Going this way" + str(dir))
        if(m.validMove(player,dir,15)):
            nPing = a.getAudio(player["location"], goal, ping)
            a.playAudio(nPing,.75)
        else:
            #print("Hit a wall")
            a.playAudio(error, .75)
        #print("My new location " + str(player["location"]))
    a.playAudio(goalS, 5)

main()
