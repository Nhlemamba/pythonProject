import pytest
from selenium import webdriver


@pytest.fixture
def setup(browser):
    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser.lower() == "Edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Firefox()
        return driver


def pytest_options(parser):
    parser.options("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
