from lib2to3.pgen2 import driver

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from Pageobjects.Basepage import Basepage
from Pageobjects.Login_Page import Login_Page
from Testcases.conftest import appium_driver_1, clear_app_data, restart_app
# from Testcases.test_base import Basetest_1

"""By locators"""


class Language_page(Basepage):
    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    """ These are the page actions for the Home_page"""

    def ORDER_SUCCESS_TITLE(self):
        return self.get_Text("SUCCESS_TEXT_ID")

    def ORDER_CANCELLED_TEXT(self):
        return self.get_Text("ORDER_CANCELLED_TEXT_ID")

    def EFARM_USER_TITLE(self):
        return self.get_Text("EFARM_TITLE_ID")

    def LOGGED_USER_NAME(self):
        return self.get_Text("LOGGED_USER_NAME_ID")

    def language_selection_page(self, desired_cap=None):

        # self.clear_room_database("com.digitalgreen.org.d2fo", "d2fo_loop_digital_green_db")
        # self.driver.execute_script("run-as", "com.digitalgreen.org.d2fo", "rm -rf")
        self.do_click("LANGUAGE_OPTION_XPATH")
        self.do_click("CONTINUE_BUTTON_ID")
        # return Login_Page(self.driver)
        extracted_text = Language_page.EFARM_USER_TITLE(self)
        print(extracted_text)
        expected_text = "Welcome to eFarm"
        if expected_text == extracted_text:
            allure.attach(self.driver.get_screenshot_as_png(), name=" Selection of Langugage is successful",
                          attachment_type=AttachmentType.PNG)
            assert True, " Selection of Langugage is successful"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name=" Selection of Langugage is failed",
                          attachment_type=AttachmentType.PNG)
            assert False, " Selection of Langugage is failed"
