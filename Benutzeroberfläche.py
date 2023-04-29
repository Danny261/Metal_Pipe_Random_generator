import tkinter as tk
from tkinter import simpledialog
import random


ROOT = tk.Tk()

ROOT.withdraw()

dialognumber = simpledialog.askstring(title="Metal pipe falling sound",
                                  prompt="1. Number r: random, m: halfn hour, h: hour, t: two hours")
ROOT.withdraw()

dialognumber2 = simpledialog.askstring(title="Metal pipe falling sound",
                                  prompt="2. Number r: random, m: halfn hour, h: hour, t: two hours")
ROOT.withdraw()

version = simpledialog.askstring(title="Metal pipe erape or not",
                                  prompt="Input 'n' for normal metal pipe sound or 'e' for earrape version")



if dialognumber == 'r':
    dialog = random.randint(10, 3600)
elif dialognumber == 'm':
    dialog = 1800
elif dialognumber == 'h':
    dialog = 3600
elif dialognumber == 't':
    dialog = 7200
else:
    dialog = dialognumber

if dialognumber2 == 'r':
    dialog2 = random.randint(10, 3600)
elif dialognumber == 'm':
    dialog2 = 1800
elif dialognumber == 'h':
    dialog2 = 3600
elif dialognumber == 't':
    dialog2 = 7200
else:
    dialog2 = dialognumber2

