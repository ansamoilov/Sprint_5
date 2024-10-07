from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from actions import Actions


class TestLogOut:
    def test_log_out_from_profile_page(self, driver):
        self.actions = Actions()
        self.actions.redirect_to_profile_page(driver)

        logout_button = WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable(Locators.LOGOUT_BUTTON)
        )
        logout_button.click()

        assert WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(Locators.LOGIN_BUTTON)
        )
