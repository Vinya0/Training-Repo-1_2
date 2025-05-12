from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

# Step 1: Launch the browser
driver = webdriver.Chrome()

# Step 2: Open the OrangeHRM login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

# Wait for the page to load
time.sleep(2)

# Step 3: Enter "Admin" in the username field
# ele = driver.find_element(By.NAME, "username").send_keys("Admin")
# time.sleep(2)
# ele.send_keys(Keys.CONTROL + "a")
# ele.send_keys(Keys.BACKSPACE)
# # Clear the username field
# Step 3: Enter "Admin" in the username field
ele = driver.find_element(By.NAME, "username")  # First, get the element
ele.send_keys("Admin")                          # Then send the text
time.sleep(2)

# Clear the text using CTRL + A and Backspace
ele.send_keys(Keys.CONTROL + "a")
ele.send_keys(Keys.BACKSPACE)



# Step 4: Enter "admin1234" in the password field
driver.find_element(By.NAME, "password").send_keys("admin1234")
time.sleep(2)
