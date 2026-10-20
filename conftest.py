import pytest
import requests
from driver_factory import WebdriverFactory
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from pages.account_page import AccountPage
from pages.orders_feed_page import OrdersFeedPage
from constants.urls import CREATE_USER_URL
from helpers import delete_user_by_token, generate_user_payload


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
def created_user():
    payload = generate_user_payload()
    r = requests.post(CREATE_USER_URL, json=payload)
    r.raise_for_status()

    data = r.json()

    user_access_token = data['accessToken']
    user_email = data['user']['email']
    user_name = data['user']['name']
    user_password = payload['password']

    yield {
        'token': user_access_token, 
        'email': user_email, 
        'name': user_name,
        'password': user_password
    }

    delete_user_by_token(user_access_token)


@pytest.fixture
def created_order(main_page, login_page, created_user):
        
    login_page.login(created_user['email'], created_user['password'])
        
    main_page.wait_for_load_main_page()
    main_page.drag_and_drop_ingredient()
    main_page.click_make_order_button()
    main_page.wait_for_load_order_id()

    return main_page


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


@pytest.fixture
def account_page(driver):
    return AccountPage(driver)


@pytest.fixture
def orders_feed_page(driver):
    return OrdersFeedPage(driver)