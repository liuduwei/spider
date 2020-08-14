import requests
proxy = '127.0.0.1:1087'
proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy,
}
try:
    resp = requests.get('https://httpbin.org/get', proxies=proxies)
    print(resp.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)
