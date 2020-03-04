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
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

from utils.Utils import ScreenShot


def test_rare_car_model(driver, wait):
    driver.get('https://www.copart.com/')
    driver.find_element_by_id("input-search").send_keys("nissan" + Keys.ENTER)
    try:
        # Created re-usable function for filtering functionality
        # Args: Filter name, Filter Value
        # Examples: "Model", "Skyline" | "Year", "2007",
        # Both the input type would be string
        # For Valid filter names, please look at commented lines in the bottom.
        Filter(driver, wait).select_filter_by_name_value("Newly Added Lots", "Last 7 Days")
    except NoSuchElementException or BaseException as error:
        ScreenShot(driver).capture_screenshot('Element_Not_Found_' + datetime.now().strftime("%m_%d_%Y_%H_%M_%S"))
        raise error


"""
Accordions for the following 3 filters will be automatically expanded while search result page gets loaded(due to step#22)
1. Newly Added Lots 2. Featured Item 3.Make

Rest of the following 16 filters, accordion has to be expanded

1. Model 2. Year 3.Odometer 4.Location 5. Sale Name 6.Sale Date 7. Ownership Doc Type 8.Source
9. Vehicle Type 10.Damage 11.Body Style 12.Fuel Type 13.Engine Type 14.Transmission
15.Drive Train 16. Cylinder

"""


class Filter:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def select_filter_by_name_value(self, filter_name, filter_value):
        if filter_name not in ["Newly Added Lots", "Featured Items", "Make"]:
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(.,'" + filter_name + "')]/i"))).click()

        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(.,'" + filter_name + "')]/parent::h4/following"
                                                                                         "-sibling::div/form "
                                                                                         "//input")))
        self.driver.find_element_by_xpath(
            "//a[contains(.,'" + filter_name + "')]/parent::h4/following-sibling::div/form"
                                               "//input").send_keys(filter_value)
        assert self.driver.find_element_by_xpath("//abbr[@value='" + filter_value + "']").is_displayed()
