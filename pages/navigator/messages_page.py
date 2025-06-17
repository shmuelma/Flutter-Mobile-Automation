from pages.navigator.base_navigator import NavBarPage
from locators.navigator.messages_locators import MessagesLocators

class MessagesPage(NavBarPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MessagesLocators
        self.validate_screen_loaded(essential_locators=[
            self.locators.MESSAGE_TEXT
        ])

    def is_message_text_equal(self, expected_text: str) -> bool:
        """
        Compares the text inside the message element with the expected value.
        Returns True if they match, False otherwise.
        """
        try:
            actual_text = self.get_text(self.locators.MESSAGE_TEXT)
            return actual_text == expected_text
        except Exception:
            return False
