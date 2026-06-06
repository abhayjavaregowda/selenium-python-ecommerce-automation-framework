import pytest

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.config_reader import get_base_url
from utils.data_reader import get_product, get_user


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.cart
def test_user_can_add_product_to_cart(driver):
    user = get_user("standard")
    product_name = get_product("backpack")

    login_page = LoginPage(driver)
    login_page.load(get_base_url())
    login_page.login(user["username"], user["password"])

    products_page = ProductsPage(driver)
    products_page.add_product_to_cart(product_name)

    assert products_page.get_cart_badge_count() == 1

    products_page.open_cart()
    assert product_name in CartPage(driver).get_cart_item_names()
