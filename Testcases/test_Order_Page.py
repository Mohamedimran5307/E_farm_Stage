import time
# import HybridAndroidDriver
import allure
from appium import webdriver

# from Pageobjects.Farmer_page import Farmer_section
from Pageobjects.LanguagePage import Language_page
from Pageobjects.Login_Page import Login_Page

from Testcases.test_base import Basetest_1
from Testcases.conftest import appium_driver_1
from ConfigurationData.config import Testdata
from allure_commons.types import AttachmentType

from Utilities.scroll_util import ScrollUtil


class Test_order_page(Basetest_1):

    def test_Order_Placememt_functionality(self):
        language_page = Language_page(self.driver)
        language_page.language_selection_page().user_number_page(Testdata.usernumber, Testdata.OTP_1, Testdata.OTP_2,
                                                                 Testdata.OTP_3, Testdata.OTP_4, Testdata.OTP_5,
                                                                 Testdata.OTP_6, ).Order_Placememt()
        extracted_text = language_page.ORDER_SUCCESS_TITLE()
        print(extracted_text)
        expected_text = "Order request has been successfully submitted!"
        if expected_text == extracted_text:
            allure.attach(self.driver.get_screenshot_as_png(), name=" Order is successful",
                          attachment_type=AttachmentType.PNG)
            assert True, " Login is successful"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name=" Order is failed",
                          attachment_type=AttachmentType.PNG)
            assert False, " Order is failed"

    def test_Order_Cancel_functionality(self):
        language_page = Language_page(self.driver)
        language_page.language_selection_page().user_number_page(Testdata.usernumber, Testdata.OTP_1, Testdata.OTP_2,
                                                                 Testdata.OTP_3, Testdata.OTP_4, Testdata.OTP_5,
                                                                 Testdata.OTP_6, ).Order_Cancel()
        extracted_text = language_page.ORDER_CANCELLED_TEXT()
        print(extracted_text)
        expected_text = "Order Cancelled Successfully"
        if expected_text == extracted_text:
            allure.attach(self.driver.get_screenshot_as_png(), name=" Cancelling Order is successful",
                          attachment_type=AttachmentType.PNG)
            assert True, " Cancelling Order is successful"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name=" Cancelling Order is failed",
                          attachment_type=AttachmentType.PNG)
            assert False, " Cancelling Order is failed"
