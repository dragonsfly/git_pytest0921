from base.base_driver import init_driver
from page.page import Page


class TestNewContact:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_new_contact(self):
        self.page.contactpage.click_add()
        self.page.newcontactpage.save()
        self.page.addcontactpage.new_name("222")
        self.page.addcontactpage.new_phone("186")
        self.page.addcontactpage.back()
        assert self.page.confirmpage.get_attribute() == "222"

    def test_login(self):
        assert 1
