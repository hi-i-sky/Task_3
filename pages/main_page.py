from pages.base_page import BasePage
import time
from constants.urls import BASE_URL, ORDERS_FEED_URL
from locators.main_page_locators import PERSONAL_ACCOUNT_BUTTON, ORDERS_FEED_BUTTON, CONSTRUCTOR_BUTTON, INGREDIENT_BUTTON, INGREDIENTS_DETAILS, CLOSE_INGREDIENTS_DETAILS_BUTTON, MAKE_ORDER_BUTTON, ORDER_AREA, ORDERS_FEED_HEADER, INGREDIENTS_COUNTER, ORDER_ID, CLOSE_CREATED_ORDER_WINDOW_BUTTON, CONSTRUCTOR_HEADER, INGREDIENTS_DETAILS_NAME, ORDER_IN_PROCESS_HEADER


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_base_page(self):
        self.open_page(BASE_URL)

    def get_base_page_with_orders_feed(self):
        self.open_page(ORDERS_FEED_URL)

    def wait_for_load_main_page(self):
        self.wait_for_element_clickable(PERSONAL_ACCOUNT_BUTTON)

    def click_personal_account_button(self):
        self.find_element(PERSONAL_ACCOUNT_BUTTON).click()

    # метод для клика по личному кабинету после логина: приходится 
    # ждать когда оверлей исчезнет и только потом кликаем
    def click_personal_account_button_after_login(self):
        time.sleep(1)
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
        self.wait_for_text_not_to_be(ORDER_ID, '9999')

    def close_created_order_window(self):
        self.find_element(CLOSE_CREATED_ORDER_WINDOW_BUTTON).click()

    def wait_for_created_order_window_close(self):
        self.wait_for_element_invisible(CLOSE_CREATED_ORDER_WINDOW_BUTTON)

    def get_created_order_id(self):
        return self.get_locators_text(ORDER_ID)

    def get_element_orders_feed_header(self):
        return self.find_element(ORDERS_FEED_HEADER)

    def get_element_constructor_header(self):
        return self.find_element(CONSTRUCTOR_HEADER)

    def get_element_ingredients_details_header(self):
        return self.find_element(INGREDIENTS_DETAILS)

    def get_element_ingredients_details_name(self):
        return self.find_element(INGREDIENTS_DETAILS_NAME)

    def get_element_order_id(self):
        return self.find_element(ORDER_ID)

    def get_element_order_in_process_header(self):
        return self.find_element(ORDER_IN_PROCESS_HEADER)

    def make_order(self):
        self.wait_for_load_main_page()
        self.drag_and_drop_ingredient()
        self.click_make_order_button()
        self.wait_for_load_order_id()