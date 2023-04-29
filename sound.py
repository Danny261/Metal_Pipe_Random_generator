import random
from playsound import playsound
import time
from Benutzeroberfläche import dialog, dialog2,version

i = 0


def soundplay():
    while i <= 10:
        number = random.randint(int(dialog), int(dialog2))
        time.sleep(number)
        print("The Pipe Fell after: "+str(number)+" seconds")
        if version == "n":
            playsound("Pipe.mp3")
        elif version == "e":
            playsound("PipeR.mp3")
        else:
           quit()


