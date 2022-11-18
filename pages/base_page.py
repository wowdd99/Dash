from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import TimeoutException


class BasePage:

    def open(self):
        self.browser.get(self.url)

    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def elements_are_visible(self, locator, timeout=5):
        return wait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator))

    def is_not_element_present(self, how, what, timeout=4):
        try:
            wait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

