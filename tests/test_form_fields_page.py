import time

import allure


class TestFormFieldsPage:
    def test_form_fields_page(self, form_fields_page):

        form_fields_page.enter_name()
        time.sleep(2)
        form_fields_page.enter_empty_name()
        time.sleep(2)
        form_fields_page.enter_password()
        time.sleep(2)
        form_fields_page.click_random_favorite_drink()
        time.sleep(2)
        form_fields_page.click_all_favorite_drinks()
        time.sleep(2)
        form_fields_page.click_random_favorite_color()
        time.sleep(2)
        form_fields_page.click_random_automation()
        time.sleep(2)
        form_fields_page.enter_email()
        time.sleep(2)
        form_fields_page.enter_message()
        time.sleep(2)
        form_fields_page.click_submit()
