from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.test_config import get_config

def get_timeout(timeout):
    return timeout if timeout is not None else get_config()["timeout"]

def wait_for_element(driver, locator: tuple, timeout: int = None):
    return WebDriverWait(driver, get_timeout(timeout)).until(
        EC.presence_of_element_located(locator)
    )

def wait_for_element_visible(driver, locator: tuple, timeout: int = None):
    return WebDriverWait(driver, get_timeout(timeout)).until(
        EC.visibility_of_element_located(locator)
    )

def wait_for_element_not_visible(driver, locator: tuple, timeout: int = None):
    return WebDriverWait(driver, get_timeout(timeout)).until(
        EC.invisibility_of_element_located(locator)
    )

def wait_for_all_elements(driver, locator: tuple, timeout: int = None):
    return WebDriverWait(driver, get_timeout(timeout)).until(
        lambda d: len(d.find_elements(*locator)) > 0
    )