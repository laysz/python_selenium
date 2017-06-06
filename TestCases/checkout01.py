from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from basetest import BaseTest


# a sample end to end check out flow
class CheckOut01(BaseTest):

    def test_basic_checkout_flow(self):
        # go to home page and do simple search
        assert self.home_page.is_title_matches(), "Home Page Title does not match"
        self.home_page.enter_search_box("shirt")
        self.home_page.search_box_btn().click()

        # go to search page and click on the first item
        assert self.search.is_title_matches(), "Search Page Title does not match"
        self.search.click_first_product()

        # go through product page
        assert self.product.is_title_matches('Faded Short Sleeve T-shirts - My Store')
        self.product.get_color_locator_id(13).click()
        self.product.quantity().clear()
        self.product.quantity().send_keys('2')
        self.product.cart_btn().click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.element_to_be_clickable(self.product.layer_cart_btn_locator())).click()

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

        # check the final order message
        assert self.order.is_confirmation_message_correct()

