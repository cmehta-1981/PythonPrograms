import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions


class TestCLI:

    def test_login(self,setup):
        print('this is driver calling', setup)
        self.driver = setup
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
        self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()
        self.driver.implicitly_wait(time_to_wait=200)
        self.pagetitle = self.driver.title
        try:
            assert "Swag Labs" == self.pagetitle
            self.driver.quit()
        except:
            self.driver.quit
            assert False
