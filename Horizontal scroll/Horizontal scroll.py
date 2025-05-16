from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()
driver.get("https://practice.expandtesting.com/scrollbars")
driver.maximize_window()
time.sleep(2)

# Scroll into view if needed
scroll_button = driver.find_element(By.ID, "hscroll-right")
driver.execute_script("arguments[0].scrollIntoView();", scroll_button)

# Click the right scroll button multiple times
for _ in range(5):  # adjust the range as needed
    scroll_button.click()
    time.sleep(0.5)  # small delay to see scrolling effect

time.sleep(2)
driver.quit()
