import threading
from datetime import datetime, timedelta
from xxlimited import Null

from selenium import webdriver
from selenium.webdriver.common.by import By

base_url = "https://orteil.dashnet.org/experiments/cookie"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

chrome_driver = webdriver.Chrome(options=chrome_options)

chrome_driver.get(base_url)

cookie_element = chrome_driver.find_element(By.ID, "cookie")


def clicker():

    if not chrome_driver.window_handles:
        return;

    able_element = None
    store_elements = chrome_driver.find_elements(By.CSS_SELECTOR, "#store div")

    for n in range(len(store_elements)):
        store_element = store_elements[n]
        class_name = store_element.get_attribute("class")
        if class_name == "":
            able_element = store_element

    if able_element is not None:
        able_element.click()

    t = threading.Timer(3, clicker)
    t.start()

t = threading.Timer(3, clicker)
t.start()

start_time = datetime.now()
end_time = start_time + timedelta(seconds=10)

def end():
    money_element = chrome_driver.find_element(By.ID, "money")
    money = money_element.text

    cps_element = chrome_driver.find_element(By.ID, "cps")
    cps = cps_element.text

    chrome_driver.quit()

    print("End Game")
    print("Money: " + money + "  || CPS: " + cps)

while start_time < end_time:
    start_time=datetime.now()
    cookie_element.click()

    if start_time >= end_time:
        t.cancel()
        end()
