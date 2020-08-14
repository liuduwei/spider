from selenium import webdriver
browser = webdriver.Edge()
url = 'https://dynamic2.scrape.cuiqingcai.com/'
browser.get(url)
logo = browser.find_element_by_class_name('logo-image')
print(logo)
print(logo.get_attribute('src'))