import time
from appium import webdriver

from Pageobjects.Basepage import Basepage
from Pageobjects.Dev_Group_Page import Dev_group_section
from Testcases.conftest import appium_driver
from Pageobjects.Farmer_page import Farmer_section
from ConfigurationData.config import Testdata
"""By locators"""


class Login_Usename_Page(Basepage):

    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    """ These are the page actions for the Home_page"""

    def username_page(self,username,password):
        #
        # self.driver.execute_script("run-as", "com.digitalgreen.org.d2fo", "rm -rf")
        self.do_click("USER_NUMBER_FIELD_ID")
        self.do_type("USER_NUMBER_FIELD_ID",username)
        self.do_click("PASSWORD_FIELD_ID")
        self.do_type("PASSWORD_FIELD_ID",password)
        self.do_click("LOGIN_BUTTON_ID")
        time.sleep(15)
        # return Farmer_section(self.driver)
        return Dev_group_section (self.driver)

    def username_page_0(self,username,password):
        #
        # self.driver.execute_script("run-as", "com.digitalgreen.org.d2fo", "rm -rf")
        self.do_click("USER_NUMBER_FIELD_ID")
        self.do_type("USER_NUMBER_FIELD_ID",username)
        self.do_click("PASSWORD_FIELD_ID")
        self.do_type("PASSWORD_FIELD_ID",password)
        self.do_click("LOGIN_BUTTON_ID")
        time.sleep(15)
        return Farmer_section(self.driver)
        # return Dev_group_section (self.driver)

    def EA_USER_TITLE(self):
        return self.get_Text("EA_USER_TITLE_ID")

    def NEW_DEV_GROUP_NAME(self):
        return self.get_Text("NEW_DEV_GROUP_NAME_XPATH")