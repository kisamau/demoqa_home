import time

from pages.modal_dialogs import ModelPage


def test_check_modal(browser):
        modal_page = ModelPage(browser)
        modal_page.visit()

        modal_page.btn_small.click()
        time.sleep(2)
        modal_page.btn_close_small.click()

        modal_page.btn_large.click()
        time.sleep(2)
        modal_page.btn_close_large.click()