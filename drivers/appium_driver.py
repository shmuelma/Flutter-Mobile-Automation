from appium import webdriver
from config.capabilities.loader import get_capabilities
from config.test_config import get_config

def create_driver(platform):
    config = get_config()
    options = get_capabilities(platform)
    driver = webdriver.Remote(command_executor=config["base_url"], options=options)
    driver.implicitly_wait(config["timeout"])
    return driver