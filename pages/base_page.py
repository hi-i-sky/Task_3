from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:


    def __init__(self, driver):
        self.driver = driver 
        self.wait = WebDriverWait(self.driver, 10)

    def open_page(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def send_keys(self, locator, text):
        element = self.wait_for_element_visible(locator)
        element.send_keys(text)

    def switch_to_new_window(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[-1])

    def wait_for_url_contains(self, url):
        self.wait.until(EC.url_contains(url))

    def wait_for_url_to_be(self, url):
        self.wait.until(EC.url_to_be(url))

    def wait_for_css_property_border_color(self, locator, expected_color):
        self.wait.until(
            lambda d: d.find_element(*locator).value_of_css_property("border-color") == expected_color
        )