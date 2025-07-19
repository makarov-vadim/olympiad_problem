import time

import allure
import pytest

from src.configs.registration_page_config import RegistrationPageConfig

@allure.epic("Тесты сайта way2automation.com")
@allure.feature("Тест-сьют 4. Страница Registration")
class TestRegistrationPage:
    @allure.story("Тест-кейс 4.1 Проверка незаполнения обязательных полей")
    @allure.title("Проверка незаполнения обязательных полей")
    @allure.id("4.1")
    @pytest.mark.parametrize("missed_field_name", RegistrationPageConfig.REQUIRED_FIELDS)
    def test_unfill_required_fields(self, registration_page, fields_data, missed_field_name):
        with allure.step("Заполнение формы"):
            registration_page.fill_required_fields(fields_data, missed_field_name=missed_field_name)

        with allure.step("Отправление запроса на обработку формы"):
            registration_page.click_submit()

        with allure.step("Проверка отправления запроса"):
            registration_page.assert_required_field_not_filled(missed_field_name)


    @allure.story("Тест-кейс 4.2 Проверка заполнения обязательных полей валидными данными")
    @allure.title("Проверка заполнения обязательных полей валидными данными")
    @allure.id("4.2")
    def test_fill_required_fields(self, registration_page, fields_data):
        with allure.step("Заполнение формы"):
            registration_page.fill_required_fields(fields_data)

        with allure.step("Отправление запроса на обработку формы"):
            registration_page.click_submit()

        with allure.step("Проверка отправления запроса"):
            registration_page.assert_request_processed_correctly(fields_data)


    @allure.story("Тест-кейс 4.3 Проверка выбора всех значений из чекбокса Hobby")
    @allure.title("Проверка выбора всех значений из чекбокса Hobby")
    @allure.id("4.3")
    def test_select_all_hobbies(self, registration_page_without_hobby, fields_data):
        with allure.step("Заполнение формы"):
            registration_page_without_hobby.select_all_hobbies()

        with allure.step("Отправление запроса на обработку формы"):
            registration_page_without_hobby.click_submit()

        with allure.step("Проверка отправления запроса"):
            registration_page_without_hobby.assert_request_processed_correctly(fields_data)


    @allure.story("Тест-кейс 4.4 Проверка ввода невалидного адреса электронной почты в поле E-mail")
    @allure.title("Проверка ввода невалидного адреса электронной почты в поле E-mail")
    @allure.id("4.4")
    def test_enter_invalid_email(self, registration_page_without_email, fields_data):
        with allure.step("Заполнение формы"):
            registration_page_without_email.enter_invalid_email()

        with allure.step("Отправление запроса на обработку формы"):
            registration_page_without_email.click_submit()

        with allure.step("Проверка отправления запроса"):
            registration_page_without_email.assert_required_field_not_filled(missed_field_name="email")


    @allure.story("Тест-кейс 4.5 Проверка выбора значения в радиобаттоне Marital Status")
    @allure.title("Проверка выбора значения в радиобаттоне Marital Status")
    @allure.id("4.5")
    def test_select_random_marital_status(self, registration_page_with_required_fields, fields_data):
        with allure.step("Заполнение формы"):
            registration_page_with_required_fields.select_random_marital_status()

        with allure.step("Отправление запроса на обработку формы"):
            registration_page_with_required_fields.click_submit()

        with allure.step("Проверка отправления запроса"):
            registration_page_with_required_fields.assert_request_processed_correctly(fields_data)


    @allure.story("Тест-кейс 4.6 Проверка выбора значения в выпадающем списке Country")
    @allure.title("Проверка выбора значения в выпадающем списке Country")
    @allure.id("4.6")
    def test_select_random_country(self, registration_page_with_required_fields, fields_data):
        with allure.step("Заполнение формы"):
            registration_page_with_required_fields.select_random_country()

        with allure.step("Отправление запроса на обработку формы"):
            registration_page_with_required_fields.click_submit()

        with allure.step("Проверка отправления запроса"):
            registration_page_with_required_fields.assert_request_processed_correctly(fields_data)


    @allure.story("Тест-кейс 4.7 Проверка выбора значения в выпадающем списке Date of Birth. Month")
    @allure.title("Проверка выбора значения в выпадающем списке Date of Birth. Month")
    @allure.id("4.7")
    def test_select_random_date_of_birth_month(self, registration_page_with_required_fields, fields_data):
        with allure.step("Заполнение формы"):
            registration_page_with_required_fields.select_random_date_of_birth_month()

        with allure.step("Отправление запроса на обработку формы"):
            registration_page_with_required_fields.click_submit()

        with allure.step("Проверка отправления запроса"):
            registration_page_with_required_fields.assert_request_processed_correctly(fields_data)


    @allure.story("Тест-кейс 4.8 Проверка выбора значения в выпадающем списке Date of Birth. Day")
    @allure.title("Проверка выбора значения в выпадающем списке Date of Birth. Day")
    @allure.id("4.8")
    def test_select_random_date_of_birth_day(self, registration_page_with_required_fields, fields_data):
        with allure.step("Заполнение формы"):
            registration_page_with_required_fields.select_random_date_of_birth_day()

        with allure.step("Отправление запроса на обработку формы"):
            registration_page_with_required_fields.click_submit()

        with allure.step("Проверка отправления запроса"):
            registration_page_with_required_fields.assert_request_processed_correctly(fields_data)

    @allure.story("Тест-кейс 4.9 Проверка выбора значения в выпадающем списке Date of Birth. Year")
    @allure.title("Проверка выбора значения в выпадающем списке Date of Birth. Year")
    @allure.id("4.9")
    def test_select_random_date_of_birth_year(self, registration_page_with_required_fields, fields_data):
        with allure.step("Заполнение формы"):
            registration_page_with_required_fields.select_random_date_of_birth_year()

        with allure.step("Отправление запроса на обработку формы"):
            registration_page_with_required_fields.click_submit()

        with allure.step("Проверка отправления запроса"):
            registration_page_with_required_fields.assert_request_processed_correctly(fields_data)


    @allure.story("Тест-кейс 4.10 Проверка прикрепления файла в поле загрузки файла Your Profile Picture")
    @allure.title("Проверка прикрепления файла в поле загрузки файла Your Profile Picture")
    @allure.id("4.10")
    def test_enter_profile_picture_path(self, registration_page_with_required_fields, fields_data):
        with allure.step("Заполнение формы"):
            registration_page_with_required_fields.enter_profile_picture_path()

        with allure.step("Отправление запроса на обработку формы"):
            registration_page_with_required_fields.click_submit()

        with allure.step("Проверка отправления запроса"):
            registration_page_with_required_fields.assert_request_processed_correctly(fields_data)


    @allure.story("Тест-кейс 4.11 Проверка ввода текста в поле About Yourself")
    @allure.title("Проверка ввода текста в поле About Yourself")
    @allure.id("4.11")
    def test_enter_about_yourself(self, registration_page_with_required_fields, fields_data):
        with allure.step("Заполнение формы"):
            registration_page_with_required_fields.enter_about_yourself()


        with allure.step("Отправление запроса на обработку формы"):
            registration_page_with_required_fields.click_submit()

        with allure.step("Проверка отправления запроса"):
            registration_page_with_required_fields.assert_request_processed_correctly(fields_data)
