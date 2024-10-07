from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from actions import Actions


class TestTabs:
    def test_sauces_tab_select(self, driver):
        self.actions = Actions()
        self.actions.valid_credentials_log_in(driver)

        sauces_tab = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(Locators.SAUCES_TAB)
        )
        sauces_tab.click()

        WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located(Locators.SAUCES_HEADER)
        )

    def test_fillings_tab_select(self, driver):
        self.actions = Actions()
        self.actions.valid_credentials_log_in(driver)

        # Ожидание таба начинки и клик на него
        fillings_tab = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(Locators.FILLINGS_TAB)
        )
        fillings_tab.click()

        # Проверка появления заголовка раздела начинки
        WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located(Locators.FILLINGS_HEADER)
        )

    def test_buns_tab_select(self, driver):
        self.actions = Actions()
        self.actions.valid_credentials_log_in(driver)

        sauces_tab = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(Locators.SAUCES_TAB)
        )
        sauces_tab.click()

        buns_tab = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable(Locators.BUNS_TAB)
        )
        buns_tab.click()

        WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located(Locators.BUNS_HEADER)
        )
