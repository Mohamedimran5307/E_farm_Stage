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

    def test_adding_farmers_functionality(self):

        #  Login_Usename_Page correctly navigates and returns an instance of Farmer_section
        farmer_section = Login_Usename_Page(self.driver).username_page_0(Testdata.username, Testdata.password)

        # Now, assuming farmer_section is an instance of Farmer_section, you can chain the methods directly
        # It's important that Adding_farmer_page should return self to allow chaining
        farmer_section.Adding_farmer_page().Adding_personal_info_page(Testdata.Farmer_name, Testdata.Father_name,
                                                                      Testdata.Grandfather_name,Testdata.Age,Testdata.FIRST_FOUR,Testdata.SECOND_FOUR,Testdata.THIRD_FOUR).Adding_contact_info_page()
        # login_page = Login_Usename_Page(self.driver)
        # login_page.username_page_0(Testdata.username, Testdata.password).Adding_farmer_page().Adding_Personal_info_page(Testdata.Farmer_name,Testdata.Father_name,Testdata.Grandfather_name)
        # # if expected_text == extracted_text:
        #     allure.attach(self.driver.get_screenshot_as_png(), name=" Login is successful",
        #                   attachment_type=AttachmentType.PNG)
        #     assert True, " Login is successful"
        # else:
        #     allure.attach(self.driver.get_screenshot_as_png(), name=" Login is failed",
        #                   attachment_type=AttachmentType.PNG)
        #     assert False, " Login is failed"
