import allure
import pytest
from selenium import webdriver

from src.pages.practice_automation.click_events_page import ClickEventsPage
from src.pages.practice_automation.form_fields_page import FormFieldsPage
from src.pages.practice_automation.popups_page import PopupsPage


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def form_fields_page(driver):
    form_fields_page = FormFieldsPage(driver)
    form_fields_page.open()
    yield form_fields_page

@pytest.fixture(scope="function")
def form_fields_page_with_name(driver):
    form_fields_page = FormFieldsPage(driver)
    form_fields_page.open()
    with allure.step("Заполнение формы"):
        form_fields_page.enter_name()
    yield form_fields_page

@pytest.fixture(scope="function")
def click_events_page(driver):
    click_events_page = ClickEventsPage(driver)
    click_events_page.open()
    yield click_events_page

@pytest.fixture(scope="function")
def popups_page(driver):
    popups_page = PopupsPage(driver)
    popups_page.open()
    yield popups_page