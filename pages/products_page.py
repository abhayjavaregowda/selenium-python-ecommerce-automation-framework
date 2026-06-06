from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductsPage(BasePage):
    PAGE_TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    INVENTORY_ITEMS = (By.CSS_SELECTOR, ".inventory_item")
    INVENTORY_ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    INVENTORY_BUTTON = (By.CSS_SELECTOR, "button.btn_inventory")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")

    def is_opened(self):
        return (
            self.is_displayed(self.PAGE_TITLE)
            and self.get_text(self.PAGE_TITLE) == "Products"
        )

    def get_product_names(self):
        return [element.text for element in self.find_all(self.INVENTORY_ITEM_NAME)]

    def add_product_to_cart(self, product_name):
        product = self._find_product_card(product_name)
        product.find_element(*self.INVENTORY_BUTTON).click()

    def remove_product_from_cart(self, product_name):
        product = self._find_product_card(product_name)
        product.find_element(*self.INVENTORY_BUTTON).click()

    def get_cart_badge_count(self):
        if not self.is_displayed(self.CART_BADGE, timeout=2):
            return 0
        return int(self.get_text(self.CART_BADGE))

    def open_cart(self):
        self.click(self.CART_LINK)
        self.wait_for_url_contains("cart.html")

    def _find_product_card(self, product_name):
        for product in self.find_all(self.INVENTORY_ITEMS):
            name = product.find_element(*self.INVENTORY_ITEM_NAME).text
            if name == product_name:
                return product
        raise AssertionError(f"Product not found: {product_name}")
