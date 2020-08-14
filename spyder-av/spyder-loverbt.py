import requests
import pymongo
import logging
import re
from pyquery import PyQuery as pq
from urllib.parse import urljoin

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s -\%(levelname)s: %(message)s')

BASE_URL = "https://407mp3.com"
TOTAL_PAGE = 4

MONGO_CONNECTINO_STRING = "mongodb://localhost:27017"
MONGO_DB_NAME = "loverbt-bluelight"
MONGO_CONNECTION_NAME = "loverbt_bluelight"

client = pymongo.MongoClient(MONGO_CONNECTINO_STRING)
db = client[MONGO_DB_NAME]
collection = db[MONGO_CONNECTION_NAME]

def scrape_page(url):
    '''get a url
    return url's html
    '''
    logging.info("Scrape %s begin...",url)
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.content.decode('utf-8')
        logging.error("get a invalid status code %s while Scrapeing %s", r.status_code, url)
    except:
        logging.error("error occured in scrapeing %s", url, exc_info=True)


def scrape_index_url(page):
    url = f'{BASE_URL}/a/lg/index{page}.html'
    return scrape_page(url)


def parse_index_page(html):
    doc = pq(html)
    hrefs = doc('.mnewest ul li > a').items()
    for href in hrefs:
        url = urljoin(BASE_URL,href.attr('href'))
        yield url


def scrape_detail_page(url):
    return scrape_page(url)


def parse_detail(html):
    doc = pq(html)
    name = doc('.location font').text()
    img_srcs = doc('.pagecon img').items()
    imgs = []
    for img in img_srcs:
        imgs.append(img.attr('src'))
    url_bt_match = re.search('[a-zA-z]+://[^\s]*',doc('.pagecon').text())
    url_bt = url_bt_match.group()
    return {
        'name' : name,
        'cover': str(imgs[0]),
        'imgs' : str(imgs),
        'url_bt': url_bt
    }


def sava_data(data):
    collection.update_one({
        'name' : data.get('name')
    }, {'$set' : data}
    ,upsert = True)
    logging.info('data save successed ')



def main():
    for page in range(1,TOTAL_PAGE+1):
        if page == 1:
            page = ""
        else:
            page = '_'+str(page)
        html = scrape_index_url(page)
        index_url = parse_index_page(html)
        for detail_url in index_url:
            deatil_html = scrape_detail_page(detail_url)
            data = parse_detail(deatil_html)
            sava_data(data)
        



if __name__ == "__main__":
    main()
    logging.info('scrape done')


