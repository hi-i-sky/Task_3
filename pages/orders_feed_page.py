from pages.base_page import BasePage
from constants.urls import ORDERS_FEED_URL
from locators.orders_feed_page_locators import ORDER_BUTTON, COUNT_COMPLETED_ALL_TIME, COUNT_COMPLETED_TODAY, LAST_ORDER_FROM_ORDERS_FEED_ID, LAST_ORDER_IS_READY_ID, ORDER_ID, ORDER_DATE, ORDER_NAME, COMPOSITION_HEADER


class OrdersFeedPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_orders_feed_page(self):
        self.open_page(ORDERS_FEED_URL)

    def click_on_order(self):
        self.find_element(ORDER_BUTTON).click()

    def get_last_order_from_orders_feed_id(self):
        return self.get_locators_text(LAST_ORDER_FROM_ORDERS_FEED_ID)

    def wait_for_load_orders_feed_page(self):
        return self.wait_for_element_visible(LAST_ORDER_FROM_ORDERS_FEED_ID)

    def get_count_completed_all_time(self):
        return self.get_locators_text(COUNT_COMPLETED_ALL_TIME)

    def get_count_completed_today(self):
        return self.get_locators_text(COUNT_COMPLETED_TODAY)

    def get_last_order_is_ready_id(self):
        return self.get_locators_text(LAST_ORDER_IS_READY_ID)

    def get_element_order_id(self):
        return self.find_element(ORDER_ID)

    def get_element_order_name(self):
        return self.find_element(ORDER_NAME)

    def get_element_order_date(self):
        return self.find_element(ORDER_DATE)

    def get_element_composition_header(self):
        return self.find_element(COMPOSITION_HEADER)