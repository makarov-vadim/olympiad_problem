import pytest

from src.helpers.helper import generate_email, generate_first_name, generate_password, generate_phone_number, \
    generate_username



@pytest.fixture(scope="function")
def fields_data():
    password = f"{generate_password()}&"
    required_fields_data = {
        "name": generate_first_name(),
        "m_status":"on",
        "hobby": "on",
        "phone": generate_phone_number(),
        "username": generate_username(),
        "email": generate_email(),
        "password": password,
        "c_password": password,
    }
    return required_fields_data
