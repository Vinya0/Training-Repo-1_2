from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, "txtUsername").clear()
        self.driver.find_element(By.ID, "txtUsername").send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, "txtPassword").clear()
        self.driver.find_element(By.ID, "txtPassword").send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.ID, "btnLogin").click()


class TestLogin:
    def test_login(self):
        # Update these paths as per your system
        chrome_binary_path = "/usr/bin/google-chrome"   # Or path to your chromium binary
        chromedriver_path = "/usr/bin/chromedriver"     # Or wherever your chromedriver is located

        options = Options()
        options.binary_location = chrome_binary_path

        service = Service(chromedriver_path)

        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.maximize_window()

        lp = LoginPage(driver)
        lp.setUserName("Admin")
        lp.setPassword("admin123")
        lp.clickLogin()

        assert "Dashboard" in driver.page_source

        driver.quit()


if __name__ == "__main__":
    test = TestLogin()
    test.test_login()
