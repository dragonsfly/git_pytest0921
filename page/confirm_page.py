from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class Confirmpage(BaseAction):
    def get_attribute(self):
        confirm = By.ID, "com.android.contacts:id/title_gradient"
        return self.find_element(confirm).text
