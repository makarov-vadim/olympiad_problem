from itertools import permutations

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

def generate_first_name() -> str:
    """Функция, возвращающая случайное имя"""
    return Faker('ru_RU').first_name()

def generate_last_name() -> str:
    """Функция, возвращающая случайную фамилию"""
    return Faker('ru_RU').last_name()

def generate_phone_number() -> str:
    """Функция, возвращающая случайный номер телефона"""
    return Faker('ru_RU').phone_number()

def generate_username() -> str:
    """Функция, возвращающая случайный никнейм"""
    return Faker('ru_RU').user_name()


def get_permutations(nums: list[int]) -> str:
    """Функция, возвращающая строку, содержащую все возможные перестановки массива без повторяющихся элементов"""
    return ", ".join(f"{list(i)}" for i in permutations(nums, len(nums)))


def get_size_longest_subsequence(nums: list[int]) -> int:
    """Функция, возвращающая длину самой длинной строго возрастающей подпоследовательности в массиве"""
    len_subsequence = 1
    max_len_subsequence = 0

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            len_subsequence += 1
        else:
            max_len_subsequence = max([max_len_subsequence, len_subsequence])
            len_subsequence = 1

    return max_len_subsequence


def get_subsequences_in_texts(text_1: str, text_2: str) -> list[str]:
    """
    Функция, возвращающая список, содержащий все подпоследовательности из text_1,
    которые встречается в text_2 в одинаковом порядке, но не обязательно подряд
    """
    sequences = []
    for i in range(len(text_1)):
        subsequence = ""
        k = 0
        for j in range(i, len(text_1)):
            target_char = text_1[j]
            target_char_index = text_2.find(target_char, k)
            if target_char_index != -1:
                subsequence += target_char
                k = target_char_index + 1
        if subsequence not in sequences:
            sequences.append(subsequence)
    return sequences


def get_longest_subsequences_in_texts(text_1: str, text_2: str) -> str:
    """
    Функция, возвращающая строку, содержащую самые длинные подпоследовательности,
    которые встречается в двух строках в одинаковом порядке, но не обязательно подряд
    """
    sequences_1 = get_subsequences_in_texts(text_1, text_2)
    sequences_2 = get_subsequences_in_texts(text_2, text_1)
    all_sequences = sequences_1 + sequences_2

    max_len = len(max(all_sequences, key=len))
    longest_sequences = list(filter(lambda i: len(i) == max_len, all_sequences))

    return ", ".join(longest_sequences)
