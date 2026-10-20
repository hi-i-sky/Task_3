import allure


class TestMainPage():


    @allure.title('Проверка кнопки "Лента заказов"')
    def test_orders_feed_button(self, main_page):

        main_page.get_base_page()
        main_page.click_orders_feed_button()
        main_page.wait_for_load_orders_feed()
        
        assert main_page.get_element_orders_feed_header().is_displayed()
        assert main_page.get_element_orders_feed_header().text == 'Лента заказов'


    @allure.title('Проверка кнопки "Конструктор"')
    def test_constructor_button(self, main_page):

        main_page.get_base_page_with_orders_feed()
        main_page.click_constructor_button()
        main_page.wait_for_load_main_page()

        assert main_page.get_element_constructor_header().is_displayed()
        assert main_page.get_element_constructor_header().text == 'Соберите бургер'


    @allure.title('Проверка окна с деталями об ингредиенте при клике на ингредиент')
    def test_click_on_ingredient_opens_window_with_details(self, main_page):

        main_page.get_base_page()
        main_page.click_on_ingredient()
        main_page.wait_for_load_ingredients_details()

        assert main_page.get_element_ingredients_details_header().is_displayed()
        assert main_page.get_element_ingredients_details_header().text == 'Детали ингредиента'
        assert main_page.get_element_ingredients_details_name().is_displayed()
        assert main_page.get_element_ingredients_details_name().text == 'Краторная булка N-200i'


    @allure.title('Проверка закрытия окна с деталями об ингредиенте по крестику')
    def test_click_on_close_ingredients_details_button(self, main_page):

        main_page.get_base_page()
        main_page.click_on_ingredient()
        main_page.wait_for_load_ingredients_details()
        main_page.click_close_ingredients_details_button()

        assert main_page.wait_for_ingredient_details_close()


    @allure.title('Проверка увеличения счетчика ингредиента при переносе ингредиента в заказ')
    def test_ingredients_counter_increases_when_ingredient_added(self, main_page):

        main_page.get_base_page()
        main_page.drag_and_drop_ingredient()

        assert main_page.get_ingredients_count() == '2'


    @allure.title('Проверка создания заказа зарегистрированным пользователем')
    def test_user_make_order(self, main_page, login_page, created_user):

        login_page.login(created_user['email'], created_user['password'])
        
        main_page.make_order()

        assert main_page.get_element_order_id().is_displayed()
        assert main_page.get_element_order_in_process_header().text == 'Ваш заказ начали готовить'