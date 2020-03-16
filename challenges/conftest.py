import os
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver():
    # code before yield is run Before Each test
    ROOT_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    driver_path = os.path.join(os.path.sep, ROOT_DIR, 'venv' + os.sep)
    driver = webdriver.Chrome(driver_path+'chromedriver.exe')
    driver.maximize_window()
    yield driver
    # code after yield is run After Each test
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, timeout=10)
