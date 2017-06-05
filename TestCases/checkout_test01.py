import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

import sys
sys.path.insert(0, '../pageObjects')

import page
import homepage

class CheckOut01(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        # set everything up
        self.driver = webdriver.Chrome('../chromedriver')
        self.driver.get("http://automationpractice.com/index.php")
        self.home_page = page.HomePage(self.driver)
        self.search = page.SearchPage(self.driver)
        self.product = page.ProductPage(self.driver)
        self.order = page.OrderPage(self.driver)


    def test_basic_checkout_flow(self):
        # Load the main page. In this case the home page of Python.org.

        # Checks if the word "Python" is in title
        assert self.home_page.is_title_matches(), "Home Page Title does not match"

        self.home_page.enter_search_box("shirt")
        self.home_page.search_box_btn().click()

        assert self.search.is_title_matches(), "Search Page Title does not match"

        self.search.click_first_product()

        assert self.product.is_title_matches('Faded Short Sleeve T-shirts - My Store')


        self.product.get_color_locator_id(13).click()

        self.product.quantity().clear()
        self.product.quantity().send_keys('2')

        self.product.cart_btn().click()

        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a/span'))).click()

        # go through order page
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.title_is('Order - My Store'))
        self.order.summary_continue().click()
        self.order.user_email().send_keys('nothing@mailsac.com')
        self.order.user_password().send_keys('godgod')
        self.order.submit_login().click()
        self.order.address_continue().click()
        self.order.agree_to_terms().click()
        self.order.shipping_continue().click()
        self.order.pay_by_cheque().click()
        self.order.final_confirmation().click()

        assert self.order.is_confirmation_message_correct()

        # self.order.

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()