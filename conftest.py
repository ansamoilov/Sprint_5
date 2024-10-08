import pytest
from selenium import webdriver
from constants import MAIN_PAGE_URL, REGISTRATION_PAGE_URL, LOGIN_PAGE_URL
from actions import Actions


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def driver_main(driver):
    driver.get(MAIN_PAGE_URL)
    yield driver


@pytest.fixture
def driver_registration(driver):
    driver.get(REGISTRATION_PAGE_URL)
    yield driver, REGISTRATION_PAGE_URL


@pytest.fixture
def driver_log_in(driver):
    driver.get(LOGIN_PAGE_URL)
    yield driver, LOGIN_PAGE_URL


@pytest.fixture
def actions():
    return Actions()
