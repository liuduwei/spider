import requests
import logging
from os import makedirs
from os.path import exists
import json

logging.basicConfig(level=logging.INFO,
                    format = '%(asctime)s - %(levelname)s: %(message)s')
INDEX_URL = 'https://dynamic1.scrape.cuiqingcai.com/api/movie/?limit={limit}&offset={offset}'

def scrape_api(url):
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        logging.error('get invalid status code %s while scraping %s', response.code,url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)

LIMIT = 10

def scrape_index(page):
    url = INDEX_URL.format(limit=LIMIT, offset=LIMIT * (page - 1))
    return scrape_api(url)

DETAIL_URL = 'https://dynamic1.scrape,cuiqingcai.com/api/movie/{id}'

def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    return scrape_api(url)


RESULT_DIR = 'results'
exists(RESULT_DIR) or makedirs(RESULT_DIR)


def save_data(data):
    name = data.get('name')
    data_path = f'{RESULT_DIR}/{name}.json'
    json.dump(data, open(data_path, 'w', encoding='utf-8'),ensure_ascii=False ,indent=2)


TOTAL_PAGE = 10


def main():
    for page in range(1,TOTAL_PAGE):
        index_data = scrape_index(page)
        for item in index_data.get('results'):
            id = item.get('id')
            detail_data = scrape_detail(id)
            logging.info('detail data %s', detail_data)
            save_data(detail_data)

if __name__== "__main__":
    main()
    logging.info('scrape done')




 