from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Launch browser and open the login page
driver = webdriver.Chrome()
driver.get("https://safarr-admin-dev.webelight.co.in/sign-in")
driver.maximize_window()

time.sleep(2)  # Wait for page to load

# Step 2: Enter valid credentials and click login
driver.find_element(By.NAME, "email").send_keys("Admin@gmail.com")
driver.find_element(By.NAME, "password").send_keys("Admin@123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Step 3: Wait and capture toast message
time.sleep(3)
Toast_message = driver.find_element(By.XPATH,"//div[@class='toast']")
print("Toast message text:", Toast_message.text)
assert "Logged in successfully." in Toast_message.text,"Error message not found: {Toast_message.text}"
# Give the page time to load
time.sleep(2)

# Step 4: Close browser
time.sleep(2)
driver.quit()
