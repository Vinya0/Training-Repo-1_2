from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Launch the browser
driver = webdriver.Chrome()

# Step 2:
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()
#Used to check if radio button is selected or not
print(driver.find_element(By.NAME, "RESULT_RadioButton-7").is_selected())
time.sleep(2)

#To select the radio button
driver.execute_script("arguments[0].click();", driver.find_element(By.ID, "RESULT_RadioButton-7_0"))
status = driver.find_element(By.ID, "RESULT_RadioButton-7_0").is_selected()
print(status)
