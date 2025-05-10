from components.components_test import Components
from pages.basic_page import BasicPage


class WebTables(BasicPage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.btn_delete_row = Components(driver, '//span[@title="Delete"]', 'xpath')
        self.no_data = Components(driver, 'div.rt-noData')
        self.add_btn = Components(driver,'#addNewRecordButton')
        self.window_add_modal = Components(driver, 'body > div.fade.modal.show > div > div')
        self.add_modal_click = Components(driver, '#submit')

        self.modal_first_name = Components(driver, '#firstName')
        self.modal_last_name = Components(driver, '#lastName')
        self.modal_email = Components(driver, '#userEmail')
        self.modal_age = Components(driver, '#age')
        self.modal_salary = Components(driver, '#salary')
        self.modal_dept = Components(driver, '#department')

        self.fn_row = Components(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(1)')
        self.edit_row = Components(driver, '#edit-record-1')
        self.delete_row = Components(driver, '#delete-record-1')
        # self.fn_row = Components(driver, '// *[ @ id = "app"] / div / div / div / div[2] / div[2] / div[3] / div[1] / div[2] / div[3] / div / div[1]', 'xpath')

        self.header_column = Components(driver, 'div > div.rt-th.rt-resizable-header')