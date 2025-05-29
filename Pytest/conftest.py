# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
# @pytest.fixture()
# def setup():
#     print("Launching browser...")
# #     if browser == "chrome":
# #         from selenium.webdriver.chrome.service import Service
# #         serv_obj = Service("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
# #         driver = webdriver.Chrome(service=serv_obj)
# #     elif browser == "edge":
# #         from selenium.webdriver.edge.service import Service
# #         serv_obj = Service("C:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
# #         driver = webdriver.Edge(service=serv_obj)
# #     elif browser == "firefox":
# #         from selenium.webdriver.firefox.service import Service
# #         serv_obj = Service("C:\\Drivers\\geckodriver-v0.29.1-win64\\geckodriver.exe")
# #         driver = webdriver.Firefox(service=serv_obj)
# #     return driver
# #
# # def pytest_addoption(parser):    # This will get the value from CLI
# #     parser.addoption("--browser")
# #
# # @pytest.fixture()
# # def browser(request):       # This will return the Browser value to setup method
# #     return request.config.getoption("--browser")
# #
# # # customizing reHTML Report
# # # It is hook for Adding Environment info to HTML Report
# # def pytest_configure(config):
# #     config._metadata['Project Name'] = 'Orange HRM'
# #     config._metadata['Module Name'] = 'Login Module'
# #     config._metadata['Tester Name'] = 'Pavan'
# #
# # # It is hook for delete/Modify Environment info to HTML Report
# # @pytest.mark.optionalhook
# # def pytest_metadata(metadata):
# #     metadata.pop("JAVA_HOME", None)
# #     metadata.pop("Plugins", None)



# conftest.py or test file

import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    driver = webdriver.Chrome()  # or Firefox, etc.
    yield driver                 # Provide the driver to the test
    driver.quit()


    # Cleanup after test

    # import pytest
    # from selenium import webdriver
    # from selenium.webdriver.chrome.service import Service as ChromeService
    # from selenium.webdriver.edge.service import Service as EdgeService
    # from selenium.webdriver.firefox.service import Service as FirefoxService
    #
    # def pytest_addoption(parser):
    #     parser.addoption(
    #         "--browser",
    #         action="store",
    #         default="chrome",
    #         help="Browser to run tests: chrome, edge, firefox",
    #     )
    #
    # @pytest.fixture
    # def driver(request):
    #     browser = request.config.getoption("--browser")
    #
    #     if browser == "chrome":
    #         driver = webdriver.Chrome()
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
    #
    #     yield driver
    #     driver.quit()
