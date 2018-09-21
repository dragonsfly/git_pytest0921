from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class Contactpage(BaseAction):
    add_button = By.XPATH, "//*[@content-desc='添加新联系人']"

    def click_add(self):
        self.click(self.add_button)
