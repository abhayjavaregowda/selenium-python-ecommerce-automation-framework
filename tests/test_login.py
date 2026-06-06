import pytest

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.config_reader import get_base_url
from utils.data_reader import get_user


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.login
@pytest.mark.positive
def test_valid_user_can_login(driver):
    user = get_user("standard")

    login_page = LoginPage(driver)
    login_page.load(get_base_url())
    login_page.login(user["username"], user["password"])

    assert ProductsPage(driver).is_opened()


@pytest.mark.regression
@pytest.mark.login
@pytest.mark.negative
@pytest.mark.parametrize("user_key", ["locked_out", "invalid"])
def test_login_fails_for_invalid_or_blocked_users(driver, user_key):
    user = get_user(user_key)

    login_page = LoginPage(driver)
    login_page.load(get_base_url())
    login_page.login(user["username"], user["password"])

    assert user["expected_error"] in login_page.get_error_message()
