import os
from constants.enums import DEFAULT_TIMEOUT 
def get_config():
    return {
        "platform": os.getenv("PLATFORM", "android"),
        "base_url": os.getenv("APPIUM_URL", "http://localhost:4723"),
        "timeout": int(os.getenv("DEFAULT_TIMEOUT", DEFAULT_TIMEOUT))
    }
