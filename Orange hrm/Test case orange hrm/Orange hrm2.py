from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Launch browser
driver = webdriver.Chrome()
driver.implicitly_wait(10)

# Step 2: Open OrangeHRM login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

time.sleep(2)

# Step 3: Click the Login button without entering anything
driver.find_element(By.XPATH, "//button[@type='submit']").click()
# Step 4: Check for username "Required" message
error_username = driver.find_element(By.XPATH, "(//span[@class=\'oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message\'])[1]")
print("Username error message:", error_username.text)
assert "Required" == error_username.text, "Expected 'Required' but got '{error_username.text}'"

time.sleep(1)

# Step 5: Check for password "Required" message
error_password = driver.find_element(By.XPATH, "(//span[@class=\'oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message\'])[2]")
print("Password error message:", error_password.text)
assert "Require" == error_password.text, "Expected 'Required' but got '{error_password.text}'"

# time.sleep(2)
# driver.quit()
# # Check if Successful message is displayed
# Successful_message = driver.find_element(By.XPATH, "//div[contains(text(), 'Logged in successfully.')]")  # Change to actual error text if different
# print("Successful text:", Successful_message.text)
# assert Successful_message.is_displayed(), "Successful message is not found after login"

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import re
#
# # from SafarAdminPanel.Advertisements import error_message
#
# # Init WebDriver
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
#
# # Open the Site
# driver.get("https://dev.webelight.co.in/contact-us")
# driver.maximize_window()
#
# # Give the page time to load
# time.sleep(2)
#
# driver.execute_script('window.scrollBy(0,500)',"")
# time.sleep(2)
# # Submit the form using the submit() method
# form = driver.find_element(By.XPATH, "//button[@type='submit']")  # Adjust with the actual form's ID
# form.submit()
#
# error_message = driver.find_element(By.XPATH,"//p[normalize-space()='Full name is required.']")
# print("Error message text:", error_message.text)
# assert "Full name is required." in error_message.text,f"Error message not found: {error_message.text}"
# # Give the page time to load
# time.sleep(2)
#
# error_message = driver.find_element(By.XPATH,"//p[normalize-space()='Please enter a valid email address.']")
# print("Error message text:", error_message.text)
# assert "Please enter a valid email address." in error_message.text,f"Error message not found: {error_message.text}"
# # Give the page time to load
# time.sleep(2)
#
# error_message = driver.find_element(By.XPATH,"//p[normalize-space()='Phone number is required.']")
# print ("Error message text:", error_message.text)
# assert "Phone number is required." in error_message.text,f"Error message not found: {error_message.text}"
# # Give the page time to load
# time.sleep(2)
# # Close the browser