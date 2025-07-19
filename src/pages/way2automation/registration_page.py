import random
from urllib.parse import unquote_plus

import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.configs.registration_page_config import (RegistrationPageConfig,
                                                  RegistrationPageExpectedResults,
                                                  RegistrationPageURLS)
from src.helpers.helper import (generate_email,
                                get_longest_subsequences_in_texts,
                                get_permutations,
                                get_size_longest_subsequence)
from src.pages.base_page import BasePage


class RegistrationPage(BasePage):

    # Локаторы страницы RegistrationPage
    FIELD_FIRST_NAME = (By.CSS_SELECTOR, 'p:nth-child(1) > input[type=text]')
    FIELD_LAST_NAME = (By.CSS_SELECTOR, 'p:nth-child(2) > input[type=text]')
    FIELD_PHONE_NUMBER = (By.CSS_SELECTOR, 'fieldset:nth-child(6) > input[type=text]')
    FIELD_USERNAME = (By.CSS_SELECTOR, 'fieldset:nth-child(7) > input[type=text]')
    FIELD_EMAIL = (By.CSS_SELECTOR, 'fieldset:nth-child(8) > input[type=text]')
    FIELD_ABOUT_YOURSELF = (By.CSS_SELECTOR, 'fieldset:nth-child(10) > textarea')
    FIELD_PASSWORD = (By.XPATH, '//*/fieldset[11]/input')
    FIELD_CONFIRM_PASSWORD = (By.XPATH, '//*/fieldset[12]/input')

    RADIOBUTTONS_MARITAL_STATUS = (By.CSS_SELECTOR, 'input[type=radio]')

    CHECKBOXES_HOBBY = (By.NAME, 'hobby')

    DROPDOWN_LIST_COUNTRY = (By.CSS_SELECTOR, 'fieldset:nth-child(4) > select')
    DROPDOWN_LIST_DATE_OF_BIRTH_MONTH = (By.CSS_SELECTOR, 'div:nth-child(2) > select')
    DROPDOWN_LIST_DATE_OF_BIRTH_DAY = (By.CSS_SELECTOR, 'div:nth-child(3) > select')
    DROPDOWN_LIST_DATE_OF_BIRTH_YEAR = (By.CSS_SELECTOR, 'div:nth-child(4) > select')

    FILE_FIELD_PROFILE_PICTURE = (By.CSS_SELECTOR, 'fieldset:nth-child(9) > input[type=file]')

    BUTTON_SUBMIT = (By.XPATH, '//*/fieldset[13]/input')


    REQUIRED_FIELDS = {
        "name": FIELD_FIRST_NAME,
        "hobby": CHECKBOXES_HOBBY,
        "phone": FIELD_PHONE_NUMBER,
        "username": FIELD_USERNAME,
        "email": FIELD_EMAIL,
        "password": FIELD_PASSWORD,
        "c_password": FIELD_CONFIRM_PASSWORD,
    }


    def __init__(self, driver: WebDriver):
        url = RegistrationPageURLS.REGISTRATION_PAGE_URL
        super().__init__(driver, url)


    def _get_hobbies(self) -> list[WebElement]:
        return self._find_elements(self.CHECKBOXES_HOBBY)

    def _get_request_body(self) -> dict[str, str] | None:
        for request in self.driver.requests:
            if request.method == 'POST' and request.url == RegistrationPageURLS.REQUEST_URL:
                body = request.body.decode("utf-8")
                body_dict = {k: unquote_plus(v) for k, v in [item.split("=") for item in body.split("&")]}
                return body_dict
        return None

    @staticmethod
    def _is_correct_request_body(request_body, required_fields_data) -> bool:
        for arg in request_body:
            if request_body[arg] != required_fields_data[arg]:
                return False
        return True


    @allure.step("Ввод имени в поле First Name")
    def enter_first_name(self, first_name: str) -> None:
        self._enter_text(self.FIELD_FIRST_NAME, first_name)
        self._add_screenshot_to_report()

    @allure.step("Ввод фамилии в поле Last Name")
    def enter_last_name(self, last_name: str) -> None:
        self._enter_text(self.FIELD_LAST_NAME, last_name)
        self._add_screenshot_to_report()

    @allure.step("Ввод номера телефона в поле Phone Number")
    def enter_phone_number(self, phone_number: str) -> None:
        self._enter_text(self.FIELD_PHONE_NUMBER, phone_number)
        self._add_screenshot_to_report()

    @allure.step("Ввод username в поле Username")
    def enter_username(self, username: str) -> None:
        self._enter_text(self.FIELD_USERNAME, username)
        self._add_screenshot_to_report()

    @allure.step("Ввод адреса электронной почты в поле E-mail")
    def enter_email(self, email: str) -> None:
        self._enter_text(self.FIELD_EMAIL, email)
        self._add_screenshot_to_report()

    @allure.step("Ввод невалидного адреса электронной почты в поле E-mail")
    def enter_invalid_email(self) -> None:
        self._enter_text(self.FIELD_EMAIL, generate_email().split("@")[0])
        self._add_screenshot_to_report()

    @allure.step("Ввод текста в поле About Yourself")
    def enter_about_yourself(self,) -> None:
        nums_permutations = get_permutations(RegistrationPageConfig.NUMS_FOR_PERMUTATIONS)
        size_longest_subsequence = get_size_longest_subsequence(RegistrationPageConfig.NUMS_FOR_SEQUENCE)
        longest_subsequences_in_texts = get_longest_subsequences_in_texts(*RegistrationPageConfig.TEXTS_FOR_SEQUENCE)

        about_yourself =  f"{nums_permutations}\n{size_longest_subsequence}\n{longest_subsequences_in_texts}"
        self._enter_text(self.FIELD_ABOUT_YOURSELF, about_yourself)
        self._add_screenshot_to_report()

    @allure.step("Ввод пароля в поле Password")
    def enter_password(self, password: str) -> None:
        self._enter_text(self.FIELD_PASSWORD, password)
        self._add_screenshot_to_report()

    @allure.step("Ввод пароля в поле Confirm Password")
    def enter_confirm_password(self, password: str) -> None:
        self._enter_text(self.FIELD_CONFIRM_PASSWORD, password)
        self._add_screenshot_to_report()

    @allure.step("Ввод пути к файлу в поле загрузки файла Your Profile Picture")
    def enter_profile_picture_path(self) -> None:
        self._enter_file_path(self.FILE_FIELD_PROFILE_PICTURE, RegistrationPageConfig.PROFILE_PICTURE_PATH)
        self._add_screenshot_to_report()

    @allure.step("Выбор случайного элемента радиобаттона Marital Status")
    def select_random_marital_status(self) -> None:
        marital_status_list = self._find_elements(self.RADIOBUTTONS_MARITAL_STATUS)
        marital_status = random.choice(marital_status_list)
        marital_status.click()
        self._add_screenshot_to_report()

    @allure.step("Выбор случайного элемента чекбокса Hobby")
    def select_random_hobby(self, *args) -> None:
        hobbies = self._get_hobbies()
        hobby = random.choice(hobbies)
        hobby.click()
        self._add_screenshot_to_report()

    @allure.step("Выбор всех элементов чекбокса Hobby")
    def select_all_hobbies(self, *args) -> None:
        hobbies = self._get_hobbies()
        for hobby in hobbies:
            if not hobby.is_selected():
                hobby.click()
        self._add_screenshot_to_report()

    @allure.step("Выбор случайного элемента из выпадающего списка Country")
    def select_random_country(self) -> None:
        self._select_random_in_dropdown(self.DROPDOWN_LIST_COUNTRY)
        self._add_screenshot_to_report()

    @allure.step("Выбор случайного месяца из выпадающего списка Date of Birth. Month")
    def select_random_date_of_birth_month(self) -> None:
        self._select_random_in_dropdown(self.DROPDOWN_LIST_DATE_OF_BIRTH_MONTH)
        self._add_screenshot_to_report()

    @allure.step("Выбор случайного дня из выпадающего списка Date of Birth. Day")
    def select_random_date_of_birth_day(self) -> None:
        self._select_random_in_dropdown(self.DROPDOWN_LIST_DATE_OF_BIRTH_DAY)
        self._add_screenshot_to_report()

    @allure.step("Выбор случайного года из выпадающего списка Date of Birth. Year")
    def select_random_date_of_birth_year(self) -> None:
        self._select_random_in_dropdown(self.DROPDOWN_LIST_DATE_OF_BIRTH_YEAR)
        self._add_screenshot_to_report()

    @allure.step("Нажатие кнопки SUBMIT")
    def click_submit(self) -> None:
        self._click_element(self.BUTTON_SUBMIT)
        self._find_element(self.FIELD_FIRST_NAME)
        self._add_screenshot_to_report()

    @allure.step("Заполнение обязательных полей")
    def fill_required_fields(self, required_fields_data: dict[str, str], missed_field_name: str|None = None) -> None:
        fill_required_fields = {
            "name": {
                "action": self.enter_first_name,
                "arg": required_fields_data["name"]
            },
            "hobby": {
                "action": self.select_random_hobby,
                "arg": required_fields_data["hobby"]
            },
            "phone": {
                "action": self.enter_phone_number,
                "arg": required_fields_data["phone"]
            },
            "username": {
                "action": self.enter_username,
                "arg": required_fields_data["username"]
            },
            "email": {
                "action": self.enter_email,
                "arg": required_fields_data["email"]
            },
            "password": {
                "action": self.enter_password,
                "arg": required_fields_data["password"]
            },
            "c_password": {
                "action": self.enter_confirm_password,
                "arg": required_fields_data["c_password"]
            }
        }

        for required_field_name, func in fill_required_fields.items():
            action, arg = func.values()
            if required_field_name == missed_field_name:
                with allure.step(f"Незаполнение поля {missed_field_name}"):
                    pass
            else:
                action(arg)

    @allure.step("Проверка незаполнения обязательного поля")
    def assert_required_field_not_filled(self, missed_field_name: str) -> None:
        request_body = self._get_request_body()

        err_message_1 = "Запрос был отправлен и обработан"
        assert request_body is None, err_message_1

        missed_field = self._find_element(self.REQUIRED_FIELDS[missed_field_name])

        current_class = missed_field.get_attribute("class")
        expected_class = RegistrationPageExpectedResults.ERROR_CLASS

        err_message_2 = f"Текущий класс веб-элемента {expected_class} не соответствует ожидаемому {current_class}"
        assert current_class == expected_class, err_message_2

    @allure.step("Проверка обработки запроса")
    def assert_request_processed_correctly(self, required_fields_data: dict[str, str]):
        request_body = self._get_request_body()

        err_message_1 = "Запрос не был отправлен"
        assert request_body is not None and isinstance(request_body, dict), err_message_1

        err_message_2 = "Данные из payload ответа на запрос не совпадают с отправленными данными"
        assert self._is_correct_request_body(request_body, required_fields_data), err_message_2
