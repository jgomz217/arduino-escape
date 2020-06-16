import time
import simpleaudio
from pydub import AudioSegment
from math import hypot as h

error = AudioSegment.from_wav("wallHit.wav")

def getDist(p1,p2):
    return h(p2[0]-p1[0], p2[1]-p1[1])


def getDb(oldMax,oldMin,newMax,newMin,oldValue):
    oldRange = (oldMax-oldMin)
    newRange = (newMax-newMin)
    return (((oldValue - oldMin) * newRange) / oldRange) + newMin

def getAudio(coords,goal,ping):
    dist = getDist(coords, goal)
    dbLevel = getDb(10.6,0,-10,30,dist)
    return ping + dbLevel

def playAudio(aSeg,n):
    playback = simpleaudio.play_buffer(
        aSeg.raw_data, 
        num_channels=aSeg.channels, 
        bytes_per_sample=aSeg.sample_width, 
        sample_rate=aSeg.frame_rate
    )
    time.sleep(n)
    playback.stop()
