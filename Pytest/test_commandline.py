from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class TestCLI:
    def test_Login(self,setup):
        self.driver=setup
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.NAME, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        try:
            self.status = self.driver.find_element(By.XPATH, "//h1[normalize-space()='Dashboard']").is_displayed()
            assert self.status == True
            self.driver.close()
            # assert self.status == True
        except:
            self.driver.close()
            assert False