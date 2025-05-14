# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# # Initialize the Chrome driver
# driver = webdriver.Chrome()
# driver.get("https://safarr-admin-dev.webelight.co.in/sign-in")
# driver.maximize_window()
#
# # Wait for the username field to be visible
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "email")))
#
# # Enter invalid credentials
# driver.find_element(By.NAME, "email").send_keys("invalid@example.com")
# driver.find_element(By.NAME, "password").send_keys("wrongpassword")
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
#
# # Wait for the toast message to appear
# try:
#     toast = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.CLASS_NAME, "Toastify__toast-body"))
#     )
#     print("Toast message:", toast.text)
# except:
#     print("No toast message appeared.")
# time.sleep(3)
# # Close the browser
# driver.quit()

# for log in
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()
driver.get("https://safarr-admin-dev.webelight.co.in/sign-in")
driver.maximize_window()

# Wait for the username field to be visible
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "email")))

# Enter invalid credentials
driver.find_element(By.NAME, "email").send_keys("Admin@gmail.com")
driver.find_element(By.NAME, "password").send_keys("Admin@123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Wait for the toast message to appear
# Wait for the toast message to appear
try:
    toast = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.toast"))
    )
    print("Toast message:", toast.text)
except:
    print("No toast message appeared.")

time.sleep(3)
# Close the browser
driver.quit()


