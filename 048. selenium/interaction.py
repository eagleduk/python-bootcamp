from selenium import webdriver
from selenium.webdriver.common.by import By

base_url = 'https://en.wikipedia.org/wiki/Main_Page'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

chrome_driver = webdriver.Chrome(options=chrome_options)

chrome_driver.get(base_url)

upcoming_events = chrome_driver.find_element(By.XPATH, '//*[@id="articlecount"]/ul/li[1]/a')

active_editors = upcoming_events.text

print(active_editors)

chrome_driver.quit()