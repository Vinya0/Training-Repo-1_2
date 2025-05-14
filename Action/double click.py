from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Start the driver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

# Open the site
driver.get("https://testautomationpractice.blogspot.com/")

# Scroll to bring the double-click section into view
driver.execute_script("window.scrollBy(0, 600);")

# Find the field1 and field2
field1 = driver.find_element(By.ID, "field1")
field2 = driver.find_element(By.ID, "field2")

# Clear and type something in field1
field1.clear()
field1.send_keys("Hello from Selenium!")

# Find the double-click button
copy_button = driver.find_element(By.XPATH, "//button[text()='Copy Text']")

# Perform double-click on the button
ActionChains(driver).double_click(copy_button).perform()

# Wait and check result
time.sleep(2)
print("Field 2 value:", field2.get_attribute("value"))  # Should match field1

# Close the browser
driver.quit()
