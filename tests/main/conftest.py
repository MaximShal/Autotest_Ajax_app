import pytest

from framework.main_page import MainPage


@pytest.fixture(scope='function')
def main_fixture(driver):
    yield MainPage(driver)

