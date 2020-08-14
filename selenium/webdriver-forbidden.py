from selenium import webdriver
from selenium.webdriver import ChromeOptions
option = ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])
option.add_experimental_option('useAutomationExtension', False)
browser = webdriver.Chrome(option = option)
browser.execute_cdp_cmd('Page.add')