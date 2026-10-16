from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.color import Color


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

    def drag_and_drop(self, start_locator: tuple, finish_locator: tuple):
        start_point = self.wait.until(EC.element_to_be_clickable(start_locator))
        finish_point = self.wait.until(EC.element_to_be_clickable(finish_locator))
        
        actions = ActionChains(self.driver)
        actions.click_and_hold(start_point).move_to_element(finish_point).release().perform()

    def wait_for_element_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def get_locators_text(self, locator):
        return self.driver.find_element(*locator).text

    def drag_and_drop_js(self, start_locator, finish_locator):
        source = self.wait.until(EC.visibility_of_element_located(start_locator))
        target = self.wait.until(EC.visibility_of_element_located(finish_locator))

        script = """
        const source = arguments[0];
        const target = arguments[1];

        const dataTransfer = new DataTransfer();

        function fire(element, type) {
            const event = new DragEvent(type, {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            element.dispatchEvent(event);
        }

        fire(source, 'dragstart');
        fire(target, 'dragenter');
        fire(target, 'dragover');
        fire(target, 'drop');
        fire(source, 'dragend');
        """
        self.driver.execute_script(script, source, target)

    def wait_for_css_property_border_color(self, locator, expected_color, prop="border-bottom-color"):
        expected = Color.from_string(expected_color)
        self.wait.until(
            lambda d: Color.from_string(
                d.find_element(*locator).value_of_css_property(prop)
            ) == expected,
            message=f"Цвет {prop} не стал {expected_color}"
        )