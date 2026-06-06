import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.config_reader import get_base_url
from utils.data_reader import get_checkout_information, get_product, get_user


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.checkout
def test_user_can_complete_checkout(driver):
    user = get_user("standard")
    product_name = get_product("backpack")
    checkout_information = get_checkout_information()

    login_page = LoginPage(driver)
    login_page.load(get_base_url())
    login_page.login(user["username"], user["password"])

    products_page = ProductsPage(driver)
    products_page.add_product_to_cart(product_name)
    products_page.open_cart()

    cart_page = CartPage(driver)
    assert product_name in cart_page.get_cart_item_names()
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.complete_checkout(
        checkout_information["first_name"],
        checkout_information["last_name"],
        checkout_information["postal_code"],
    )

    assert checkout_page.get_confirmation_message() == "Thank you for your order!"
