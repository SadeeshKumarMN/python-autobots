"""
******************
Challenge#2:
******************
Go to copart.com
Search for "exotics"
Assert "PORSCHE" is in the list of cars on the Results Page
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


def test_go_to_copart(driver, wait):
    driver.get('https://www.copart.com/')
    driver.find_element_by_id("input-search").send_keys("exotics"+Keys.ENTER)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'PORSCHE')]")))
    content = driver.find_element(By.XPATH, "//span[contains(.,'PORSCHE')]")
    assert content.is_displayed()
    # Verified no of 'PORSHE' cars in the resultant web table
    # assert len(driver.find_elements(By.XPATH, "//td[5]/span[contains(.,'PORSCHE')]")) == 16
