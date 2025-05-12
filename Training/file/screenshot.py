from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Launch the browser
driver = webdriver.Chrome()

# Step 2: Open the OrangeHRM login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)

# Step 3: Save a screenshot
driver.save_screenshot("/home/web-h-044/PycharmProjects/Training/file/homepage.png")  #just copy the path of file (absolute path)

# Step 4: Close the browser
driver.quit()
