# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# class TestClass:
#     @pytest.mark.parametrize('user,pwd',
#                              [("Admin","admin123"),
#                               ("adm","admin123"),
#                               ("Admin","adm"),
#                               ("adm","adm")
#                               ]
#                              )
#     def test_Login(self,user,pwd):
#         # self.serv_obj=Service("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
#         self.driver=webdriver.Chrome()
#         self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login/")
#         self.driver.find_element(By.NAME, "Username").send_keys(user)
#         self.driver.find_element(By.NAME, "Password").send_keys(pwd)
#         self.driver.find_element(By.XPATH, "//*[@id=app]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
#         try:
#             self.status=self.driver.find_element(By.XPATH,"//*[@id=app]/div[1]/div[1]/header/div[1]/div[1]/span/h6").is_displayed()
#             self.driver.close()
#             assert self.status==True
#         except:
#             self.driver.close()
#             assert False
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestClass:
    @pytest.mark.parametrize('user,pwd',
                             [("Admin","admin123"),
                              ("adm","admin123"),
                              ("Admin","adm"),
                              ("adm","adm")
                              ]
                             )
    def test_Login(self, user, pwd):
        # Set the path to chromedriver executable if needed
        # For example:
        # service_obj = Service("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
        # driver = webdriver.Chrome(service=service_obj)

        driver = webdriver.Chrome()  # Use this if chromedriver is in PATH
        driver.get("https://opensource-demo.orangehrmlive.com/")

        wait = WebDriverWait(driver, 10)

        # Corrected locator names to lowercase
        username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_input = driver.find_element(By.NAME, "password")

        username_input.clear()
        username_input.send_keys(user)
        password_input.clear()
        password_input.send_keys(pwd)

        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        try:
            # Wait for the element that appears after successful login
            dashboard_header = wait.until(
                EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
            )
            assert dashboard_header.is_displayed()
        except:
            assert False
        finally:
            driver.quit()
