from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestRegistration:
    def test_registration_valid_creds_success(self, driver_main, actions):
        driver = driver_main
        driver.find_element(*Locators.SIGN_IN_BUTTON).click()
        register_link = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(Locators.REGISTER_LINK)
        )
        register_link.click()
        name, email, password = actions.generate_random_credentials()
        driver.find_element(*Locators.NAME_INPUT).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        register_button = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(Locators.REGISTER_BUTTON_LOGIN_PAGE)
        )
        register_button.click()
        login_button = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located(Locators.LOGIN_BUTTON)
        )
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        login_button.click()
        assert WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located(Locators.ORDER_BUTTON)
        )

    def test_registration_short_password_error(self, driver_registration, actions):
        driver, registration_page_url = driver_registration
        name, email, password = actions.generate_short_password_credentials()
        driver.find_element(*Locators.NAME_INPUT).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        register_button = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(Locators.REGISTER_BUTTON)
        )
        register_button.click()
        error_message = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located(Locators.PASSWORD_ERROR)
        )
        assert error_message.is_displayed()

    def test_registration_empty_name_error(self, driver_registration, actions):
        driver, registration_page_url = driver_registration
        name, email, password = actions.generate_random_credentials()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        register_button = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(Locators.REGISTER_BUTTON)
        )
        register_button.click()
        assert driver.current_url == registration_page_url

    def test_registration_invalid_email_error(self, driver_registration, actions):
        driver, registration_page_url = driver_registration
        name, email, password = actions.generate_invalid_email_credentials()
        driver.find_element(*Locators.NAME_INPUT).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        register_button = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(Locators.REGISTER_BUTTON)
        )
        register_button.click()
        assert driver.current_url == registration_page_url
