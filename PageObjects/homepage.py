from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base_page import BasePage


class HomePage(BasePage):

    SEARCH_BOX = (By.ID, 'search_query_top')

    PAGE_TITLE = 'My Store'

    def enter_search_box (self, text):
        elem = self.driver.find_element(*self.SEARCH_BOX)
        elem.clear()
        elem.send_keys(text)
        elem.send_keys(Keys.RETURN)

    def search_box_btn(self):
        return self.find(By.XPATH, '//*[@id="searchbox"]/button')

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return self.PAGE_TITLE in self.driver.title
