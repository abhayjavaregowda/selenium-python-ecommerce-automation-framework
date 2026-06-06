from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """Common Selenium actions shared by all page objects."""

    DEFAULT_TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def wait_for_element_visible(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_clickable(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_url_contains(self, value, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.url_contains(value))

    def find(self, locator, timeout=DEFAULT_TIMEOUT):
        return self.wait_for_element_visible(locator, timeout)

    def find_all(self, locator, timeout=DEFAULT_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
        return self.driver.find_elements(*locator)

    def click(self, locator, timeout=DEFAULT_TIMEOUT):
        self.wait_for_element_clickable(locator, timeout).click()

    def enter_text(self, locator, text, timeout=DEFAULT_TIMEOUT, clear=True):
        element = self.wait_for_element_visible(locator, timeout)
        if clear:
            element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=DEFAULT_TIMEOUT):
        return self.wait_for_element_visible(locator, timeout).text

    def is_displayed(self, locator, timeout=5):
        try:
            return self.wait_for_element_visible(locator, timeout).is_displayed()
        except TimeoutException:
            return False
