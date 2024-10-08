from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestLogIn:
    def test_log_in_creds_success(self, driver_log_in, actions):
        driver, login_page_url = driver_log_in
        actions.valid_credentials_log_in(driver)
        assert WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(Locators.ORDER_BUTTON)
        )

    def test_log_in_via_profile_button(self, driver_main, actions):
        driver = driver_main
        profile_button = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(Locators.PROFILE_BUTTON_MAIN)
        )
        profile_button.click()
        actions.valid_credentials_log_in(driver)
        assert WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(Locators.ORDER_BUTTON)
        )

    def test_log_in_via_registration_page(self, driver_registration, actions):
        driver, registration_page_url = driver_registration
        login_button = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(Locators.REGISTRATION_LOGIN_BUTTON)
        )
        login_button.click()
        actions.valid_credentials_log_in(driver)
        assert WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(Locators.ORDER_BUTTON)
        )

    def test_log_in_via_forgot_password_button(self, driver_log_in, actions):
        driver, login_page_url = driver_log_in
        forgot_password_button = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(Locators.FORGOT_PASSWORD_BUTTON)
        )
        forgot_password_button.click()
        actions.valid_credentials_log_in(driver)
        assert WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(Locators.ORDER_BUTTON)
        )
