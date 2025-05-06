from components.components_test import Components
from pages.basic_page import BasicPage


class TextBox(BasicPage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver,self.base_url)

        self.full_name = Components(driver, '#userName.mr-sm-2.form-control')
        self.current_address = Components(driver, '#currentAddress.form-control')
        self.btn_submit = Components(driver, '#submit', "css")
        self.name_check = Components(driver, '#name')
        self.cur_address_check = Components(driver, '#output > div> #currentAddress')

