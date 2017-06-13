from selenium import webdriver
import unittest
from selenium.webdriver.chrome.options import Options


import sys
sys.path.insert(0, '../pageObjects')
import page

class BaseTest(unittest.TestCase):

    def setUp(self):
        # set everything up

        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")

        # chrome_options.add_argument('headless')
        caps = chrome_options.to_capabilities()

        self.driver = webdriver.Chrome('../chromedriver', chrome_options=chrome_options)


        # selenium Grid code (for some reason the latest version of selenium grid is funky on the mac. From forums
        # it is recommended to use older version or point the remote to a hub node
        # self.driver = webdriver.Remote(
        #     command_executor='http://10.52.112.26:5555/wd/hub',
        #     desired_capabilities=caps)

        self.driver.get("http://automationpractice.com/index.php")
        self.home_page = page.HomePage(self.driver)
        self.search = page.SearchPage(self.driver)
        self.product = page.ProductPage(self.driver)
        self.order = page.OrderPage(self.driver)
        self.contact = page.ContactUs(self.driver)

    # this doesn't work with headless
    def take_screenshot(self, location):
        self.driver.save_screenshot(location)

    def tearDown(self):
        # self.driver.close()
        pass