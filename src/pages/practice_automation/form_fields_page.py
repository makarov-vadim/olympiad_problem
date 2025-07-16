import random

import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from src.configs.form_fields_page_config import FormFieldsPageExpectedResults, FormFieldsPageURLS
from src.helpers.helper import generate_email, generate_full_name, generate_password
from src.pages.base_page import BasePage


class FormFieldsPage(BasePage):
    # Локаторы страницы FormFieldsPage
    FIELD_NAME = (By.ID, 'name-input')
    FIELD_PASSWORD = (By.CSS_SELECTOR, 'input[type=password]')
    FIELD_EMAIL = (By.ID, 'email')
    FIELD_MESSAGE = (By.ID, 'message')

    BUTTON_SUBMIT = (By.ID, 'submit-btn')

    CHECKBOXES_FAVORITE_DRINKS = (By.CSS_SELECTOR, '[type="checkbox"]')

    RADIOBUTTONS_FAVORITE_COLORS = (By.CSS_SELECTOR, '[type="radio"]')

    DROPDOWN_LIST_AUTOMATION = (By.XPATH, '//*[@id="automation"]')
    DROPDOWN_LIST_AUTOMATION_VALUES = (By.XPATH, '//*[@id="automation"]/option')

    LIST_AUTOMATION_TOOLS = (By.XPATH, '//*[@id="feedbackForm"]/ul/li')


    def __init__(self, driver: WebDriver):
        url = FormFieldsPageURLS.FORM_FIELDS_PAGE_URL
        super().__init__(driver, url)

    def _enter_name(self, name: str):
        self._enter_text(self.FIELD_NAME, name)

    def _get_favorite_drinks(self):
        return self._find_elements(self.CHECKBOXES_FAVORITE_DRINKS)

    def _get_automation_tools(self):
        return self._find_elements(self.LIST_AUTOMATION_TOOLS)

    def _assert_alert_is_present(self):
        assert self._is_alert_present(), "Всплывающее окно отсутствует"

    def _assert_alert_is_not_present(self):
        assert not self._is_alert_present(), "Всплывающее окно присутствует"


    @allure.step("Ввод пустого значения в поле Name")
    def enter_empty_name(self):
        self._enter_name("")
        self._add_screenshot_to_report()

    @allure.step("Ввод случайного имени в поле Name")
    def enter_name(self):
        self._enter_name(generate_full_name())
        self._add_screenshot_to_report()

    @allure.step("Ввод случайного пароля в поле Password")
    def enter_password(self):
        self._enter_text(self.FIELD_PASSWORD, generate_password())
        self._add_screenshot_to_report()

    @allure.step("Ввод случайной электронной почты в поле Email")
    def enter_email(self):
        self._enter_text(self.FIELD_EMAIL, generate_email())
        self._add_screenshot_to_report()

    @allure.step("Ввод элементов Automation tools в поле Message")
    def enter_message(self):
        automation_tools = self._get_automation_tools()
        automation_tools_texts = "\n".join([automation_tool.text for automation_tool in automation_tools])
        self._enter_text(self.FIELD_MESSAGE, automation_tools_texts)
        self._add_screenshot_to_report()

    @allure.step("Выбор случайного любимого напитка")
    def click_random_favorite_drink(self):
        favorite_drinks = self._get_favorite_drinks()
        favorite_drink = random.choice(favorite_drinks)
        favorite_drink.click()
        self._add_screenshot_to_report()

    @allure.step("Выбор всех любимых напитков")
    def click_all_favorite_drinks(self):
        favorite_drinks = self._get_favorite_drinks()
        for favorite_drink in favorite_drinks:
            if not favorite_drink.is_selected():
                favorite_drink.click()
        self._add_screenshot_to_report()

    def choice_favorite_drink(self, favorite_drink: str):
        _choices = {
            "any": self.click_random_favorite_drink,
            "all": self.click_all_favorite_drinks,
        }
        _choices[favorite_drink]()


    @allure.step("Выбор случайного любимого цвета")
    def click_random_favorite_color(self):
        favorite_colors = self._find_elements(self.RADIOBUTTONS_FAVORITE_COLORS)
        favorite_color = random.choice(favorite_colors)
        favorite_color.click()
        self._add_screenshot_to_report()

    @allure.step('Выбор случайного ответа на вопрос "Do you like automation?"')
    def click_random_automation(self):
        options = self._get_dropdown_options(self.DROPDOWN_LIST_AUTOMATION)
        option_index = random.randint(0, len(options) - 1)
        self._select_in_dropdown(self.DROPDOWN_LIST_AUTOMATION, index=option_index)
        self._add_screenshot_to_report()

    @allure.step("Нажатие кнопки SUBMIT")
    def click_submit(self):
        self._click_element(self.BUTTON_SUBMIT)

    @allure.step("Проверка того, что форма не была отправлена")
    def assert_form_not_submitted(self):
        self._assert_alert_is_not_present()
        self._assert_element_is_focused(self.FIELD_NAME)

    @allure.step("Проверка того, что форма была отправлена")
    def assert_form_submitted(self):
        self._assert_alert_is_present()
        alert = self._get_alert()
        alert_text = alert.text
        alert.accept()

        self._assert_text(
            element_name="alert",
            current_text=alert_text,
            expected_text=FormFieldsPageExpectedResults.ALERT_TEXT,
        )

