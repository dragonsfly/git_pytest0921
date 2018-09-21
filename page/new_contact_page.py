from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class Newcontactpage(BaseAction):
    def save(self):
        save_button = By.XPATH, "//*[@text='本地保存']"
        self.click(save_button)
