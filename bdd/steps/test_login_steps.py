from pytest_bdd import given, parsers, scenarios, then, when

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.config_reader import get_base_url
from utils.data_reader import get_user


scenarios("../features/login.feature")


@given("I am on the SauceDemo login page")
def open_login_page(driver):
    LoginPage(driver).load(get_base_url())


@when(parsers.parse('I login with the "{user_key}" user'))
def login_with_user(driver, user_key):
    user = get_user(user_key)
    LoginPage(driver).login(user["username"], user["password"])


@then("I should see the products page")
def verify_products_page(driver):
    assert ProductsPage(driver).is_opened()


@then(parsers.parse('I should see the login error for the "{user_key}" user'))
def verify_login_error(driver, user_key):
    user = get_user(user_key)
    assert user["expected_error"] in LoginPage(driver).get_error_message()
