import time

from pages.base_page import BasePage
from pages.locatorsnew import LoginPageLocators
from pages.locatorsnew import MainPageLocators
from pages.locatorsnew import ManageShowLocators
from pages.locatorsnew import CreateNewShowLocators


class MainPage(BasePage):
    def should_be_logout_button(self):
        assert self.is_element_present(*LoginPageLocators.LOGOUT_BUTTON), "Logout isn't displayed"

    def should_be_manage_show_link(self):
        assert self.is_element_present(*MainPageLocators.MANAGE_SHOWS_LINK), "Manage Show link isn't displayed"

    def should_open_manage_show_page(self):
        self.should_be_manage_show_link()
        time.sleep(5)
        manage_show_link = self.browser.find_element(*MainPageLocators.MANAGE_SHOWS_LINK)
        manage_show_link.click()
        time.sleep(5)
        assert self.is_element_present(*ManageShowLocators.MANAGE_SHOWS_TITLE), "Manage Show page isn't opened"

    def should_be_create_new_show_link(self):
        assert self.is_element_present(*MainPageLocators.CREATE_NEW_SHOW_LINK), "Create New Show link isn't displayed"

    def should_open_create_new_show_page(self):
        self.should_be_create_new_show_link()
        create_new_user_link = self.browser.find_element(*MainPageLocators.CREATE_NEW_SHOW_LINK)
        create_new_user_link.click()
        time.sleep(10)
        assert self.is_element_present(*CreateNewShowLocators.CREATE_SHOW_TITLE), "Create new Show page isn't opened"