from selenium import webdriver
import time
import logging

browser = webdriver.Edge()
browser.get('https://www.taobao.com')
input_first = browser.find_element_by_id('q')
input_first.send_keys('iphone')
time.sleep(1)
input_first.clear()
input_first.send_keys('ipad')
button = browser.find_element_by_class_name('btn-search')
button.click()
browser.close()