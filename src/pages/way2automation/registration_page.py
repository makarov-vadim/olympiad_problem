import os
import random

import allure
from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.configs.registration_page_config import RegistrationPageConfig, RegistrationPageURLS
from src.pages.base_page import BasePage


class RegistrationPage(BasePage):

    # Локаторы страницы RegistrationPage
    FIELD_FIRST_NAME = (By.CSS_SELECTOR, 'p:nth-child(1) > input[type=text]')                               #
    FIELD_LAST_NAME = (By.CSS_SELECTOR, 'p:nth-child(2) > input[type=text]')                                #
    FIELD_PHONE_NUMBER = (By.CSS_SELECTOR, 'fieldset:nth-child(6) > input[type=text]')                      #
    FIELD_USERNAME = (By.CSS_SELECTOR, 'fieldset:nth-child(7) > input[type=text]')                          #
    FIELD_EMAIL = (By.CSS_SELECTOR, 'fieldset:nth-child(8) > input[type=text]')                             #
    FIELD_ABOUT_YOURSELF = (By.CSS_SELECTOR, 'fieldset:nth-child(10) > textarea')                           #
    FIELD_PASSWORD = (By.XPATH, '//*/fieldset[11]/input')                                                   #
    FIELD_CONFIRM_PASSWORD = (By.XPATH, '//*/fieldset[12]/input')                                           #

    RADIOBUTTONS_MARITAL_STATUS = (By.CSS_SELECTOR, 'input[type=radio]')                                    #

    CHECKBOXES_HOBBY = (By.NAME, 'hobby')                                              #

    DROPDOWN_LIST_COUNTRY = (By.CSS_SELECTOR, 'fieldset:nth-child(4) > select')                             #
    DROPDOWN_LIST_DATE_OF_BIRTH_MONTH = (By.CSS_SELECTOR, 'div:nth-child(2) > select')                      #
    DROPDOWN_LIST_DATE_OF_BIRTH_DAY = (By.CSS_SELECTOR, 'div:nth-child(3) > select')                        #
    DROPDOWN_LIST_DATE_OF_BIRTH_YEAR = (By.CSS_SELECTOR, 'div:nth-child(4) > select')                       #

    FILE_FIELD_PROFILE_PICTURE = (By.CSS_SELECTOR, 'fieldset:nth-child(9) > input[type=file]')              #

    BUTTON_SUBMIT = (By.XPATH, '//*/fieldset[13]/input')                                                    #

    def __init__(self, driver: WebDriver):
        url = RegistrationPageURLS.REGISTRATION_PAGE_URL
        super().__init__(driver, url)


    def _get_hobbies(self) -> list[WebElement]:
        return self._find_elements(self.CHECKBOXES_HOBBY)

    def enter_first_name(self, first_name: str):
        self._enter_text(self.FIELD_FIRST_NAME, first_name)

    def enter_last_name(self, last_name: str):
        self._enter_text(self.FIELD_LAST_NAME, last_name)

    def enter_phone_number(self, number: str):
        self._enter_text(self.FIELD_PHONE_NUMBER, number)

    def enter_username(self, username: str):
        self._enter_text(self.FIELD_USERNAME, username)

    def enter_email(self, email: str):
        self._enter_text(self.FIELD_EMAIL, email)

    def enter_about_yourself(self, about_yourself: str):
        self._enter_text(self.FIELD_ABOUT_YOURSELF, about_yourself)

    def enter_password(self, password: str):
        self._enter_text(self.FIELD_PASSWORD, password)

    def enter_confirm_password(self, password: str):
        self._enter_text(self.FIELD_CONFIRM_PASSWORD, password)

    def enter_profile_picture_path(self):
        self._enter_file_path(self.FILE_FIELD_PROFILE_PICTURE, RegistrationPageConfig.PROFILE_PICTURE_PATH)

    def click_random_marital_status(self):
        marital_status_list = self._find_elements(self.RADIOBUTTONS_MARITAL_STATUS)
        marital_status = random.choice(marital_status_list)
        marital_status.click()

    def click_random_hobby(self):
        hobbies = self._get_hobbies()
        hobby = random.choice(hobbies)
        hobby.click()

    def click_all_hobbies(self):
        hobbies = self._get_hobbies()
        for hobby in hobbies:
            if not hobby.is_selected():
                hobby.click()

    def click_random_country(self):
        self._select_random_in_dropdown(self.DROPDOWN_LIST_COUNTRY)

    def click_random_date_of_birth_month(self):
        self._select_random_in_dropdown(self.DROPDOWN_LIST_DATE_OF_BIRTH_MONTH)

    def click_random_date_of_birth_day(self):
        self._select_random_in_dropdown(self.DROPDOWN_LIST_DATE_OF_BIRTH_DAY)

    def click_random_date_of_birth_year(self):
        self._select_random_in_dropdown(self.DROPDOWN_LIST_DATE_OF_BIRTH_YEAR)

    def click_submit(self):
        self._click_element(self.BUTTON_SUBMIT)
