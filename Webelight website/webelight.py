from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://dev.webelight.co.in/blog")

wait = WebDriverWait(driver, 10)

# Step 1: Click "Services"
wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Services")]'))).click()
time.sleep(1)

# Step 2: Click "AI & ML Development"
wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "AI") and contains(text(), "ML")]'))).click()
time.sleep(2)

# Step 3: Go back and reopen "Services"
driver.back()
time.sleep(2)
wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Services")]'))).click()
time.sleep(1)

# Step 4: Click "Custom Software Development"
wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Custom Software Development")]'))).click()
time.sleep(2)

# Step 5: Go back and reopen "Services"
driver.back()
time.sleep(2)
wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Services")]'))).click()
time.sleep(1)

# Step 6: Click "Mobile App Development"
wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Mobile App Development")]'))).click()
time.sleep(2)

# Step 7: Go back and reopen "Services"
driver.back()
time.sleep(2)
wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Services")]'))).click()
time.sleep(1)

# Step 8: Click "Advanced Automation"
wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Advanced Automation")]'))).click()
time.sleep(2)

# Step 9: Go back and reopen "Services"
driver.back()
time.sleep(2)
wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Services")]'))).click()
time.sleep(1)

# Step 10: Click "Blockchain Development"
wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Blockchain Development")]'))).click()
time.sleep(2)

# Step 11: Go back and reopen "Services"
driver.back()
time.sleep(2)
wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Services")]'))).click()
time.sleep(1)

# Step 12: Click "DevOps & Cloud"
wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "DevOps & Cloud")]'))).click()
time.sleep(2)

# Step 13: Go back and reopen "Services"
driver.back()
time.sleep(2)
wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Services")]'))).click()
time.sleep(1)

# Step 14: Click "Data Analytics Services"
wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Data Analytics Services")]'))).click()
time.sleep(2)

# Step 15: Go back and reopen "Services"
driver.back()
time.sleep(2)
wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Services")]'))).click()
time.sleep(1)

# Step 16: Click "MVP Development"
wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "MVP Development")]'))).click()
time.sleep(2)

# Step 17: Go back and reopen "Services"
driver.back()
time.sleep(2)
wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Services")]'))).click()
time.sleep(1)

# Step 18: Click "Discovery Phase Services"
wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Discovery Phase Services")]'))).click()
time.sleep(2)

# Step 19: Go back and reopen "Services"
driver.back()
time.sleep(2)
wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Services")]'))).click()
time.sleep(1)# # Step 6: Verify "Career link"
wait.until(EC.visibility_of_element_located((By.XPATH, '//p[normalize-space()="career[at]webelight[dot]co[dot]in"]')))
time.sleep(2)


# Step 20: Click "CTO Services"
wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "CTO Services")]'))).click()
time.sleep(2)

# Step 21: Go back and reopen "Services"
driver.back()
time.sleep(2)
wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Services")]'))).click()
time.sleep(1)

# Step 22: Verify and print "Sales link"
sales_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'sales[at]webelight[dot]co[dot]in')))
sales_href = sales_link.get_attribute('href')
print("Sales email href:", sales_href)
assert sales_href == 'mailto:sales@webelight.co.in'

# Step 23: Verify and print "Career link"
career_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'career[at]webelight[dot]co[dot]in')))
career_href = career_link.get_attribute('href')
print("Career email href:", career_href)
assert career_href == 'mailto:career@webelight.co.in'
time.sleep(2)

#Step 24: Scroll down the page till element found
scroll = driver.find_element(By.XPATH, '/html/body/main/section[1]/div/div[1]/div[1]/input')
driver.execute_script("arguments[0].scrollIntoView();", scroll)
time.sleep(2)
# Step 25: Type "Blockchain" in search bar
ele = driver.find_element(By.CLASS_NAME, 'search-input')
ele.send_keys("Blockchain")                          # Then send the text
time.sleep(2)

# Clear the text using CTRL + A and Backspace
ele.send_keys(Keys.CONTROL + "a")
ele.send_keys(Keys.BACKSPACE)
time.sleep(2)


# More reliable way to handle the categories and checkboxes
try:
    # Locate the "All Categories" element
    all_categories = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[contains(@class, "categories") or contains(@class, "filter")]//*[contains(text(), "All Categories")]')
    ))
    
    # Scroll it into view
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", all_categories)
    time.sleep(1)
    
    # Click to open dropdown (instead of just hovering)
    all_categories.click()
    time.sleep(1)
    
    # Wait for dropdown to be visible and get all checkboxes
    checkbox_container = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'dropdown-content')))
    
    # Click checkbox 3 with better wait and error handling
    checkbox_3 = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '.dropdown-content li:nth-child(3) input')
    ))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbox_3)
    checkbox_3.click()
    time.sleep(1)
    
    # Click checkbox 5 with better wait and error handling
    checkbox_5 = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '.dropdown-content li:nth-child(5) input')
    ))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbox_5)
    checkbox_5.click()
    time.sleep(1)

except Exception as e:
    print(f"Error interacting with checkboxes: {str(e)}")
    # Optionally add alternative action or error recovery here


# Content cards
wait.until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/main/section[1]/div/div[2]/div/div[1]/a/div/div[3]/h3')
)).click()
time.sleep(5)
driver.back()
time.sleep(2)
wait.until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/main/section[1]/div/div[2]/div/div[2]/a/div/div[3]/h3')
)).click()
time.sleep(5)

# Load more Content cards after scrolling
driver.back()
scroll = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
    By.XPATH, '//button//*[contains(text(), "Load") or contains(text(), "More")]'
)))
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", scroll)
time.sleep(1)

# Now click the Load More button
load_more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
    By.XPATH, '//button[contains(.,"Load") or contains(.,"More")]'
)))
load_more_button.click()

time.sleep(5)

# Scroll up smoothly
for _ in range(40):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_UP)
    time.sleep(0.2)

#Drop your queries
wait.until(EC.element_to_be_clickable(
    (By.XPATH, '//button[contains(text(),"Drop Your Queries")]')
)).click()
time.sleep(3)

#Fill the form
#Scroll down the page till element found
scroll = driver.find_element(By.XPATH, '//*[@id="contact-us"]/section/div/div[1]/div/h3/span[2]')
driver.execute_script("arguments[0].scrollIntoView();", scroll)
# time.sleep(2)
driver.find_element(By.ID, "name").send_keys("Prachi")
time.sleep(2)
driver.find_element(By.ID, "email").send_keys("prachi@gmail.com")
time.sleep(2)
driver.find_element(By.ID, "phone").send_keys("6364654757")
time.sleep(2)
driver.find_element(By.ID, "companyName").send_keys("Webelight")
time.sleep(2)
driver.find_element(By.ID, "message").send_keys("Inquiry")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="submit-contact-us-form"]/div/div[4]/button/div/div[1]').click()
time.sleep(2)

#click on social login
# Scroll down until the element with text "FOLLOW US" is found
scroll = driver.find_element(By.XPATH, '//p[normalize-space()="FOLLOW US"]')
driver.execute_script("arguments[0].scrollIntoView();", scroll)

# Wait for Facebook button (case-insensitive contains)
wait.until(EC.element_to_be_clickable(
    (By.XPATH, '//img[@alt="facebook"]'))).click()