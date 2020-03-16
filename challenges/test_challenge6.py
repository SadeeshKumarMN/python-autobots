"""
****************
Challenge#6
****************
Go to copart.com
Search for 'nissan'
Then for the Model, search 'skyline'. This is a rare car that might not exist
If it doesn't exist, catch the exception and take a screenshot
"""
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

from common.filter import Filter
from common.screenshot import ScreenShot


def test_rare_car_model(driver, wait):
    driver.get('https://www.copart.com/')
    driver.find_element_by_id("input-search").send_keys("nissan")
    driver.find_element_by_xpath(".//button[contains(.,'Search')]").click()
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Cylinder")))
    try:
        # Created re-usable function for filtering functionality
        # Args: Filter name, Filter Value
        # Examples: "Newly Added Lots", "Last 7 Days"|"Model", "Skyline" | "Year", "2007" |"Cylinder", "U"
        # Both the input type would be string
        # For Valid filter names, please look at commented lines in the bottom.
        # For Invalid input, Pass with ex: Cylinder, UU
        Filter(driver, wait).select_filter_by_name_value("Cylinder", "UU")
    except NoSuchElementException or BaseException as error:
        ScreenShot(driver).capture_screenshot('Element_Not_Found_' + datetime.now().strftime("%m_%d_%Y_%H_%M_%S"))
        raise error






