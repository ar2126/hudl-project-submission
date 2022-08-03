"""
Description: POM representing the Login page on the Hudl site

@author aidanrubenstein
@since 08/04/2022
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Login:
    def __init__(self, page):
        self.page = page

    def set_email(self, email):
        self.page.find_element(By.ID, "email").send_keys(email)

    def set_password(self, password):
        self.page.find_element(By.ID, "password").send_keys(password)

    def set_email_and_password_with_tab(self, email, password):
        self.page.find_element(By.ID, "email").send_keys(email + Keys.TAB + password)

    def enter_login(self):
        self.page.find_element(By.ID, "email").send_keys(Keys.RETURN)

    def click_login(self):
        self.page.find_element(By.ID, "logIn").click()

    def click_reset_password(self):
        self.page.find_element(By.CSS_SELECTOR, "[data-qa-id='need-help-link']").click()

    def get_invalid_login_text(self):
        return self.page.find_element(By.CSS_SELECTOR, "[data-qa-id='error-display']").text
