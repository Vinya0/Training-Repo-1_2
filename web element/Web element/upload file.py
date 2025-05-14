from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#Single file
# driver = webdriver.Chrome()
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# time.sleep(2)
# #Scroll down the page till element found
# scroll = driver.find_element(By.XPATH, '//*[@id="HTML15"]/h2')
# driver.execute_script("arguments[0].scrollIntoView();", scroll)
# time.sleep(2)
# input=driver.find_element(By.ID, "singleFileInput")
# input.send_keys("/home/web-h-044/Pictures/Screenshots/Screenshot from 2025-05-01 18-16-24.png")
# time.sleep(2)
# driver.find_element(By.XPATH, "//*[@id='singleFileForm']/button").click()
# time.sleep(2)
# if input.get_attribute("value"):
#     print("File uploaded successfully")
# else:
#     print("File not uploaded successfully")
#Multiple files
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)
scroll = driver.find_element(By.XPATH, '//*[@id="HTML15"]/h2')
driver.execute_script("arguments[0].scrollIntoView();", scroll)
time.sleep(2)
input = driver.find_element(By.ID, "multipleFilesInput")
input.send_keys("/home/web-h-044/Pictures/Screenshots/Screenshot from 2025-05-01 18-16-24.png\n""/home/web-h-044/Pictures/Screenshots/Screenshot from 2025-05-02 10-39-07.png\n""/home/web-h-044/Pictures/Screenshots/Screenshot from 2025-05-02 10-53-10.png")
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='multipleFilesForm']/button").click()
time.sleep(2)
if input.get_attribute("value"):
     print("Files uploaded successfully")
else:
     print("Files not uploaded successfully")