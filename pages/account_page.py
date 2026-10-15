from pages.base_page import BasePage
from locators.account_page_locators import ORDERS_HISTORY, LOGOUT_BUTTON
from constants.urls import ORDERS_HISTORY_IN_ACCOUNT_URL


class AccountPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_load_account_page(self):
        self.wait_for_element_clickable(LOGOUT_BUTTON)

    def click_orders_history_button(self):
        self.find_element(ORDERS_HISTORY).click()

    def click_logout_button(self):
        self.find_element(LOGOUT_BUTTON).click()

    def wait_for_load_orders_history_in_account(self):
        self.wait_for_url_to_be(ORDERS_HISTORY_IN_ACCOUNT_URL)