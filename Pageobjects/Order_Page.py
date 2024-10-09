import time

from Pageobjects.Basepage import Basepage
from Testcases.conftest import appium_driver_1
from Pageobjects.Farmer_registry_page import Farmer_registry

from ConfigurationData.config import Testdata

"""By locators"""


class Order_section(Basepage):
    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.farmer_registry =  Farmer_registry(self.driver)

    def navigate_to_farmer_registry(self):
        # Assuming there's a method in Order_section to navigate to Farmer Registry
        # If not, you might need to implement this navigation in the Order_section class
        self.farmer_registry = Farmer_registry(self.driver)
        return self

    def perform_farmer_registry_action(self):
        return self.farmer_registry.Farmer_registry_section()
    
    """ These are the page actions for the Home_page"""

    def Order_Placememt(self):
        time.sleep(3)
        self.do_click("SELECT_ORDER_ID")
        time.sleep(5)
        self.do_click("TAKE_NEW_ORDERS_ID")
        time.sleep(5)
        self.do_click("SELECT_FARMER_XPATH")
        time.sleep(2)
        self.do_click("ADD_TO_CART_XPATH")
        time.sleep(2)
        # self.do_click("REQUIRED_BY_XPATH")
        # self.do_click("NEXT_MONTH_ID")
        # self.do_click("SELECT_DATE_XPATH")
        # self.do_click("OK_BUTTON_ID")
        self.do_click("ORDER_CONTINUE_BUTTON_ID")
        time.sleep(2)
        self.do_click("LOCATION_ORDER_ID")
        time.sleep(3)
        self.do_click("SUBMIT_BUTTON_ID")
        return Farmer_registry(self.driver)

    def Order_Cancel(self):
        time.sleep(3)
        self.do_click("SELECT_ORDER_ID")
        time.sleep(5)
        self.do_click("CANCEL_ORDER_ID")
        self.do_click("CONFIRM_CANCEL_ORDER_ID")


    # def NEW_DEV_GROUP_NAME(self):
    #     return self.get_Text("NEW_DEV_GROUP_NAME_XPATH")
