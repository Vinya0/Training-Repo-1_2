from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)

# Find the draggable and droppable elements
draggable = driver.find_element(By.XPATH, '//*[@id="draggable"]')
droppable = driver.find_element(By.XPATH, '//*[@id="droppable"]')

# Create ActionChains object
actions = ActionChains(driver)

# Perform drag and drop
actions.drag_and_drop(draggable, droppable).perform()

# Optional: Wait to observe the result
time.sleep(2)

driver.quit()
