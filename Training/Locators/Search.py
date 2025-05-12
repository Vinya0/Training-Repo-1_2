from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Launch browser
driver = webdriver.Chrome()

# Open a website with a search field (example: Google)
driver.get("https://www.google.com")
time.sleep(2)

# Locate the search input box (by name in this case)
search_box = driver.find_element(By.NAME, "q")

# Type your query
search_box.send_keys("OrangeHRM")

# Press Enter
search_box.send_keys(Keys.RETURN)

# Wait to see results
time.sleep(3)

driver.quit()
