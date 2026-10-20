from pages.base_page import BasePage
from locators.account_page_locators import ORDERS_HISTORY, LOGOUT_BUTTON, LAST_ORDER_FROM_ORDERS_HISTORY_ID


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
        self.wait_for_element_visible(LAST_ORDER_FROM_ORDERS_HISTORY_ID)

    def get_last_order_from_orders_history_id(self):
        return self.get_locators_text(LAST_ORDER_FROM_ORDERS_HISTORY_ID)