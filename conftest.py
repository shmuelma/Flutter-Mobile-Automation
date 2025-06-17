import pytest
from drivers.appium_driver import create_driver
from config.test_config import get_config
from utils.screenshot_utils import take_screenshot

@pytest.fixture(scope="function")
def driver():
    config = get_config()
    platform = config["platform"]
    driver = create_driver(platform=platform)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    """
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        driver = item.funcargs.get("driver")
        if driver and not getattr(driver, "_screenshot_taken", False):
            path = take_screenshot(driver, name_prefix=item.name)
            if path:
                print(f"❌ Test '{item.name}' failed. Screenshot saved to: {path}")
            else:
                print(f"❌ Test '{item.name}' failed. Screenshot failed to save.")
            driver._screenshot_taken = True