import allure
from locators.base_page_locators import RESET_PASSWORD_FIELD_BORDER
from constants.urls import FORGOT_PASSWORD_URL, RESET_PASSWORD_URL


class TestResetPassword:


    def test_get_forgot_password_page(self, main_page, login_page, forgot_password_page, reset_password_page):

        main_page.get_base_page()
        main_page.click_personal_account_button()

        login_page.wait_for_load_login_page()
        login_page.click_reset_password_button()

        forgot_password_page.wait_for_load_forgot_password_page()


        assert reset_password_page.get_current_url() == FORGOT_PASSWORD_URL


    def test_get_reset_password_page(self, main_page, login_page, forgot_password_page, reset_password_page):

        main_page.get_base_page()
        main_page.click_personal_account_button()

        login_page.wait_for_load_login_page()
        login_page.click_reset_password_button()

        forgot_password_page.wait_for_load_forgot_password_page()
        forgot_password_page.set_email_for_reset_password()
        forgot_password_page.click_reset_password_confirm_button()

        reset_password_page.wait_for_load_reset_password_page()

        assert reset_password_page.get_current_url() == RESET_PASSWORD_URL

    
    def test_show_password_button_highlights_field(self, main_page, login_page, forgot_password_page, reset_password_page):

        main_page.get_base_page()
        main_page.click_personal_account_button()

        login_page.wait_for_load_login_page()
        login_page.click_reset_password_button()

        forgot_password_page.wait_for_load_forgot_password_page()
        forgot_password_page.set_email_for_reset_password()
        forgot_password_page.click_reset_password_confirm_button()

        reset_password_page.wait_for_load_reset_password_page()
        reset_password_page.click_show_password_button()
        reset_password_page.wait_for_border_color_password_field()

        assert reset_password_page.get_border_color_of_password_field() == "rgb(76, 76, 255)"