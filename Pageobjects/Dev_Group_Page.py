import time

from Pageobjects.Basepage import Basepage
from Testcases.conftest import appium_driver

from ConfigurationData.config import Testdata

"""By locators"""


class Dev_group_section(Basepage):
    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    """ These are the page actions for the Home_page"""

    def Adding_Dev_group_page(self, Dev_group_name):
        self.do_click("SELECT_DEV_GROUP_ID")
        self.do_click("SELECT_ADD_DEV_GROUP_ID")
        time.sleep(5)
        self.do_click("DEV_GROUP_NAME_ID")
        self.do_type("DEV_GROUP_NAME_ID", Dev_group_name)
        time.sleep(2)
        self.do_click("DEV_GROUP_TYPE_ID")
        self.do_tap_dev_group_type()
        self.do_click("DEV_GROUP_VILLAGE_ID")
        self.do_tap_dev_group_village()
        self.do_click("DEV_GROUP_SUBMIT_BUTTON_ID")
        time.sleep(5)
        # return Order_Page(self.driver)

    def NEW_DEV_GROUP_NAME(self):
        return self.get_Text("NEW_DEV_GROUP_NAME_XPATH")
