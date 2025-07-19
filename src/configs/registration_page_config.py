import os
import sys


class RegistrationPageConfig:
    PROJECT_ROOT = sys.path[1]
    PROFILE_PICTURE_PATH = os.path.join(PROJECT_ROOT, "src/attachments/profile_picture.png")

    REQUIRED_FIELDS = ["name", "hobby", "phone", "username", "email", "password", "c_password"]

    NUMS_FOR_PERMUTATIONS = [2025, 3, 11]
    NUMS_FOR_SEQUENCE = [1, 3, 6, 7, 9, 4, 10, 5, 6, 12, 2, 7, 11]
    TEXTS_FOR_SEQUENCE = ("aabbdsaacc", "abadc")


class RegistrationPageURLS:
    REGISTRATION_PAGE_URL = "https://way2automation.com/way2auto_jquery/registration.php#load_box"
    REQUEST_URL = "https://way2automation.com/way2auto_jquery/registration.php"


class RegistrationPageExpectedResults:
    ERROR_CLASS ="error_p"
