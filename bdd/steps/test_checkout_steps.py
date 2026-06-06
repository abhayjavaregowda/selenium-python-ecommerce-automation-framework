from pytest_bdd import given, parsers, scenarios, then, when

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.config_reader import get_base_url
from utils.data_reader import get_checkout_information, get_product, get_user


scenarios("../features/checkout.feature")


@given(parsers.parse('I am logged in as the "{user_key}" user'))
def logged_in_user(driver, user_key):
    user = get_user(user_key)
    login_page = LoginPage(driver)
    login_page.load(get_base_url())
    login_page.login(user["username"], user["password"])
    assert ProductsPage(driver).is_opened()


@when(parsers.parse('I add the "{product_key}" product to my cart'))
def add_product_to_cart(driver, product_key):
    product_name = get_product(product_key)
    products_page = ProductsPage(driver)
    products_page.add_product_to_cart(product_name)
    products_page.open_cart()
    assert product_name in CartPage(driver).get_cart_item_names()


@when("I checkout with valid customer information")
def checkout_with_valid_information(driver):
    checkout_information = get_checkout_information()
    CartPage(driver).proceed_to_checkout()
    CheckoutPage(driver).complete_checkout(
        checkout_information["first_name"],
        checkout_information["last_name"],
        checkout_information["postal_code"],
    )


@then("I should see the checkout confirmation message")
def verify_checkout_confirmation(driver):
    assert (
        CheckoutPage(driver).get_confirmation_message()
        == "Thank you for your order!"
    )
