from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base_page import BasePage

class OrderPage(BasePage):

    PAGE_TITLE = 'Order - My Store'
    SUCCESS_ORDER_MESSAGE = 'Your order on My Store is complete.'

    def get_color_locator_id(self, color):
        return self.find(By.ID, 'color_' + str(color))

    def is_title_matches(self):
        return self.PAGE_TITLE in self.driver.title

    def user_email (self):
        return self.find(By.ID, 'email')

    def user_password(self):
        return self.find(By.ID, 'passwd')

    def submit_login(self):
        return self.find(By.ID, 'SubmitLogin')

    def address_continue(self):
        return self.find(By.XPATH, '//*[@id="center_column"]/form/p/button/span')

    def summary_continue(self):
        return self.find(By.XPATH, '//*[@id="center_column"]/p[2]/a[1]/span')

    def agree_to_terms(self):
        return self.find(By.ID, 'cgv')

    def shipping_continue(self):
        return self.find(By.XPATH, '//*[@id="form"]/p/button/span')

    def pay_by_cheque(self):
        return self.find(By.XPATH, '//*[@id="HOOK_PAYMENT"]/div[2]/div/p/a/span')

    def final_confirmation(self):
        return self.find(By.XPATH, '//*[@id="cart_navigation"]/button')

    def get_confirmation_message(self):
        return self.find(By.XPATH, '//*[@id="center_column"]/p[1]').text

    def is_confirmation_message_correct(self):
        return self.SUCCESS_ORDER_MESSAGE in self.get_confirmation_message()