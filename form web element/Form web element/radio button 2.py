from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Launch the browser
driver = webdriver.Chrome()

# Step 2: Open the website
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Used to check if radio button is selected or not
print(driver.find_element(By.ID, "male").is_selected())  # Check before click
time.sleep(2)

# To select the radio button
driver.execute_script("arguments[0].click();", driver.find_element(By.ID, "male"))
status = driver.find_element(By.ID, "male").is_selected()
print(status)  # Check after click

time.sleep(3)
driver.quit()
