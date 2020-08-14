import requests
from pyquery import PyQuery as pq
import logging
import os 
import re

logging.basicConfig(level=logging.INFO,
                format='%(asctime)s - %(levelname)s: %(message)s')


BASIC_URL = 'http://hsck6.com/vodtype/8-{bin}.html'
INITAL_URL = 'http://hsck6.com{href}'
name = ""
total = 0
current = 0
PATH = '/Users/liuduwei/.spyder/spyder-av/spyder-yellowstore/'

def scrape_page(url):
    logging.info('scrape %s begging',url)
    i = 0
    try:
        r = requests.get(url)
        while i<5:
            if r.status_code == 200:
                return r.text
            logging.error('get a invalid status code %s while scraping %s,try again (tried %s times)',r.status_code,url,i)
            i += 1
    except requests.RequestException:
        logging.error('error occured in scraping %s',url,exc_info = True)

def scrape_index(bin):
    url = BASIC_URL.format(bin = bin)
    return scrape_page(url)


def parse_index(html):
    global name
    doc = pq(html)
    contents = doc('.stui-vodlist__box > a')
    for content in contents.items():
        name = str(content.attr('title'))+'.ts'
        href = content.attr('href')
        yield href

def scrape_detail(url):
    url = INITAL_URL.format(href=url)
    return scrape_page(url)

def parse_detial(html):
    global total
    global current
    doc = pq(html)
    content = doc('.stui-player__video').text()
    m3u8_url = re.search('(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?',re.sub('[\\\\]',"",content)).group()
    m3u8 = scrape_page(m3u8_url)
    total = re.search('(([0-9]*).ts)\\n#EXT-X-ENDLIST',m3u8).group(2)
    for number in range(int(total)+1):
        ts_sub = str(number).zfill(4)+'.ts'
        current = number
        ts_url = re.sub('index.m3u8',ts_sub,m3u8_url)
        ts = scrape_ts(ts_url)
        yield ts

def scrape_ts(url):
    logging.info('scrape %s begging',url)
    i = 0
    try:
        r = requests.get(url)
        while i<5:
            if r.status_code == 200:
                return r.content
            logging.error('get a invalid status code %s while scraping %s,try again (tried %s times)',r.status_code,url,i)
            i += 1
    except requests.RequestException:
        logging.error('error occured in scraping %s',url,exc_info = True)
        
def save_data(name,ts):
    logging.info('save begin')
    file = open(name,'ab')
    try:
        file.write(ts)
    except TypeError:
        logging.info('TypeError occur try again')
    file.close()
    logging.info('data save successfully!  (%s/%s)', current,total)

def main():
    for bin in [1,2]:
        index_html = scrape_index(bin)
        for detail_hrefs in parse_index(index_html):
            detail_html = scrape_detail(detail_hrefs)
            if os.path.exists(PATH+name):
                logging.info('%s is already scraped,skip it',name) 
                continue
            for t_s in parse_detial(detail_html):
                    save_data(name,t_s)
    logging.info('scrape done')

if __name__=="__main__":
    main()




    

        













