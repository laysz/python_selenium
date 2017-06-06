from selenium import webdriver
import unittest

import sys
sys.path.insert(0, '../pageObjects')
import page

class BaseTest(unittest.TestCase):

    def setUp(self):
        # set everything up
        self.driver = webdriver.Chrome('../chromedriver')
        self.driver.get("http://automationpractice.com/index.php")
        self.home_page = page.HomePage(self.driver)
        self.search = page.SearchPage(self.driver)
        self.product = page.ProductPage(self.driver)
        self.order = page.OrderPage(self.driver)
        self.contact = page.ContactUs(self.driver)

    def tearDown(self):
        self.driver.close()