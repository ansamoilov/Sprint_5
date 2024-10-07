from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from actions import Actions
from constants import MAIN_PAGE_URL, REGISTRATION_PAGE_URL, LOGIN_PAGE_URL


class TestLogIn:
    def test_log_in_creds_success(self, driver):
        self.actions = Actions()
        self.actions.valid_credentials_log_in(driver)
        assert WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(Locators.ORDER_BUTTON)
        )

    def test_log_in_via_profile_button(self, driver):
        driver.get(MAIN_PAGE_URL)
        self.actions = Actions()
        profile_button = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(Locators.PROFILE_BUTTON_MAIN)
        )
        profile_button.click()
        self.actions.valid_credentials_log_in(driver)
        assert WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(Locators.ORDER_BUTTON)
        )

    def test_log_in_via_registration_page(self, driver):
        driver.get(REGISTRATION_PAGE_URL)
        self.actions = Actions()
        login_button = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(Locators.REGISTRATION_LOGIN_BUTTON)
        )
        login_button.click()
        self.actions.valid_credentials_log_in(driver)
        assert WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(Locators.ORDER_BUTTON)
        )

    def test_log_in_via_forgot_password_button(self, driver):
        self.actions = Actions()
        driver.get(LOGIN_PAGE_URL)
        forgot_password_button = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(Locators.FORGOT_PASSWORD_BUTTON)
        )
        forgot_password_button.click()
        self.actions.valid_credentials_log_in(driver)
        assert WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(Locators.ORDER_BUTTON)
        )
