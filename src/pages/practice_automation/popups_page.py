import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from src.configs.popups_page_config import PopupsPageExpectedResults, PopupsPageURLS
from src.pages.base_page import BasePage


class PopupsPage(BasePage):
    # Локаторы страницы PopupsPage
    BUTTON_ALERT_POPUP = (By.ID, "alert")
    BUTTON_CONFIRM_POPUP = (By.ID, "confirm")
    BUTTON_PROMPT_POPUP = (By.ID, "prompt")

    TEXT_CONFIRM_RESULT = (By.ID, "confirmResult")
    TEXT_PROMPT_RESULT = (By.ID, "promptResult")


    def __init__(self, driver: WebDriver):
        url = PopupsPageURLS.POPUPS_PAGE_URL
        super().__init__(driver, url)

    @allure.step('Нажатие на кнопку "Alert Popup"')
    def click_alert_popup(self):
        self._click_element(self.BUTTON_ALERT_POPUP)

    @allure.step('Нажатие на кнопку "Confirm Popup"')
    def click_confirm_popup(self):
        self._click_element(self.BUTTON_CONFIRM_POPUP)

    @allure.step('Нажатие на кнопку "Prompt Popup"')
    def click_prompt_popup(self):
        self._click_element(self.BUTTON_PROMPT_POPUP)

    @allure.step('Нажатие "ОК" во всплывающем окне "Confirm Popup"')
    def accept_confirm_popup(self):
        confirm_popup = self._get_alert()
        confirm_popup.accept()
        self._add_screenshot_to_report()

    @allure.step('Нажатие "Отмена" во всплывающем окне "Confirm Popup"')
    def dismiss_confirm_popup(self):
        confirm_popup = self._get_alert()
        confirm_popup.dismiss()
        self._add_screenshot_to_report()

    @allure.step('Ввод текста в поле всплывающего окна "Prompt Popup" и нажатие "ОК"')
    def enter_text_to_prompt_popup(self, text: str = ""):
        prompt_popup = self._get_alert()
        prompt_popup.send_keys(text)
        prompt_popup.accept()
        self._add_screenshot_to_report()

    @allure.step('Нажатие "Отмена" во всплывающем окне "Prompt Popup"')
    def dismiss_prompt_popup(self):
        prompt_popup = self._get_alert()
        prompt_popup.dismiss()
        self._add_screenshot_to_report()

    @allure.step('Проверка текста внутри всплывающего окна "Alert Popup"')
    def assert_text_after_accept_alert_popup(self):
        alert = self._get_alert()
        alert_text = alert.text
        alert.accept()

        self._assert_text(
            element_name="alert",
            current_text=alert_text,
            expected_text=PopupsPageExpectedResults.ALERT_TEXT,
        )

    @allure.step('Проверка текста после нажатия "ОК" во всплывающем окне "Confirm Popup"')
    def assert_text_after_accept_confirm_popup(self):
        self._assert_text(
            element_name="confirm result",
            current_text=self._find_element(self.TEXT_CONFIRM_RESULT).text,
            expected_text=PopupsPageExpectedResults.TEXT_CONFIRM_RESULT_AFTER_ACCEPT
        )

    @allure.step('Проверка текста после нажатия "Отмена" во всплывающем окне "Confirm Popup"')
    def assert_text_after_dismiss_confirm_popup(self):
        self._assert_text(
            element_name="confirm result",
            current_text=self._find_element(self.TEXT_CONFIRM_RESULT).text,
            expected_text=PopupsPageExpectedResults.TEXT_CONFIRM_RESULT_AFTER_DISMISS
        )

    @allure.step('Проверка текста после работы с всплывающем окном "Prompt Popup"')
    def assert_text_prompt_result(self, text: str = ""):
        if text:
            self._assert_text(
                element_name="prompt result",
                current_text=self._find_element(self.TEXT_PROMPT_RESULT).text,
                expected_text=PopupsPageExpectedResults.TEXT_PROMPT_RESULT_AFTER_ENTER.format(text)
            )
        else:
            self._assert_text(
                element_name="prompt result",
                current_text=self._find_element(self.TEXT_PROMPT_RESULT).text,
                expected_text=PopupsPageExpectedResults.TEXT_PROMPT_RESULT_AFTER_DISMISS
            )
