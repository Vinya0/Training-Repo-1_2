from selenium import webdriver
from selenium.webdriver.common.by import By
import time



driver = webdriver.Chrome()
driver.get("https://in.search.yahoo.com/?fr2=inr")
driver.maximize_window()
linkcount=driver.find_elements(By.TAG_NAME,'a')
time.sleep(2)
print(len(linkcount))

for link in linkcount:
     print(link.get_attribute('href'))
     print(link.text)


driver.quit()