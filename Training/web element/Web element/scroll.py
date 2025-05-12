from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# driver = webdriver.Chrome()
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# time.sleep(2)

#Scroll down the page by pixel
# driver.execute_script("window.scrollBy(0,500)")  # Scroll down 500 pixels
# time.sleep(2)
#Scroll down the page till element found
# scroll = driver.find_element(By.XPATH, '//*[@id="HTML12"]/h2')
# driver.execute_script("arguments[0].scrollIntoView();", scroll)
# time.sleep(2)

#Scroll to end of the page
# driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
# time.sleep(2)


# driver = webdriver.Chrome()
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# time.sleep(2)

# Scroll down slowly in steps

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)

# Scroll down smoothly
for _ in range(10):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_DOWN)
    time.sleep(0.2)

# Scroll up smoothly
for _ in range(5):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_UP)
    time.sleep(0.2)

driver.quit()
