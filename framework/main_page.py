from selenium.webdriver.common.by import By

from .page import Page


class MainPage(Page):
    def __init__(self, driver):
        super().__init__(driver)

    def check_side_bar_elements(self):
        self.click_element(By.XPATH, '//*[@resource-id="com.ajaxsystems:id/menuDrawer"]')
        sidebar_elements = self.get_elements(By.XPATH, '//*[@index="0" and @class="android.widget.ScrollView"]/*')
        sidebar_elements_img = self.get_elements(By.XPATH, '//*[@index="0" and @class="android.widget.ScrollView"]'
                                                           '/*/*[@class="android.view.View"]')
        sidebar_elements_text = self.get_elements(By.XPATH, '//*[@index="0" and @class="android.widget.ScrollView"]'
                                                            '/*/*[@class="android.widget.TextView"]')

        sidebar_terms_of_use = self.get_element(By.XPATH, '//*[@resource-id="com.ajaxsystems:id/documentation_text"]')
        sidebar_elements += [sidebar_terms_of_use]
        sidebar_elements_text += [sidebar_terms_of_use]

        return {
            'clickable': all([bool(elem.get_attribute('clickable')) for elem in sidebar_elements]),
            'show_img': all([bool(elem.get_attribute('enabled')) for elem in sidebar_elements_img]),
            'show_text': all([bool(elem.get_attribute('enabled')) for elem in sidebar_elements_text]),
            'text': [elem.get_attribute('text') for elem in sidebar_elements_text],
        }
