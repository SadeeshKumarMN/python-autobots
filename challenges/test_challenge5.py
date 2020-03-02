"""
******************
Challenge#5:
******************
Part 1 - Create test_challenge5.py and write a test that does the following:

Go to copart.com
Search for "porsche"
Change Show Entries to 100
Print the number of occurrences for each Model
Example: There might be x3 PANAMERA T and x11 CAYENNE

Part 2 - Using the same, first three steps of Part 1, write a test that then does the following:

Count the number of occurrences of each Damage type
However, you need to map the Damage types to these:
REAR END
FRONT END
MINOR DENT/SCRATCHES
UNDERCARRIAGE

Any Damage type that does NOT match the above types should be grouped into a MISC Damage type
Example: SIDE and ALL OVER would each count towards MISC
Example Output: REAR END: 2, FRONT END: 7, MINOR DENT/SCRATCHES: 22, UNDERCARRIAGE: 0, MISC: 4
"""
from pprint import pprint
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *


def test_how_many_car_model(driver, wait):
    # Created reusable function for avoiding duplicate lines of code
    reusable_component(driver, wait)
    table_id = driver.find_element(By.ID, 'serverSideDataTable')
    table_body = table_id.find_element_by_tag_name('tbody')
    rows = table_body.find_elements_by_tag_name("tr")
    car_model_dict = {}
    for row in rows:
        col = row.find_elements_by_tag_name("td")[5]
        if col.text not in car_model_dict.keys():
            car_model_dict[col.text] = 1
        else:
            car_model_dict[col.text] = car_model_dict.get(col.text) + 1

    print()
    pprint(car_model_dict)
    # The above line helps to replace the following 2 lines
    # for car_model_name in sorted(car_model_dict):
    #     print(car_model_name, car_model_dict[car_model_name])
    assert sum(car_model_dict.values()) == 100


def test_how_many_damage_type(driver, wait):
    reusable_component(driver, wait)
    table_id = driver.find_element(By.ID, 'serverSideDataTable')
    table_body = table_id.find_element_by_tag_name('tbody')
    rows = table_body.find_elements_by_tag_name("tr")
    car_damage_type_dict = {
        "REAR END": 0,
        "FRONT END": 0,
        "MINOR DENT/SCRATCHES": 0,
        "UNDERCARRIAGE": 0,
        "MISC": 0
    }
    for row in rows:
        col = row.find_elements_by_tag_name("td")[11]
        if col.text.strip() not in car_damage_type_dict.keys():
            car_damage_type_dict["MISC"] += 1
        else:
            car_damage_type_dict[col.text.strip()] += 1
    print()
    pprint(car_damage_type_dict)
    assert sum(car_damage_type_dict.values()) == 100


def reusable_component(driver, wait):
    driver.get('https://www.copart.com/')
    driver.find_element_by_id('input-search').send_keys("porsche"+Keys.ENTER)
    wait.until(EC.presence_of_element_located((By.XPATH, "//select[@name='serverSideDataTable_length']/option[text("
                                                         ")='100']"))).click()
    # Achieved FluentWait logic here
    wait = WebDriverWait(driver, 20, poll_frequency=1,
                         ignored_exceptions=[StaleElementReferenceException])
    wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'MACAN')]")))
