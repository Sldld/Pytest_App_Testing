import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="session")
def config():
    with open('C:/Users/Q1/PythonAlgoritmika/PytestCodes/Ders45Algoritmika/constants.yaml', 'r') as file:
        return yaml.safe_load(file)

@pytest.fixture(scope="session")
def driver(config):
    service = Service(config['driver_path'])
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def tested_elements():
    return {
        "cookie_div": {
            "selector": "div.cookies",
            "properties": {
                "background-color": "rgba(255, 0, 0, 1)",
                "height": "155.2px"
            }
        }
    }
