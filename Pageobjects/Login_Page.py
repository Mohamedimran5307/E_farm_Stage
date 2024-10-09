import time
from appium import webdriver

from Pageobjects.Basepage import Basepage
from Pageobjects.Order_Page import Order_section
from Testcases.conftest import appium_driver_1
from Pageobjects.Farmer_registry_page import Farmer_registry
from ConfigurationData.config import Testdata

"""By locators"""


class Login_Page(Basepage):
    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    """ These are the page actions for the Home_page"""

    def user_number_page(self, usernumber, OTP_1, OTP_2, OTP_3, OTP_4, OTP_5, OTP_6):
        #
        # self.driver.execute_script("run-as", "com.digitalgreen.org.d2fo", "rm -rf")
        self.do_click("ENTER_PHONE_NUMBER_FIELD_ID")
        self.do_type("ENTER_PHONE_NUMBER_FIELD_ID", usernumber)
        self.driver.press_keycode(4)
        self.do_click("REQUEST_OTP_ID")
        self.do_click("OTP_1_ID")
        self.do_type("OTP_1_ID", OTP_1)
        self.do_click("OTP_2_ID")
        self.do_type("OTP_2_ID", OTP_2)
        self.do_click("OTP_3_ID")
        self.do_type("OTP_3_ID", OTP_3)
        self.do_click("OTP_4_ID")
        self.do_type("OTP_4_ID", OTP_4)
        self.do_click("OTP_5_ID")
        self.do_type("OTP_5_ID", OTP_5)
        self.do_click("OTP_6_ID")
        self.do_type("OTP_6_ID", OTP_6)
        time.sleep(15)
        return Order_section(self.driver)

    def LOGGED_USER_NAME(self):
        return self.get_Text("LOGGED_USER_NAME_ID")

        # return Dev_group_section(self.driver)

    def NEW_DEV_GROUP_NAME(self):
        return self.get_Text("NEW_DEV_GROUP_NAME_XPATH")
