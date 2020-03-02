"""
******************
Challenge#1:
******************
Go to google.com
Search for “puppies”
Assert that the results page that loads has “puppies” in its title
"""
from selenium.webdriver.common.keys import Keys


def test_go_to_google(driver):
    driver.get('https://google.com')
    driver.find_element_by_name("q").send_keys("puppies"+Keys.ENTER)
    assert 'puppies' in driver.title
