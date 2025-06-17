from pages.base_page import BasePage
from locators.navigator.base_navbar_locators import NavBarLocators
class NavBarPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = NavBarLocators
    
    def click_home(self):
        self.click(self.locators.HOME_BUTTON)

    def click_messages(self):
        self.click(self.locators.MESSAGES_BUTTON)

    def click_profile(self):
        self.click(self.locators.PROFILE_BUTTON)

    def click_logout(self):
        self.click(self.locators.LOGOUT_BUTTON)
