import random

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.options import Options

import time


class TestLogin:

    def test_login_chrome(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-gpu')
        options.add_argument('--user-agent={}'.format(random.choice(list(self.user_agents))))

        driver = webdriver.Chrome(options=options)
        driver.set_page_load_timeout(90)

        # Load the URL and get the page source
        driver.implicitly_wait(6)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()



    def test_login_edge(self):
        edgeOption = webdriver.EdgeOptions()
        edgeOption.add_argument('--guest')
        edgeOption.add_argument("start-maximized")
        self.serv_obj = Service("D:\Drivers\msedgedriver.exe")
        self.driver = webdriver.Edge(service=self.serv_obj, options=edgeOption)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

