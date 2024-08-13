from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('headless')
chrome = webdriver.Chrome(options=options)
find = chrome.find_element