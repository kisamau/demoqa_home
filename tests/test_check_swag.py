from pages.swag_labs import SwagLabs

def test_check_icon(browser):
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    assert swag_labs_page.exist_icon()
    assert swag_labs_page.exist_user_name()
    assert swag_labs_page.exist_password()