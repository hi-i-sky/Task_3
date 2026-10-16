from pages.base_page import BasePage
from constants.urls import LOGIN_URL
from locators.login_page_locators import EMAIL_FIELD, PASSWORD_FIELD, LOGIN_BUTTON, RESET_PASSWORD_BUTTON


class LoginPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)

    def get_login_page(self):
        self.open_page(LOGIN_URL)

    def wait_for_load_login_page(self):
        self.wait_for_element_clickable(RESET_PASSWORD_BUTTON)

    def click_reset_password_button(self):
        self.find_element(RESET_PASSWORD_BUTTON).click()

    def set_email(self, email: str):
        self.send_keys(EMAIL_FIELD, email)

    def set_password(self, password: str):
        self.send_keys(PASSWORD_FIELD, password)

    def click_login_button(self):
        self.find_element(LOGIN_BUTTON).click()

    # шаг логина
    def login(self, email: str, password: str):
        self.get_login_page()
        self.wait_for_load_login_page()
        self.set_email(email)
        self.set_password(password)
        self.click_login_button()