import numpy as np
import re

dirpath = '/home/natalie/Documents/Projects/podxiv/'
textpath = 'sample_abstract.txt'

with open (dirpath+textpath, "r") as file:
    abstract = file.read().replace('\n', '')

def clean_latex(text):
    no_dollars = re.sub('\$|\\|', ' ', text)
    no_backslashes = re.sub('\\\\', '', no_dollars)
    return no_backslashes

clean_abstract = clean_latex(abstract)

with open(dirpath+'clean_sample_abstract.txt', 'w') as text_file:
    text_file.write(clean_abstract)
