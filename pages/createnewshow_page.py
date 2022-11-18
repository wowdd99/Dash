from pages.base_page import BasePage
from pages.locatorsnew import ManageShowLocators


class CreateShowPage(BasePage):

    def should_be_show_status(self):
        assert self.is_element_present(*ManageShowLocators.SHOW_STATS_TAB), "Show Stats btn isn't default"
