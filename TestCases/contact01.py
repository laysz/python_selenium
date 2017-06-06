from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from basetest import BaseTest


# a sample test that tries to
class ContactUs(BaseTest):

    def test_contact_us(self):
        # go to home page and do simple search
        assert self.home_page.is_title_matches(), "Home Page Title does not match"

        # the contact us page has a function to upload files
        # this is outside selenium but i would use the robot api to select a file

        # go to contact us page
        self.home_page.contact_us().click()
        assert self.contact.is_title_matches()

        # fill it out and click submit
        self.contact.subject_heading_dropdown('Customer service')
        self.contact.email_address().clear()
        self.contact.email_address().send_keys('nothing@mailsac.com')
        self.contact.message().send_keys("Hello world")
        self.contact.submit().click()

        # now check if the message is success respsonse
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.text_to_be_present_in_element(self.contact.return_message(), 'Your message has been successfully sent to our team.'))
