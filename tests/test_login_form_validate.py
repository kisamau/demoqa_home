# from pages.form_page import FormPage
#
#
# def test_login_form_validate(browser):
#     loginform = FormPage(browser)
#     loginform.visit()
#     assert loginform.first_name.get_dom_attribute('placeholder') == 'First Name'
#     assert loginform.last_name.get_dom_attribute('placeholder') == 'Last Name'
#     assert loginform.user_email.get_dom_attribute('placeholder') == 'name@example.com'
#     assert loginform.user_email.get_dom_attribute('pattern') == '^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'
#     loginform.btn_submit.click_force()
#     assert loginform.validated_form.get_dom_attribute('class') == 'was-validated'