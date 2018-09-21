from page.add_contact_page import Addcontactpage
from page.confirm_page import Confirmpage
from page.contact_page import Contactpage
from page.new_contact_page import Newcontactpage


class Page:
    def __init__(self, driver):
        self.driver = driver

    @property
    def addcontactpage(self):
        return Addcontactpage(self.driver)

    @property
    def confirmpage(self):
        return Confirmpage(self.driver)

    @property
    def contactpage(self):
        return Contactpage(self.driver)

    @property
    def newcontactpage(self):
        return Newcontactpage(self.driver)
