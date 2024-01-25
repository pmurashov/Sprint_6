import pytest
from selenium import webdriver



@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def url():
    return "https://qa-scooter.praktikum-services.ru/"