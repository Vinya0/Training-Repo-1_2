from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# Step 1: Launch the browser
driver = webdriver.Chrome()

# Step 2: Open the OrangeHRM login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)

# Step 3: Step 2: Open the Flipkart login page
driver.get("https://www.flipkart.com/account/login?ret=/")
driver.maximize_window()
time.sleep(2)

driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)