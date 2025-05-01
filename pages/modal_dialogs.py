
from tests.tests_hw.components_test import Components


class ModelPage(Components):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver,self.base_url)

        self.icon = Components(driver, 'header > a > img')
        self.hdr_element = Components(driver, "#app > header > a > img")
        self.link = Components(driver, "#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(3) > div > ul > li")