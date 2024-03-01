import pytest
from selenium import webdriver


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com")
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

