from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base_page import BasePage


class SearchPage(BasePage):

    FIRST_PRODUCT = (By.XPATH, '//*[@id="center_column"]/ul/li/div/div[1]/div/a[1]/img')

    PAGE_TITLE = 'Search - My Store'


    def click_first_product(self):
        elem = self.find(By.XPATH, '//*[@id="center_column"]/ul/li/div/div[1]/div/a[1]/img')
        elem.click()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return self.PAGE_TITLE in self.driver.title

    def find_product_in_search_results(self, text):
        pass
