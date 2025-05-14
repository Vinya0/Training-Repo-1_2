from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.irctc.co.in/nget/train-search")

time.sleep(3)

menu = driver.find_element(By.XPATH, "//a[@aria-label='Menu. more. has sub menu']")
submenu = driver.find_element(By.XPATH, "//a[@aria-label='Sub Menu of More, Counter Ticket Cancellation. Website will be opened in new tab']")
time.sleep(3)

actions = ActionChains(driver)
actions.move_to_element(menu)
actions.click(submenu)
actions.perform()

time.sleep(2)

driver.quit()
