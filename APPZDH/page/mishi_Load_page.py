from time import sleep
from page.base_page import BasePage


class LoadPage(BasePage):
    def load(self):
        for i in range(3):
            self.driver.swipe(860, 730, 66, 730, 1000)
