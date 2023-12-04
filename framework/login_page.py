from .page import Page
from selenium.webdriver.common.by import By


class LoginPage(Page):
    def __init__(self, driver):
        super().__init__(driver)

    def sign_in(self, username, password):
        self.click_element(By.XPATH, '//*[@bounds="[32,1160][688,1256]" and @clickable="true"]')
