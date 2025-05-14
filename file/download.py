# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import time
# import os
# for chrome
# location = os.getcwd()

# def chrome_setup():
#     preferences = {"download.default_directory": location}  #command all three lines and remove options=ops to just download and not saving in directory
#     ops = webdriver.ChromeOptions()
#     ops.add_experimental_option("prefs", preferences)
#     driver = webdriver.Chrome(options=ops)  # Apply options here
#     return driver
#
# driver = chrome_setup()
#
# driver.get("https://examplefile.com/document/pdf/6-mb-pdf")
# driver.maximize_window()
# driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/aside/div[1]/div[2]/a").click()
#
# time.sleep(5)  # Add sleep duration, e.g., 5 seconds

#for edge
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time

def edge_setup():
    # No download directory setting, use default location
    ops = webdriver.EdgeOptions()  # Keep the options but don't set custom preferences
    driver = webdriver.Edge(options=ops)  # Apply options here
    return driver

driver = edge_setup()

driver.get("https://examplefile.com/document/pdf/6-mb-pdf")
driver.maximize_window()
driver.find_element(By.XPATH, "/html/body/section[2]/div/div/div[2]/aside/div[1]/div[2]/a").click()

time.sleep(5)  # Add sleep duration, e.g., 5 seconds


