import allure
from constants.urls import ACCOUNT_URL


class TestLoginPage():

    @allure.title('Проверка логина зарегистрированным пользователем')
    def test_login_and_get_account_page(self, main_page, login_page, account_page, created_user):

        login_page.login(created_user['email'], created_user['password'])

        main_page.wait_for_load_main_page()
        main_page.click_personal_account_button_after_login()

        account_page.wait_for_load_account_page()
        
        assert account_page.get_current_url() == ACCOUNT_URL