from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base_page import BasePage


class ProductPage(BasePage):

    def get_color_locator_id(self, color):
        return self.driver.find_element(By.ID, 'color_' + str(color))

    def quantity(self):
        return self.find(By.XPATH, '//*[@id="quantity_wanted"]')

    def size(self):
        return self.find(By.XPATH, '//*[@id="group_1"]')

    def is_title_matches(self, title):
        return title in self.driver.title

    def cart_btn(self):
        return self.find(By.XPATH, '//*[@id="add_to_cart"]/button/span')

    def layer_cart_btn(self):
        return self.find(By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a/span')