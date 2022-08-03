"""
Description: Login test class

@author aidanrubenstein
@since 08/04/2022
"""
import time

import pytest

from Automation.page_objects.LoginPage.login import Login
from pytest_bdd import given, parsers, scenario, then, when
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@scenario("../features/login.feature", "Login with valid credentials")
def test_login_success(env_object):
    """Logging into Hudl"""
    pass


@scenario("../features/login.feature", "Login with valid credentials with keyboard shortcuts")
def test_login_success_keyboard_shortcuts(env_object):
    """Logging into Hudl with tabs/enter"""
    pass


@scenario("../features/login.feature", "Login with valid credentials go back/forward")
def test_login_success_browser_navigation(env_object):
    """Logging into Hudl with browser back/forward functionality"""
    pass


@scenario("../features/login.feature", "Login with valid credentials new tab")
def test_login_success_new_tab(env_object):
    """Logging into Hudl with new browser tab"""
    pass


@scenario("../features/login.feature", "View Reset Password page")
def test_view_password_reset(env_object):
    """View password reset page"""
    pass


@scenario("../features/login.feature", "Login with invalid credentials")
def test_login_fail(env_object):
    """Invalid login when logging into Hudl"""
    pass


@scenario("../features/login.feature", "Login with invalid credentials edge cases")
def test_login_fail_edge_cases(env_object):
    """Invalid login when logging into Hudl with edge cases"""
    pass


@pytest.fixture(scope="function")
def page():
    """
    Creates a page object for handling the browser context

    :return page: the browser driver for the tests
    """
    page = webdriver.Chrome(executable_path="chromedriver")
    return page


@pytest.fixture(scope="function")
def login(page):
    """
    Creates a Login page object for handling selectors and input functions for the login screen

    :page: Object responsible for the browser and page windows
    :return Login: POM which contains the functionality for the login page
    """
    return Login(page)


def enter_creds(env_object, page, login, email, password):
    url = env_object("BASE_URL")
    page.get(url + '/login')
    login.set_email(email)
    login.set_password(password)


# Givens ----------------------------------------------------------------------


@given("I am a user", target_fixture="credentials")
def credentials(env_object):
    """
    Holds the login credentials for a user trying to login to Hudl

    :param env_object: The configuration from the .env file
    :return: Dictionary which contains the email and password for the valid user
    """
    return {"email": env_object("EMAIL"), "password": env_object("PASSWORD")}


# Whens ----------------------------------------------------------------------


@when("I enter my email and password on the login screen")
def step_enter_creds(env_object, page, login, credentials):
    """
    Navigate to Hudl and enter the email and password.
    """
    enter_creds(env_object, page, login, credentials["email"], credentials["password"])


@when("I enter my email and password on the login screen using the tab key")
def step_enter_creds(env_object, page, login, credentials):
    """
    Navigate to Hudl and enter the email and password.
    """
    url = env_object("BASE_URL")
    page.get(url + '/login')
    login.set_email_and_password_with_tab(credentials["email"], credentials["password"])


@when(parsers.parse("I enter my email and incorrect password {password}"))
def step_enter_invalid_creds(env_object, page, login, credentials, password=None):
    """
    Navigate to the Hudl site and enter the email and an incorrect password.
    """
    enter_creds(env_object, page, login, credentials["email"], password)


@when(parsers.parse("I enter my {email} and incorrect password {password}"))
def step_enter_invalid_creds(env_object, page, login, email, password=None):
    """
    Navigate to the Hudl site and enter the email and an incorrect password.
    """
    # This is derived from the feature file - if we have a null this should resort to a blank string (input nothing)
    if email == "null":
        email = ""
    if password == "null":
        password = ""
    enter_creds(env_object, page, login, email, password)


@when("I click on the login button")
def step_click_login(login):
    """Click Log In to submit credentials"""
    login.click_login()


@when("I use the enter key to login")
def step_enter_login(login):
    """Enter to submit credentials"""
    login.enter_login()


@when("I navigate back using the browser")
def step_go_back(page):
    """Browser's back function"""
    page.back()


@when("I navigate forward using the browser")
def step_go_forward(page):
    """Browser's forward function"""
    page.forward()


@when("I open a new tab to the Hudl home page")
def step_create_new_tab(page, env_object):
    """New tab & navigate to Hudl"""
    page.execute_script(f'''window.open("{env_object("BASE_URL")}","_blank");''')


@when("I navigate to perform a password reset")
def step_create_new_tab(page, env_object, login):
    """Navigate to login and click to reset password"""
    url = env_object("BASE_URL")
    page.get(url + '/login')
    login.click_reset_password()

# Thens ----------------------------------------------------------------------


@then("I expect to be redirected to the home page")
def step_home_page_load(page):
    """Assert the page is redirected at the Hudl home page if a user can login"""
    try:
        # Since there's no static header to grab onto, we want to ensure the main homepage divs are loaded successfully
        nav_bar = WebDriverWait(page, 30).until(ec.presence_of_element_located((By.ID, "ssr-webnav")))
        home_content = WebDriverWait(page, 30).until(ec.presence_of_element_located((By.ID, "home-content")))
    except Exception:
        assert False, "Could not find #home-content in Home page"
    assert "Home" in page.title


@then("I expect to see the reset password screen")
def step_home_page_load(page):
    """Assert the page is redirected at the Hudl Password Reset screen"""
    try:
        # Since there's no static header to grab onto, we want to ensure the main homepage divs are loaded successfully
        reset_password_header = WebDriverWait(page, 30).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "[data-qa-id='login-help-headline']"))
        )
    except Exception:
        assert False, "Could not find reset password header in Login Help page"
    assert "/help#" in page.current_url


@then("I expect an error should display on the page indicating that my login is incorrect")
def step_login_error(page, login):
    """Assert the page is at the Hudl Login page if a user can't login"""
    # Implicitly wait 3 second to get the error box displayed
    time.sleep(3)
    assert "Log In" in page.title
    assert login.get_invalid_login_text() == "We didn't recognize that email and/or password.Need help?", \
        "Expected invalid login message"
