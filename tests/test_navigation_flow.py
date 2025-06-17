import pytest
from pages.login_page import LoginPage
from pages.navigator.welcome_page import WelcomePage
from pages.navigator.messages_page import MessagesPage
from pages.navigator.profile_page import ProfilePage
from constants.login_mocks import LOGIN
from constants.welcome_mocks import REACH_COUNTER_CASES


def test_navigation_flow(driver):
    """
    Full navigation flow test with counter verification:
    
    Steps:
    1. Login with valid credentials.
    2. Assert the counter is initially 0.
    3. Navigate through: Messages → Profile → Home.
    4. Assert the counter is now 3 after three navigations.
    5. Click logout and return to the login screen.
    
    This test verifies:
    - Successful login and initial state.
    - Navigation between screens updates the counter.
    - Logout returns the user to the login page.
    """

    # Step 1: Login
    login_page = LoginPage(driver)
    login_page.login(**LOGIN["CREDENTIALS"]["valid"])
    welcome_page = WelcomePage(driver)

    # Step 2: Initial counter check
    assert welcome_page.get_counter_value() == 0, "❌ Expected counter to be 0 after login"

    # Step 3: Navigate through Messages → Profile → Home
    welcome_page.click_messages()
    messages_page = MessagesPage(driver)

    messages_page.click_profile()
    profile_page = ProfilePage(driver)

    profile_page.click_home()
    welcome_page = WelcomePage(driver)

    # Step 4: Final counter check
    assert welcome_page.get_counter_value() == 3, "❌ Expected counter to be 3 after navigation sequence"

    # Step 5: Logout
    welcome_page.click_logout()
    login_page = LoginPage(driver)


@pytest.mark.parametrize("target_value, button_names", REACH_COUNTER_CASES)
def test_counter_reach_scenario(driver, target_value, button_names):
    """
    Test reaching a specific counter value by clicking a given sequence of navigation buttons.
    Verifies initial counter is 0, performs navigation, checks final value, then logs out.
    """
    # Login to the app
    login_page = LoginPage(driver)
    login_page.login(
        LOGIN["CREDENTIALS"]["valid"]["email"],
        LOGIN["CREDENTIALS"]["valid"]["password"]
    )

    welcome_page = WelcomePage(driver)

    # Check counter starts at 0
    assert welcome_page.get_counter_value() == 0, "❌ Counter should start at 0"

    # Perform navigation via buttons
    success = welcome_page.reach_counter_via_buttons(target_value, button_names)
    assert success, f"❌ Failed to reach counter value {target_value} via {button_names}"

    # Logout
    welcome_page.click_logout()

   # Confirm return to login screen
    login_page = LoginPage(driver)