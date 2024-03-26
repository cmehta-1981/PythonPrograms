import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service


class TestLogin:

    """
    def test_login_edg1(self):
        sedgeOption = webdriver.EdgeOptions()
        sedgeOption.add_argument('--guest')
        sedgeOption.add_argument("start-maximized")
        self.serv_obj = Service("D:\\Drivers\\msedgedriver.exe")
        self.driver = webdriver.Edge(service=self.serv_obj, options=sedgeOption)
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
        self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()
        self.driver.implicitly_wait(time_to_wait=200)
        print(self.driver.title)
        """

    def test_login_edge(self):
        from selenium import webdriver
        from selenium.webdriver.edge.options import Options as EdgeOptions

        options = EdgeOptions()
        options.add_argument('--guest')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Edge(options=options)
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
        self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()
        self.driver.implicitly_wait(time_to_wait=200)
        print(self.driver.title)
        self.driver.quit()

    def test_login_edge1(self):
        from selenium import webdriver
        from selenium.webdriver.edge.options import Options as EdgeOptions

        options = EdgeOptions()
        options.add_argument('--guest')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Edge(options=options)
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
        self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()
        self.driver.implicitly_wait(time_to_wait=200)
        print(self.driver.title)
        self.driver.quit()