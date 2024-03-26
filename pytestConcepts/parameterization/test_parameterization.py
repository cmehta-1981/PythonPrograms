import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions


class TestClass:

    @pytest.mark.parametrize('num1,num2',
                             [(1, 1), (2, 2), (2, 3), (3, 4), (4, 4)])  # execute the test with combination of data
    def test_parameter(self, num1, num2):
        assert num1 == num2

    @pytest.mark.parametrize('username,password',
                             [('standard_user', 'secret_sauce'), ('locked_out_user', 'secret_sauce')])
    def test_login(self, username, password):

        options = EdgeOptions()
        options.add_argument('--guest')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Edge(options=options)
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(username)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()
        self.driver.implicitly_wait(time_to_wait=200)
        self.pagetitle = self.driver.title
        try:
            assert "Swag Labs" == self.pagetitle
            self.driver.quit()
        except:
            self.driver.quit
            assert False
