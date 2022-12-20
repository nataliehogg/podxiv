import pyttsx3
import numpy as np

dirpath = '/home/natalie/Documents/Projects/podxiv/'
textpath = 'sample_abstract.txt'

with open (dirpath+textpath, "r") as file:
    text = file.read().replace('\n', '')

engine = pyttsx3.init()

engine.setProperty('rate', 100)

engine.say(text)
engine.runAndWait()
