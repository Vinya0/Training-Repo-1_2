from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Launch the browser
driver = webdriver.Chrome()

# Step 2: Open the SAUCEDEMO login page
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(2)

# Step 3: Enter credentials and login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(2)
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(2)
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# Step 4: Wait to observe the result (optional)
time.sleep(5)

# Step 5: Close the browser
driver.quit()
