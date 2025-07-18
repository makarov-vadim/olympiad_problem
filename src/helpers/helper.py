from faker import Faker

def generate_full_name() -> str:
    """Функция, возвращающая случайное полное имя"""
    return Faker('ru_RU').name()

def generate_password() -> str:
    """Функция, возвращающая случайный пароль"""
    return Faker('ru_RU').password(length=10)

def generate_email() -> str:
    """Функция, возвращающая случайную электронную почту"""
    return Faker('ru_RU').email()