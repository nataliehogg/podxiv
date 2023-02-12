from gtts import gTTS
import numpy as np

type = 'clean_'

dirpath = '/home/natalie/Documents/Projects/podxiv/'
textpath = type + 'sample_abstract.txt'

with open (dirpath+textpath, "r") as file:
    text = file.read().replace('\n', '')

tts = gTTS(text=text, lang='en')
tts.save(dirpath+type+'abstract.mp3')
