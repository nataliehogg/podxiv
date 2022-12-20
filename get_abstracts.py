import urllib, urllib.request

# url = 'http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1'
# url = 'http://export.arxiv.org/api/query?id_list'
#
# data = urllib.request.urlopen(url)
# print(data.read().decode('utf-8'))

url_base = 'https://arxiv.org/e-print/'
url_bib_base = 'http://adsabs.harvard.edu/cgi-bin/bib_query?arXiv:'
postings = 'https://arxiv.org/list/astro-ph/new'

data = urllib.request.urlopen(postings)
# ids = []
# print('Postings loaded. Processing list...')
# for line in data:
#     cline = line.decode('utf-8')
#     if "arXiv:" in line.decode('utf-8'):
#         start = cline[cline.find("arXiv:"):]
#         ids.append(start[6:start.find("</a>")])
# print(len(ids), 'IDs in todays new astro-ph listing')
#
# print(ids)

print(data.read().decode('utf-8'))
