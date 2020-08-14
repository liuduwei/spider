import requests
from pyquery import PyQuery as pq


r = requests.get('https://407mp3.com/a/lg/index.html')
doc = pq(r.text)
hrefs = doc('.mnewest ul li > a').items()
for href in hrefs:
    print(href)
    print(href.attr('href'))
    print(href('img').attr('src'))
    print(href('img').attr('title'))
    print("###############")
print(type(href))

