from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.find_element(By.PARTIAL_LINK_TEXT, 'Gm').click()
