# # import pytest
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# #
# # class TestLogin:
# #     def test_login_chrome(self):
# #         from selenium.webdriver.chrome.service import Service
# #         self.serv_obj = Service()  # You can optionally give executable_path if needed
# #         self.driver = webdriver.Chrome()
# #         self.driver.get("https://opensource-demo.orangehrmlive.com/")
# #         self.driver.find_element(By.NAME, "username").send_keys("Admin")
# #         self.driver.find_element(By.NAME, "password").send_keys("admin123")
# #         self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
# #         assert "OrangeHRM" in self.driver.title
# #         self.driver.quit()
# #
# #     def test_login_edge(self):
# #         from selenium.webdriver.edge.service import Service
# #         self.serv_obj = Service()
# #         self.driver = webdriver.Edge()
# #         self.driver.get("https://opensource-demo.orangehrmlive.com/")
# #         self.driver.find_element(By.NAME, "username").send_keys("Admin")
# #         self.driver.find_element(By.NAME, "password").send_keys("admin123")
# #         self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
# #         assert "OrangeHRM" in self.driver.title
# #         self.driver.quit()
# #
# #     def test_login_firefox(self):
# #         from selenium.webdriver.firefox.service import Service
# #         self.serv_obj = Service()
# #         self.driver = webdriver.Firefox()
# #         self.driver.get("https://opensource-demo.orangehrmlive.com/")
# #         self.driver.find_element(By.NAME, "username").send_keys("Admin")
# #         self.driver.find_element(By.NAME, "password").send_keys("admin123")
# #         self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
# #         assert "OrangeHRM" in self.driver.title
# #         self.driver.quit()
# # # import pytest
# # # from selenium import webdriver
# # # from selenium.webdriver.common.by import By
# # # from selenium.webdriver.support.ui import WebDriverWait
# # # from selenium.webdriver.support import expected_conditions as EC
# # #
# # #
# # # class TestLogin:
# # #     def login_test(self, driver):
# # #         self.driver = driver
# # #         self.driver.get("https://opensource-demo.orangehrmlive.com/")
# # #         print("Page loaded:", self.driver.title)
# # #
# # #         wait = WebDriverWait(self.driver, 10)
# # #         try:
# # #             wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
# # #             wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("admin123")
# # #             wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))).click()
# # #
# # #             wait.until(EC.title_contains("OrangeHRM"))
# # #             print("Login successful. Page title is:", self.driver.title)
# # #             assert "OrangeHRM" in self.driver.title
# # #         except Exception as e:
# # #             print("Login failed:", e)
# # #             raise
# # #         finally:
# # #             self.driver.quit()
# # #
# # #     def test_login_chrome(self):
# # #         from selenium.webdriver.chrome.service import Service as ChromeService
# # #         service = ChromeService()  # Use executable_path if needed
# # #         options = webdriver.ChromeOptions()
# # #         driver = webdriver.Chrome(service=service, options=options)
# # #         self.login_test(driver)
# # #
# # #     def test_login_edge(self):
# # #         from selenium.webdriver.edge.service import Service as EdgeService
# # #         service = EdgeService()  # Use executable_path if needed
# # #         options = webdriver.EdgeOptions()
# # #         driver = webdriver.Edge(service=service, options=options)
# # #         self.login_test(driver)
# # #
# # #     def test_login_firefox(self):
# # #         from selenium.webdriver.firefox.service import Service as FirefoxService
# # #         service = FirefoxService(executable_path="/snap/bin/geckodriver")  # Adjust path if needed
# # #         options = webdriver.FirefoxOptions()
# # #         driver = webdriver.Firefox(service=service, options=options)
# # #         self.login_test(driver)
# import pytest
# from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # import time
# #
# # class TestLogin:
# #     def login_test(self, driver):
# #         self.driver = driver
# #         self.driver.get("https://opensource-demo.orangehrmlive.com/")
# #         print("Page loaded:", self.driver.title)
# #
# #         wait = WebDriverWait(self.driver, 10)
# #         try:
# #             wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
# #             wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("admin123")
# #             wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))).click()
# #
# #             wait.until(EC.title_contains("OrangeHRM"))
# #             print("Login successful. Page title is:", self.driver.title)
# #             assert "OrangeHRM" in self.driver.title
# #         except Exception as e:
# #             print("Login failed:", e)
# #             raise
# #         finally:
# #             self.driver.quit()
# #
# #     def test_login_chrome(self):
# #         from selenium.webdriver.chrome.service import Service as ChromeService
# #         service = ChromeService()  # Use executable_path if needed
# #         options = webdriver.ChromeOptions()
# #         driver = webdriver.Chrome(service=service, options=options)
# #         self.login_test(driver)
# #         time.sleep(2)
# #
# #     def test_login_edge(self):
# #         from selenium.webdriver.edge.service import Service as EdgeService
# #         service = EdgeService()  # Use executable_path if needed
# #         options = webdriver.EdgeOptions()
# #         driver = webdriver.Edge(service=service, options=options)
# #         self.login_test(driver)
# #
# #     def test_login_firefox(self):
# #         from selenium.webdriver.firefox.service import Service as FirefoxService
# #         service = FirefoxService(executable_path="/snap/bin/geckodriver")  # Adjust path if needed
# #         options = webdriver.FirefoxOptions()
# #         driver = webdriver.Firefox(service=service, options=options)
# #         self.login_test(driver)
#
#
# # conftest.py
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.edge.service import Service as EdgeService
# from selenium.webdriver.firefox.service import Service as FirefoxService
#
# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome", help="browser to run tests")
#
# @pytest.fixture
# def driver(request):
#     browser = request.config.getoption("--browser")# # import pytest
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# #
# # class TestLogin:
# #     def test_login_chrome(self):
# #         from selenium.webdriver.chrome.service import Service
# #         self.serv_obj = Service()  # You can optionally give executable_path if needed
# #         self.driver = webdriver.Chrome()
# #         self.driver.get("https://opensource-demo.orangehrmlive.com/")
# #         self.driver.find_element(By.NAME, "username").send_keys("Admin")
# #         self.driver.find_element(By.NAME, "password").send_keys("admin123")
# #         self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
# #         assert "OrangeHRM" in self.driver.title
# #         self.driver.quit()
# #
# #     def test_login_edge(self):
# #         from selenium.webdriver.edge.service import Service
# #         self.serv_obj = Service()
# #         self.driver = webdriver.Edge()
# #         self.driver.get("https://opensource-demo.orangehrmlive.com/")
# #         self.driver.find_element(By.NAME, "username").send_keys("Admin")
# #         self.driver.find_element(By.NAME, "password").send_keys("admin123")
# #         self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
# #         assert "OrangeHRM" in self.driver.title
# #         self.driver.quit()
# #
# #     def test_login_firefox(self):
# #         from selenium.webdriver.firefox.service import Service
# #         self.serv_obj = Service()
# #         self.driver = webdriver.Firefox()
# #         self.driver.get("https://opensource-demo.orangehrmlive.com/")
# #         self.driver.find_element(By.NAME, "username").send_keys("Admin")
# #         self.driver.find_element(By.NAME, "password").send_keys("admin123")
# #         self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
# #         assert "OrangeHRM" in self.driver.title
# #         self.driver.quit()
# # # import pytest
# # # from selenium import webdriver
# # # from selenium.webdriver.common.by import By
# # # from selenium.webdriver.support.ui import WebDriverWait
# # # from selenium.webdriver.support import expected_conditions as EC
# # #
# # #
# # # class TestLogin:
# # #     def login_test(self, driver):
# # #         self.driver = driver
# # #         self.driver.get("https://opensource-demo.orangehrmlive.com/")
# # #         print("Page loaded:", self.driver.title)
# # #
# # #         wait = WebDriverWait(self.driver, 10)
# # #         try:
# # #             wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
# # #             wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("admin123")
# # #             wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))).click()
# # #
# # #             wait.until(EC.title_contains("OrangeHRM"))
# # #             print("Login successful. Page title is:", self.driver.title)
# # #             assert "OrangeHRM" in self.driver.title
# # #         except Exception as e:
# # #             print("Login failed:", e)
# # #             raise
# # #         finally:
# # #             self.driver.quit()
# # #
# # #     def test_login_chrome(self):
# # #         from selenium.webdriver.chrome.service import Service as ChromeService
# # #         service = ChromeService()  # Use executable_path if needed
# # #         options = webdriver.ChromeOptions()
# # #         driver = webdriver.Chrome(service=service, options=options)
# # #         self.login_test(driver)
# # #
# # #     def test_login_edge(self):
# # #         from selenium.webdriver.edge.service import Service as EdgeService
# # #         service = EdgeService()  # Use executable_path if needed
# # #         options = webdriver.EdgeOptions()
# # #         driver = webdriver.Edge(service=service, options=options)
# # #         self.login_test(driver)
# # #
# # #     def test_login_firefox(self):
# # #         from selenium.webdriver.firefox.service import Service as FirefoxService
# # #         service = FirefoxService(executable_path="/snap/bin/geckodriver")  # Adjust path if needed
# # #         options = webdriver.FirefoxOptions()
# # #         driver = webdriver.Firefox(service=service, options=options)
# # #         self.login_test(driver)
# import pytest
# from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # import time
# #
# # class TestLogin:
# #     def login_test(self, driver):
# #         self.driver = driver
# #         self.driver.get("https://opensource-demo.orangehrmlive.com/")
# #         print("Page loaded:", self.driver.title)
# #
# #         wait = WebDriverWait(self.driver, 10)
# #         try:
# #             wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
# #             wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("admin123")
# #             wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))).click()
# #
# #             wait.until(EC.title_contains("OrangeHRM"))
# #             print("Login successful. Page title is:", self.driver.title)
# #             assert "OrangeHRM" in self.driver.title
# #         except Exception as e:
# #             print("Login failed:", e)
# #             raise
# #         finally:
# #             self.driver.quit()
# #
# #     def test_login_chrome(self):
# #         from selenium.webdriver.chrome.service import Service as ChromeService
# #         service = ChromeService()  # Use executable_path if needed
# #         options = webdriver.ChromeOptions()
# #         driver = webdriver.Chrome(service=service, options=options)
# #         self.login_test(driver)
# #         time.sleep(2)
# #
# #     def test_login_edge(self):
# #         from selenium.webdriver.edge.service import Service as EdgeService
# #         service = EdgeService()  # Use executable_path if needed
# #         options = webdriver.EdgeOptions()
# #         driver = webdriver.Edge(service=service, options=options)
# #         self.login_test(driver)
# #
# #     def test_login_firefox(self):
# #         from selenium.webdriver.firefox.service import Service as FirefoxService
# #         service = FirefoxService(executable_path="/snap/bin/geckodriver")  # Adjust path if needed
# #         options = webdriver.FirefoxOptions()
# #         driver = webdriver.Firefox(service=service, options=options)
# #         self.login_test(driver)
#
#
# # conftest.py
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.edge.service import Service as EdgeService
# from selenium.webdriver.firefox.service import Service as FirefoxService
#
# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome", help="browser to run tests")
#
# @pytest.fixture
# def driver(request):
#     browser = request.config.getoption("--browser")
#     if browser == "chrome":
#         service = ChromeService()
#         options = webdriver.ChromeOptions()
#         driver = webdriver.Chrome(service=service, options=options)
#     elif browser == "edge":
#         service = EdgeService()
#         options = webdriver.EdgeOptions()
#         driver = webdriver.Edge(service=service, options=options)
#     elif browser == "firefox":
#         service = FirefoxService()
#         options = webdriver.FirefoxOptions()
#         driver = webdriver.Firefox(service=service, options=options)
#     else:
#         raise ValueError(f"Unsupported browser: {browser}")
#     yield driver
#     driver.quit()
#
#

#     if browser == "chrome":
#         service = ChromeService()
#         options = webdriver.ChromeOptions()
#         driver = webdriver.Chrome(service=service, options=options)
#     elif browser == "edge":
#         service = EdgeService()
#         options = webdriver.EdgeOptions()
#         driver = webdriver.Edge(service=service, options=options)
#     elif browser == "firefox":
#         service = FirefoxService()
#         options = webdriver.FirefoxOptions()
#         driver = webdriver.Firefox(service=service, options=options)
#     else:
#         raise ValueError(f"Unsupported browser: {browser}")
#     yield driver
#     driver.quit()
#
#
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestLogin:
    def test_login_chrome(self):


        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()  # Signin
        assert self.driver.title == "OrangeHRM"

        self.driver.quit()


    def test_login_edge(self):
        self.driver = webdriver.Edge()

        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()  # Signin
        assert self.driver.title == "OrangeHRM"
        self.driver.quit()

    def test_login_firefox(self):
        self.driver = webdriver.Firefox()

        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()  # Signin
        assert self.driver.title == "OrangeHRM"
        self.driver.quit()
