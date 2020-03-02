"""
******************
Challenge#3:
******************
Go to copart.com
On the Home Page, under Most Popular Items, there is a Makes/Models section. For each Make or Model in this section,
print the name of the Make or Model with its URL (aka href) next to it
Example Output: SILVERADO - https://www.copart.com/popular/model/silverado
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_scrap_car_model_and_url(driver, wait):
    driver.get('https://www.copart.com/')
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li[ng-repeat*='popular']>a")))
    popular_items = driver.find_elements_by_css_selector("li[ng-repeat*='popular']>a")
    assert len(popular_items) == 10
    print()
    for car in popular_items:
        print(car.text, "-", car.get_attribute("href"))



