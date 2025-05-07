import time

from pages.webtables_page import WebTables


def test_webtables(browser):
    wt = WebTables(browser)

    wt.visit()

    wt.add_btn.click()
    assert not wt.no_data.exist()

    while wt.btn_delete_row.exist():
        wt.btn_delete_row.click_force()

    time.sleep(2)
    assert wt.no_data.exist()

    wt.modal_first_name.send_keys('Stella')
    wt.modal_last_name.send_keys('Trailblazer')
    wt.modal_email.send_keys('trashcat@exxxpress.com')
    wt.modal_age.send_keys('25')
    wt.modal_salary.send_keys('100000')
    wt.modal_dept.send_keys('KMM')
    wt.add_modal_click.click()
    time.sleep(2)
    assert wt.fn_row.exist()

    wt.edit_row.click()
    time.sleep(2)
    wt.modal_first_name.clear()
    time.sleep(2)
    wt.modal_first_name.send_keys('Caelus')
    wt.add_modal_click.click()
    time.sleep(2)
