import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class Components:

    def __init__(self, driver, locator='', locator_type='css'):
        self.driver = driver
        self.locator = locator
        self.locator_type = locator_type

    def click(self):
        self.find_element().click()

    def find_element(self):
        return self.driver.find_element(self.get_by_type(), self.locator)

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def get_text(self):
        return str(self.find_element().text)

    def send_keys(self, text: str):
        self.find_element().send_keys(text)

    def clear(self):
        self.send_keys(Keys.CONTROL + 'a')
        self.send_keys(Keys.DELETE)

    def get_dom_attribute(self, name: str):
        value = self.find_element().get_dom_attribute(name)

        if value is None:
            return False
        if len(value) > 0:
            return value
        return True

    def get_by_type(self):
        if self.locator_type == "id":
            return By.ID
        elif self.locator_type == "name":
            return By.NAME
        elif self.locator_type == "xpath":
            return By.XPATH
        elif self.locator_type == "css":
            return By.CSS_SELECTOR
        elif self.locator_type == "class":
            return By.CLASS_NAME
        elif self.locator_type == "link":
            return By.LINK_TEXT
        else:
            print("Locator type " + self.locator_type + "not correct")
        return False

    def scroll_to_element(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", self.find_element())

    def verify_footer_text(self):
        footer_text = self.get_text()
        expected_text = '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
        if footer_text == expected_text:
            return True
        else:
            return False

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
        time.sleep(2)
        return self.driver.find_elements(By.CSS_SELECTOR, self.locator)

    def check_count (self, count:int):
        if len(self.find_elements()) == count:
            return True
        else:
            return False

    def click_force(self):
            self.driver.execute_script('arguments[0].click();', self.find_element())