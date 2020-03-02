"""
****************
Challenge#6
****************
Go to copart.com
Search for 'nissan'
Then for the Model, search 'skyline'. This is a rare car that might not exist
If it doesn't exist, catch the exception and take a screenshot
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


def test_rare_car_model(driver, wait):
    driver.get('https://www.copart.com/')
    driver.find_element_by_id("input-search").send_keys("nissan"+Keys.ENTER)
    wait.until(EC.presence_of_element_located((By.XPATH, "//li[4]/h4/a/i"))).click()
    driver.find_element_by_xpath("(//input[@type='text'])[6]").send_keys("skyline")
    try:
        # Find the element belongs to Skyline; at present 3 Skyline cars are available in the page
        skyline_car = driver.find_element_by_id("lot_model_descSKYLINE")
        assert skyline_car.is_displayed()
    except NoSuchElementException or BaseException as error:
        driver.save_screenshot('test_challenge6_skyline_model_not_found.png')
        raise error

