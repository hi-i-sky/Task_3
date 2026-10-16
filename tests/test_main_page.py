import allure
from locators.main_page_locators import ORDERS_FEED_HEADER, CONSTRUCTOR_HEADER, INGREDIENTS_DETAILS, INGREDIENTS_DETAILS_NAME, ORDER_ID, ORDER_IN_PROCESS_HEADER


class TestMainPage():


    def test_orders_feed_button(self, main_page):

        main_page.get_base_page()
        main_page.click_orders_feed_button()
        main_page.wait_for_load_orders_feed()

        orders_feed_header = main_page.find_element(ORDERS_FEED_HEADER)
        
        assert orders_feed_header.is_displayed()
        assert orders_feed_header.text == 'Лента заказов'


    def test_constructor_button(self, main_page):

        main_page.get_base_page_with_orders_feed()
        main_page.click_constructor_button()
        main_page.wait_for_load_main_page()

        constructor_header = main_page.find_element(CONSTRUCTOR_HEADER)

        assert constructor_header.is_displayed()
        assert constructor_header.text == 'Соберите бургер'


    def test_click_on_ingredient_opens_window_with_details(self, main_page):

        main_page.get_base_page()
        main_page.click_on_ingredient()
        main_page.wait_for_load_ingredients_details()

        ingredients_details_header = main_page.find_element(INGREDIENTS_DETAILS)
        ingredient = main_page.find_element(INGREDIENTS_DETAILS_NAME)

        assert ingredients_details_header.is_displayed()
        assert ingredients_details_header.text == 'Детали ингредиента'
        assert ingredient.is_displayed()
        assert ingredient.text == 'Краторная булка N-200i'


    def test_click_on_close_ingredients_details_button(self, main_page):

        main_page.get_base_page()
        main_page.click_on_ingredient()
        main_page.wait_for_load_ingredients_details()
        main_page.click_close_ingredients_details_button()
        main_page.wait_for_ingredient_details_close()

        ingredients_details_header = main_page.find_element(INGREDIENTS_DETAILS)

        assert not ingredients_details_header.is_displayed()


    def test_ingredients_counter_increases_when_ingredient_added(self, main_page):

        main_page.get_base_page()
        assert main_page.get_ingredients_count() == '0'

        main_page.drag_and_drop_ingredient()
        assert main_page.get_ingredients_count() == '2'


    def test_user_make_order(self, main_page, login_page, created_user):

        main_page.get_base_page()
        main_page.click_personal_account_button()
        
        login_page.wait_for_load_login_page()
        login_page.set_email(created_user['email'])
        login_page.set_password(created_user['password'])
        login_page.click_login_button()
        
        main_page.wait_for_load_main_page()
        main_page.drag_and_drop_ingredient()
        main_page.click_make_order_button()
        main_page.wait_for_load_order_id()

        order_id = main_page.find_element(ORDER_ID)
        order_in_process_header = main_page.find_element(ORDER_IN_PROCESS_HEADER)

        assert order_id.is_displayed()
        assert order_in_process_header.text == 'Ваш заказ начали готовить'