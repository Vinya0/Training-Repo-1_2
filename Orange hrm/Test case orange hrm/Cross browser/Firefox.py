from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time

options = Options()

# Specify the path to geckodriver using Service
service = Service(executable_path='/snap/bin/geckodriver')

driver = webdriver.Firefox(service=service, options=options)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(4)

print(driver.title)
driver.quit()
