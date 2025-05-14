from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.find_element(By.XPATH, '//*[@id="confirmBtn"]').click()
time.sleep(3)
# driver.switch_to.alert.accept()
driver.switch_to.alert.dismiss()

time.sleep(3)