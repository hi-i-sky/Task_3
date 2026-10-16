from pages.base_page import BasePage

from constants.urls import BASE_URL, ORDERS_FEED_URL
from locators.base_page_locators import PERSONAL_ACCOUNT_BUTTON
from locators.main_page_locators import ORDERS_FEED_BUTTON, CONSTRUCTOR_BUTTON, INGREDIENT_BUTTON, INGREDIENTS_DETAILS, CLOSE_INGREDIENTS_DETAILS_BUTTON, MAKE_ORDER_BUTTON, ORDER_AREA, ORDERS_FEED_HEADER, INGREDIENTS_COUNTER, ORDER_ID


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_base_page(self):
        self.open_page(BASE_URL)

    def get_base_page_with_orders_feed(self):
        self.open_page(ORDERS_FEED_URL)

    def wait_for_load_main_page(self):
        self.wait_for_url_to_be(BASE_URL)

    def click_personal_account_button(self):
        self.find_element(PERSONAL_ACCOUNT_BUTTON).click()

    def click_orders_feed_button(self):
        self.find_element(ORDERS_FEED_BUTTON).click()

    def wait_for_load_orders_feed(self):
        self.wait_for_element_visible(ORDERS_FEED_HEADER)

    def click_constructor_button(self):
        self.find_element(CONSTRUCTOR_BUTTON).click()

    def click_close_ingredients_details_button(self):
        self.find_element(CLOSE_INGREDIENTS_DETAILS_BUTTON).click()

    def click_make_order_button(self):
        self.find_element(MAKE_ORDER_BUTTON).click()

    def drag_and_drop_ingredient(self):
        self.drag_and_drop_js(INGREDIENT_BUTTON, ORDER_AREA)

    def click_on_ingredient(self):
        self.find_element(INGREDIENT_BUTTON).click()

    def wait_for_load_ingredients_details(self):
        self.wait_for_element_visible(INGREDIENTS_DETAILS)

    def wait_for_ingredient_details_close(self):
        self.wait_for_element_invisible(INGREDIENTS_DETAILS)

    def get_ingredients_count(self):
        return self.get_locators_text(INGREDIENTS_COUNTER)

    def wait_for_load_order_id(self):
        self.wait_for_element_visible(ORDER_ID)