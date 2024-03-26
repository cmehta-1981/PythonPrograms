import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture()
def setup(browser):
    try:
        print("Launching browser")
        if browser == 'edge':
            options = EdgeOptions()
            options.add_argument('--guest')
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Edge(options=options)

        elif browser == 'chrome':
            options = ChromeOptions()
            options.add_argument('--guest')
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Chrome(options=options)

        return driver
    except:
        print("browser not found")


# This will get the value from CLI
def pytest_addoption(parser):
    parser.addoption("--browser")


# This will return the browser value to setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# it is hook for adding Environment info to HTML report
def pytest_configure(config):
    config._metadata = {
        "Tester": "CM",
        "Project Name": "Pytest Framework Practice",
    }

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    #metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)