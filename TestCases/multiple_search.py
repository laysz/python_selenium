from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from basetest import BaseTest


# just reviewing some basic xpath
class SearchMultiple(BaseTest):

    def test_basic_checkout_flow(self):
        # go to home page and do simple search
        assert self.home_page.is_title_matches(), "Home Page Title does not match"
        self.home_page.enter_search_box("dress")
        self.home_page.search_box_btn().click()

        # select from search the item with Blouse
        self.search.find_product_in_search_results('Blouse')[0].click()

