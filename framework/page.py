import time
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.time_out = 30

    def find_element(self, by, selector: str, expected_condition=EC.presence_of_element_located):
        locator = by, selector
        return WebDriverWait(self.driver, self.time_out).until(expected_condition(locator))

    def click_element(self, by, selector: str) -> None:
        element = self.find_element(by, selector)
        actions = ActionChains(self.driver)
        actions.click(element).perform()

    def fill_element(self, by, selector: str, value: str, clean=False) -> None:
        element = self.find_element(by, selector, expected_condition=EC.element_to_be_clickable)
        if clean:
            self._clear_input(element)
        time.sleep(2)
        self._insert_value(element, value)

    @staticmethod
    def _clear_input(elem) -> None:
        elem.send_keys(Keys.CONTROL + "a")
        elem.send_keys(Keys.BACKSPACE)

    @staticmethod
    def _insert_value(elem, value: str) -> None:
        for char in value:
            timeout_random = random.randint(20, 40)
            elem.send_keys(char)
            time.sleep(timeout_random / 100)
