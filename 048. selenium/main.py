from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

chrome_driver = webdriver.Chrome(options=chrome_options)

chrome_driver.get("https://www.python.org/")

upcoming_events = chrome_driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li')

events = {}

for n in range(len(upcoming_events)):
    upcoming_event_element = upcoming_events[n]

    events[n] = {
        "time": upcoming_event_element.find_element(By.CSS_SELECTOR, value="time").text,
        "name": upcoming_event_element.find_element(By.CSS_SELECTOR, value="a").text,
    }

print(events)

chrome_driver.quit()