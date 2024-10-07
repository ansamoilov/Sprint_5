import random
import string

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from constants import MAIN_PAGE_URL


class Actions:

    def generate_random_credentials(self):
        name = "User " + ''.join(random.choices(string.ascii_lowercase, k=5)).capitalize()
        email = f"user_{random.randint(1000, 9999)}@ya.ru"
        password = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=6))
        return name, email, password

    def generate_short_password_credentials(self):
        name = "User " + ''.join(random.choices(string.ascii_lowercase, k=5)).capitalize()
        email = f"anton_{random.randint(1000, 9999)}@ya.ru"
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=5))  # 5 символов
        return name, email, password

    def generate_invalid_email_credentials(self):
        name = "User " + ''.join(random.choices(string.ascii_lowercase, k=5)).capitalize()
        email = f"user_{random.randint(1000, 9999)}.com"
        password = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=8))
        return name, email, password

    def valid_credentials_log_in(self, driver):
        driver = driver
        driver.get("https://stellarburgers.nomoreparties.site/login")
        email = "anton_samoilov_14_123@yandex.ru"
        password = "14123!"
        driver.find_element(*Locators.EMAIL_INPUT_LOGIN_PAGE).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT_LOGIN_PAGE).send_keys(password)
        login_button = WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(Locators.LOGIN_BUTTON))
        login_button.click()

    def redirect_to_profile_page(self, driver):
        self.valid_credentials_log_in(driver)
        WebDriverWait(driver, 10).until(
            ec.url_to_be(MAIN_PAGE_URL)
        )
        profile_button = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(Locators.PROFILE_BUTTON_MAIN)
        )
        profile_button.click()

