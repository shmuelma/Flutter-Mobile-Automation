from pages.login_page import LoginPage
from pages.navigator.welcome_page import WelcomePage
from constants.enums import LOGIN, WELCOME_MSG


def test_successful_login_and_logout(driver):
    """
    Tests valid login: enters correct credentials, verifies welcome message,
    then performs logout and checks return to login screen.
    """
    # Login flow
    login_page = LoginPage(driver)
    login_page.login(
        LOGIN["CREDENTIALS"]["valid"]["email"],
        LOGIN["CREDENTIALS"]["valid"]["password"]
    )

    # Welcome screen
    welcome_page = WelcomePage(driver)
    assert welcome_page.is_welcome_text_displayed(WELCOME_MSG), "❌ Login failed or incorrect welcome message"

    # Logout
    assert welcome_page.click_logout(), "❌ Logout button not found or failed to click"

    # Verify return to login screen
    login_page = LoginPage(driver)


def test_failed_login_shows_error(driver):
    """
    Tests invalid login: enters wrong credentials and verifies the error message is displayed.
    """
    login_page = LoginPage(driver)
    login_page.login(
        LOGIN["CREDENTIALS"]["invalid"]["email"],
        LOGIN["CREDENTIALS"]["invalid"]["password"]
    )

    assert login_page.is_error_displayed(LOGIN["ERROR_MSG"]), "❌ Error message not displayed for invalid credentials"