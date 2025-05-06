# import time
# from pages.demoqa import DemoQa
# from pages.modal_dialogs import ModelPage
#
#
# def test_modal_elements(browser):
#     modal_page = ModelPage(browser)
#     modal_page.visit()
#     # assert modal_page.link.check_count(count=5)
#
# def test_navigation_modal(browser):
#     demo_qa_page = DemoQa(browser)
#     modal_page = ModelPage(browser)
#     modal_page.visit()
#     modal_page.refresh()
#
#     modal_page.hdr_element.click()
#     time.sleep(3)
#     demo_qa_page.back()
#     demo_qa_page.set_window_size(900, 400)
#     demo_qa_page.forward()
#     assert demo_qa_page.equal_url()
#     assert demo_qa_page.title()
#
#     browser.set_window_size(1000, 1000)