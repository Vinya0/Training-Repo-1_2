from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Launch browser and open the webpage
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://dev.webelight.co.in/services/custom-software-development")
time.sleep(3)

# Step 2: Scroll down to the horizontal scroll section
scroll = driver.find_element(By.XPATH, '//span[normalize-space()="More"]')
driver.execute_script("arguments[0].scrollIntoView();", scroll)
time.sleep(2)

# Step 3: Find the right arrow for horizontal scroll
right_arrow = driver.find_element(By.XPATH, '//img[@alt="right_active"]')

# Step 4: Click the right arrow 4 times
for _ in range(5):
    right_arrow.click()
    time.sleep(1)


# Step 5: Find and click the left arrow 4 times
left_arrow = driver.find_element(By.XPATH, '//img[@alt="left_active"]')
for _ in range(5):
    left_arrow.click()
    time.sleep(1)

# Optional: Close browser
driver.quit()