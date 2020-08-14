# 隐式等待
# from selenium import webdriver
# browser = webdriver.Edge()
# browser.implicitly_wait(10)
# browser.get('https://dynamic2.scrape.cuiqingcai.com/')
# input = browser.find_element_by_class_name('logo-image')
# print(input)

#显示等待
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# browser = webdriver.Edge()
# browser.get('https://www.taobao.com/')
# wait = WebDriverWait(browser, 10)
# input = wait.until(EC.presence_of_all_elements_located((By.ID,'q')))
# # 判断等待条件是是否存在有元素
# button = wait.until(EC.element_to_be_clickable(By.CSS_SELECTOR, '.btn-search')))
# # 判断等待条件是是否可以点击
# print(input, button) 
