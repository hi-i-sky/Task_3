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
    
    def wait_for_element_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def send_keys(self, locator, text):
        element = self.wait_for_element_visible(locator)
        element.send_keys(text)

    def wait_for_url_contains(self, url):
        self.wait.until(EC.url_contains(url))

    def wait_for_url_to_be(self, url):
        self.wait.until(EC.url_to_be(url))

    def wait_for_css_property_border_color(self, locator, expected_color):
        self.wait.until(
            lambda d: d.find_element(*locator).value_of_css_property("border-color") == expected_color
        )

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

    def wait_for_text_not_to_be(self, locator, text):
        self.wait.until(lambda d: d.find_element(*locator).text != text)