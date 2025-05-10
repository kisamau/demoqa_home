import time

from pages.alert_page import AlertPage


def test_timer(browser):
    alert_page = AlertPage(browser)
    alert_page.visit()

    assert not alert_page.alert()

    alert_page.btn_timer.click_force()
    time.sleep(5)
    assert alert_page.alert()
    assert alert_page.alert().text == 'This alert appeared after 5 seconds'