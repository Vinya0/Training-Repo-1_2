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
print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.close()