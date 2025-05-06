from components.components_test import Components
from pages.basic_page import BasicPage


class Elements(BasicPage):

    def __init__(self, driver):
        super().__init__(driver, self.base_url)
        self.base_url = 'https://demoqa.com/elements'

        self.footer = Components(driver, 'footer')
        self.button_elements = Components(driver, '#app > div > div > div > div.category-cards > div.card.mt-4.top-card')
        self.text_page = Components(driver, '#app > div.row > div.col-12.mt-4.col-md-6')
