import allure
from constants.urls import FORGOT_PASSWORD_URL, RESET_PASSWORD_URL
from constants.data_set import COLOR_OF_HIGHLIGHTS


class TestResetPassword:

    @allure.title('Проверка кнопки "Восстановить пароль"')
    def test_get_forgot_password_page(self, main_page, login_page, forgot_password_page, reset_password_page):

        main_page.get_base_page()
        main_page.click_personal_account_button()

        login_page.wait_for_load_login_page()
        login_page.click_reset_password_button()

        forgot_password_page.wait_for_load_forgot_password_page()

        assert reset_password_page.get_current_url() == FORGOT_PASSWORD_URL


    @allure.title('Проверка перехода на страницу для ввода нового пароля для восстановления')
    def test_get_reset_password_page(self, main_page, login_page, forgot_password_page, reset_password_page):

        main_page.get_base_page()
        main_page.click_personal_account_button()

        login_page.wait_for_load_login_page()
        login_page.click_reset_password_button()

        forgot_password_page.set_forgot_password_page()

        reset_password_page.wait_for_load_reset_password_page()

        assert reset_password_page.get_current_url() == RESET_PASSWORD_URL


    @allure.title('Проверка подсветки поля с паролем при клике по иконке "Показать пароль"')
    def test_show_password_button_highlights_field(self, main_page, login_page, forgot_password_page, reset_password_page):

        main_page.get_base_page()
        main_page.click_personal_account_button()

        login_page.wait_for_load_login_page()
        login_page.click_reset_password_button()

        forgot_password_page.set_forgot_password_page()

        reset_password_page.wait_for_load_reset_password_page()
        reset_password_page.click_show_password_button()
        reset_password_page.wait_for_border_color_password_field()

        assert reset_password_page.get_border_color_of_password_field() == COLOR_OF_HIGHLIGHTS