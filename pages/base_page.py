from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils import wait_utils
from utils.screenshot_utils import take_screenshot
from constants.enums import POSSIBLE_ERRORS


class BasePage:
    
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self, locator: tuple, timeout=None):
            """
            Waits for a single element to appear and returns it.
            Raises an AssertionError and takes a screenshot if the element is not found.
            """
            try:
                return wait_utils.wait_for_element(self.driver, locator, timeout)
            except Exception as e:
                self.take_screenshot_on_error("find_failed")
                raise AssertionError(f"❌ Failed to find element: {locator}") from e

    def find_all(self, locator: tuple, timeout=None):
        try:
            wait_utils.wait_for_all_elements(self.driver, locator, timeout)
            return self.driver.find_elements(*locator)
        except Exception as e:
            self.take_screenshot_on_error("find_all_failed")
            raise AssertionError(f"❌ Failed to find all elements: {locator}") from e

    def click(self, locator: tuple, timeout=None):
        """
        Clicks the given element. Raises an error and takes a screenshot on failure.
        """
        try:
            self.find(locator, timeout).click()
        except Exception as e:
            self.take_screenshot_on_error("click_failed")
            raise AssertionError(f"❌ Failed to click element: {locator}") from e

    def send_text(self, locator: tuple, text: str, clear=True, timeout=None):
        """
        Sends text to a field. Optionally clears the field first.
        """
        try:
            element = self.find(locator, timeout)
            if clear:
                element.clear()
            element.send_keys(text)
        except Exception as e:
            self.take_screenshot_on_error("send_text_failed")
            raise AssertionError(f"❌ Failed to send text to element: {locator}") from e

    def get_text(self, locator: tuple, timeout=None) -> str:
        """
        Retrieves and returns the text content of the given element.
        """
        try:
            return self.find(locator, timeout).text
        except Exception as e:
            self.take_screenshot_on_error("get_text_failed")
            raise AssertionError(f"❌ Failed to get text from element: {locator}") from e

    def is_visible(self, locator: tuple, timeout=None) -> bool:
        """
        Checks if the element is visible within the timeout.
        """
        try:
            wait_utils.wait_for_element_visible(self.driver, locator, timeout)
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def is_present(self, locator: tuple, timeout=None) -> bool:
        """
        Returns True if the element is present (regardless of visibility).
        """
        try:
            self.find(locator, timeout)
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def wait_for_not_visible(self, locator: tuple, timeout=None) -> bool:
        """
        Waits for the element to disappear from the screen.
        """
        try:
            return wait_utils.wait_for_element_not_visible(self.driver, locator, timeout)
        except TimeoutException:
            return False

        
    def validate_screen_loaded(self, essential_locators: list[tuple] = None, timeout=None):
        """
        Validates that the screen is loaded properly.
        Checks for presence of essential elements and looks for known error texts in the page source.
        """
        if essential_locators:
            for locator in essential_locators:
                try:
                    self.find(locator, timeout=timeout)
                except Exception as e:
                    self.take_screenshot_on_error("element_not_found")
                    raise AssertionError(f"Element {locator} not found on screen") from e

        page_source = self.driver.page_source.lower()
        if any(err in page_source for err in POSSIBLE_ERRORS):
            self.take_screenshot_on_error("error_detected")
            raise AssertionError("Detected error in page source!")
        
    def take_screenshot_on_error(self, name: str = None):
        """
        Takes a screenshot only if one hasn't already been taken during the current test.
        """
        if getattr(self.driver, "_screenshot_taken", False):
            return  # אל תצלם שוב
        take_screenshot(self.driver, name_prefix=name)
        self.driver._screenshot_taken = True
