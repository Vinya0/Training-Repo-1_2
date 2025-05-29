# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# class TestCLI:
#     def test_Login(self, setup):
#         self.driver = setup
#         self.driver.get("https://opensource-demo.orangehrmlive.com/")
#
#         wait = WebDriverWait(self.driver, 10)
#         username_input = wait.until(EC.visibility_of_element_located((By.NAME, "txtUsername")))
#         username_input.send_keys("Admin")
#
#         password_input = wait.until(EC.visibility_of_element_located((By.ID, "txtPassword")))
#         password_input.send_keys("admin123")
#
#         login_button = wait.until(EC.element_to_be_clickable((By.ID, "btnLogin")))
#         login_button.click()
#
#         try:
#             status = wait.until(
#                 EC.visibility_of_element_located((By.XPATH, "//h1[normalize-space()='Dashboard']"))).is_displayed()
#             assert status == True
#         finally:
#             self.driver.close()

from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCLI:
    def test_Login(self,setup):
        self.driver=setup
        self.driver = setup
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

        try:
            self.status = self.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").is_displayed()
            self.driver.close()
            assert self.status == True
        except:
            self.driver.close()
            assert False