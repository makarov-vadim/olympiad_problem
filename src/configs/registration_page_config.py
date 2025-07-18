import os
import sys


class RegistrationPageConfig:
    PROJECT_ROOT = sys.path[1]
    PROFILE_PICTURE_PATH = os.path.join(PROJECT_ROOT, "src/attachments/profile_picture.png")

class RegistrationPageURLS:
    REGISTRATION_PAGE_URL = "https://way2automation.com/way2auto_jquery/registration.php#load_box"


class RegistrationPageExpectedResults:
    pass
