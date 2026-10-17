from pages.base_page import BasePage
from selenium.webdriver.support.color import Color
from locators.reset_password_page_locators import SHOW_PASSWORD_BUTTON, RESET_PASSWORD_FIELD, RESET_PASSWORD_FIELD_BORDER


class ResetPasswordPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)

    def set_new_password(self):
        self.send_keys(RESET_PASSWORD_FIELD, '123654789rR!')

    def click_show_password_button(self):
        self.find_element(SHOW_PASSWORD_BUTTON).click()

    def wait_for_load_reset_password_page(self):
        self.wait_for_element_clickable(SHOW_PASSWORD_BUTTON)

    def get_border_color_of_password_field(self):
        element = self.find_element(RESET_PASSWORD_FIELD_BORDER)
        return Color.from_string(element.value_of_css_property("border-bottom-color")).rgb

    def wait_for_border_color_password_field(self):
        self.wait_for_css_property_border_color(RESET_PASSWORD_FIELD_BORDER, "rgb(76, 76, 255)")