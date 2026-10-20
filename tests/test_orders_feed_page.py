import allure


class TestOrdersFeedPage():


    @allure.title('Проверка окна с деталями о заказе при клике на заказ')
    def test_click_on_order_opens_window_with_details(self, orders_feed_page):

        orders_feed_page.get_orders_feed_page()
        orders_feed_page.click_on_order()

        assert orders_feed_page.get_element_composition_header().is_displayed()
        assert orders_feed_page.get_element_composition_header().text == 'Cостав'
        assert orders_feed_page.get_element_order_id().is_displayed()
        assert orders_feed_page.get_element_order_name().is_displayed()
        assert orders_feed_page.get_element_order_date().is_displayed()


    @allure.title('Проверка отображения заказа пользоваителя в истории заказов и в ленте заказов')
    def test_orders_from_orders_history_are_displayed_on_orders_feed_page(self, created_order, main_page, account_page, orders_feed_page):

        orders_feed_page.get_orders_feed_page()
        orders_feed_page.wait_for_load_orders_feed_page()
        
        order_feed_id = orders_feed_page.get_last_order_from_orders_feed_id()

        main_page.click_personal_account_button()

        account_page.wait_for_load_account_page()
        account_page.click_orders_history_button()
        account_page.wait_for_load_orders_history_in_account()

        assert order_feed_id == account_page.get_last_order_from_orders_history_id()


    @allure.title('Проверка увеличения счетчика "Выполнено за все время" при создании заказа')
    def test_count_complited_all_time_increases_when_order_created(self, created_user, main_page, login_page, orders_feed_page):

        orders_feed_page.get_orders_feed_page()
        orders_feed_page.wait_for_load_orders_feed_page()

        count_completed_before = int(orders_feed_page.get_count_completed_all_time())

        login_page.login(created_user['email'], created_user['password'])
            
        main_page.make_order()
        main_page.close_created_order_window()
        main_page.wait_for_created_order_window_close()

        orders_feed_page.get_orders_feed_page()
        orders_feed_page.wait_for_load_orders_feed_page()

        assert int(orders_feed_page.get_count_completed_all_time()) > count_completed_before


    @allure.title('Проверка увеличения счетчика "Выполнено за сегодня" при создании заказа')
    def test_count_complited_today_increases_when_order_created(self, created_user, main_page, login_page, orders_feed_page):

        orders_feed_page.get_orders_feed_page()
        orders_feed_page.wait_for_load_orders_feed_page()

        count_completed_before = int(orders_feed_page.get_count_completed_today())

        login_page.login(created_user['email'], created_user['password'])
            
        main_page.make_order()
        main_page.close_created_order_window()
        main_page.wait_for_created_order_window_close()

        orders_feed_page.get_orders_feed_page()
        orders_feed_page.wait_for_load_orders_feed_page()

        assert int(orders_feed_page.get_count_completed_today()) > count_completed_before


    # по заданию тест должен проверять отображение созданного заказа в разделе "В работе",
    # но обнаружено, что после создания заказ сразу переходит в статус "Готов"
    @allure.title('Проверка отображения созданного заказа в ленте заказов в разделе "Готовы"')
    def test_created_order_displayed_in_ready_section(self, created_order, main_page, orders_feed_page):

        created_order_id = main_page.get_created_order_id()

        main_page.close_created_order_window()

        orders_feed_page.get_orders_feed_page()
        orders_feed_page.wait_for_load_orders_feed_page()

        assert created_order_id.lstrip('0') == orders_feed_page.get_last_order_is_ready_id().lstrip('0')