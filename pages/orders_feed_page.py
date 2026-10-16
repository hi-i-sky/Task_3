from pages.base_page import BasePage

from constants.urls import BASE_URL, ORDERS_FEED_URL
from locators.orders_feed_page_locators import ORDER_BUTTON, ORDER_DATE, ORDER_ID, ORDER_NAME, COMPOSITION_HEADER, COUNT_COMPLETED_ALL_TIME, COUNT_COMPLETED_TODAY, LAST_ORDER_FROM_ORDERS_FEED_ID, LAST_ORDER_IS_READY_ID


class OrdersFeedPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_orders_feed_page(self):
        self.open_page(ORDERS_FEED_URL)

    def click_on_order(self):
        self.find_element(ORDER_BUTTON).click()

    def get_last_order_from_orders_feed_id(self):
        self.find_element(LAST_ORDER_FROM_ORDERS_FEED_ID).text

    def wait_for_load_orders_feed_page(self):
        self.wait_for_element_visible(LAST_ORDER_FROM_ORDERS_FEED_ID)

    def get_count_completed_all_time(self):
        return self.find_element(COUNT_COMPLETED_ALL_TIME).text

    def get_count_completed_today(self):
        return self.find_element(COUNT_COMPLETED_TODAY).text

    def get_last_order_is_redy_id(self):
        return self.find_element(LAST_ORDER_IS_READY_ID).text