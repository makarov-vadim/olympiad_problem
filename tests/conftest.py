import pytest
from selenium import webdriver

from src.pages.practice_automation.form_fields_page import FormFieldsPage


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
