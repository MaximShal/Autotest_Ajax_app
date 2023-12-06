import time
from selenium.webdriver.common.by import By

from .page import Page


class LoginPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.name_or_pass_not_confirm_msg = "Невірний логін або пароль"

    def sign_in(self, username: str, password: str) -> bool:
        self.click_element(By.XPATH, '//*[@bounds="[32,1160][688,1256]" and @clickable="true"]')
        self.fill_element(By.XPATH, '//*[@resource-id="defaultAutomationId" and @bounds="[0,208][720,339]"]', username)
        self.fill_element(By.XPATH, '//*[@resource-id="defaultAutomationId" and @bounds="[0,339][720,470]"]', password)
        self.click_element(By.XPATH, '//*[@bounds="[32,654][688,750]" and @clickable="true"]')

        msg = None
        if self.check_is_element_on_page(By.XPATH, '//*[@resource-id="com.ajaxsystems:id/snackbar_text"]'):
            msg = self.get_element(By.XPATH, '//*[@resource-id="com.ajaxsystems:id/snackbar_text"]') \
                .get_attribute("text")

        time.sleep(5)

        if self.check_is_element_on_page(By.XPATH, '//*[@resource-id="com.ajaxsystems:id/back"]'):
            retries = 0
            while retries < 5:
                if msg == self.name_or_pass_not_confirm_msg:
                    break
                time.sleep(5)

                self.click_element(By.XPATH, '//*[@text="Вхід"]')
                msg = self.get_element(By.XPATH, '//*[@resource-id="com.ajaxsystems:id/snackbar_text"]')\
                            .get_attribute("text")
                retries += 1

            self.click_element(By.XPATH, '//*[@resource-id="com.ajaxsystems:id/back"]')
            return False

        else:
            if self.check_is_element_on_page(By.XPATH, '//*[@resource-id="com.ajaxsystems:id/icNoHub"]'):
                return True
