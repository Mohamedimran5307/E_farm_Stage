import time
import allure
from Pageobjects.Basepage import Basepage
from Testcases.conftest import appium_driver_1
from allure_commons.types import AttachmentType

from ConfigurationData.config import Testdata

"""By locators"""


class Procurement(Basepage):
    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    def PROCUREMENT_SUCCESS_TITLE(self):
        return self.get_Text("SUCCESS_TEXT_ID")

    def PROCUREMENT_CANCELLED_TEXT(self):
        return self.get_Text("CANCELLED_PROCUREMENT_TEXT_ID")

    """ These are the page actions for the Home_page"""

    def Procurement_section(self):
        self.do_click("SELECT_PROCUREMENT_ID")
        time.sleep(5)
        self.do_click("TAKE_NEW_PROCUREMENT_ID")
        time.sleep(5)
        self.do_click("SELECT_PROCUREMENT_FARMER_XPATH")
        time.sleep(2)
        self.do_click("SELECT_CATEGORY_XPATH")
        time.sleep(2)
        self.do_click("SELECT_CROP_XPATH")
        time.sleep(2)
        self.do_click("DEVICE_LOCATION_PROCUREMENT_ID")
        time.sleep(2)
        self.do_click("SELECT_QUANTITY_DROPDOWN_ID")
        time.sleep(2)
        self.do_click("SELECT_QUANTITY_FIELD_ID")
        time.sleep(2)
        self.do_type("SELECT_QUANTITY_FIELD_ID", Testdata.Procurement_Qunatity)
        self.driver.press_keycode(4)
        self.do_click("SELECT_UOM_ID")
        time.sleep(2)
        self.do_tap_select_UOM_units()
        self.do_click("SELECT_REASON_ID")
        self.do_tap_select_Reason()
        self.do_click("SUBMIT_PROCUREMENT_BUTTON_ID")
        time.sleep(6)
        extracted_text = Procurement.PROCUREMENT_SUCCESS_TITLE(self)
        print(extracted_text)
        expected_text = "Request has been successfully submitted!"
        if expected_text == extracted_text:
            allure.attach(self.driver.get_screenshot_as_png(), name=" Procurement is successfully",
                          attachment_type=AttachmentType.PNG)
            assert True, " Procurement is successfully"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name=" Procurement is failed",
                          attachment_type=AttachmentType.PNG)
            assert False, " Procurement is failed"

    def Procurement_Cancel(self):
        self.do_click("SELECT_PROCUREMENT_ID")
        time.sleep(5)
        self.do_click("CANCEL_PROCUREMENT_ID")
        self.do_click("CONFIRM_CANCEL_PROCUREMENT_ID")
        time.sleep(3)
        extracted_text = Procurement.PROCUREMENT_CANCELLED_TEXT(self)
        print(extracted_text)
        expected_text = "Cancelled"
        if expected_text == extracted_text:
            allure.attach(self.driver.get_screenshot_as_png(), name=" Procurement is successfully",
                          attachment_type=AttachmentType.PNG)
            assert True, " Procurement is successfully"
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name=" Procurement is failed",
                          attachment_type=AttachmentType.PNG)
            assert False, " Procurement is failed"
