import allure
import pytest

from src.helpers.helper import generate_full_name


@allure.epic("Тесты сайта practice-automation.com")
@allure.feature("Тест-сьют 3. Страница Popups")
class TestClickEventsPage:
    @allure.story('Тест-кейс 3.1 Проверка нажатия на кнопку "Alert Popup"')
    @allure.title('Проверка нажатия на кнопку "Alert Popup"')
    @allure.id("3.1")
    def test_click_alert_popup(self, popups_page):
        with allure.step("Работа с всплывающем окном"):
            popups_page.click_alert_popup()

        with allure.step("Проверка работы с всплывающем окном"):
            popups_page.assert_text_after_accept_alert_popup()


    @allure.story('Тест-кейс 3.2 Проверка подтверждения всплывающего окна после нажатия на кнопку "Confirm Popup"')
    @allure.title('Проверка подтверждения всплывающего окна после нажатия на кнопку "Confirm Popup"')
    @allure.id("3.2")
    def test_accept_confirm_popup(self, popups_page):
        with allure.step("Работа с всплывающем окном"):
            popups_page.click_confirm_popup()
            popups_page.accept_confirm_popup()

        with allure.step("Проверка работы с всплывающем окном"):
            popups_page.assert_text_after_accept_confirm_popup()


    @allure.story('Тест-кейс 3.3 Проверка отмены всплывающего окна после нажатия на кнопку "Confirm Popup"')
    @allure.title('Проверка отмены всплывающего окна после нажатия на кнопку "Confirm Popup"')
    @allure.id("3.3")
    def test_dismiss_confirm_popup(self, popups_page):
        with allure.step("Работа с всплывающем окном"):
            popups_page.click_confirm_popup()
            popups_page.dismiss_confirm_popup()

        with allure.step("Проверка работы с всплывающем окном"):
            popups_page.assert_text_after_dismiss_confirm_popup()


    @allure.story('Тест-кейс 3.4 Проверка ввода значений во всплывающем окне после нажатия на кнопку "Prompt Popup"')
    @allure.title('Проверка ввода значений во всплывающем окне после нажатия на кнопку "Prompt Popup"')
    @allure.id("3.4")
    @pytest.mark.parametrize("text", ["", generate_full_name()])
    def test_enter_to_prompt_popup(self, popups_page, text):
        with allure.step("Работа с всплывающем окном"):
            popups_page.click_prompt_popup()
            popups_page.enter_text_to_prompt_popup(text)

        with allure.step("Проверка работы с всплывающем окном"):
            popups_page.assert_text_prompt_result(text)


    @allure.story('Тест-кейс 3.5 Проверка отмены всплывающего окна после нажатия на кнопку "Prompt Popup"')
    @allure.title('Проверка отмены всплывающего окна после нажатия на кнопку "Prompt Popup"')
    @allure.id("3.5")
    def test_dismiss_prompt_popup(self, popups_page):
        with allure.step("Работа с всплывающем окном"):
            popups_page.click_prompt_popup()
            popups_page.dismiss_prompt_popup()

        with allure.step("Проверка работы с всплывающем окном"):
            popups_page.assert_text_prompt_result()
