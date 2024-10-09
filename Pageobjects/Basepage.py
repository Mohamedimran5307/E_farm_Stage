import logging
import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from ConfigurationData.config import Testdata
from Utilities import configReader
from Utilities.Logutilities import Logger
from selenium.webdriver.common.by import By

log = Logger(__name__, logging.INFO)


class Basepage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(MobileBy.XPATH, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_element(MobileBy.ACCESSIBILITY_ID, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_ID"):
            # print("REACHED", locator)
            self.driver.find_element(MobileBy.ID, configReader.readConfig("locators", locator)).click()
        log.logger.info("Clicking on element: " + str(locator))

    def do_click_ORDER(self, by_locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(by_locator))

    def do_click_index(self, locator, index):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(MobileBy.ID, configReader.readConfig("locators", locator))[index].click()
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_element(MobileBy.ID, configReader.readConfig("locators", locator))[index].click()
        elif str(locator).endswith("_ID"):
            self.driver.find_elements(MobileBy.ID, configReader.readConfig("locators", locator))[index].click()
        log.logger.info("Clicking on element" + str(locator) + "with index:" + str(index))

    def do_type(self, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(MobileBy.XPATH, configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_element(MobileBy.ACCESSIBILITY_ID, configReader.readConfig("locators", locator)).send_keys(
                value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element(MobileBy.ID, configReader.readConfig("locators", locator)).send_keys(value)
        log.logger.info("Typing in an element" + "Entering the value as:" + value)

    def get_Text(self, locator):
        if str(locator).endswith("_XPATH"):
            text = self.driver.find_element(MobileBy.XPATH, configReader.readConfig("locators", locator)).text
        elif str(locator).endswith("_ACCESSIBILITYID"):
            text = self.driver.find_element(MobileBy.ACCESSIBILITY_ID,
                                            configReader.readConfig("locators", locator)).text
        elif str(locator).endswith("_ID"):
            text = self.driver.find_element(MobileBy.ID, configReader.readConfig("locators", locator)).text
        log.logger.info("Getting text from an element" + str(locator))
        return text

    def do_swipeUp(self, howManySwipes, driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(514, 600, 514, 200, 1000)

    def do_tap_gender(self):

        # Define x and y coordinates
        x = 125  #
        y = 662  #
        # Create a TouchAction instance
        touch_action = TouchAction(self.driver)

        # Perform tap action on the specified x and y coordinates
        touch_action.tap(x=x, y=y).perform()

    #
    def do_tap_producer_group(self):

        # Define x and y coordinates
        x = 125  #
        y = 776  #
        # Create a TouchAction instance
        touch_action = TouchAction(self.driver)
        time.sleep(5)
        # Perform tap action on the specified x and y coordinates
        touch_action.tap(x=x, y=y).perform()

    #
    def do_tap_select_District(self):

        # Define x and y coordinates
        x1 = 177  #
        y2 = 432  #
        # Create a TouchAction instance
        touch_action = TouchAction(self.driver)
        time.sleep(3)

        # Perform tap action on the specified x and y coordinates
        i = touch_action.tap(x=x1, y=y2).perform()
        print("imran", i)

    #
    def do_tap_select_Block(self):

        # Define x and y coordinates
        x3 = 150  #
        y4 = 434  #
        # Create a TouchAction instance
        touch_action = TouchAction(self.driver)

        # Perform tap action on the specified x and y coordinates
        touch_action.tap(x=x3, y=y4).perform()

    #
    def do_tap_select_Village(self):

        # Define x and y coordinates
        x5 = 150  #
        y6 = 382  #
        # Create a TouchAction instance
        touch_action = TouchAction(self.driver)
        time.sleep(5)
        # Perform tap action on the specified x and y coordinates
        touch_action.tap(x=x5, y=y6).perform()

    #
    def do_tap_select_FLW(self):

        # Define x and y coordinates
        x7 = 152  #
        y8 = 226  #
        # Create a TouchAction instance
        touch_action = TouchAction(self.driver)
        time.sleep(5)
        # Perform tap action on the specified x and y coordinates
        touch_action.tap(x=x7, y=y8).perform()

    #
    def do_tap_select_smartphone(self):

        # Define x and y coordinates
        x9 = 114  #
        y10 = 474  #
        # Create a TouchAction instance
        touch_action = TouchAction(self.driver)
        time.sleep(5)
        # Perform tap action on the specified x and y coordinates
        touch_action.tap(x=x9, y=y10).perform()

    #
    def do_tap_select_Education(self):

        # Define x and y coordinates
        x11 = 192  #
        y12 = 224  #
        # Create a TouchAction instance
        touch_action = TouchAction(self.driver)
        time.sleep(5)
        # Perform tap action on the specified x and y coordinates
        touch_action.tap(x=x11, y=y12).perform()

    #
    def do_tap_select_UOM(self):

        # Define x and y coordinates
        x13 = 432  #
        y14 = 890  #
        # Create a TouchAction instance
        touch_action = TouchAction(self.driver)
        time.sleep(5)
        # Perform tap action on the specified x and y coordinates
        touch_action.tap(x=x13, y=y14).perform()

    #
    def do_tap_select_UOM_units(self):

        # Define x and y coordinates
        x15 = 437  #
        y16 = 889  #
        # Create a TouchAction instance
        touch_action = TouchAction(self.driver)
        time.sleep(5)
        # Perform tap action on the specified x and y coordinates
        touch_action.tap(x=x15, y=y16).perform()

    #
    def do_tap_select_Reason(self):

        # Define x and y coordinates
        x17 = 127  #
        y18 = 1199  #
        # Create a TouchAction instance
        touch_action = TouchAction(self.driver)
        time.sleep(5)
        # Perform tap action on the specified x and y coordinates
        touch_action.tap(x=x17, y=y18).perform()

    #
    def do_select_Product_category_type(self):

        # Define x and y coordinates
        x19 = 110  #
        y20 = 865  #
        # Create a TouchAction instance
        touch_action = TouchAction(self.driver)
        time.sleep(5)
        # Perform tap action on the specified x and y coordinates
        touch_action.tap(x=x19, y=y20).perform()
    #
    # def do_tap_select_crop_being_cultivated(self):
    #
    #     # Define x and y coordinates
    #     x21 = 99  #
    #     y22 = 129  #
    #     # Create a TouchAction instance
    #     touch_action = TouchAction(self.driver)
    #     time.sleep(5)
    #     # Perform tap action on the specified x and y coordinates
    #     touch_action.tap(x=x21, y=y22).perform()
    #
    # def do_tap_select_livestock_type(self):
    #
    #     # Define x and y coordinates
    #     x23 = 101  #
    #     y24 = 282  #
    #     # Create a TouchAction instance
    #     touch_action = TouchAction(self.driver)
    #     time.sleep(5)
    #     # Perform tap action on the specified x and y coordinates
    #     touch_action.tap(x=x23, y=y24).perform()
    #
    # def do_tap_select_livestock_breed(self):
    #
    #     # Define x and y coordinates
    #     x25 = 129  #
    #     y26 = 129  #
    #     # Create a TouchAction instance
    #     touch_action = TouchAction(self.driver)
    #     time.sleep(5)
    #     # Perform tap action on the specified x and y coordinates
    #     touch_action.tap(x=x25, y=y26).perform()
