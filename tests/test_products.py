import pytest

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.config_reader import get_base_url
from utils.data_reader import get_product, get_user


@pytest.mark.sanity
@pytest.mark.regression
@pytest.mark.products
def test_products_are_displayed_after_login(driver):
    user = get_user("standard")
    expected_product = get_product("backpack")

    login_page = LoginPage(driver)
    login_page.load(get_base_url())
    login_page.login(user["username"], user["password"])

    product_names = ProductsPage(driver).get_product_names()

    assert expected_product in product_names
    assert len(product_names) > 0
