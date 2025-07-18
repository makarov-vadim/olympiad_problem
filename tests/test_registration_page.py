import time


class TestClickEventsPage:
    def test_1(self, registration_page):
        registration_page.enter_first_name(first_name="John")
        time.sleep(2)

        registration_page.enter_last_name(last_name="Doe")
        time.sleep(2)

        registration_page.click_random_marital_status()
        time.sleep(2)

        registration_page.click_random_hobby()
        time.sleep(2)
        #
        registration_page.click_all_hobbies()
        time.sleep(2)

        registration_page.click_random_country()
        time.sleep(2)

        registration_page.click_random_date_of_birth_month()
        time.sleep(2)

        registration_page.click_random_date_of_birth_day()
        time.sleep(2)

        registration_page.click_random_date_of_birth_year()
        time.sleep(2)

        registration_page.enter_phone_number(number="5551234")
        time.sleep(2)

        registration_page.enter_username(username="John!!!!!!!!!!!!!!")
        time.sleep(2)

        registration_page.enter_email(email="email@email.com")
        time.sleep(2)

        registration_page.enter_profile_picture_path()
        time.sleep(5)

        registration_page.enter_about_yourself(about_yourself="Hello World")
        time.sleep(2)

        registration_page.enter_password(password="<PASSWORD>")
        time.sleep(2)

        registration_page.enter_confirm_password(password="<PASSWORD>")
        time.sleep(2)

        registration_page.click_submit()
        time.sleep(2)









