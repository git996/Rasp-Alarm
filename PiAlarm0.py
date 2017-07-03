#script by iamnewdev/git996

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import threading
import sys
from time import time,sleep
from pygame import mixer
from random import *
import schedule


def main():
   schedule.every().day.at("19:01").do(runAlarm)
   while True:
      schedule.run_pending()
      sleep(1)
   





def runAlarm():
    def alarm():
        x = randint(1,119)

        mixer.init()
        mixer.music.load('C:/Users/New/Music/im/iMusic/song (%d).mp3'% x)
        mixer.music.play()
        print('ALARM!')
        sleep(240)
        mixer.music.fadeout(7000)
        sleep(7)
        mixer.quit()
        print('Closing Mixer')

      

    alarm()



if __name__ == "__main__":
    # execute only if run as a script
    main()
