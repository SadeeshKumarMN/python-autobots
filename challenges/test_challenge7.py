"""
*****************
Challenge#7
******************
Go to copart.com
Look at the Makes/Models section of the page
Create a two-dimensional list that stores the names of the Make/Model as well as their URLs
Check that each element in this list navigates to the correct page
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_verify_each_make_and_model(driver, wait):
    driver.get('https://www.copart.com/')
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li[ng-repeat*='popular']>a")))
    make_models = driver.find_elements_by_css_selector("li[ng-repeat*='popular']>a")
    # Created 2D list for store name and URL of each make/model
    make_models_with_urls = []
    for make_model in make_models:
        name = make_model.text
        url = make_model.get_attribute('href')
        make_models_with_urls.append([name, url])

    # Verified the navigation of each URL belongs to make/model goes to the correct page
    print()
    for vehicle in make_models_with_urls:
        name = vehicle[0]
        url = vehicle[1]
        driver.get(url)
        wait.until(lambda _: (name.replace(" ", "-").lower()) in driver.title)
        print(f'{vehicle} PASSED')
