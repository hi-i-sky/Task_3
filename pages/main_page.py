from pages.base_page import BasePage
from constants.urls import BASE_URL
from locators.base_page_locators import PERSONAL_ACCOUNT_BUTTON

class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_base_page(self):
        self.open_page(BASE_URL)

    def click_personal_account_button(self):
        self.find_element(PERSONAL_ACCOUNT_BUTTON).click()