import allure
import pytest

# @pytest.mark.skip
@allure.epic("Тесты сайта practice-automation.com")
@allure.feature("Тест-сьют 2. Страница Сlick Events")
class TestClickEventsPage:
    @allure.story('Тест-кейс 2.1 Проверка нажатия на кнопку "Cat"')
    @allure.title('Проверка нажатия на кнопку "Cat"')
    @allure.id("2.1")
    def test_click_cat(self, click_events_page):
        with allure.step("Нажатие на кнопку"):
            click_events_page.click_cat()

        with allure.step("Проверка текста после нажатия на кнопку"):
            click_events_page.assert_cat_text_label()


    @allure.story('Тест-кейс 2.2 Проверка нажатия на кнопку "Dog"')
    @allure.title('Проверка нажатия на кнопку "Dog"')
    @allure.id("2.2")
    def test_click_dog(self, click_events_page):
        with allure.step("Нажатие на кнопку"):
            click_events_page.click_dog()

        with allure.step("Проверка текста после нажатия на кнопку"):
            click_events_page.assert_dog_text_label()


    @allure.story('Тест-кейс 2.3 Проверка нажатия на кнопку "Pig"')
    @allure.title('Проверка нажатия на кнопку "Pig"')
    @allure.id("2.3")
    def test_click_pig(self, click_events_page):
        with allure.step("Нажатие на кнопку"):
            click_events_page.click_pig()

        with allure.step("Проверка текста после нажатия на кнопку"):
            click_events_page.assert_pig_text_label()


    @allure.story('Тест-кейс 2.4 Проверка нажатия на кнопку "Cow"')
    @allure.title('Проверка нажатия на кнопку "Cow"')
    @allure.id("2.4")
    def test_click_cow(self, click_events_page):
        with allure.step("Нажатие на кнопку"):
            click_events_page.click_cow()

        with allure.step("Проверка текста после нажатия на кнопку"):
            click_events_page.assert_cow_text_label()
