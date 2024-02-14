import time

from Pageobjects.Basepage import Basepage
from Testcases.conftest import appium_driver

from ConfigurationData.config import Testdata

"""By locators"""

class Farmer_section(Basepage):
    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    """ These are the page actions for the Home_page"""

    def Adding_farmer_page(self):
        # Selecting location for EA USER
        self.do_click("SELECT_FARMER_ID")
        self.do_click("SELECT_ADD_FARMER_ID")
        time.sleep(5)
        self.do_click("SELECT_VILLAGE_ID")
        time.sleep(5)
        self.do_tap_add_farmer_village()
        self.do_click("LOCATION_NEXT_BUTTON_ID")
        print("BYE")
        time.sleep(5)
        return self

    def Adding_personal_info_page(self, Farmer_name, Father_name, Grandfather_name,Age,FIRST_FOUR,SECOND_FOUR,THIRD_FOUR):
        self.do_click("SELECT_DEVELOPMENT_GROUP_ID")
        time.sleep(2)
        self.do_tap_select_dev_group()
        time.sleep(2)
        self.do_click("FARMER_NAME_ID")
        self.do_type("FARMER_NAME_ID", Farmer_name)
        self.do_click("FATHER_NAME_ID")
        self.do_type("FATHER_NAME_ID", Father_name)
        self.do_click("GRANDFATHER_NAME_ID")
        self.do_type("GRANDFATHER_NAME_ID", Grandfather_name)
        self.do_click("GENDER_DROP_DOWN_ID")
        time.sleep(5)
        self.do_tap_select_gender()
        self.do_click("AGE_ID")
        self.do_type("AGE_ID", Age)
        self.do_click("NATIONAL_ID_FIRST_BOX_ID")
        self.do_type("NATIONAL_ID_FIRST_BOX_ID", FIRST_FOUR)
        self.do_click("NATIONAL_ID_SECOND_BOX_ID")
        self.do_type("NATIONAL_ID_SECOND_BOX_ID", SECOND_FOUR)
        self.do_click("NATIONAL_ID_THIRD_BOX_ID")
        self.do_type("NATIONAL_ID_THIRD_BOX_ID", THIRD_FOUR)
        # self.do_click("LOCATION_NEXT_BUTTON_ID")
        return self

    def Adding_contact_info_page(self):
        self.do_click("CONTACT_INFORMATION_ID")
        time.sleep(2)

        # return Order_Page(self.driver)
    #
    # def FLW_NAME_SECTION(self):
    #     return self.get_Text("FLW_NAME_ID")
