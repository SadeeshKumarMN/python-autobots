"""
*****************
Challenge#7
******************
Go to copart.com
Look at the Makes/Models section of the page
Create a two-dimensional list that stores the names of the Make/Model as well as their URLs
Check that each element in this list navigates to the correct page
"""
import sys
import traceback
from pprint import pprint
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_verify_each_make_and_model(driver, wait):
    try:
        driver.get('https://www.copart.com/')
        wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[starts-with(@href,'./popular')]")))
        popular_items = driver.find_elements_by_xpath("//a[starts-with(@href,'./popular')]")

        # Created 2D list for store name and URL of each popular items
        popular_vehicles = []
        for vehicle in popular_items:
            name = vehicle.text
            url = vehicle.get_attribute('href')
            popular_vehicles.append([name, url])
        print()
        print("Count# of vehicles under "'Most Popular items'" section is {}".format(len(popular_vehicles)))

        # Verified the navigation of each URL belongs to popular items(make/models,categories) goes to the correct page
        print()
        success_items = []
        failure_items = []
        error_messages = set([])
        for vehicle in popular_vehicles:
            name = vehicle[0]
            url = vehicle[1]
            driver.get(url)
            wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@id='serverSideDataTable']//tbody")))
            if name in driver.find_element_by_xpath("//*[@id='serverSideDataTable']//tbody").text:
                success_items.append([name, url])
            else:
                failure_items.append([name, url])

    except BaseException as error:
        # This comment block is about to capture the error/exception thrown at specific line
        # _, _, tb = sys.exc_info()
        # traceback.print_tb(tb)
        # tb_info = traceback.extract_tb(tb)
        # filename, line, func, text = tb_info[-1]
        # error_messages.add('An error occurred on line {} in statement {}'.format(line, text))
        error_messages.add(error)
    finally:
        if len(success_items) == len(popular_vehicles):
            print("Success! All the vehicles belongs to popular section are navigated to the correct page")
            print()
            pprint(success_items)
        elif len(failure_items) > 0:
            print("Failures are there! Please check with Business")
            print("Count# of incorrect-navigation items: {}".format(len(failure_items)))
            pprint(failure_items)
            print()
            print("Count# of correct-navigation items: {}".format(len(success_items)))
            pprint(success_items)
        else:
            print("Exceptions/Errors#:")
            pprint(error_messages)
