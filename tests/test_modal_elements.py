# import time
#
# from pages.modal_dialogs import ModelPage
# from components.components_test import Components
#
#
# def test_modal_elements(browser):
#     modal_page = ModelPage(browser)
#     modal_page.visit()
#     # assert modal_page.link.check_count(count=5)
#
#
# def test_navigation_modal(browser):
#     demo_qa_page = Components(browser)
#     modal_page = ModelPage(browser)
#
#     modal_page.visit()
#     modal_page.refresh()
#
#     modal_page.hdr_element.click()
#     time.sleep(3)
#     browser.back()
#     browser.set_window_size(900, 400)
#     browser.forward()
#     assert demo_qa_page.equal_url()
#     assert demo_qa_page.title()
#
#     browser.set_window_size(1000, 1000)