from locators.navigator.base_navbar_locators import NavBarLocators

class WelcomeLocators(NavBarLocators):
    WELCOME_TEXT = ("id", "welcome_message")
    COUNTER_TEXT = ("id", "counter_value")
    RESTART_BUTTON = ("id", "restart_button")
    LOGOUT_BUTTON = ("id", "logout_button")
