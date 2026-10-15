import allure
from constants.urls import ACCOUNT_URL, LOGIN_URL, ORDERS_HISTORY_IN_ACCOUNT_URL


class TestAccountPage():


    def test_login_and_get_account_page(self, main_page, login_page, account_page, created_user):

        main_page.get_base_page()
        main_page.click_personal_account_button()

        login_page.wait_for_load_login_page()
        login_page.set_email(created_user['email'])
        login_page.set_password(created_user['password'])
        login_page.click_login_button()

        main_page.wait_for_load_main_page()
        main_page.click_personal_account_button()

        account_page.wait_for_load_account_page()
        
        assert account_page.get_current_url() == ACCOUNT_URL


    def test_logout(self, main_page, login_page, account_page, created_user):

        main_page.get_base_page()
        main_page.click_personal_account_button()
        
        login_page.wait_for_load_login_page()
        login_page.set_email(created_user['email'])
        login_page.set_password(created_user['password'])
        login_page.click_login_button()
        
        main_page.wait_for_load_main_page()
        main_page.click_personal_account_button()
        
        account_page.wait_for_load_account_page()
        account_page.click_logout_button()

        login_page.wait_for_load_login_page()

        assert login_page.get_current_url() == LOGIN_URL


    def test_get_orders_history_in_account(self, main_page, login_page, account_page, created_user):

        main_page.get_base_page()
        main_page.click_personal_account_button()
        
        login_page.wait_for_load_login_page()
        login_page.set_email(created_user['email'])
        login_page.set_password(created_user['password'])
        login_page.click_login_button()
        
        main_page.wait_for_load_main_page()
        main_page.click_personal_account_button()
        
        account_page.wait_for_load_account_page()
        account_page.click_orders_history_button()
        account_page.wait_for_load_orders_history_in_account

        assert account_page.get_current_url() == ORDERS_HISTORY_IN_ACCOUNT_URL
        