import sys
import json
import os

try:
    import urllib3
except ImportError:
    os.system('cmd /k "pip install urllib3"')
try:
    import bs4
except ImportError:
    os.system('cmd /k "pip install bs4"')
try:
    import requests
except ImportError:
    os.system('cmd /k "pip install requests"')
try:
    import asyncio
except ImportError:
    os.system('cmd /k "pip install asyncio"')

class Youtube():
    def search(self, type, search):
        fullcontent = ('http://www.youtube.com/results?search_query=' + search)
        text = requests.get(fullcontent).text
        soup = bs4.BeautifulSoup(text, 'html.parser')
        img = str(soup.find_all('img')[9]["src"])
        div = [ d for d in soup.find_all('div') if d.has_attr('class') and 'yt-lockup-dismissable' in d['class']]
        a = [ x for x in div[0].find_all('a') if x.has_attr('title')]
        title = (a[0]['title'])
        a0 = [ x for x in div[0].find_all('a') if x.has_attr('title') ][0]
        url = ('http://www.youtube.com'+a0['href'])
        if type == "url":
            return url
        if type == "title":
            return title
        if type == 'search':
            return search
    

if __name__ == "__main__":
    exit()
