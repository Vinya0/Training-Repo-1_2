from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

regilink = driver.find_element(By.LINK_TEXT, "Register")
ActionChains(driver).key_down(Keys.CONTROL).click(regilink).key_up(Keys.CONTROL).perform()  #ActionChains(driver)
    # .key_down(Keys.CONTROL)     # Hold down the CTRL key (on Mac use COMMAND)
    # .click(regilink)            # Click the link while CTRL is held down
    # .key_up(Keys.CONTROL)       # Release the CTRL key
    # .perform()                  # Execute the full action chain

time.sleep(2)  # Wait for the new tab to open

driver.switch_to.window(driver.window_handles[1])  # Switch to new tab
print("Now on:", driver.current_url)


# #New Tab - Selenium4 :  Opens a new tab and switches to new tab
# driver.get("https://www.opencart.com/")
# driver.switch_to.new_window('tab')
# driver.get("https://www.orangehrm.com/")
#
# #New Window - Selenium4 :  Opens a new browser window and switches to new window
# driver.get("https://www.opencart.com/")
# driver.switch_to.new_window('window')
# driver.get("https://www.orangehrm.com/")





