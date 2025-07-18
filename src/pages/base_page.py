from random import randint
from time import sleep

import allure
from selenium.common import NoAlertPresentException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Класс, описывающий базовую страницу"""

    def __init__(self, driver: WebDriver, url: str, timeout: int = 20):
        self.timeout = timeout
        self.driver = driver
        self.url = url


    def open(self) ->  None:
        """Метод, который открывает и разворачивает страницу"""
        self.driver.maximize_window()
        return self.driver.get(self.url)


    def _wait_until_visibility(self, element: WebElement) -> None:
        """
        Ожидает, пока указанный веб-элемент станет видимым на странице.

        Args:
            element (WebElement): веб-элемент, видимость которого необходимо дождаться
        Returns:
            None
        Raises:
            TimeoutException: если элемент не стал видимым в течение заданного времени
        """
        WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of(element)
        )


    def _scroll_to(self, element: WebElement) -> None:
        """
        Прокручивает страницу до указанного элемента и ожидает его видимости.

        Args:
            element (WebElement): веб-элемент, до которого необходимо прокрутить страницу
        Returns:
            None
        Raises:
            TimeoutException: если элемент не стал видимым в течение заданного времени
        """
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self._wait_until_visibility(element)


    def _find_element(self, locator: tuple[str, str]) -> WebElement:
        """
        Метод находит и возвращает веб-элемент на странице по указанному локатору.

        Args:
            locator (tuple[str, str]): Кортеж, содержащий тип локатора и значение.
                Первый элемент - тип локатора (например, 'xpath', 'css selector').
                Второй элемент - значение локатора.
        Returns:
            WebElement: Найденный веб-элемент.
        Raises:
            TimeoutException: Если веб-элемент не найден в течение заданного времени.
                Сообщение:
                "Can't find element by locator {locator}"
        """

        element = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )
        # self._scroll_to(element)
        return element


    def _find_elements(self, locator: tuple[str, str]) -> list[WebElement]:
        """
        Метод находит и возвращает список веб-элементов на странице по указанному локатору.

        Args:
            locator (tuple[str, str]): Кортеж, содержащий тип локатора и значение.
                Первый элемент - тип локатора (например, 'xpath', 'css selector').
                Второй элемент - значение локатора.
        Returns:
            list[WebElement]: Список найденных веб-элементов.
        Raises:
            TimeoutException: Если ни одного веб-элемента не найдено в течение заданного времени.
                Сообщение:
                "Can't find elements by locator {locator}"
        """

        elements = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}",
        )
        for element in elements:
            self._scroll_to(element)
        return elements


    def _click_element(self, locator: tuple[str, str]) -> WebElement:
        """
        Метод находит веб-элемент на странице и выполняет клик по нему.

        Args:
            locator (tuple[str, str]): Кортеж, содержащий тип локатора и значение.
                Первый элемент - тип локатора (например, 'xpath', 'css selector').
                Второй элемент - значение локатора.
        Returns:
            WebElement: Веб-элемент, по которому был выполнен клик.
        Raises:
            TimeoutException: Если веб-элемент не найден в течение заданного времени.
        """

        clickable_element = self._find_element(locator)
        self._scroll_to(clickable_element)
        clickable_element.click()
        return clickable_element


    def _enter_text(self, locator: tuple[str, str], text: str) -> WebElement:
        """
        Метод находит поле ввода, очищает его и вводит указанный текст,
        имитируя ручной ввод с небольшой задержкой между символами.

        Args:
            locator (tuple[str, str]): Кортеж, содержащий тип локатора и значение.
                Первый элемент - тип локатора (например, 'xpath', 'css selector').
                Второй элемент - значение локатора.
            text (str): Текст, который необходимо ввести в поле.
        Returns:
            WebElement: Веб-элемент поля, в которое был введен текст.
        Raises:
            TimeoutException: Если поле ввода не найдено в течение заданного времени.
        """

        search_field = self._click_element(locator)
        search_field.clear()
        for char in text:
            search_field.send_keys(char)
            sleep(randint(10, 30) / 1000)
        return search_field


    def _get_focused_element(self) -> WebElement:
        """
        Возвращает текущий активный (сфокусированный) элемент в веб-браузере.

        Returns:
            WebElement: объект WebElement, представляющий текущий активный элемент.
        """
        return self.driver.switch_to.active_element


    def _get_alert(self) -> Alert:
        """
        Возвращает всплывающее окно (alert/prompt/confirm).

        Returns:
            Alert: объект Alert, представляющий текущее модальное окно оповещения
        Raises:
            NoAlertPresentException: если в данный момент нет активного оповещения
            TimeoutException: если время ожидания появления оповещения истекло
        """
        return self.driver.switch_to.alert


    def _is_alert_present(self):
        """
        Проверяет наличие модального окна оповещения (alert/prompt/confirm) в текущем окне браузера.

        Returns:
            bool:
                True, если модальное окно оповещения присутствует
                False, если оповещения нет
        """
        try:
            self._get_alert()
            return True
        except NoAlertPresentException:
            return False


    def _get_dropdown_options(self, dropdown_locator: tuple[str, str]) -> list[WebElement]:
        """
        Получает список всех доступных опций из выпадающего списка.

        Args:
            dropdown_locator (tuple[str, str]): Кортеж, содержащий тип локатора и значение.
                Первый элемент - тип локатора (например, 'xpath', 'css selector').
                Второй элемент - значение локатора.
        Returns:
            list[WebElement]: список веб-элементов, представляющих опции выпадающего списка
        """
        return Select(self._find_element(dropdown_locator)).options


    def _select_in_dropdown(self, dropdown_locator: tuple[str, str], index: int = 0) -> None:
        """
        Выбирает опцию в выпадающем списке по указанному индексу.

        Args:
            dropdown_locator (tuple[str, str]): Кортеж, содержащий тип локатора и значение.
                Первый элемент - тип локатора (например, 'xpath', 'css selector').
                Второй элемент - значение локатора,
            index (int): индекс опции, которую необходимо выбрать (по умолчанию 0 - первая опция)
        Returns:
            None
        Raises:
            IndexError: если указанный индекс выходит за пределы доступных опций
            TimeoutException: если элемент не стал видимым в течение заданного времени
        """
        select = Select(self._find_element(dropdown_locator))
        self._scroll_to(self._find_element(dropdown_locator))
        select.select_by_index(index)


    def _add_screenshot_to_report(self):
        """
        Добавляет скриншот текущей страницы в отчет тестирования.

        Returns:
            None
        Raises:
            WebDriverException: если произошла ошибка при получении скриншота
        """
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name='screenshot',
            attachment_type=allure.attachment_type.PNG
        )


    @staticmethod
    def _assert_text(element_name: str, current_text: str, expected_text: str) -> None:
        """
        Метод сравнивает текст указанного элемента с ожидаемым значением.
        В случае несоответствия возбуждает исключение AssertionError.

        Args:
            element_name (str): Имя элемента, для которого проверяется текст.
            current_text (str): Текущий текст элемента, полученный на странице.
            expected_text (str): Ожидаемый текст, с которым необходимо сравнить текущий текст.
        Returns:
            None
        Raises:
            AssertionError: Если текущий текст элемента не совпадает с ожидаемым.
                Сообщение:
                Текущий текст элемента "{element_name}" ({current_text}) не соответствует ожидаемому ({expected_text})
        """

        assert current_text == expected_text, \
            f'Текущий текст элемента "{element_name}" ({current_text}) не соответствует ожидаемому ({expected_text})'


    def _assert_element_is_focused(self, locator: tuple[str, str]) -> None:
        """
        Проверяет, что указанный элемент присутствует на странице, виден и имеет фокус ввода.

        Args:
            locator (tuple[str, str]): Кортеж, содержащий тип локатора и значение.
                Первый элемент - тип локатора (например, 'xpath', 'css selector').
                Второй элемент - значение локатора.
        Returns:
            None
        Raises:
            AssertionError: если элемент не виден или не имеет фокус
        """
        element = self._find_element(locator)
        self._wait_until_visibility(element)
        assert element.is_displayed(), "Заданный элемент не виден"
        assert element == self._get_focused_element(), "Фокус не на заданном элементе"