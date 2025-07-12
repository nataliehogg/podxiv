'''
text-to-speech from saved files
'''

from gtts import gTTS
from datetime import datetime, timedelta

timestamp = (datetime.now() - timedelta(days=2)).strftime('%Y%m%d')

dirpath = r'/home/nataliehogg/Documents/Projects/podxiv/'
textpath = 'text/output-{}.md'.format(timestamp)


with open (dirpath+textpath, "r") as file:
    text = file.read().replace('\n', '')

tts = gTTS(text=text, lang='en')
tts.save(dirpath+'audio/abstracts-{}.mp3'.format(timestamp))
