from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    PAGE_TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")
    CART_ITEM_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")

    def is_opened(self):
        return self.is_displayed(self.PAGE_TITLE) and self.get_text(self.PAGE_TITLE) == "Your Cart"

    def get_cart_item_names(self):
        if not self.is_displayed(self.CART_ITEMS, timeout=2):
            return []
        return [element.text for element in self.find_all(self.CART_ITEM_NAMES)]

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
