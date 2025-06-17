import os
from datetime import datetime
from constants.enums import DATE_FORMAT

def take_screenshot(driver, name_prefix="screenshot"):

    folder = "screenshots"
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime(DATE_FORMAT)
    filename = f"{name_prefix}_{timestamp}.png"
    path = os.path.join(folder, filename)
    try:
        driver.save_screenshot(path)
        return path
    except Exception as e:
        print(f"❌ [Screenshot Error] Failed to save screenshot to '{path}': {e}")
        return None
