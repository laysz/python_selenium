
class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, driver):
        self.driver = driver

    # make find_element less verbose
    def find(self, *loc):
        return self.driver.find_element(*loc)



