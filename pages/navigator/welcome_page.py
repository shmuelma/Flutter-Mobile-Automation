from pages.navigator.base_navigator import NavBarPage
from locators.navigator.welcome_locators import WelcomeLocators

class WelcomePage(NavBarPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = WelcomeLocators
        self.validate_screen_loaded([self.locators.WELCOME_TEXT])

        
    def is_welcome_text_displayed(self, expected: str) -> bool:
        try:
            actual = self.get_text(self.locators.WELCOME_TEXT)
            return actual == expected
        except Exception:
            return False

 # ------------------- Counter Handling -------------------

    def is_counter_value(self, expected: int) -> bool:
        try:
            actual = int(self.get_text(self.locators.COUNTER_TEXT))
            return actual == expected
        except Exception:
            return False

    def get_counter_value(self) -> int:
        """Returns the current counter value as an integer."""
        text = self.get_text(self.locators.COUNTER_TEXT)
        try:
            return int(text)
        except Exception:
            return -1  # Indicates error in parsing
        
    def click_restart(self) -> bool:
        try:
            self.click(self.locators.RESTART_BUTTON)
            return self.is_counter_value(0)  
        except Exception:
            return False

    def reach_counter_via_buttons(self, target_value: int, button_sequence: list[str]) -> bool:
        """
        Clicks the given buttons in order until the counter reaches the target value.
        If button_names is empty or invalid, clicks all three buttons in a round-robin loop.
        Returns True if the counter reaches the target value, False otherwise.
        """
        valid_buttons = {
            "home": self.click_home,
            "messages": self.click_messages,
            "profile": self.click_profile
        }

        actions = [valid_buttons[name] for name in button_sequence if name in valid_buttons]
        if not actions:
            actions = list(valid_buttons.values()) 

        current_value = self.get_counter_value()
        index = 0

        while current_value < target_value:
            actions[index % len(actions)]()
            current_value = self.get_counter_value()
            index += 1

        return current_value == target_value
