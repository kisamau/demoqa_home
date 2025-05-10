from components.components_test import Components
from pages.basic_page import BasicPage


class AlertPage(BasicPage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)

        self.btn_timer = Components(self.driver, '#timerAlertButton')