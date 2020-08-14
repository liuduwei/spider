import re
import requests
from lxml import etree
def getip():
    url = "http://proxylist.fatezero.org/proxy.list"
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52'
            }
    resp = requests.get(url, headers=headers)
    text = resp.text
    ssl = re.findall(r'"type": "(.*?)"', text)
    ip = re.findall(r'"host": "(.*?)"', text)
    port = re.findall(r'"port": (.*?),', text)
    realurl = ('\n'.join([str(i[0]) + str("://") + str(i[1]) + str(":") + str(i[2]) for i in zip(ssl, ip, port)]))
    print(realurl)
getip()
