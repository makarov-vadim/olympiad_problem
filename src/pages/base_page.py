import time
from random import randint
from time import sleep


from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
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


    def _scroll_to(self, element: WebElement) -> None:
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of(element)
        )

    def _get_dropdown_options(self, dropdown_locator: tuple[str, str]) -> list[WebElement]:
        return Select(self._find_element(dropdown_locator)).options


    def _select_in_dropdown(self, dropdown_locator: tuple[str, str], index: int = 0) -> None:
        select = Select(self._find_element(dropdown_locator))
        select.select_by_index(index)


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
        self._scroll_to(element)
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


    def _assert_url(self, expected_url: str, timeout: float | None = None) -> None:
        """
        Метод использует явное ожидание загрузки страницы с ожидаемым URL.

        Args:
            expected_url (str): Ожидаемый URL, загрузку которого необходимо дождаться.
            timeout (float | None): Время ожидания загрузки страницы. Если не задано, определяется как self.timeout
        Returns:
            None
        Raises:
            TimeoutException: Если страница с ожидаемым URL не загружается дольше заданного времени.
                Сообщение:
                Текущий URL ({self.driver.current_url}) не соответствует ожидаемому ({expected_url})
        """

        if timeout is None:
            timeout = self.timeout
        message = f"Текущий URL ({self.driver.current_url}) не соответствует ожидаемому ({expected_url})"
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(expected_url), message=message)


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
