import requests
from pyquery import PyQuery as pq
import re
#([0-9]*.ts)\\n#EXT-X-ENDLIST
#[//]
#匹配m3u8url
#提取反扒处理m3u8url
r = requests.get('http://hsck6.com/vodplay/1077-1-1.html')
doc = pq(r.text)
print('   ')