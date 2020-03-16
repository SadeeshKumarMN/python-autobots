"""
Accordions for the following 3 filters will be automatically expanded while search result page gets loaded(due to step#22)
1. Newly Added Lots 2. Featured Item 3.Make

Rest of the following 16 filters, accordion has to be expanded

1. Model 2. Year 3.Odometer 4.Location 5. Sale Name 6.Sale Date 7. Ownership Doc Type 8.Source
9. Vehicle Type 10.Damage 11.Body Style 12.Fuel Type 13.Engine Type 14.Transmission
15.Drive Train 16. Cylinder

"""
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Filter:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def select_filter_by_name_value(self, filter_name, filter_value):
        filter_name_element = self.driver.find_element_by_xpath("//a[contains(.,'" + filter_name + "')]")

        # For Scroll to the element- for taking right screenshot
        self.driver.execute_script("arguments[0].scrollIntoView();", filter_name_element)
        if filter_name not in ["Newly Added Lots", "Featured Items", "Make"]:
            filter_name_element.click()

        # Used regular expression and conversion here for extract number from string
        hyperlink_text = (filter_name_element.get_attribute("href"))
        temp = re.findall(r'\d+', hyperlink_text)
        index_of_filter_name = str(list(map(int, temp))[0])

        self.driver.find_element_by_xpath("//*[@id='collapseinside"+index_of_filter_name+"']//input").send_keys(filter_value)
        assert self.driver.find_element_by_xpath("//abbr[@value='" + filter_value + "']").is_displayed()