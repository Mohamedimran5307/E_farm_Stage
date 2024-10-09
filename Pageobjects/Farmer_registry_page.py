import time

import allure
from allure_commons.types import AttachmentType

from Pageobjects.Basepage import Basepage
from Testcases.conftest import appium_driver_2
# from Testcases.test_base import Basetest_2
from ConfigurationData.config import Testdata

"""By locators"""


class Farmer_registry(Basepage):
    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    def FARMER_NAME(self):
        return self.get_Text("NEW_ADDED_FARMER_XPATH")

    """ These are the page actions for the Home_page"""

    def Farmer_registry_section(self):
        self.do_swipeUp(1, self.driver)
        self.do_click("SELECT_FARMER_REGISTRY_ID")
        time.sleep(5)
        self.do_click("ADD_NEW_FARMER_ID")
        time.sleep(3)
        self.do_click("ALLOW_TO_PICTURES_RECORD_ID")
        self.do_click("ALLOW_TO_PHOTOS_MEDIA_ID")
        time.sleep(2)
        self.do_click("SELECT_FARMER_IMAGE_ID")
        time.sleep(2)
        self.do_click("SELECT_GALLERY_OPTION_ID")
        time.sleep(2)
        self.do_click("SELECT_GALLERY_ICON_XPATH")
        time.sleep(2)
        self.do_click("SELECT_ALBUM_XPATH")
        time.sleep(2)
        self.do_click("SELECT_GALLERY_IMAGE_XPATH")
        time.sleep(2)
        self.do_click("SHAREHOLDER_TOGGLE_BUTTON_ID")
        self.do_click("FIRST_NAME_FIELD_ID")
        time.sleep(2)
        self.do_type("FIRST_NAME_FIELD_ID", Testdata.First_name)
        self.driver.press_keycode(4)
        self.do_click("SECOND_NAME_FIELD_ID")
        time.sleep(2)
        self.do_type("SECOND_NAME_FIELD_ID", Testdata.Second_name)
        self.driver.press_keycode(4)
        self.do_click("DATE_PICKER_ID")
        self.do_click("DATE_PICKER_OK_BUTTON_ID")
        # self.do_swipeUp(2,self.driver)
        time.sleep(2)
        self.do_click("GENDER_FIELD_ID")
        time.sleep(2)
        self.do_tap_gender()
        self.driver.press_keycode(4)
        self.do_click("SELECT_PRODUCER_GROUP_ID")
        self.do_tap_producer_group()
        self.driver.press_keycode(4)
        self.do_click("NO_OF_SHARES_FIELD_ID")
        self.do_type("NO_OF_SHARES_FIELD_ID", Testdata.No_OF_SHARES)
        time.sleep(2)
        self.do_swipeUp(2, self.driver)
        self.do_click("SELECT_DiSTRICT_ID")
        self.do_tap_select_District()
        self.driver.press_keycode(4)
        self.do_click("SELECT_BLOCK_ID")
        time.sleep(2)
        self.do_tap_select_Block()
        self.driver.press_keycode(4)
        self.do_click("SELECT_VILLAGE_ID")
        self.do_tap_select_Village()
        self.driver.press_keycode(4)
        self.do_click("SELECT_FLW_ID")
        self.do_tap_select_FLW()
        self.driver.press_keycode(4)
        self.do_click("SELECT_AADHAR_ID")
        self.do_type("SELECT_AADHAR_ID", Testdata.Aadhar_number)
        self.do_swipeUp(2, self.driver)
        self.do_click("SELECT_SMARTPHONE_ID")
        self.do_tap_select_smartphone()
        self.do_click("SELECT_MOBILE_NUMBER_FIELD_ID")
        self.do_type("SELECT_MOBILE_NUMBER_FIELD_ID", Testdata.Mobile_number)
        time.sleep(2)
        self.do_click("SELECT_WHATSAPP_NUMBER_CHECKBOX_ID")
        self.do_click("SELECT_EDUCATION_ID")
        time.sleep(2)
        self.do_tap_select_Education()
        self.driver.press_keycode(4)
        self.do_click("SELECT_LANDHOLDING_FIELD_ID")
        self.do_type("SELECT_LANDHOLDING_FIELD_ID", Testdata.LANDHOLDING)
        self.driver.press_keycode(4)
        self.do_click("SELECT_IRRIGATED_LAND_FIELD_ID")
        self.do_type("SELECT_IRRIGATED_LAND_FIELD_ID", Testdata.IRRIGATED_LAND)
        self.do_swipeUp(1, self.driver)
        self.do_click("SELECT_RAINFED_LAND_FIELD_ID")
        self.do_type("SELECT_RAINFED_LAND_FIELD_ID", Testdata.RAINFED_LAND)
        time.sleep(2)
        self.do_click("SELECT_MAJOR_CROP_1_ID")
        self.do_type("SELECT_MAJOR_CROP_1_ID", Testdata.Major_crop_1)
        time.sleep(2)
        self.driver.press_keycode(4)
        self.do_click("SELECT_MAJOR_CROP_2_ID")
        self.do_type("SELECT_MAJOR_CROP_2_ID", Testdata.Major_crop_2)
        self.do_swipeUp(1, self.driver)
        self.do_click("SELECT_NO_OF_COWS_ID")
        self.do_type("SELECT_NO_OF_COWS_ID", Testdata.NO_OF_COWS)
        self.do_click("SELECT_NO_OF_GOATS_ID")
        self.do_type("SELECT_NO_OF_GOATS_ID", Testdata.NO_OF_GOATS)
        self.do_swipeUp(1, self.driver)
        self.do_click("SELECT_NO_OF_CHICKS_ID")
        self.do_type("SELECT_NO_OF_CHICKS_ID", Testdata.NO_OF_CHICKS)
        time.sleep(2)
        self.driver.press_keycode(4)
        self.do_click("NEXT_BUTTON_ID")
        self.do_click("CONSENT_YES_ID")
        time.sleep(10)
        self.do_click("SEARCH_TEXT_FIELD_ID")
        time.sleep(2)
        # print(f"-----------{Testdata.First_name}")
        self.do_type("SEARCH_TEXT_FIELD_ID", Testdata.First_name)
        time.sleep(5)
        extracted_text = Farmer_registry.FARMER_NAME(self)
        print(f"{extracted_text}-----{Testdata.First_name}")
        expected_text = Testdata.First_name
        if expected_text == extracted_text.split(" ")[0]:
            allure.attach(self.driver.get_screenshot_as_png(), name=" Adding Farmer is successful",
                          attachment_type=AttachmentType.PNG)
            assert True, " Adding Farmer is successful "
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name=" Adding Farmer is failed",
                          attachment_type=AttachmentType.PNG)
            assert False, " Adding Farmer is failed "


