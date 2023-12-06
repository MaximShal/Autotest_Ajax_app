import time
import random
from selenium.common import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.time_out = 30

    def get_element(self, by, selector: str, expected_condition=EC.presence_of_element_located):
        locator = by, selector
        return WebDriverWait(self.driver, self.time_out).until(expected_condition(locator))

    def get_elements(self, by, selector, expected_condition=EC.presence_of_element_located):
        locator = by, selector
        WebDriverWait(self.driver, self.time_out).until(expected_condition(locator))
        return self.driver.find_elements(by, selector)

    def click_element(self, by, selector: str) -> None:
        element = self.get_element(by, selector)
        actions = ActionChains(self.driver)
        actions.click(element).perform()

    def fill_element(self, by, selector: str, value: str, clean=False) -> None:
        element = self.get_element(by, selector, expected_condition=EC.element_to_be_clickable)
        element.click()

        if clean:
            element.clear()
        time.sleep(2)

        element.send_keys(value)

    def check_is_element_on_page(self, by, selector) -> bool:
        locator = by, selector
        try:
            WebDriverWait(self.driver, self.time_out).until(EC.presence_of_element_located(locator))
            return True
        except WebDriverException:
            return False
