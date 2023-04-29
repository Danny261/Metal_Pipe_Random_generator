from sound import soundplay
from Benutzeroberfläche import dialog, dialog2

x = 1
low_sec = dialog
high_sec = dialog2

print("input your time in seconds in which the metal pipe will be randomly dropped")
print("'r' for random Time between 10 sec and a hour, 'm' for 30 Minutes, 'h' for an hour and 't' for two hours")
print("'n' for the standard metal pipe sound and 'e' for the earrape version")
print("The metal pipe will be dropped randomly in a interval of "+str(low_sec)+" to "+str(high_sec)+" seconds")
print("starting now!")

i = 0
while x <= 10:
    soundplay()



