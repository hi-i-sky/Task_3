from selenium.webdriver.common.by import By

PERSONAL_ACCOUNT_BUTTON = [By.XPATH, ".//p[text()='Личный Кабинет']"]
RESET_PASSWORD_BUTTON = [By.XPATH, ".//a[text()='Восстановить пароль']"]
RESET_PASSWORD_EMAIL_FIELD = [By.CSS_SELECTOR, "input.input__textfield"]
RESET_PASSWORD_CONFIRM_BUTTON = [By.XPATH, ".//button[text()='Восстановить']"]
SHOW_PASSWORD_BUTTON = [By.CSS_SELECTOR, "div.input_type_password svg"]
RESET_PASSWORD_FIELD = [By.CSS_SELECTOR, "div.input_type_password input.input__textfield"]
RESET_PASSWORD_FIELD_BORDER = [By.CSS_SELECTOR, "div.input_type_password"]

MAKE_ORDER_BUTTON = [By.CSS_SELECTOR, "button.button_button_type_primary__1O7Bx"]
