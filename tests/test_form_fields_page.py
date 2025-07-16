import allure
import pytest

# @pytest.mark.skip
@allure.epic("Тесты сайта practice-automation.com")
@allure.feature("Тест-сьют 1. Страница Form Fields")
class TestFormFieldsPage:
    @allure.story("Тест-кейс 1.1 Проверка ввода пустой строки в поле Name")
    @allure.title("Проверка ввода пустой строки в поле Name")
    @allure.id("1.1")
    def test_empty_name(self, form_fields_page):
        with allure.step("Заполнение формы"):
            form_fields_page.enter_empty_name()

        with allure.step("Отправление формы на обработку"):
            form_fields_page.click_submit()

        with allure.step("Проверка отправления формы"):
            form_fields_page.assert_form_not_submitted()


    @allure.story("Тест-кейс 1.2 Проверка ввода значений в поле Password")
    @allure.title("Проверка ввода значений в поле Password")
    @allure.id("1.2")
    def test_password(self, form_fields_page_with_name):
        with allure.step("Заполнение формы"):
            form_fields_page_with_name.enter_password()

        with allure.step("Отправление формы на обработку"):
            form_fields_page_with_name.click_submit()

        with allure.step("Проверка отправления формы"):
            form_fields_page_with_name.assert_form_submitted()


    @allure.story("Тест-кейс 1.3 Проверка выбора элементов из чек-бокса Favorite Drink")
    @allure.title("Проверка выбора элементов из чек-бокса Favorite Drink")
    @allure.id("1.3")
    @pytest.mark.parametrize("favorite_drink", ["any", "all"])
    def test_checkbox_favorite_drinks(self, form_fields_page_with_name, favorite_drink):
        with allure.step("Заполнение формы"):
            form_fields_page_with_name.choice_favorite_drink(favorite_drink)

        with allure.step("Отправление формы на обработку"):
            form_fields_page_with_name.click_submit()

        with allure.step("Проверка отправления формы"):
            form_fields_page_with_name.assert_form_submitted()


    @allure.story("Тест-кейс 1.4 Проверка выбора элементов из радиобаттона Favorite Color")
    @allure.title("Проверка выбора элементов из радиобаттона Favorite Color")
    @allure.id("1.4")
    def test_radiobutton_favorite_colors(self, form_fields_page_with_name):
        with allure.step("Заполнение формы"):
            form_fields_page_with_name.click_random_favorite_color()

        with allure.step("Отправление формы на обработку"):
            form_fields_page_with_name.click_submit()

        with allure.step("Проверка отправления формы"):
            form_fields_page_with_name.assert_form_submitted()


    @allure.story("Тест-кейс 1.5 Проверка выбора элементов из выпадающего списка Do you like automation")
    @allure.title("Проверка выбора элементов из выпадающего списка Do you like automation")
    @allure.id("1.5")
    def test_automation(self, form_fields_page_with_name):
        with allure.step("Заполнение формы"):
            form_fields_page_with_name.click_random_automation()

        with allure.step("Отправление формы на обработку"):
            form_fields_page_with_name.click_submit()

        with allure.step("Проверка отправления формы"):
            form_fields_page_with_name.assert_form_submitted()


    @allure.story("Тест-кейс 1.6 Проверка ввода значений в поле Email")
    @allure.title("Проверка ввода значений в поле Email")
    @allure.id("1.6")
    def test_email(self, form_fields_page_with_name):
        with allure.step("Заполнение формы"):
            form_fields_page_with_name.enter_email()

        with allure.step("Отправление формы на обработку"):
            form_fields_page_with_name.click_submit()

        with allure.step("Проверка отправления формы"):
            form_fields_page_with_name.assert_form_submitted()


    @allure.story("Тест-кейс 1.7 Проверка ввода значений в поле Message")
    @allure.title("Проверка ввода значений в поле Message")
    @allure.id("1.7")
    def test_message(self, form_fields_page_with_name):
        with allure.step("Заполнение формы"):
            form_fields_page_with_name.enter_message()

        with allure.step("Отправление формы на обработку"):
            form_fields_page_with_name.click_submit()

        with allure.step("Проверка отправления формы"):
            form_fields_page_with_name.assert_form_submitted()
