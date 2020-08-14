from selenium import webdriver
proxy = '127.0.0.1:1087'
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=http://' + proxy)
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
browser.get('https://httpbin.org/get')
print(browser.page_source)
browser.close()
