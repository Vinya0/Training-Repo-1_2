# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://mv-i.github.io/me/projects/login/dummy.html")
# driver.maximize_window()
# time.sleep(3)
#
# # Type 'Admin' into the username field
# username = driver.find_element(By.ID, "loginUsernameEmail")
# username.send_keys("Admin")
#
# # Select all text and copy (Ctrl + A, Ctrl + C)
# username.send_keys(Keys.CONTROL, 'a')
# username.send_keys(Keys.CONTROL, 'c')
#
# # Paste into password field (Ctrl + V)
# password = driver.find_element(By.ID, "loginPassword")
# password.send_keys(Keys.CONTROL, 'v')
#
# time.sleep(2)
# driver.quit()


#CUT AND PASTE
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://mv-i.github.io/me/projects/login/dummy.html")
driver.maximize_window()
time.sleep(3)

# Type 'Admin' into the username field
username = driver.find_element(By.ID, "loginUsernameEmail")
username.send_keys("Admin")

# Select all text and cut (Ctrl + A, Ctrl + X)
username.send_keys(Keys.CONTROL, 'a')
time.sleep(2)
username.send_keys(Keys.CONTROL, 'x')
# Paste into password field (Ctrl + V)
password = driver.find_element(By.ID, "loginPassword")
password.send_keys(Keys.CONTROL, 'v')

time.sleep(2)
driver.quit()
