from components.components_test import Components
from pages.basic_page import BasicPage


class FormPage(BasicPage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)

        self.first_name = Components(driver, '#firstName')
        self.last_name = Components(driver, '#lastName')
        self.user_email = Components(driver, '#userEmail')
        self.btn_submit = Components(driver, '#submit')
        self.validated_form = Components(driver, '#userForm')