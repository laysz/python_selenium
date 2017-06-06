from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base_page import BasePage
from selenium.webdriver.support.ui import Select


class ContactUs(BasePage):

    SEARCH_BOX = (By.ID, 'search_query_top')

    PAGE_TITLE = 'Contact us - My Store'

    def subject_heading_dropdown(self, text):
        select = Select(self.find(By.ID, 'id_contact'))
        select.select_by_visible_text(text)


    def email_address(self):
        return self.find(By.ID, 'email')

    def message(self):
        return self.find(By.ID, 'message')

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return self.PAGE_TITLE in self.driver.title

    def select(self, text):
        select = Select(self.subject_heading_dropdown())
        # select by visible text
        select.select_by_visible_text(text)

    def submit(self):
        return self.find(By.ID, 'submitMessage')

    def return_message(self):
        return (By.XPATH, '//*[@id="center_column"]/p')