import time
# import HybridAndroidDriver
import allure
from appium import webdriver

from Pageobjects.Farmer_page import Farmer_section
from Pageobjects.LanguagePage import Language_page
from Pageobjects.Login_Usename_Page import Login_Usename_Page

from Testcases.test_base import Basetest
from Testcases.conftest import appium_driver
from ConfigurationData.config import Testdata
from allure_commons.types import AttachmentType

from Utilities.scroll_util import ScrollUtil


class Test_farmer_page(Basetest):

    def test_adding_Dev_group_functionality(self):
        login_page = Login_Usename_Page(self.driver)
        login_page.username_page(Testdata.username, Testdata.password).Adding_Dev_group_page(Testdata.Dev_group_name)
        extracted_text = login_page.NEW_DEV_GROUP_NAME()
        print(extracted_text)
        expected_text = Testdata.Dev_group_name
        if expected_text == extracted_text:
            allure.attach(self.driver.get_screenshot_as_png(), name=" Login is successful",
                          attachment_type=AttachmentType.PNG)
            assert True, " Login is successful"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name=" Login is failed",
                          attachment_type=AttachmentType.PNG)
            assert False, " Login is failed"