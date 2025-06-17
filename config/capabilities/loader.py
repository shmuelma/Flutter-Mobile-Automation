import yaml
import os

from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from utils.string_utils import to_snake_case  

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "capabilities.yaml")

def get_capabilities(platform="android"):
    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        all_caps = yaml.safe_load(file)

    if platform not in all_caps:
        raise ValueError(f"Unsupported platform: {platform}")

    config = all_caps[platform]

    if platform.startswith("android"):
        options = UiAutomator2Options()
    elif platform == "ios":
        options = XCUITestOptions()
    else:
        raise ValueError(f"Unsupported platform type: {platform}")

    for key, value in config.items():
        setattr(options, to_snake_case(key), value)

    return options
