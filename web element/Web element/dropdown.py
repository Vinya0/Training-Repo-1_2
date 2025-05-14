from selenium import webdriver
from selenium.webdriver.common.by import By
import time



driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(3)

driver.find_element(By.CLASS_NAME, "oxd-userdropdown-tab").click()
time.sleep(2)

# Get dropdown items
options = driver.find_elements(By.XPATH, "//ul[@class='oxd-dropdown-menu']/li")
print(len(options))
driver.find_elements(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[1]/a')[0].click()
time.sleep(2)

