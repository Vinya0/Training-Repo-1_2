from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Launch the browser
driver = webdriver.Chrome()

# Step 2:
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)

#To select the checkbox
driver.execute_script("arguments[0].click();", driver.find_element(By.ID, "sunday"))
time.sleep(2)
driver.execute_script("arguments[0].click();", driver.find_element(By.ID, "wednesday"))
time.sleep(2)
driver.execute_script("arguments[0].click();", driver.find_element(By.ID, "monday"))
time.sleep(2)
