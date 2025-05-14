#Full name
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://dev.webelight.co.in/contact-us#contact-us")
# driver.maximize_window()
# time.sleep(2)
#
# input=driver.find_element(By.XPATH, "//input[@name='name']")
# input.click()
# input.send_keys("standard_user")

# phone number
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://dev.webelight.co.in/contact-us#contact-us")
# driver.maximize_window()
# time.sleep(2)
#
# input=driver.find_element(By.XPATH, "//input[@name='phone']")
# input.click()
# input.send_keys("6254454213")
# time.sleep(2)

#Your message
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://dev.webelight.co.in/contact-us#contact-us")
# driver.maximize_window()
# time.sleep(2)
#
# # Use a more descriptive variable name
# input_field = driver.find_element(By.XPATH, "//textarea[@id='message']")
# input_field.click()  # Click the input field (optional)
# input_field.send_keys("Hello")  # Send text to the input field
# time.sleep(2)

#headless browser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get("https://dev.webelight.co.in/contact-us#contact-us")
driver.maximize_window()
time.sleep(2)

# Use a more descriptive variable name
input_field = driver.find_element(By.XPATH, "//textarea[@id='message']")
input_field.click()  # Click the input field (optional)
input_field.send_keys("Hello")  # Send text to the input field
time.sleep(2)
