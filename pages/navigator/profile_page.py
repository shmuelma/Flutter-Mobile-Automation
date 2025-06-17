from pages.navigator.base_navigator import NavBarPage
from locators.navigator.profile_locators import ProfileLocators

class ProfilePage(NavBarPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ProfileLocators
        self.validate_screen_loaded(essential_locators=[
            self.locators.PROFILE_NAME
        ])

    def is_profile_name_equal(self, expected_name: str) -> bool:
        """
        Compares the displayed profile name with the expected name.
        Returns True if they match, False otherwise.
        """
        try:
            actual_name = self.get_text(self.locators.PROFILE_NAME)
            return actual_name == expected_name
        except Exception:
            return False
