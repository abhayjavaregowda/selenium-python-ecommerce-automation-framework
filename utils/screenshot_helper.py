import re
from datetime import datetime

from utils.config_reader import get_screenshots_dir


def save_screenshot(driver, test_name):
    screenshots_dir = get_screenshots_dir()
    screenshots_dir.mkdir(parents=True, exist_ok=True)

    safe_test_name = re.sub(r"[^A-Za-z0-9_.-]+", "_", test_name)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = screenshots_dir / f"{safe_test_name}_{timestamp}.png"

    driver.save_screenshot(str(screenshot_path))
    return screenshot_path
