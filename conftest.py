import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from utils.screenshot_helper import save_screenshot


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=("chrome", "firefox"),
        help="Browser to run tests on: chrome or firefox",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser tests without opening a visible browser window",
    )
    parser.addoption(
        "--base-url",
        action="store",
        default=None,
        help="Override the application URL. Example: --base-url=https://www.saucedemo.com/",
    )


@pytest.fixture
def driver(request, monkeypatch):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    base_url = request.config.getoption("--base-url")

    if base_url:
        monkeypatch.setenv("BASE_URL", base_url)

    driver_instance = _create_driver(browser, headless)
    driver_instance.set_page_load_timeout(30)
    if headless:
        driver_instance.set_window_size(1920, 1080)
    else:
        driver_instance.maximize_window()

    yield driver_instance

    driver_instance.quit()


def _create_driver(browser, headless):
    if browser == "chrome":
        options = ChromeOptions()
        chrome_binary = os.getenv("CHROME_BINARY") or os.getenv("CHROME_BIN")
        if chrome_binary:
            options.binary_location = chrome_binary
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-extensions")
        options.add_argument("--remote-allow-origins=*")
        service = ChromeService(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)

    if browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        service = FirefoxService(GeckoDriverManager().install())
        return webdriver.Firefox(service=service, options=options)

    raise ValueError(f"Unsupported browser: {browser}")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    driver = item.funcargs.get("driver")
    if driver is None:
        return

    screenshot_path = save_screenshot(driver, item.name)

    # Attach the screenshot to pytest-html when the plugin is installed.
    try:
        from pytest_html import extras

        report.extras = getattr(report, "extras", [])
        report.extras.append(extras.image(str(screenshot_path), name="Failure screenshot"))
    except Exception:
        pass
