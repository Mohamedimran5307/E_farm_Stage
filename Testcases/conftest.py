import subprocess

import allure
import pytest
from allure_commons.types import AttachmentType
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from appium.webdriver.extensions.options import Options

#
#
# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, "rep_" + rep.when, rep)
#     return rep
#
#
# @pytest.fixture(scope="class")
# def init_appium_driver():
#     # global appium_service
#     # appium_service = AppiumService()
#     # appium_service.start()
#
#     desired_cap = {}
#     desired_cap['platformName'] = 'Android'
#     desired_cap['deviceName'] = 'Android'
#     desired_cap['udid'] = "YLWOI7EACAAAHQDM"
#     desired_cap['app'] = '/Users/shaikmohamedimran/PycharmProjects/Appium Page Object Model/APP/app-dev-debug.apk'
#
#     # global driver
#     driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
#     driver.implcdicitly_wait(10)
#     appium_driver  = init_appium_driver()
#     yield driver
#     driver.quit()
#     # appium_service.stop()

# @pytest.fixture(scope="function")
# def appium_driver(request):
#     options = webdriver.Options()
#     options.platformName = 'Android'
#     options.deviceName = 'Android'
#     options.udid = 'RZ8M50082GZ'
#     options.app = '/Users/shaikmohamedimran/PycharmProjects/Appium Page Object Model/APP/app-dev-debug.apk'
#     # options.noReset = True  # Uncomment if needed
#
#     driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
#     request.cls.driver = driver
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()


import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


def clear_app_data(package_name):
    try:
        # Clear app data
        subprocess.run(['adb', 'shell', 'pm', 'clear', package_name], check=True)
        print(f"Successfully cleared data for {package_name}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to clear app data: {e}")


def restart_app(driver, package_name, activity_name):
    try:
        # Stop the app
        driver.terminate_app(package_name)

        # Start the app
        driver.activate_app(package_name)

        print(f"Successfully restarted {package_name}")
    except Exception as e:
        print(f"Failed to restart app: {e}")


@pytest.fixture(scope="function")
def appium_driver_1(request):
    desired_cap = {}
    desired_cap['platformName'] = 'Android'
    desired_cap['deviceName'] = 'Samsung'
    # desired_cap['udid'] = '192.168.29.243:5555'
    desired_cap['udid'] = "RZ8M50082GZ"  # YLWOI7EACAAAHQDM  "HA1AGEVG"
    desired_cap['app'] = '/Users/shaikmohamedimran/PycharmProjects/E_farm_Mobile_D2FO/APP/EFarm_Latest_01.apk'
    desired_cap['automationName'] = 'uiautomator2'
    desired_cap['appPackage'] = 'com.digitalgreen.org.d2fo'
    desired_cap['appActivity'] = '.ui.activity.SplashActivity'
    desired_cap['noReset'] = True
    #
    desired_cap["appium:newCommandTimeout"] = 3600
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)

    # Clear app data
    # clear_app_data(desired_cap['appPackage'])
    #
    # # Restart the app
    # restart_app(driver, desired_cap['appPackage'], desired_cap['appActivity'])

    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def appium_driver_2(request):
    desired_cap = {}
    desired_cap['platformName'] = 'Android'
    desired_cap['deviceName'] = 'Samsung'
    # desired_cap['udid'] = '192.168.29.243:5555'
    desired_cap['udid'] = "RZ8M50082GZ"  # YLWOI7EACAAAHQDM  "HA1AGEVG"
    desired_cap['app'] = '/Users/shaikmohamedimran/PycharmProjects/E_farm_Mobile_D2FO/APP/EFarm_Latest_01.apk'
    desired_cap['automationName'] = 'uiautomator2'
    desired_cap['appPackage'] = 'com.digitalgreen.org.d2fo'
    desired_cap['appActivity'] = '.ui.activity.SplashActivity'
    desired_cap['noReset'] = False
    #
    desired_cap["appium:newCommandTimeout"] = 3600
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)

    # Clear app data
    clear_app_data(desired_cap['appPackage'])

    # Restart the app
    restart_app(driver, desired_cap['appPackage'], desired_cap['appActivity'])

    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield driver
    driver.quit()



# @pytest.fixture()
# def log_on_failure(request, appium_driver):
#     yield
#     item = request.node
#     driver = appium_driver
#     if item.rep_call.failed:
#         allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
