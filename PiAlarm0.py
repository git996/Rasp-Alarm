#script by iamnewdev/git996

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import threading
from time import time,sleep
from pygame import mixer
from random import *


def main():
   
   runAlarm()
   
 
def alarmTime():
    t1 = '07:30:00'
    t2 = '13:18:30'
    return t2
	
def tones():
    url0 ="https://www.pandora.com/stations/"
    
    return url0;
	
def runAlarm():

    timenow = datetime.now()       
    al1 = str(timenow.strftime("%H:%M:%S"))
    print(al1)
       
    if al1== alarmTime():    

        x = randint(1,6)
        mixer.init()
        mixer.music.load('C:/Users/New/Dropbox/Apps/New folder/song%d.mp3'% x)
        mixer.music.play()            
        print('ALARM! ALARM!')    
        sleep(180)           
        mixer.music.fadeout(7000)
        sleep(7) 
        mixer.quit()
        print('Mixer Ended')
            
            
    if al1 != alarmTime():
        print("Systems Normal")
    sleep(1)
    runAlarm()
     
     

	
if __name__ == "__main__":
    # execute only if run as a script
    main() 
