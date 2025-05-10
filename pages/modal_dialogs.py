
from components.components_test import Components
from pages.basic_page import BasicPage


class ModelPage(BasicPage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver,self.base_url)

        self.icon = Components(driver, 'header > a > img')
        self.hdr_element = Components(driver, "#app > header > a > img")
        self.link = Components(driver, "#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(3) > div > ul > li")

        self.btn_small = Components(driver, '#showSmallModal')
        self.btn_close_small = Components(driver, '#closeSmallModal')
        self.btn_large = Components(driver, '#showLargeModal')
        self.btn_close_large = Components(driver, '#closeLargeModal')