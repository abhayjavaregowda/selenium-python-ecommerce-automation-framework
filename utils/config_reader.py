import os
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]


def get_base_url():
    """Read the application URL from an environment variable or use SauceDemo."""
    return os.getenv("BASE_URL", "https://www.saucedemo.com/")


def get_reports_dir():
    return ROOT_DIR / "reports"


def get_screenshots_dir():
    return ROOT_DIR / "screenshots"


def get_test_data_dir():
    return ROOT_DIR / "test_data"
