import time
# import HybridAndroidDriver
import allure
from appium import webdriver
from Pageobjects.LanguagePage import Language_page
from Pageobjects.Login_Usename_Page import Login_Usename_Page

from Testcases.test_base import Basetest
from Testcases.conftest import appium_driver
from ConfigurationData.config import Testdata
from allure_commons.types import AttachmentType

from Utilities.scroll_util import ScrollUtil


class Test_login_page(Basetest):

    def test_Login_functionality(self):
        login_page = Login_Usename_Page(self.driver)
        login_page.username_page(Testdata.username,Testdata.password)
        extracted_text = login_page.EA_USER_TITLE()
        print(extracted_text)
        expected_text = "Welcome, , ( EA )"
        if expected_text == extracted_text:
            allure.attach(self.driver.get_screenshot_as_png(), name=" Login is successful",
                          attachment_type=AttachmentType.PNG)
            assert True, " Login is successful"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name=" Login is failed",
                          attachment_type=AttachmentType.PNG)
            assert False, " Login is failed"

    # def test_Order_Functionality(self):
    #     language_page = Language_page(self.driver)
    #     language_page.language_selection_page().username_page(Testdata.usernumber)
    #     otp_page = OTP_Page(self.driver)
    #     otp_page.OTP_Number_page(Testdata.OTP_1,
    #                              Testdata.OTP_2, Testdata.OTP_3, Testdata.OTP_4, Testdata.OTP_5, Testdata.OTP_6)
    #     self.driver.implicitly_wait(200)
    #     time.sleep(20)
    #     adb_shell_command = "run-as com.digitalgreen.org.d2fo rm -rf"
    #     result = self.driver.execute_script('mobile: shell', {'command': adb_shell_command})
    #     time.sleep(2)
    #     order_page = Order_Page(self.driver)
    #     # Execute an ADB shell command
    #     time.sleep(2)
    #     order_page.do_click("ORDER_ICON_ID")
    #     time.sleep(2)
    #     order_page.do_click("TAKE_NEW_ORDERS_ICON_ACCESSIBILITYID")
    #     time.sleep(2)
    #     order_page.do_click("TAKE_NEW_ORDERS_2_ID")
    #     time.sleep(2)
    #     order_page.do_click("SELECT_FARMER_XPATH")
    #     time.sleep(2)
    #     order_page.do_click("SELECT_DATE_OF_REQUIREMENT_XPATH")
    #     time.sleep(2)
    #     order_page.do_click("NEXT_MONTH_ID")
    #     time.sleep(2)
    #     order_page.do_click("NEXT_MONTH_ID")
    #     time.sleep(2)
    #     order_page.do_click("DATE_ACCESSIBILITYID")
    #     time.sleep(2)
    #     order_page.do_click("OK_BUTTON_ID")
    #     time.sleep(2)
    #     order_page.do_click("ADD_TO_CART_ID")
    #     time.sleep(2)
    #     order_page.do_click("INCREASE_ID")
    #     time.sleep(2)
    #     order_page.do_click("DECREASE_ID")
    #     time.sleep(2)
        # ScrollUtil.scrollToTextByAndroidUIAutomator(Testdata.Variety, self.driver)
        # order_page.do_swipeUp(1,self.driver)