import requests
from pyquery import PyQuery as pq


BASIC_URL = 'http://hsck6.com/vodtype/8-{bin}.html'
INITAL_URL = 'http://hsck6.com{href}'

response = requests.get(BASIC_URL.format(bin=1))
print(response.status_code)

#parse_indexurl

#stui-vodlist__box    div
#stui-vodlist clearfix   ul
doc = pq(response.text)


contents = doc('.stui-vodlist__box > a')
for content in contents.items():
    print(content.attr('href'))
    print(content.attr('title'))
    print(content.attr('data-original'))#cover
    print(content('span').text())
    print(' ')
    print(' ')

INDEX_URL = INDEX_URL.format(href=content.attr('href'))


