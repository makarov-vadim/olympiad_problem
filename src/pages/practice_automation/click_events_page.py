import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from src.configs.click_events_page_config import ClickEventsPageExpectedResults, ClickEventsPageURLS
from src.pages.base_page import BasePage


class ClickEventsPage(BasePage):
    # Локаторы страницы ClickEventsPage
    BUTTON_CAT = (By.CSS_SELECTOR, 'div > div > div > div:nth-child(1) > button')
    BUTTON_DOG = (By.CSS_SELECTOR, 'div > div > div > div:nth-child(2) > button')
    BUTTON_PIG = (By.CSS_SELECTOR, 'div:nth-child(5) > div:nth-child(1) > button')
    BUTTON_COW = (By.CSS_SELECTOR, 'div:nth-child(5) > div:nth-child(2) > button')

    TEXT_LABEL = (By.ID, 'demo')


    def __init__(self, driver: WebDriver):
        url = ClickEventsPageURLS.CLICK_EVENTS_PAGE_URL
        super().__init__(driver, url)

    @allure.step("Нажатие на кнопку Cat")
    def click_cat(self):
        self._click_element(self.BUTTON_CAT)

    @allure.step("Нажатие на кнопку Dog")
    def click_dog(self):
        self._click_element(self.BUTTON_DOG)

    @allure.step("Нажатие на кнопку Pig")
    def click_pig(self):
        self._click_element(self.BUTTON_PIG)

    @allure.step("Нажатие на кнопку Cow")
    def click_cow(self):
        self._click_element(self.BUTTON_COW)

    @allure.step("Проверка текста после нажатия на кнопку Cat")
    def assert_cat_text_label(self):
        self._add_screenshot_to_report()
        self._assert_text(
            element_name = "cat button",
            current_text = self._find_element(self.TEXT_LABEL).text,
            expected_text = ClickEventsPageExpectedResults.CAT_TEXT
        )

    @allure.step("Проверка текста после нажатия на кнопку Dog")
    def assert_dog_text_label(self):
        self._add_screenshot_to_report()
        self._assert_text(
            element_name = "dog button",
            current_text = self._find_element(self.TEXT_LABEL).text,
            expected_text = ClickEventsPageExpectedResults.DOG_TEXT
        )

    @allure.step("Проверка текста после нажатия на кнопку Pig")
    def assert_pig_text_label(self):
        self._add_screenshot_to_report()
        self._assert_text(
            element_name = "pig button",
            current_text = self._find_element(self.TEXT_LABEL).text,
            expected_text = ClickEventsPageExpectedResults.PIG_TEXT
        )

    @allure.step("Проверка текста после нажатия на кнопку Cow")
    def assert_cow_text_label(self):
        self._add_screenshot_to_report()
        self._assert_text(
            element_name = "cow button",
            current_text = self._find_element(self.TEXT_LABEL).text,
            expected_text = ClickEventsPageExpectedResults.COW_TEXT
        )
