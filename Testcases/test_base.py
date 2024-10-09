import pytest
from appium.webdriver import webdriver

from ConfigurationData.config import Testdata
from Utilities.Navigation_flow import Flow_of_test


# @pytest.mark.flaky(reruns=2)
@pytest.mark.usefixtures("appium_driver_1")
class Basetest_1:
    # driver = None
    logged_in = True

    @classmethod
    def setup_class(cls):
        # Set up the driver
        # cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities={...})

        # Log in once for the entire test suite
        if not cls.logged_in:
            test_flow = Flow_of_test(cls.driver)
            test_flow.navigate_to_language_page().login(
                Testdata.usernumber, Testdata.OTP_1, Testdata.OTP_2,
                Testdata.OTP_3, Testdata.OTP_4, Testdata.OTP_5, Testdata.OTP_6
            )
            cls.logged_in = True


@pytest.mark.usefixtures("appium_driver_2")
class Basetest_2:
    pass
