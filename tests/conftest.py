import allure
import pytest
from selenium import webdriver
from seleniumwire import webdriver as webdriver_wire

from src.pages.practice_automation.click_events_page import ClickEventsPage
from src.pages.practice_automation.form_fields_page import FormFieldsPage
from src.pages.practice_automation.popups_page import PopupsPage
from src.pages.way2automation.registration_page import RegistrationPage
from src.fixtures.registration_page_fixtures import fields_data


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def driver_wire():
    driver = webdriver_wire.Chrome()
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

@pytest.fixture(scope="function")
def registration_page(driver_wire):
    registration_page = RegistrationPage(driver_wire)
    registration_page.open()
    yield registration_page

@pytest.fixture(scope="function")
def registration_page_without_hobby(registration_page, fields_data):
    registration_page.fill_required_fields(fields_data, missed_field_name="hobby")
    yield registration_page

@pytest.fixture(scope="function")
def registration_page_without_email(registration_page, fields_data):
    registration_page.fill_required_fields(fields_data, missed_field_name="email")
    yield registration_page

@pytest.fixture(scope="function")
def registration_page_with_required_fields(registration_page, fields_data):
    registration_page.fill_required_fields(fields_data)
    yield registration_page
