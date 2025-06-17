from pages.base_page import BasePage
from locators.login_locators import LoginLocators

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginLocators
        
        self.validate_screen_loaded(essential_locators=[
            self.locators.EMAIL_FIELD,
            self.locators.PASSWORD_FIELD,
            self.locators.LOGIN_BUTTON
        ])

    def enter_email(self, email: str):
        """
        Types the provided email into the email input field.
        """
        self.find(self.locators.EMAIL_FIELD).send_keys(email)

    def enter_password(self, password: str):
        """
        Types the provided password into the password input field.
        """
        self.find(self.locators.PASSWORD_FIELD).send_keys(password)

    def click_login(self):
        """
        Clicks the login button.
        """
        self.click(self.locators.LOGIN_BUTTON)

    def login(self, email: str, password: str):
        """
        Performs a full login sequence: enters email and password, then clicks login.
        """
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def is_error_displayed(self, expected_error: str) -> bool:
        """
        Checks whether the expected error message is currently displayed.
        Returns True if matches, otherwise False.
        """
        try:
            actual_error = self.get_text(self.locators.ERROR_MESSAGE)
            return actual_error == expected_error
        except Exception:
            return False