from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from actions import Actions
from constants import MAIN_PAGE_URL


class TestAccount:
    def test_profile_redirect_via_my_profile_button(self, driver):
        self.actions = Actions()
        self.actions.redirect_to_profile_page(driver)
        assert WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located(Locators.PROFILE_BUTTON_MY_PROFILE_PAGE)
        )

    def test_constructor_redirect_from_profile_page(self, driver):
        self.actions = Actions()
        self.actions.redirect_to_profile_page(driver)
        constructor_button = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON_MY_PROFILE_PAGE)
        )
        constructor_button.click()
        WebDriverWait(driver, 10).until(
            ec.url_to_be(MAIN_PAGE_URL)
        )
        assert WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located(Locators.MAKE_BURGER_HEADER)
        )

    def test_logo_redirect_from_profile_page(self, driver):
        self.actions = Actions()
        self.actions.redirect_to_profile_page(driver)
        logo = WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable(Locators.LOGO)
        )
        logo.click()
        assert WebDriverWait(driver, 10).until(
            ec.url_to_be(MAIN_PAGE_URL)
        )
