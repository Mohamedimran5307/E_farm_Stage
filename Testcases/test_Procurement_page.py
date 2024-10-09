import time
# import HybridAndroidDriver
import allure
from appium import webdriver

# from Pageobjects.Farmer_page import Farmer_section
from Pageobjects.Farmer_registry_page import Farmer_registry
from Pageobjects.LanguagePage import Language_page
from Pageobjects.Login_Page import Login_Page
from Pageobjects.Procurement_page import Procurement

from Testcases.test_base import Basetest_1
from Testcases.conftest import appium_driver_1
from ConfigurationData.config import Testdata
from allure_commons.types import AttachmentType

from Utilities.scroll_util import ScrollUtil
from Utilities.Navigation_flow import Flow_of_test


class Test_Procurement_page(Basetest_1):

    def test_adding_procurement_functionality(self):
        test_flow = Flow_of_test(self.driver)
        test_flow.navigate_to_language_page() \
            .login(Testdata.usernumber, Testdata.OTP_1, Testdata.OTP_2, Testdata.OTP_3, Testdata.OTP_4, Testdata.OTP_5,
                   Testdata.OTP_6) \
            .navigate_to_procurement_page() \
            .perform_procurement_action()

    def test_cancel_procurement_functionality(self):
        test_flow = Flow_of_test(self.driver)
        test_flow.navigate_to_language_page() \
            .login(Testdata.usernumber, Testdata.OTP_1, Testdata.OTP_2, Testdata.OTP_3, Testdata.OTP_4, Testdata.OTP_5,
                   Testdata.OTP_6) \
            .navigate_to_procurement_page() \
            .perform_procurement_action_2()

