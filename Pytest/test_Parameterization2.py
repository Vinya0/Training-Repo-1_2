import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestLogin:
    @pytest.mark.parametrize('user,pwd,should_pass', [
        ("Admin", "admin123", True),    # Valid credentials
        ("adm", "admin123", False),     # Invalid username
        ("Admin", "adm", False),        # Invalid password
        ("adm", "adm", False),          # Both invalid
        ("", "", False)                 # Both empty
    ])
    def test_login(self, user, pwd, should_pass):
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/")
        wait = WebDriverWait(driver, 10)

        username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password = driver.find_element(By.NAME, "password")

        username.clear()
        username.send_keys(user)
        password.clear()
        password.send_keys(pwd)

        login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_btn.click()

        time.sleep(2)  # wait for response

        if should_pass:
            dashboard = wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))
            print(f"Login successful for user: {user}")
            assert dashboard.is_displayed()
        elif user == "" and pwd == "":
            errors = driver.find_elements(By.XPATH, "//span[text()='Required']")
            print("Validation errors for empty fields:")
            for e in errors:
                print("-", e.text)
            assert len(errors) >= 2
        else:
            toast = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]")))
            print("Toast message on invalid login:", toast.text)
            assert "invalid credentials" in toast.text.lower()

        driver.quit()
