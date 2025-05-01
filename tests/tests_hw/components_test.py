import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class Components:

    def __init__(self, driver, locator= ''):
        self.driver = driver
        self.locator = locator
        self.base_url = 'https://demoqa.com/'

    def visit(self):
        return self.driver.get(self.base_url)

    def find_element(self):
        time.sleep(2)
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def get_text(self):
        # footer = self.find_element()
        # if footer:
        return str(self.find_element().text)
        # else:
        #     return ''

    def verify_footer_text(self):
        footer_text = self.get_text()
        expected_text = '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
        if footer_text == expected_text:
            return True
        else:
            return False

    def click(self):
        self.find_element().click()

    def verify_center_text(self):
        text_page = self.locator
        center_text = 'Please select an item from left to start practice'
        if text_page == center_text:
            return True
        else:
            return False

    def visible (self):
        return self.find_element().is_displayed()

    def find_elements(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.locator)

    def check_count (self, count:int):
        if len(self.find_elements()) == count:
            return True
        else:
            return False

class Elements(Components):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        self.footer = Components(driver, 'footer')
        self.button_elements = Components(driver, '#app > div > div > div > div.category-cards > div.card.mt-4.top-card')
        self.text_page = Components(driver, '#app > div.row > div.col-12.mt-4.col-md-6')
        super().__init__(driver)
