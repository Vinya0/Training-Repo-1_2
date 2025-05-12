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

# Step 3: Enter "Admin" in the username field
driver.find_element(By.NAME, "username").send_keys("Admin")
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[3]/p[2]/a').click()
time.sleep(7)
driver.close()
# driver.quit()

