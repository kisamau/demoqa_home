from pages.basic_page import BasicPage


class DemoQa(BasicPage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)