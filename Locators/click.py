from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[2]').click()
