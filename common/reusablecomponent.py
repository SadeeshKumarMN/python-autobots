from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ReusableComponent:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def reusable_component(self):
        self.driver.get('https://www.copart.com/')
        self.driver.find_element_by_id('input-search').send_keys("porsche" + Keys.ENTER)
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//select[@name='serverSideDataTable_length']/option[text("
                           ")='100']"))).click()
        # Achieved FluentWait logic here
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[StaleElementReferenceException])
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'MACAN')]")))
