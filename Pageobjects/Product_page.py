import time
import allure
from Pageobjects.Basepage import Basepage
from Testcases.conftest import appium_driver_2
from allure_commons.types import AttachmentType

from ConfigurationData.config import Testdata

"""By locators"""


class Product(Basepage):
    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    # def PROCUREMENT_SUCCESS_TITLE(self):
    #     return self.get_Text("SUCCESS_TEXT_ID")

    """ These are the page actions for the Home_page"""

    def Product_section(self):
        self.do_click("SELECT_PRODUCT_ID")
        time.sleep(3)
        self.do_click("ADD_NEW_PRODUCT_ID")
        time.sleep(2)
        self.do_click("SELECT_PRODUCT_CATEGORY_ID")
        self.do_select_Product_category_type()
        time.sleep(2)
        self.do_click("SELECT_PRODUCT_NAME_ID")
        self.do_type("SELECT_PRODUCT_NAME_ID",Testdata.Product_name)
        self.driver.press_keycode(4)
        self.do_click("UPLOAD_PRODUCT_IMAGE_ID")
        time.sleep(2)
        self.do_click("ACCESS_TO_IMAGES_ID")
        self.do_click("ACCESS_TO_MEDIA_ID")
        self.do_click("GALLERY_OPTION_ID")
        self.do_click("GALLERY_ICON_XPATH")
        self.do_click("ALBUM_PATH_XPATH")
        self.do_click("GALLERY_IMAGE_XPATH")
        time.sleep(2)
        self.do_click("PRODUCT_VARIETY_FIELD_ID")
        self.do_type("PRODUCT_VARIETY_FIELD_ID", Testdata.Product_variety)
        self.do_swipeUp(1, self.driver)
        time.sleep(2)
        self.driver.press_keycode(4)
        self.do_click("STOCK_AVAILABLE_FIELD_ID")
        time.sleep(2)
        self.do_type("STOCK_AVAILABLE_FIELD_ID", Testdata.Stock)
        time.sleep(2)
        self.driver.press_keycode(4)
        self.do_click("MRP_FIELD_ID")
        self.do_type("MRP_FIELD_ID", Testdata.MRP)
        time.sleep(2)
        self.driver.press_keycode(4)
        self.do_swipeUp(1, self.driver)
        time.sleep(2)
        self.do_click("SHAREHOLDER_FIELD_ID")
        self.do_type("SHAREHOLDER_FIELD_ID", Testdata.Shareholder_Price)
        time.sleep(2)
        self.driver.press_keycode(4)
        self.do_click("NON_SHAREHOLDER_FIELD_ID")
        self.do_type("NON_SHAREHOLDER_FIELD_ID", Testdata.Non_Shareholder_Price)
        time.sleep(2)
        self.driver.press_keycode(4)
        self.do_click("PRODUCT_SAVE_BUTTON_ID")
        time.sleep(2)
        self.do_click("PRODUCT_REVIEW_SUBMIT_ID")
        time.sleep(5)

        # self.driver.press_keycode(4)
        # self.do_click("SELECT_CROP_XPATH")
        # time.sleep(2)
        # self.do_click("DEVICE_LOCATION_PROCUREMENT_ID")
        # time.sleep(2)
        # self.do_click("SELECT_QUANTITY_DROPDOWN_ID")
        # time.sleep(2)
        # self.do_click("SELECT_QUANTITY_FIELD_ID")
        # time.sleep(2)
        # self.do_type("SELECT_QUANTITY_FIELD_ID",Testdata.Procurement_Qunatity)
        # self.driver.press_keycode(4)
        # self.do_click("SELECT_UOM_ID")
        # time.sleep(2)
        # self.do_tap_select_UOM_units()
        # self.do_click("SELECT_REASON_ID")
        # self.do_tap_select_Reason()
        # self.do_click("SUBMIT_PROCUREMENT_BUTTON_ID")
        # time.sleep(6)
        # extracted_text = Product.PROCUREMENT_SUCCESS_TITLE(self)
        # print(extracted_text)
        # expected_text = "Request has been successfully submitted!"
        # if expected_text == extracted_text:
        #     allure.attach(self.driver.get_screenshot_as_png(), name=" Adding Product is successfully",
        #                   attachment_type=AttachmentType.PNG)
        #     assert True, " Adding Product is successfully"
        # else:
        #     allure.attach(self.driver.get_screenshot_as_png(), name=" Adding Product is failed",
        #                   attachment_type=AttachmentType.PNG)
        #     assert False, " Adding Product is failed"

