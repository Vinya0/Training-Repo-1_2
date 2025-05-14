from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Launch the browser
driver = webdriver.Chrome()

# Step 2: Open the OrangeHRM login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

# Wait for the page to load
time.sleep(2)

# Step 3: Enter "Admin" in the username field
driver.find_element(By.NAME, "username").send_keys("Admin")
time.sleep(2)

# Clear the username field
driver.find_element(By.NAME, "username").clear()
time.sleep(2)

# Step 4: Enter "admin1234" in the password field
driver.find_element(By.NAME, "password").send_keys("admin1234")
time.sleep(2)
