from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CSS_SELECTOR, "[data-test='complete-header']")
    PAGE_TITLE = (By.CSS_SELECTOR, "[data-test='title']")

    def fill_customer_information(self, first_name, last_name, postal_code):
        self.enter_text(self.FIRST_NAME_INPUT, first_name)
        self.enter_text(self.LAST_NAME_INPUT, last_name)
        self.enter_text(self.POSTAL_CODE_INPUT, postal_code)

    def continue_checkout(self):
        self.click(self.CONTINUE_BUTTON)

    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)

    def complete_checkout(self, first_name, last_name, postal_code):
        self.fill_customer_information(first_name, last_name, postal_code)
        self.continue_checkout()
        self.finish_checkout()

    def get_confirmation_message(self):
        return self.get_text(self.COMPLETE_HEADER)

    def is_overview_page_displayed(self):
        return self.is_displayed(self.PAGE_TITLE) and self.get_text(self.PAGE_TITLE) == "Checkout: Overview"
