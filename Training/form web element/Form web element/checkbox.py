from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Launch the browser
driver = webdriver.Chrome()

# Step 2:
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()
time.sleep(2)

#To select the checkbox
driver.execute_script("arguments[0].click();", driver.find_element(By.ID, "RESULT_CheckBox-8_0"))
time.sleep(2)
driver.execute_script("arguments[0].click();", driver.find_element(By.ID, "RESULT_CheckBox-8_6"))
time.sleep(2)
driver.execute_script("arguments[0].click();", driver.find_element(By.ID, "RESULT_CheckBox-8_3"))
time.sleep(2)
