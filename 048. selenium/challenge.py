from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

base_url = 'https://secure-retreat-92358.herokuapp.com'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

chrome_driver = webdriver.Chrome(options=chrome_options)

chrome_driver.get(base_url)

fname_input_element = chrome_driver.find_element(By.NAME, value="fName")
fname_input_element.send_keys("Seung Jin")
fname_input_element.send_keys(Keys.ENTER)

lname_input_element = chrome_driver.find_element(By.NAME, value="lName")
lname_input_element.send_keys("Lee")
lname_input_element.send_keys(Keys.ENTER)

email_input_element = chrome_driver.find_element(By.NAME, value="email")
email_input_element.send_keys("sjlee@e3ps.com")
email_input_element.send_keys(Keys.ENTER)

sumbit_button_element = chrome_driver.find_element(By.CSS_SELECTOR, value="button[type=submit]")
sumbit_button_element.click()