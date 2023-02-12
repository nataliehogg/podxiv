'''
we use pydetex to change the latex abstracts to plain text suitable for text-to-speech parsing.
'''
import numpy as np
import pydetex.pipelines as pyp

dirpath = '/home/natalie/Documents/Projects/podxiv/'
textpath = 'sample_abstract.txt'

with open (dirpath+textpath, "r") as file:
    text = file.read().replace('\n', ' ')

clean_abstract = pyp.simple(text)

with open(dirpath+'clean_sample_abstract.txt', 'w') as text_file:
    text_file.write(clean_abstract)
