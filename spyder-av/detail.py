import requests
from pyquery import PyQuery as pq
import re
r = requests.get('https://407mp3.com/a/lg/6051.html')
doc = pq(r.text)
bt_url = doc('.pagecon').text()
imgs = doc('.pagecon > img').items()
for img in imgs:
    print(img.attr('src'))
print(imgs)

