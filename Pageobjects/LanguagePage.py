from selenium.webdriver.common.by import By

from Pageobjects.Basepage import Basepage
from Pageobjects.Login_Usename_Page import Login_Usename_Page
from Testcases.conftest import appium_driver

"""By locators"""


class Language_page(Basepage):

    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    """ These are the page actions for the Home_page"""

    def language_selection_page(self):
        # self.clear_room_database("package_name", "database_name")
        self.do_click("LANGUAGE_OPTION_XPATH")
        self.do_click("CONTINUE_BUTTON_ID")
        return Login_Usename_Page(self.driver)



