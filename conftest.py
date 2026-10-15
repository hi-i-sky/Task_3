import pytest
from driver_factory import WebdriverFactory
from faker import Faker
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox"],
        help="Browser to use: chrome or firefox",
    )

    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode",
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    driver = WebdriverFactory.get_driver(
        browser=browser,
        headless=headless,
    )

    yield driver

    driver.quit()


@pytest.fixture
def random_user():

    fake = Faker()
    return {
        'email': fake.email(),
        'password': fake.password(),
        'name': fake.first_name()
    } 


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

    
@pytest.fixture
def forgot_password_page(driver):
    return ForgotPasswordPage(driver)


@pytest.fixture
def reset_password_page(driver):
    return ResetPasswordPage(driver)