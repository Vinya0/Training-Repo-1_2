import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Chrome
driver = webdriver.Chrome()
driver.implicitly_wait(10)  # Implicit wait to handle loading times

driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

button = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")

act = ActionChains(driver)

act.context_click(button).perform()  # Right click

# Replace time.sleep() with implicit wait
time.sleep(5)  # Still added to mimic your original behavior
driver.find_element(By.XPATH, "//span[normalize-space()='Copy']").click()  # Click "Copy"
time.sleep(3)  # Still added to mimic your original behavior

driver.switch_to.alert.accept()
