from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# Step 1: Launch the browser
driver = webdriver.Edge()

# Step 2: Open the OrangeHRM login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
exp_title = "OrangeHRM"
act_title = driver.title
time.sleep(2)
if act_title == exp_title:
    print("OrangeHRM")
else:
    print("cannot access")