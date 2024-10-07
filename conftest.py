import pytest
from selenium import webdriver
from constants import MAIN_PAGE_URL, REGISTRATION_PAGE_URL


@pytest.fixture
def driver_main():
    driver = webdriver.Chrome()
    driver.get(MAIN_PAGE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def driver_registration():
    driver = webdriver.Chrome()
    driver.get(REGISTRATION_PAGE_URL)
    yield driver, REGISTRATION_PAGE_URL
    driver.quit()


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
