from pages.base_page import BasePage
from pages.locatorsnew import LoginPageLocators
import time


class LoginPage(BasePage):
    def login_user(self, username, password):
        username_input = self.browser.find_element(*LoginPageLocators.USER_NAME)
        password_input = self.browser.find_element(*LoginPageLocators.PASS_WORD)
        username_input.send_keys(username)
        password_input.send_keys(password)
        log_in_btn = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        log_in_btn.click()
        time.sleep(20)