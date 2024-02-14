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
            self.driver.find_elements_by_xpath(configReader.readConfig("locators", locator))[index].click()
        elif str(locator).endswith("_ACCESSIBILITYID"):
            self.driver.find_elements_by_accessibility_id(configReader.readConfig("locators", locator))[index].click()
        elif str(locator).endswith("_ID"):
            self.driver.find_elements_by_id(configReader.readConfig("locators", locator))[index].click()
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

    # Clear the Room database of the Android application
    def clear_room_database(self, package_name, database_name):
        # Stop the app to ensure the database is not in use
        self.driver.execute_script("mobile: shell", {"command": "am force-stop", "args": {"target": package_name}})

        # Clear the Room database by deleting its corresponding database file
        clear_command = f"rm -rf /data/data/{package_name}/databases/{database_name}"
        self.driver.execute_script("mobile: shell",
                                   {"command": "run-as", "args": {"target": package_name, "command": clear_command}})

        # Start the app again after clearing the database
        # activity_name = "com.digitalgreen.org.d2fo.ui.activity.SplashActivity"
        # self.driver.start_activity(package_name, activity_name)

    def do_swipeUp(self, howManySwipes, driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(514, 600, 514, 200, 1000)

    def do_tap_dev_group_type(self):

        # Define x and y coordinates
        x = 200  #
        y = 434  #
        # Create a TouchAction instance
        touch_action = TouchAction(self.driver)

        # Perform tap action on the specified x and y coordinates
        touch_action.tap(x=x, y=y).perform()

    def do_tap_dev_group_village(self):

        # Define x and y coordinates
        x = 100  #
        y = 400  #
        # Create a TouchAction instance
        touch_action = TouchAction(self.driver)

        # Perform tap action on the specified x and y coordinates
        touch_action.tap(x=x, y=y).perform()

    def do_tap_add_farmer_village(self):

        # Define x and y coordinates
        x1 = 200  #
        y2 = 670  #
        # Create a TouchAction instance
        touch_action = TouchAction(self.driver)
        time.sleep(5)

        # Perform tap action on the specified x and y coordinates
        i = touch_action.tap(x=x1, y=y2).perform()
        print("imran", i)

    def do_tap_select_dev_group(self):

        # Define x and y coordinates
        x3 = 70  #
        y4 = 383  #
        # Create a TouchAction instance
        touch_action = TouchAction(self.driver)

        # Perform tap action on the specified x and y coordinates
        touch_action.tap(x=x3, y=y4).perform()

    def do_tap_select_gender(self):

        # Define x and y coordinates
        x5 = 200  #
        y6 = 485  #
        # Create a TouchAction instance
        touch_action = TouchAction(self.driver)
        time.sleep(5)
        # Perform tap action on the specified x and y coordinates
        touch_action.tap(x=x5, y=y6).perform()
