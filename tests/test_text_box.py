import time
from pages.text_box import TextBox

def test_text_box(browser):

    text_box = TextBox(browser)

    text_box.visit()
    text_box.full_name.send_keys('Dara')
    text_box.current_address.send_keys('Saint-P')
    time.sleep(2)
    text_box.btn_submit.click_force()
    time.sleep(2)

    assert text_box.name_check.get_text() == 'Name:Dara'
    assert text_box.cur_address_check.get_text() == 'Current Address :Saint-P'
