import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver():
    # code before yield is run Before Each test
    driver = webdriver.Chrome('F:\\sadeesh\\code\\python-autobots\\venv\\chromedriver.exe')
    driver.maximize_window()
    yield driver
    # code after yield is run After Each test
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, timeout=20)
