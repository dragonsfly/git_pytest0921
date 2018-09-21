from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class Addcontactpage(BaseAction):
    def new_name(self, text):
        name = By.XPATH, "//*[@text='姓名']"
        self.input(name, text)

    def new_phone(self, text):
        phone = By.XPATH, "//*[@text='电话']"
        self.input(phone, text)

    def back(self):
        back_button = By.XPATH, "//*[@text='向上导航']"
        self.click(back_button)
