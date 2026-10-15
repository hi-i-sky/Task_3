from pages.base_page import BasePage
from locators.base_page_locators import RESET_PASSWORD_CONFIRM_BUTTON, RESET_PASSWORD_EMAIL_FIELD


class ForgotPasswordPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_load_forgot_password_page(self):
        self.wait_for_element_clickable(RESET_PASSWORD_CONFIRM_BUTTON)

    def set_email_for_reset_password(self):
        self.send_keys(RESET_PASSWORD_EMAIL_FIELD, 'test@yandex.ru')

    def click_reset_password_confirm_button(self):
        self.find_element(RESET_PASSWORD_CONFIRM_BUTTON).click()