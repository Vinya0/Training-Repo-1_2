from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)

link = driver.find_element(By.LINK_TEXT, "Udemy Courses")

actions = ActionChains(driver)
# actions = ActionChains(driver)
actions.click_and_hold(link)
actions.pause(2)
actions.release(link)
actions.perform()
time.sleep(2)
driver.quit()
