'''
Get abstracts and save them; https://github.com/daveshap/weekly_arxiv
'''

import requests
from datetime import datetime, timedelta
from xml.etree import ElementTree as ET

dirpath = r'/home/nataliehogg/Documents/Projects/podxiv/'

days = 2 # needs to be 2 because today is Saturday; for weekdays it's 1

timestamp = (datetime.now() - timedelta(days=days)).strftime('%Y%m%d')

base_url = 'http://export.arxiv.org/api/query?search_query=cat:astro-ph.CO+AND+submittedDate:[{day}0000+TO+{day}2359]&max_results=1000'

url = base_url.format(day=timestamp)

response = requests.get(url)

# Parse the XML response
root = ET.fromstring(response.content)

# Namespace dictionary to find elements
namespaces = {'atom': 'http://www.w3.org/2005/Atom', 'arxiv': 'http://arxiv.org/schemas/atom'}

# Open the output file with UTF-8 encoding
with open(dirpath+"text/output-{}.md".format(timestamp), "w", encoding='utf-8') as file:
    # Iterate over each entry in the XML data
    for entry in root.findall('atom:entry', namespaces):
        # Extract and write the title
        title = entry.find('atom:title', namespaces).text
        title = ' '.join(title.split())  # Replace newlines and superfluous whitespace with a single space
        file.write(f"Title: {title}; ")

        # Extract and write the authors
        authors = entry.findall('atom:author', namespaces)
        # for author in authors:
        name = authors[0].find('atom:name', namespaces).text
        file.write(f"First author: {name}; ")

        # Extract and write the summary
        summary = entry.find('atom:summary', namespaces).text
        file.write(f"Abstract: {summary}")