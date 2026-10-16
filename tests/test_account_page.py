import allure
from constants.urls import LOGIN_URL, ORDERS_HISTORY_IN_ACCOUNT_URL


class TestAccountPage():

    @allure.title('Проверка выхода из аккаунта и перехода на страницу логина')
    def test_logout(self, main_page, login_page, account_page, created_user):
        
        login_page.login(created_user['email'], created_user['password'])
        
        main_page.wait_for_load_main_page()
        main_page.click_personal_account_button_after_login()
        
        account_page.wait_for_load_account_page()
        account_page.click_logout_button()

        login_page.wait_for_load_login_page()

        assert login_page.get_current_url() == LOGIN_URL


    @allure.title('Проверка раздела "История заказов" в личном кабинете')
    def test_get_orders_history_in_account(self, main_page, login_page, account_page, created_user):

        login_page.login(created_user['email'], created_user['password'])
        
        main_page.wait_for_load_main_page()
        main_page.click_personal_account_button_after_login()
        
        account_page.wait_for_load_account_page()
        account_page.click_orders_history_button()

        assert account_page.get_current_url() == ORDERS_HISTORY_IN_ACCOUNT_URL