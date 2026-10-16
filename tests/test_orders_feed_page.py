from locators.orders_feed_page_locators import ORDER_BUTTON, ORDER_DATE, ORDER_ID, ORDER_NAME, COMPOSITION_HEADER, COUNT_COMPLETED_ALL_TIME, COUNT_COMPLETED_TODAY


class TestOrdersFeedPage():


    def test_click_on_order_opens_window_with_details(self, orders_feed_page):

        orders_feed_page.get_orders_feed_page()
        orders_feed_page.click_on_order()

        order_id = orders_feed_page.find_element(ORDER_ID)
        order_name = orders_feed_page.find_element(ORDER_NAME)
        order_date = orders_feed_page.find_element(ORDER_DATE)
        composition_header = orders_feed_page.find_element(COMPOSITION_HEADER)

        assert composition_header.is_displayed()
        assert composition_header.text == 'Cостав'
        assert order_id.is_displayed()
        assert order_name.is_displayed()
        assert order_date.is_displayed()


    def test_orders_from_orders_history_are_displayed_on_orders_feed_page(self, created_order, main_page, account_page, orders_feed_page):

        orders_feed_page.get_orders_feed_page()
        orders_feed_page.wait_for_load_orders_feed_page()
        
        order_feed_id = orders_feed_page.get_last_order_from_orders_feed_id()

        main_page.click_personal_account_button()

        account_page.wait_for_load_account_page()
        account_page.click_orders_history_button()
        account_page.wait_for_load_orders_history_in_account()
        
        order_history_id = account_page.get_last_order_from_orders_history_id()

        assert order_feed_id == order_history_id


    def test_count_complited_all_time_increases_when_order_created(self, created_user, main_page, login_page, orders_feed_page):

        orders_feed_page.get_orders_feed_page()
        orders_feed_page.wait_for_load_orders_feed_page()

        count_completed_before = orders_feed_page.get_count_completed_all_time()

        main_page.click_personal_account_button()
            
        login_page.wait_for_load_login_page()
        login_page.set_email(created_user['email'])
        login_page.set_password(created_user['password'])
        login_page.click_login_button()
            
        main_page.wait_for_load_main_page()
        main_page.drag_and_drop_ingredient()
        main_page.click_make_order_button()
        main_page.wait_for_load_order_id()
        main_page.close_created_order_window()
        main_page.wait_for_created_order_window_close()

        orders_feed_page.get_orders_feed_page()
        orders_feed_page.wait_for_load_orders_feed_page()

        count_completed_after = orders_feed_page.get_count_completed_all_time()

        assert count_completed_after > count_completed_before


    def test_count_complited_today_increases_when_order_created(self, created_user, main_page, login_page, orders_feed_page):

        orders_feed_page.get_orders_feed_page()
        orders_feed_page.wait_for_load_orders_feed_page()

        count_completed_before = orders_feed_page.get_count_completed_today()

        main_page.click_personal_account_button()
            
        login_page.wait_for_load_login_page()
        login_page.set_email(created_user['email'])
        login_page.set_password(created_user['password'])
        login_page.click_login_button()
            
        main_page.wait_for_load_main_page()
        main_page.drag_and_drop_ingredient()
        main_page.click_make_order_button()
        main_page.wait_for_load_order_id()
        main_page.close_created_order_window()
        main_page.wait_for_created_order_window_close()

        orders_feed_page.get_orders_feed_page()
        orders_feed_page.wait_for_load_orders_feed_page()

        count_completed_after = orders_feed_page.get_count_completed_today()

        assert count_completed_after > count_completed_before


    def test_created_order_displayed_in_ready_section(self, created_order, main_page, orders_feed_page):

        created_order_id = main_page.get_created_order_id()

        main_page.close_created_order_window()

        orders_feed_page.get_orders_feed_page()
        orders_feed_page.wait_for_load_orders_feed_page()

        last_ready_order_id = orders_feed_page.get_last_order_is_redy_id()

        assert created_order_id == last_ready_order_id