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
#     driver.implicitly_wait(10)
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


@pytest.fixture(scope="function")
def appium_driver(request):
    desired_cap = {}
    desired_cap['platformName'] = 'Android'
    desired_cap['deviceName'] = 'LENOVO'
    desired_cap['udid'] = "HA1AGEVG"  # YLWOI7EACAAAHQDM RZ8M50082GZ "15982498150025Y"
    desired_cap['app'] = '/Users/shaikmohamedimran/PycharmProjects/EA_Mobile_App_POM/APP/app-stage-debug-240209102545-1.0.apk'
    # desired_cap['appPackage'] = 'com.digitalgreen.org.d2fo'
    # desired_cap['appActivity']= '.ui.activity.SplashActivity'
    # desired_cap["noReset"] = True
    desired_cap["appium:newCommandTimeout"] = 3600
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
    # # Execute an ADB shell command
    # adb_shell_command = "run-as com.digitalgreen.org.d2fo rm -rf"
    # result = driver.execute_script('mobile: shell', {'command': adb_shell_command})
    # print("Note",result)
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
